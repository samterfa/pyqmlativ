# This module contains Grading functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnCommentBucketID = True, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCommentBucket(CommentBucketID, EntityID = 1, returnCommentBucketID = True, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "get", return_params_list = return_params_list)

def modifyCommentBucket(CommentBucketID, EntityID = 1, setCommentBucketIDClonedFrom = None, setCommentSetID = None, setDisplayOrder = None, setEntityGroupKey = None, setGradingPeriodID = None, setIsLimitedByCourse = None, setName = None, setRelationships = None, returnCommentBucketID = True, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/" + str(CommentBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCommentBucket(EntityID = 1, setCommentBucketIDClonedFrom = None, setCommentSetID = None, setDisplayOrder = None, setEntityGroupKey = None, setGradingPeriodID = None, setIsLimitedByCourse = None, setName = None, setRelationships = None, returnCommentBucketID = True, returnCommentBucketIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnGradingPeriodID = False, returnIsLimitedByCourse = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCommentBucket(CommentBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCommentBucketCourse(EntityID = 1, page = 1, pageSize = 100, returnCommentBucketCourseID = True, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCommentBucketCourse(CommentBucketCourseID, EntityID = 1, returnCommentBucketCourseID = True, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "get", return_params_list = return_params_list)

def modifyCommentBucketCourse(CommentBucketCourseID, EntityID = 1, setCommentBucketID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCommentBucketCourseID = True, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/" + str(CommentBucketCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCommentBucketCourse(EntityID = 1, setCommentBucketID = None, setCourseID = None, setEntityGroupKey = None, setRelationships = None, returnCommentBucketCourseID = True, returnCommentBucketID = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentBucketCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCommentBucketCourse(CommentBucketCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCommentCode(EntityID = 1, page = 1, pageSize = 100, returnCommentCodeID = True, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCommentCode(CommentCodeID, EntityID = 1, returnCommentCodeID = True, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "get", return_params_list = return_params_list)

def modifyCommentCode(CommentCodeID, EntityID = 1, setCode = None, setCommentCodeIDClonedFrom = None, setCommentSetID = None, setDescription = None, setEntityGroupKey = None, setRelationships = None, returnCommentCodeID = True, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/" + str(CommentCodeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCommentCode(EntityID = 1, setCode = None, setCommentCodeIDClonedFrom = None, setCommentSetID = None, setDescription = None, setEntityGroupKey = None, setRelationships = None, returnCommentCodeID = True, returnCode = False, returnCodeDescription = False, returnCommentCodeIDClonedFrom = False, returnCommentSetID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentCode/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCommentCode(CommentCodeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCommentSet(EntityID = 1, page = 1, pageSize = 100, returnCommentSetID = True, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCommentSet(CommentSetID, EntityID = 1, returnCommentSetID = True, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "get", return_params_list = return_params_list)

def modifyCommentSet(CommentSetID, EntityID = 1, setCode = None, setCommentSetIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCommentSetID = True, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/" + str(CommentSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCommentSet(EntityID = 1, setCode = None, setCommentSetIDClonedFrom = None, setDescription = None, setEntityGroupKey = None, setEntityID = None, setSchoolYearID = None, setRelationships = None, returnCommentSetID = True, returnCode = False, returnCodeDescription = False, returnCommentSetIDClonedFrom = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CommentSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCommentSet(CommentSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictGroup(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1, setDistrictGroupKey = None, setDistrictID = None, setEarnedCreditsRoundingDecimals = None, setFinalGPADecimalSetting = None, setFinalGPADecimalSettingCode = None, setFinalGPARoundingDecimals = None, setGPACalculationDecimalSetting = None, setGPACalculationDecimalSettingCode = None, setGPACalculationRoundingDecimals = None, setRelationships = None, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/" + str(ConfigDistrictGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictGroup(EntityID = 1, setDistrictGroupKey = None, setDistrictID = None, setEarnedCreditsRoundingDecimals = None, setFinalGPADecimalSetting = None, setFinalGPADecimalSettingCode = None, setFinalGPARoundingDecimals = None, setGPACalculationDecimalSetting = None, setGPACalculationDecimalSettingCode = None, setGPACalculationRoundingDecimals = None, setRelationships = None, returnConfigDistrictGroupID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCreditsRoundingDecimals = False, returnFinalGPADecimalSetting = False, returnFinalGPADecimalSettingCode = False, returnFinalGPARoundingDecimals = False, returnGPACalculationDecimalSetting = False, returnGPACalculationDecimalSettingCode = False, returnGPACalculationRoundingDecimals = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictGroup(ConfigDistrictGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrictYear(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setSchoolYearID = None, setStudentSectionLinkOption = None, setStudentSectionLinkOptionCode = None, setUseStudentSectionLinkCourseType = None, setUseStudentSectionLinking = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrictYear(EntityID = 1, setConfigDistrictYearIDClonedFrom = None, setDistrictID = None, setSchoolYearID = None, setStudentSectionLinkOption = None, setStudentSectionLinkOptionCode = None, setUseStudentSectionLinkCourseType = None, setUseStudentSectionLinking = None, setRelationships = None, returnConfigDistrictYearID = True, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentSectionLinkOption = False, returnStudentSectionLinkOptionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinkCourseType = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigDistrictYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityGroupYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityGroupYearID = True, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, returnConfigEntityGroupYearID = True, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1, setConfigEntityGroupYearIDClonedFrom = None, setCurrentCalculation = None, setCurrentCalculationCode = None, setEntityGroupKey = None, setEntityID = None, setFreeFormCommentMaxLength = None, setGradebookLockMessage = None, setGradeLevelIDCohort = None, setLockGradebookAssignmentsAfterDate = None, setLockGradebookCalculation = None, setLockGradebookStartTime = None, setRetainGradesNumberOfDays = None, setSchoolYearID = None, setUseAddOnGPA = None, setUseFactorBasedAddOn = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/" + str(ConfigEntityGroupYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityGroupYear(EntityID = 1, setConfigEntityGroupYearIDClonedFrom = None, setCurrentCalculation = None, setCurrentCalculationCode = None, setEntityGroupKey = None, setEntityID = None, setFreeFormCommentMaxLength = None, setGradebookLockMessage = None, setGradeLevelIDCohort = None, setLockGradebookAssignmentsAfterDate = None, setLockGradebookCalculation = None, setLockGradebookStartTime = None, setRetainGradesNumberOfDays = None, setSchoolYearID = None, setUseAddOnGPA = None, setUseFactorBasedAddOn = None, setRelationships = None, returnConfigEntityGroupYearID = True, returnConfigEntityGroupYearIDClonedFrom = False, returnCreatedTime = False, returnCurrentCalculation = False, returnCurrentCalculationCode = False, returnEntityGroupKey = False, returnEntityID = False, returnFreeFormCommentMaxLength = False, returnGradebookLockMessage = False, returnGradeLevelIDCohort = False, returnLockGradebookAssignmentsAfterDate = False, returnLockGradebookCalculation = False, returnLockGradebookStartTime = False, returnLockGradeBuckets = False, returnModifiedTime = False, returnRetainGradesNumberOfDays = False, returnSchoolYearID = False, returnUseAddOnGPA = False, returnUseFactorBasedAddOn = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityGroupYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityGroupYear(ConfigEntityGroupYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigEntityYear(EntityID = 1, page = 1, pageSize = 100, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params_list)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearIDClonedFrom = None, setElectronicSignatureIDReportCard = None, setElectronicSignatureIDTranscript = None, setEntityID = None, setSchoolYearID = None, setTranscriptTitle = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearIDClonedFrom = None, setElectronicSignatureIDReportCard = None, setElectronicSignatureIDTranscript = None, setEntityID = None, setSchoolYearID = None, setTranscriptTitle = None, setRelationships = None, returnConfigEntityYearID = True, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnElectronicSignatureIDReportCard = False, returnElectronicSignatureIDTranscript = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnTranscriptTitle = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/ConfigEntityYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnCourseGPAMethodID = True, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGPAMethod(CourseGPAMethodID, EntityID = 1, returnCourseGPAMethodID = True, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(CourseGPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyCourseGPAMethod(CourseGPAMethodID, EntityID = 1, setCourseGPAMethodIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setGPACredit = None, setGPAMethodEntityID = None, setPointSetEntityID = None, setUseOverride = None, setRelationships = None, returnCourseGPAMethodID = True, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/" + str(CourseGPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGPAMethod(EntityID = 1, setCourseGPAMethodIDClonedFrom = None, setCourseID = None, setEntityGroupKey = None, setGPACredit = None, setGPAMethodEntityID = None, setPointSetEntityID = None, setUseOverride = None, setRelationships = None, returnCourseGPAMethodID = True, returnCourseGPAMethodIDClonedFrom = False, returnCourseID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPACredit = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGPAMethod(CourseGPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCourseGPAMethodGradeReferenceOverride(EntityID = 1, page = 1, pageSize = 100, returnCourseGPAMethodGradeReferenceOverrideID = True, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, EntityID = 1, returnCourseGPAMethodGradeReferenceOverrideID = True, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(CourseGPAMethodGradeReferenceOverrideID), verb = "get", return_params_list = return_params_list)

def modifyCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, EntityID = 1, setCourseGPAMethodID = None, setGPACredits = None, setGradeReferenceID = None, setPointSetEntityID = None, setRelationships = None, returnCourseGPAMethodGradeReferenceOverrideID = True, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/" + str(CourseGPAMethodGradeReferenceOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCourseGPAMethodGradeReferenceOverride(EntityID = 1, setCourseGPAMethodID = None, setGPACredits = None, setGradeReferenceID = None, setPointSetEntityID = None, setRelationships = None, returnCourseGPAMethodGradeReferenceOverrideID = True, returnCourseGPAMethodID = False, returnCreatedTime = False, returnGPACredits = False, returnGradeReferenceID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/CourseGPAMethodGradeReferenceOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCourseGPAMethodGradeReferenceOverride(CourseGPAMethodGradeReferenceOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarnedCreditsBucketGroup(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, EntityID = 1, returnEarnedCreditsBucketGroupID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(EarnedCreditsBucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, EntityID = 1, setEarnedCreditsBucketGroupIDClonedFrom = None, setEntityGroupKey = None, setGradingPeriodSetID = None, setSectionLengthID = None, setRelationships = None, returnEarnedCreditsBucketGroupID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/" + str(EarnedCreditsBucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarnedCreditsBucketGroup(EntityID = 1, setEarnedCreditsBucketGroupIDClonedFrom = None, setEntityGroupKey = None, setGradingPeriodSetID = None, setSectionLengthID = None, setRelationships = None, returnEarnedCreditsBucketGroupID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupIDClonedFrom = False, returnEntityGroupKey = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarnedCreditsBucketGroup(EarnedCreditsBucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarnedCreditsBucketGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupGradeBucketID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, EntityID = 1, returnEarnedCreditsBucketGroupGradeBucketID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(EarnedCreditsBucketGroupGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, EntityID = 1, setEarnedCreditsBucketGroupGradeBucketIDClonedFrom = None, setEarnedCreditsBucketGroupID = None, setEntityGroupKey = None, setGradeBucketID = None, setPercent = None, setRelationships = None, returnEarnedCreditsBucketGroupGradeBucketID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/" + str(EarnedCreditsBucketGroupGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarnedCreditsBucketGroupGradeBucket(EntityID = 1, setEarnedCreditsBucketGroupGradeBucketIDClonedFrom = None, setEarnedCreditsBucketGroupID = None, setEntityGroupKey = None, setGradeBucketID = None, setPercent = None, setRelationships = None, returnEarnedCreditsBucketGroupGradeBucketID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketIDClonedFrom = False, returnEarnedCreditsBucketGroupID = False, returnEntityGroupKey = False, returnGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarnedCreditsBucketGroupGradeBucket(EarnedCreditsBucketGroupGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarnedCreditsBucketGroupGradeBucketStudentOverride(EntityID = 1, page = 1, pageSize = 100, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, EntityID = 1, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(EarnedCreditsBucketGroupGradeBucketStudentOverrideID), verb = "get", return_params_list = return_params_list)

def modifyEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, EntityID = 1, setEarnedCreditsBucketGroupGradeBucketID = None, setPercent = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/" + str(EarnedCreditsBucketGroupGradeBucketStudentOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarnedCreditsBucketGroupGradeBucketStudentOverride(EntityID = 1, setEarnedCreditsBucketGroupGradeBucketID = None, setPercent = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnEarnedCreditsBucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnEarnedCreditsBucketGroupGradeBucketID = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/EarnedCreditsBucketGroupGradeBucketStudentOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarnedCreditsBucketGroupGradeBucketStudentOverride(EarnedCreditsBucketGroupGradeBucketStudentOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryFactorBasedAddOn(EntityID = 1, page = 1, pageSize = 100, returnFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getFactorBasedAddOn(FactorBasedAddOnID, EntityID = 1, returnFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(FactorBasedAddOnID), verb = "get", return_params_list = return_params_list)

def modifyFactorBasedAddOn(FactorBasedAddOnID, EntityID = 1, setFactor = None, setFactorBasedAddOnIDClonedFrom = None, setGPABucketEntityID = None, setGradeReferenceID = None, setGradingEndDateCutoffForCumulative = None, setRelationships = None, returnFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/" + str(FactorBasedAddOnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createFactorBasedAddOn(EntityID = 1, setFactor = None, setFactorBasedAddOnIDClonedFrom = None, setGPABucketEntityID = None, setGradeReferenceID = None, setGradingEndDateCutoffForCumulative = None, setRelationships = None, returnFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnFactorBasedAddOnIDClonedFrom = False, returnGPABucketEntityID = False, returnGradeReferenceID = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/FactorBasedAddOn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteFactorBasedAddOn(FactorBasedAddOnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucket(EntityID = 1, page = 1, pageSize = 100, returnGPABucketID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucket(GPABucketID, EntityID = 1, returnGPABucketID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(GPABucketID), verb = "get", return_params_list = return_params_list)

def modifyGPABucket(GPABucketID, EntityID = 1, setDescription = None, setDistrictGroupKey = None, setGPABucketTypeID = None, setName = None, setRelationships = None, returnGPABucketID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/" + str(GPABucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucket(EntityID = 1, setDescription = None, setDistrictGroupKey = None, setGPABucketTypeID = None, setName = None, setRelationships = None, returnGPABucketID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnGPABucketTypeID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucket(GPABucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketEntity(EntityID = 1, page = 1, pageSize = 100, returnGPABucketEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketEntity(GPABucketEntityID, EntityID = 1, returnGPABucketEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(GPABucketEntityID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketEntity(GPABucketEntityID, EntityID = 1, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGPABucketEntityIDClonedFrom = None, setGPABucketID = None, setSchoolYearID = None, setUseForFamilyAccess = None, setRelationships = None, returnGPABucketEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/" + str(GPABucketEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketEntity(EntityID = 1, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGPABucketEntityIDClonedFrom = None, setGPABucketID = None, setSchoolYearID = None, setUseForFamilyAccess = None, setRelationships = None, returnGPABucketEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPABucketEntityIDClonedFrom = False, returnGPABucketID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketEntity(GPABucketEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketGroup(GPABucketGroupID, EntityID = 1, returnGPABucketGroupID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(GPABucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketGroup(GPABucketGroupID, EntityID = 1, setEntityGroupKey = None, setGPABucketGroupIDClonedFrom = None, setGPABucketGroupSummaryID = None, setGPABucketID = None, setRelationships = None, returnGPABucketGroupID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/" + str(GPABucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketGroup(EntityID = 1, setEntityGroupKey = None, setGPABucketGroupIDClonedFrom = None, setGPABucketGroupSummaryID = None, setGPABucketID = None, setRelationships = None, returnGPABucketGroupID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupIDClonedFrom = False, returnGPABucketGroupSummaryID = False, returnGPABucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketGroup(GPABucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketGroupGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, EntityID = 1, returnGPABucketGroupGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(GPABucketGroupGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, EntityID = 1, setEntityGroupKey = None, setGPABucketGroupGradeBucketIDClonedFrom = None, setGPABucketGroupID = None, setGradeBucketID = None, setGradeRequiredForGPABucket = None, setIsUpToDate = None, setPercent = None, setRelationships = None, returnGPABucketGroupGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/" + str(GPABucketGroupGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketGroupGradeBucket(EntityID = 1, setEntityGroupKey = None, setGPABucketGroupGradeBucketIDClonedFrom = None, setGPABucketGroupID = None, setGradeBucketID = None, setGradeRequiredForGPABucket = None, setIsUpToDate = None, setPercent = None, setRelationships = None, returnGPABucketGroupGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupGradeBucketIDClonedFrom = False, returnGPABucketGroupID = False, returnGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnIsUpToDate = False, returnModifiedTime = False, returnPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketGroupGradeBucket(GPABucketGroupGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketGroupGradeBucketStudentOverride(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, EntityID = 1, returnGPABucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(GPABucketGroupGradeBucketStudentOverrideID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, EntityID = 1, setGPABucketGroupGradeBucketID = None, setGradeRequiredForGPABucket = None, setPercent = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnGPABucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/" + str(GPABucketGroupGradeBucketStudentOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketGroupGradeBucketStudentOverride(EntityID = 1, setGPABucketGroupGradeBucketID = None, setGradeRequiredForGPABucket = None, setPercent = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnGPABucketGroupGradeBucketStudentOverrideID = True, returnCreatedTime = False, returnGPABucketGroupGradeBucketID = False, returnGradeRequiredForGPABucket = False, returnModifiedTime = False, returnPercent = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupGradeBucketStudentOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketGroupGradeBucketStudentOverride(GPABucketGroupGradeBucketStudentOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketGroupSummary(EntityID = 1, page = 1, pageSize = 100, returnGPABucketGroupSummaryID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketGroupSummary(GPABucketGroupSummaryID, EntityID = 1, returnGPABucketGroupSummaryID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(GPABucketGroupSummaryID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketGroupSummary(GPABucketGroupSummaryID, EntityID = 1, setEntityGroupKey = None, setGPABucketGroupSummaryIDClonedFrom = None, setGPABucketSetID = None, setGradingPeriodSetID = None, setSectionLengthID = None, setRelationships = None, returnGPABucketGroupSummaryID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/" + str(GPABucketGroupSummaryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketGroupSummary(EntityID = 1, setEntityGroupKey = None, setGPABucketGroupSummaryIDClonedFrom = None, setGPABucketSetID = None, setGradingPeriodSetID = None, setSectionLengthID = None, setRelationships = None, returnGPABucketGroupSummaryID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketGroupSummaryIDClonedFrom = False, returnGPABucketSetID = False, returnGradingPeriodSetID = False, returnModifiedTime = False, returnSectionLengthID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketGroupSummary/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketGroupSummary(GPABucketGroupSummaryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketSet(EntityID = 1, page = 1, pageSize = 100, returnGPABucketSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketSet(GPABucketSetID, EntityID = 1, returnGPABucketSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(GPABucketSetID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketSet(GPABucketSetID, EntityID = 1, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setName = None, setRelationships = None, returnGPABucketSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/" + str(GPABucketSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketSet(EntityID = 1, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setName = None, setRelationships = None, returnGPABucketSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketSet(GPABucketSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPABucketType(EntityID = 1, page = 1, pageSize = 100, returnGPABucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPABucketType(GPABucketTypeID, EntityID = 1, returnGPABucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(GPABucketTypeID), verb = "get", return_params_list = return_params_list)

def modifyGPABucketType(GPABucketTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsCumulative = None, setRelationships = None, returnGPABucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/" + str(GPABucketTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPABucketType(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsCumulative = None, setRelationships = None, returnGPABucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsCumulative = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPABucketType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPABucketType(GPABucketTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodID = True, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPAMethod(GPAMethodID, EntityID = 1, returnGPAMethodID = True, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(GPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyGPAMethod(GPAMethodID, EntityID = 1, setAllowFurtherAttemptsOfNonHighSchoolCourses = None, setCancelSubAreaCreditFromMiddleSchoolCredit = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setExcludeTermTwoFinalYearGrade = None, setGPABucketSetID = None, setGradReqRankGPARequiredCourseRule = None, setGradReqRankGPARequiredCourseRuleCode = None, setLockGradeMarkPoints = None, setName = None, setSortNumber = None, setTotalElectiveCreditsPossible = None, setUseGradReqRankGPA = None, setUseTotalElectiveCredits = None, setRelationships = None, returnGPAMethodID = True, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/" + str(GPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPAMethod(EntityID = 1, setAllowFurtherAttemptsOfNonHighSchoolCourses = None, setCancelSubAreaCreditFromMiddleSchoolCredit = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setExcludeTermTwoFinalYearGrade = None, setGPABucketSetID = None, setGradReqRankGPARequiredCourseRule = None, setGradReqRankGPARequiredCourseRuleCode = None, setLockGradeMarkPoints = None, setName = None, setSortNumber = None, setTotalElectiveCreditsPossible = None, setUseGradReqRankGPA = None, setUseTotalElectiveCredits = None, setRelationships = None, returnGPAMethodID = True, returnAllowFurtherAttemptsOfNonHighSchoolCourses = False, returnCancelSubAreaCreditFromMiddleSchoolCredit = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnExcludeTermTwoFinalYearGrade = False, returnGPABucketSetID = False, returnGradReqRankGPARequiredCourseRule = False, returnGradReqRankGPARequiredCourseRuleCode = False, returnLockGradeMarkPoints = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnSortNumber = False, returnTotalElectiveCreditsPossible = False, returnUseGradReqRankGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTotalElectiveCredits = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPAMethod(GPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPAMethodCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPAMethodCourseGroup(GPAMethodCourseGroupID, EntityID = 1, returnGPAMethodCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(GPAMethodCourseGroupID), verb = "get", return_params_list = return_params_list)

def modifyGPAMethodCourseGroup(GPAMethodCourseGroupID, EntityID = 1, setCourseGroupID = None, setGPAMethodID = None, setRelationships = None, returnGPAMethodCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/" + str(GPAMethodCourseGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPAMethodCourseGroup(EntityID = 1, setCourseGroupID = None, setGPAMethodID = None, setRelationships = None, returnGPAMethodCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodCourseGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPAMethodCourseGroup(GPAMethodCourseGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPAMethodEntity(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPAMethodEntity(GPAMethodEntityID, EntityID = 1, returnGPAMethodEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(GPAMethodEntityID), verb = "get", return_params_list = return_params_list)

def modifyGPAMethodEntity(GPAMethodEntityID, EntityID = 1, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGPAMethodEntityIDClonedFrom = None, setGPAMethodID = None, setIsUpToDate = None, setSchoolYearID = None, setUseForFamilyAccess = None, setRelationships = None, returnGPAMethodEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/" + str(GPAMethodEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPAMethodEntity(EntityID = 1, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGPAMethodEntityIDClonedFrom = None, setGPAMethodID = None, setIsUpToDate = None, setSchoolYearID = None, setUseForFamilyAccess = None, setRelationships = None, returnGPAMethodEntityID = True, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGPAMethodEntityIDClonedFrom = False, returnGPAMethodID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSchoolYearID = False, returnStatus = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPAMethodEntity(GPAMethodEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGPAMethodGradeBucketFlagGPAPointsOverride(EntityID = 1, page = 1, pageSize = 100, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, EntityID = 1, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(GPAMethodGradeBucketFlagGPAPointsOverrideID), verb = "get", return_params_list = return_params_list)

def modifyGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, EntityID = 1, setGPAMethodID = None, setGPAPoints = None, setGPAPointsOverrideOption = None, setGPAPointsOverrideOptionCode = None, setGradeBucketFlagID = None, setRank = None, setRelationships = None, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/" + str(GPAMethodGradeBucketFlagGPAPointsOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGPAMethodGradeBucketFlagGPAPointsOverride(EntityID = 1, setGPAMethodID = None, setGPAPoints = None, setGPAPointsOverrideOption = None, setGPAPointsOverrideOptionCode = None, setGradeBucketFlagID = None, setRank = None, setRelationships = None, returnGPAMethodGradeBucketFlagGPAPointsOverrideID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GPAMethodGradeBucketFlagGPAPointsOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGPAMethodGradeBucketFlagGPAPointsOverride(GPAMethodGradeBucketFlagGPAPointsOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradebookLockGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradebookLockGradeBucketID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradebookLockGradeBucket(GradebookLockGradeBucketID, EntityID = 1, returnGradebookLockGradeBucketID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(GradebookLockGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyGradebookLockGradeBucket(GradebookLockGradeBucketID, EntityID = 1, setConfigEntityGroupYearID = None, setGradingPeriodGradeBucketID = None, setRelationships = None, returnGradebookLockGradeBucketID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/" + str(GradebookLockGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradebookLockGradeBucket(EntityID = 1, setConfigEntityGroupYearID = None, setGradingPeriodGradeBucketID = None, setRelationships = None, returnGradebookLockGradeBucketID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradebookLockGradeBucket(GradebookLockGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradebookLockGradeReference(EntityID = 1, page = 1, pageSize = 100, returnGradebookLockGradeReferenceID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradebookLockGradeReference(GradebookLockGradeReferenceID, EntityID = 1, returnGradebookLockGradeReferenceID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(GradebookLockGradeReferenceID), verb = "get", return_params_list = return_params_list)

def modifyGradebookLockGradeReference(GradebookLockGradeReferenceID, EntityID = 1, setConfigEntityGroupYearID = None, setGradeReferenceID = None, setRelationships = None, returnGradebookLockGradeReferenceID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/" + str(GradebookLockGradeReferenceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradebookLockGradeReference(EntityID = 1, setConfigEntityGroupYearID = None, setGradeReferenceID = None, setRelationships = None, returnGradebookLockGradeReferenceID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradebookLockGradeReference/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradebookLockGradeReference(GradebookLockGradeReferenceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketID = True, returnCreatedTime = False, returnDescription = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeBucket(GradeBucketID, EntityID = 1, returnGradeBucketID = True, returnCreatedTime = False, returnDescription = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(GradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyGradeBucket(GradeBucketID, EntityID = 1, setDescription = None, setEdFiGradingPeriodDescriptorID = None, setEdFiGradingPeriodID = None, setEntityGroupKey = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGradeBucketIDClonedFrom = None, setGradeBucketTypeID = None, setLabel = None, setNumber = None, setOrder = None, setUseForFamilyAccess = None, setRelationships = None, returnGradeBucketID = True, returnCreatedTime = False, returnDescription = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/" + str(GradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeBucket(EntityID = 1, setDescription = None, setEdFiGradingPeriodDescriptorID = None, setEdFiGradingPeriodID = None, setEntityGroupKey = None, setFamilyAccessDisplayGradYearHigh = None, setFamilyAccessDisplayGradYearLow = None, setGradeBucketIDClonedFrom = None, setGradeBucketTypeID = None, setLabel = None, setNumber = None, setOrder = None, setUseForFamilyAccess = None, setRelationships = None, returnGradeBucketID = True, returnCreatedTime = False, returnDescription = False, returnEdFiGradingPeriodDescriptorID = False, returnEdFiGradingPeriodID = False, returnEntityGroupKey = False, returnFamilyAccessDisplayGradYearHigh = False, returnFamilyAccessDisplayGradYearLow = False, returnGradeBucketIDClonedFrom = False, returnGradeBucketTypeID = False, returnLabel = False, returnLabelDescription = False, returnModifiedTime = False, returnNumber = False, returnOrder = False, returnUseForFamilyAccess = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeBucket(GradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeBucketFlag(GradeBucketFlagID, EntityID = 1, returnGradeBucketFlagID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(GradeBucketFlagID), verb = "get", return_params_list = return_params_list)

def modifyGradeBucketFlag(GradeBucketFlagID, EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnGradeBucketFlagID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/" + str(GradeBucketFlagID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeBucketFlag(EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setDistrictGroupKey = None, setDistrictID = None, setRelationships = None, returnGradeBucketFlagID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlag/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeBucketFlag(GradeBucketFlagID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeBucketFlagDetail(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagDetailID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeBucketFlagDetail(GradeBucketFlagDetailID, EntityID = 1, returnGradeBucketFlagDetailID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(GradeBucketFlagDetailID), verb = "get", return_params_list = return_params_list)

def modifyGradeBucketFlagDetail(GradeBucketFlagDetailID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeBucketFlagDetailIDClonedFrom = None, setGradeBucketFlagID = None, setIsActive = None, setPrintWithGradeMark = None, setSchoolYearID = None, setUseEarnedOverride = None, setUseGPAOverride = None, setUseGPAPointsOverride = None, setUseInEarned = None, setUseInFailed = None, setUseInGPA = None, setRelationships = None, returnGradeBucketFlagDetailID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/" + str(GradeBucketFlagDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeBucketFlagDetail(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeBucketFlagDetailIDClonedFrom = None, setGradeBucketFlagID = None, setIsActive = None, setPrintWithGradeMark = None, setSchoolYearID = None, setUseEarnedOverride = None, setUseGPAOverride = None, setUseGPAPointsOverride = None, setUseInEarned = None, setUseInFailed = None, setUseInGPA = None, setRelationships = None, returnGradeBucketFlagDetailID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketFlagDetailIDClonedFrom = False, returnGradeBucketFlagID = False, returnIsActive = False, returnModifiedTime = False, returnPrintWithGradeMark = False, returnSchoolYearID = False, returnUseEarnedOverride = False, returnUseGPAOverride = False, returnUseGPAPointsOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeBucketFlagDetail(GradeBucketFlagDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeBucketFlagDetailGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, EntityID = 1, returnGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(GradeBucketFlagDetailGPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, EntityID = 1, setEntityGroupKey = None, setGPAMethodEntityID = None, setGPAPoints = None, setGPAPointsOverrideOption = None, setGPAPointsOverrideOptionCode = None, setGradeBucketFlagDetailID = None, setPointSetEntityID = None, setUseOverride = None, setRelationships = None, returnGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/" + str(GradeBucketFlagDetailGPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeBucketFlagDetailGPAMethod(EntityID = 1, setEntityGroupKey = None, setGPAMethodEntityID = None, setGPAPoints = None, setGPAPointsOverrideOption = None, setGPAPointsOverrideOptionCode = None, setGradeBucketFlagDetailID = None, setPointSetEntityID = None, setUseOverride = None, setRelationships = None, returnGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGPAPoints = False, returnGPAPointsOverrideOption = False, returnGPAPointsOverrideOptionCode = False, returnGradeBucketFlagDetailID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketFlagDetailGPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeBucketFlagDetailGPAMethod(GradeBucketFlagDetailGPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeBucketType(EntityID = 1, page = 1, pageSize = 100, returnGradeBucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeBucketType(GradeBucketTypeID, EntityID = 1, returnGradeBucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(GradeBucketTypeID), verb = "get", return_params_list = return_params_list)

def modifyGradeBucketType(GradeBucketTypeID, EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setEdFiGradeTypeID = None, setEntityGroupKey = None, setEntityID = None, setGradeBucketTypeIDClonedFrom = None, setMinimumPercent = None, setSchoolYearID = None, setSnapshotGradeExtensionDays = None, setUseAllCategories = None, setUseSnapshotGrade = None, setRelationships = None, returnGradeBucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/" + str(GradeBucketTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeBucketType(EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setEdFiGradeTypeID = None, setEntityGroupKey = None, setEntityID = None, setGradeBucketTypeIDClonedFrom = None, setMinimumPercent = None, setSchoolYearID = None, setSnapshotGradeExtensionDays = None, setUseAllCategories = None, setUseSnapshotGrade = None, setRelationships = None, returnGradeBucketTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEdFiGradeTypeID = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketTypeIDClonedFrom = False, returnHasSpecificCategories = False, returnMinimumPercent = False, returnModifiedTime = False, returnSchoolYearID = False, returnSnapshotGradeExtensionDays = False, returnSpecificCategoryGradeBucketTypeCount = False, returnUseAllCategories = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSnapshotGrade = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeBucketType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeBucketType(GradeBucketTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradeMarkID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeMark(GradeMarkID, EntityID = 1, returnGradeMarkID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(GradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyGradeMark(GradeMarkID, EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDClonedFrom = None, setGradeMarkIDReverse = None, setGradYearHigh = None, setGradYearLow = None, setReportCardDisplayValue = None, setSchoolYearID = None, setStateGradeMarkMNID = None, setTranscriptDisplayValue = None, setUseAsTeacherOverride = None, setUseInEarned = None, setUseInFailed = None, setUseInGPA = None, setRelationships = None, returnGradeMarkID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/" + str(GradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeMark(EntityID = 1, setCode = None, setDescription = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setGradeMarkIDClonedFrom = None, setGradeMarkIDReverse = None, setGradYearHigh = None, setGradYearLow = None, setReportCardDisplayValue = None, setSchoolYearID = None, setStateGradeMarkMNID = None, setTranscriptDisplayValue = None, setUseAsTeacherOverride = None, setUseInEarned = None, setUseInFailed = None, setUseInGPA = None, setRelationships = None, returnGradeMarkID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkExistsInSpecifcEntity = False, returnGradeMarkIDClonedFrom = False, returnGradeMarkIDReverse = False, returnGradeMarkMNID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAHistoricRecord = False, returnModifiedTime = False, returnReportCardDisplayValue = False, returnSchoolYearID = False, returnStateGradeMarkMNID = False, returnTranscriptDisplayValue = False, returnUseAsTeacherOverride = False, returnUseInEarned = False, returnUseInFailed = False, returnUseInGPA = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeMark(GradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeMarkPointSet(EntityID = 1, page = 1, pageSize = 100, returnGradeMarkPointSetID = True, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeMarkPointSet(GradeMarkPointSetID, EntityID = 1, returnGradeMarkPointSetID = True, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(GradeMarkPointSetID), verb = "get", return_params_list = return_params_list)

def modifyGradeMarkPointSet(GradeMarkPointSetID, EntityID = 1, setAddOnPoints = None, setEntityGroupKey = None, setGPAMethodEntityID = None, setGradeMarkID = None, setGradeMarkPointSetIDClonedFrom = None, setPointSetEntityID = None, setRegularPoints = None, setRelationships = None, returnGradeMarkPointSetID = True, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/" + str(GradeMarkPointSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeMarkPointSet(EntityID = 1, setAddOnPoints = None, setEntityGroupKey = None, setGPAMethodEntityID = None, setGradeMarkID = None, setGradeMarkPointSetIDClonedFrom = None, setPointSetEntityID = None, setRegularPoints = None, setRelationships = None, returnGradeMarkPointSetID = True, returnAddOnPoints = False, returnCreatedTime = False, returnEntityGroupKey = False, returnGPAMethodEntityID = False, returnGradeMarkID = False, returnGradeMarkPointSetIDClonedFrom = False, returnModifiedTime = False, returnPointSetEntityID = False, returnRegularPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeMarkPointSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeMarkPointSet(GradeMarkPointSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSession(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionID = True, returnCreatedTime = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSession(GradeReportAcademicSessionID, EntityID = 1, returnGradeReportAcademicSessionID = True, returnCreatedTime = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(GradeReportAcademicSessionID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSession(GradeReportAcademicSessionID, EntityID = 1, setEarnedCredit = None, setEarnedCreditAttempted = None, setEarnedCreditsValue = None, setEntryDate = None, setGPAValue = None, setGradeLevelCode = None, setGradeReportAcademicSessionTemplateGroupID = None, setGradeReportStudentID = None, setHeaderDescription = None, setSchoolYearDescription = None, setSchoolYearID = None, setSortNumber = None, setWithdrawalDate = None, setRelationships = None, returnGradeReportAcademicSessionID = True, returnCreatedTime = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/" + str(GradeReportAcademicSessionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSession(EntityID = 1, setEarnedCredit = None, setEarnedCreditAttempted = None, setEarnedCreditsValue = None, setEntryDate = None, setGPAValue = None, setGradeLevelCode = None, setGradeReportAcademicSessionTemplateGroupID = None, setGradeReportStudentID = None, setHeaderDescription = None, setSchoolYearDescription = None, setSchoolYearID = None, setSortNumber = None, setWithdrawalDate = None, setRelationships = None, returnGradeReportAcademicSessionID = True, returnCreatedTime = False, returnEarnedCredit = False, returnEarnedCreditAttempted = False, returnEarnedCreditsValue = False, returnEntryDate = False, returnGPAValue = False, returnGradeLevelCode = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportStudentID = False, returnHeaderDescription = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSession/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSession(GradeReportAcademicSessionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSessionTemplate(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateID = True, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, EntityID = 1, returnGradeReportAcademicSessionTemplateID = True, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(GradeReportAcademicSessionTemplateID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, EntityID = 1, setBreakBySchoolYear = None, setCourseFilter = None, setGradeReportAcademicSessionTemplateGroupID = None, setHeaderDescription = None, setIncludeNonCreditEarningCourses = None, setSearchConditionFilter = None, setSortNumber = None, setUseSchoolYearDescending = None, setRelationships = None, returnGradeReportAcademicSessionTemplateID = True, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/" + str(GradeReportAcademicSessionTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSessionTemplate(EntityID = 1, setBreakBySchoolYear = None, setCourseFilter = None, setGradeReportAcademicSessionTemplateGroupID = None, setHeaderDescription = None, setIncludeNonCreditEarningCourses = None, setSearchConditionFilter = None, setSortNumber = None, setUseSchoolYearDescending = None, setRelationships = None, returnGradeReportAcademicSessionTemplateID = True, returnBreakBySchoolYear = False, returnCourseFilter = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnHeaderDescription = False, returnIncludeNonCreditEarningCourses = False, returnModifiedTime = False, returnSearchConditionFilter = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSchoolYearDescending = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSessionTemplate(GradeReportAcademicSessionTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSessionTemplateCourse(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateCourseID = True, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, EntityID = 1, returnGradeReportAcademicSessionTemplateCourseID = True, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(GradeReportAcademicSessionTemplateCourseID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, EntityID = 1, setCourseID = None, setGradeReportAcademicSessionTemplateCourseIDClonedFrom = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateCourseID = True, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/" + str(GradeReportAcademicSessionTemplateCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSessionTemplateCourse(EntityID = 1, setCourseID = None, setGradeReportAcademicSessionTemplateCourseIDClonedFrom = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateCourseID = True, returnCourseID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateCourseIDClonedFrom = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSessionTemplateCourse(GradeReportAcademicSessionTemplateCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSessionTemplateCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, EntityID = 1, returnGradeReportAcademicSessionTemplateCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(GradeReportAcademicSessionTemplateCourseGroupID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, EntityID = 1, setCourseGroupID = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/" + str(GradeReportAcademicSessionTemplateCourseGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSessionTemplateCourseGroup(EntityID = 1, setCourseGroupID = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateCourseGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSessionTemplateCourseGroup(GradeReportAcademicSessionTemplateCourseGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSessionTemplateGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateGradeLevelID = True, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, EntityID = 1, returnGradeReportAcademicSessionTemplateGradeLevelID = True, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(GradeReportAcademicSessionTemplateGradeLevelID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, EntityID = 1, setGradeLevelID = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateGradeLevelID = True, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/" + str(GradeReportAcademicSessionTemplateGradeLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSessionTemplateGradeLevel(EntityID = 1, setGradeLevelID = None, setGradeReportAcademicSessionTemplateID = None, setRelationships = None, returnGradeReportAcademicSessionTemplateGradeLevelID = True, returnCreatedTime = False, returnGradeLevelID = False, returnGradeReportAcademicSessionTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGradeLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSessionTemplateGradeLevel(GradeReportAcademicSessionTemplateGradeLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportAcademicSessionTemplateGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportAcademicSessionTemplateGroupID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, EntityID = 1, returnGradeReportAcademicSessionTemplateGroupID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(GradeReportAcademicSessionTemplateGroupID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, EntityID = 1, setDescription = None, setDistrictID = None, setGPABucketID = None, setGPAField = None, setGPAFieldCode = None, setGPAMethodID = None, setIncludeEarnedCredits = None, setIncludeGPA = None, setIncludeSchoolYearDescription = None, setRelationships = None, returnGradeReportAcademicSessionTemplateGroupID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/" + str(GradeReportAcademicSessionTemplateGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportAcademicSessionTemplateGroup(EntityID = 1, setDescription = None, setDistrictID = None, setGPABucketID = None, setGPAField = None, setGPAFieldCode = None, setGPAMethodID = None, setIncludeEarnedCredits = None, setIncludeGPA = None, setIncludeSchoolYearDescription = None, setRelationships = None, returnGradeReportAcademicSessionTemplateGroupID = True, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnGPABucketID = False, returnGPAField = False, returnGPAFieldCode = False, returnGPALabel1 = False, returnGPAMethodID = False, returnIncludeEarnedCredits = False, returnIncludeGPA = False, returnIncludeSchoolYearDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportAcademicSessionTemplateGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportAcademicSessionTemplateGroup(GradeReportAcademicSessionTemplateGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportColumnAttendanceCategory(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnAttendanceCategoryID = True, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, EntityID = 1, returnGradeReportColumnAttendanceCategoryID = True, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(GradeReportColumnAttendanceCategoryID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, EntityID = 1, setCategory = None, setCategoryCode = None, setGradeReportColumnAttendanceCategoryIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setRelationships = None, returnGradeReportColumnAttendanceCategoryID = True, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/" + str(GradeReportColumnAttendanceCategoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportColumnAttendanceCategory(EntityID = 1, setCategory = None, setCategoryCode = None, setGradeReportColumnAttendanceCategoryIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setRelationships = None, returnGradeReportColumnAttendanceCategoryID = True, returnCategory = False, returnCategoryCode = False, returnCreatedTime = False, returnGradeReportColumnAttendanceCategoryIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceCategory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportColumnAttendanceCategory(GradeReportColumnAttendanceCategoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportColumnAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnAttendanceTermID = True, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, EntityID = 1, returnGradeReportColumnAttendanceTermID = True, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(GradeReportColumnAttendanceTermID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, EntityID = 1, setAttendanceTermID = None, setGradeReportColumnAttendanceTermIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setRelationships = None, returnGradeReportColumnAttendanceTermID = True, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/" + str(GradeReportColumnAttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportColumnAttendanceTerm(EntityID = 1, setAttendanceTermID = None, setGradeReportColumnAttendanceTermIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setRelationships = None, returnGradeReportColumnAttendanceTermID = True, returnAttendanceTermID = False, returnCreatedTime = False, returnGradeReportColumnAttendanceTermIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportColumnAttendanceTerm(GradeReportColumnAttendanceTermID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportColumnGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGradeBucketID = True, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, EntityID = 1, returnGradeReportColumnGradeBucketID = True, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(GradeReportColumnGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, EntityID = 1, setGradeReportColumnGradeBucketIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setGradingPeriodGradeBucketID = None, setSortNumber = None, setRelationships = None, returnGradeReportColumnGradeBucketID = True, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/" + str(GradeReportColumnGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportColumnGradeBucket(EntityID = 1, setGradeReportColumnGradeBucketIDClonedFrom = None, setGradeReportColumnGroupColumnID = None, setGradingPeriodGradeBucketID = None, setSortNumber = None, setRelationships = None, returnGradeReportColumnGradeBucketID = True, returnCreatedTime = False, returnGradeReportColumnGradeBucketIDClonedFrom = False, returnGradeReportColumnGroupColumnID = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportColumnGradeBucket(GradeReportColumnGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportColumnGroup(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGroupID = True, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportColumnGroup(GradeReportColumnGroupID, EntityID = 1, returnGradeReportColumnGroupID = True, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(GradeReportColumnGroupID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportColumnGroup(GradeReportColumnGroupID, EntityID = 1, setAlwaysDisplayGradingColumns = None, setConfigDistrictYearID = None, setDescription = None, setGradeReportColumnGroupIDClonedFrom = None, setRelationships = None, returnGradeReportColumnGroupID = True, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/" + str(GradeReportColumnGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportColumnGroup(EntityID = 1, setAlwaysDisplayGradingColumns = None, setConfigDistrictYearID = None, setDescription = None, setGradeReportColumnGroupIDClonedFrom = None, setRelationships = None, returnGradeReportColumnGroupID = True, returnAlwaysDisplayGradingColumns = False, returnConfigDistrictYearID = False, returnCreatedTime = False, returnDescription = False, returnGradeReportColumnGroupIDClonedFrom = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportColumnGroup(GradeReportColumnGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportColumnGroupColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportColumnGroupColumnID = True, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, EntityID = 1, returnGradeReportColumnGroupColumnID = True, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(GradeReportColumnGroupColumnID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, EntityID = 1, setAttendanceOption = None, setAttendanceOptionCode = None, setColumnHeader = None, setColumnType = None, setColumnTypeCode = None, setContinueIfBlank = None, setGradeReportColumnGroupColumnIDClonedFrom = None, setGradeReportColumnGroupID = None, setSortNumber = None, setRelationships = None, returnGradeReportColumnGroupColumnID = True, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/" + str(GradeReportColumnGroupColumnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportColumnGroupColumn(EntityID = 1, setAttendanceOption = None, setAttendanceOptionCode = None, setColumnHeader = None, setColumnType = None, setColumnTypeCode = None, setContinueIfBlank = None, setGradeReportColumnGroupColumnIDClonedFrom = None, setGradeReportColumnGroupID = None, setSortNumber = None, setRelationships = None, returnGradeReportColumnGroupColumnID = True, returnAttendanceOption = False, returnAttendanceOptionCode = False, returnColumnHeader = False, returnColumnType = False, returnColumnTypeCode = False, returnContinueIfBlank = False, returnCreatedTime = False, returnGradeReportColumnGroupColumnIDClonedFrom = False, returnGradeReportColumnGroupID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportColumnGroupColumn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportColumnGroupColumn(GradeReportColumnGroupColumnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportEndorsementRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportEndorsementRowID = True, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportEndorsementRow(GradeReportEndorsementRowID, EntityID = 1, returnGradeReportEndorsementRowID = True, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(GradeReportEndorsementRowID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportEndorsementRow(GradeReportEndorsementRowID, EntityID = 1, setDescription = None, setGradeReportStudentID = None, setIsDistrictDefined = None, setSort1 = None, setSort2 = None, setStatus = None, setRelationships = None, returnGradeReportEndorsementRowID = True, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/" + str(GradeReportEndorsementRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportEndorsementRow(EntityID = 1, setDescription = None, setGradeReportStudentID = None, setIsDistrictDefined = None, setSort1 = None, setSort2 = None, setStatus = None, setRelationships = None, returnGradeReportEndorsementRowID = True, returnCreatedTime = False, returnDescription = False, returnGradeReportStudentID = False, returnIsDistrictDefined = False, returnModifiedTime = False, returnSort1 = False, returnSort2 = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportEndorsementRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportEndorsementRow(GradeReportEndorsementRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportGPARow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportGPARowID = True, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportGPARow(GradeReportGPARowID, EntityID = 1, returnGradeReportGPARowID = True, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(GradeReportGPARowID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportGPARow(GradeReportGPARowID, EntityID = 1, setDataColumn1 = None, setDataColumn2 = None, setDataColumn3 = None, setDataColumn4 = None, setDataColumn5 = None, setDataColumn6 = None, setDataColumn7 = None, setGPABucketDescription = None, setGPABucketID = None, setGPAMethodDescription = None, setGPAMethodID = None, setGradeReportAcademicSessionID = None, setGradeReportAcademicSessionSortNumber = None, setSortNumber = None, setRelationships = None, returnGradeReportGPARowID = True, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/" + str(GradeReportGPARowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportGPARow(EntityID = 1, setDataColumn1 = None, setDataColumn2 = None, setDataColumn3 = None, setDataColumn4 = None, setDataColumn5 = None, setDataColumn6 = None, setDataColumn7 = None, setGPABucketDescription = None, setGPABucketID = None, setGPAMethodDescription = None, setGPAMethodID = None, setGradeReportAcademicSessionID = None, setGradeReportAcademicSessionSortNumber = None, setSortNumber = None, setRelationships = None, returnGradeReportGPARowID = True, returnCreatedTime = False, returnDataColumn1 = False, returnDataColumn2 = False, returnDataColumn3 = False, returnDataColumn4 = False, returnDataColumn5 = False, returnDataColumn6 = False, returnDataColumn7 = False, returnGPABucketDescription = False, returnGPABucketID = False, returnGPAMethodDescription = False, returnGPAMethodID = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGPARow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportGPARow(GradeReportGPARowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportGradingScale(EntityID = 1, page = 1, pageSize = 100, returnGradeReportGradingScaleID = True, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportGradingScale(GradeReportGradingScaleID, EntityID = 1, returnGradeReportGradingScaleID = True, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(GradeReportGradingScaleID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportGradingScale(GradeReportGradingScaleID, EntityID = 1, setDisplayType = None, setDisplayTypeCode = None, setFreeformText = None, setGradeMarkCode = None, setGradeReportStudentID = None, setRangeHigh = None, setRangeLow = None, setSortNumber = None, setRelationships = None, returnGradeReportGradingScaleID = True, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/" + str(GradeReportGradingScaleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportGradingScale(EntityID = 1, setDisplayType = None, setDisplayTypeCode = None, setFreeformText = None, setGradeMarkCode = None, setGradeReportStudentID = None, setRangeHigh = None, setRangeLow = None, setSortNumber = None, setRelationships = None, returnGradeReportGradingScaleID = True, returnCreatedTime = False, returnDisplayType = False, returnDisplayTypeCode = False, returnFreeformText = False, returnGradeMarkCode = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnRangeHigh = False, returnRangeLow = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportGradingScale/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportGradingScale(GradeReportGradingScaleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowID = True, returnAttemptedCredit = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportRow(GradeReportRowID, EntityID = 1, returnGradeReportRowID = True, returnAttemptedCredit = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(GradeReportRowID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportRow(GradeReportRowID, EntityID = 1, setAttemptedCredit = None, setClassPeriod = None, setCourseSubjectDescription = None, setCourseTypeCode = None, setCourseTypeDescription = None, setDepartment = None, setDescription = None, setEarnedCredit = None, setGradeReportAcademicSessionID = None, setGradeReportAcademicSessionSortNumber = None, setGradeReportRowIDParent = None, setRowType = None, setRowTypeCode = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSort1 = None, setSort2 = None, setSort3 = None, setSort4 = None, setSortNumber = None, setStaffName = None, setStudentSectionID = None, setTotalPossibleCredit = None, setRelationships = None, returnGradeReportRowID = True, returnAttemptedCredit = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/" + str(GradeReportRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportRow(EntityID = 1, setAttemptedCredit = None, setClassPeriod = None, setCourseSubjectDescription = None, setCourseTypeCode = None, setCourseTypeDescription = None, setDepartment = None, setDescription = None, setEarnedCredit = None, setGradeReportAcademicSessionID = None, setGradeReportAcademicSessionSortNumber = None, setGradeReportRowIDParent = None, setRowType = None, setRowTypeCode = None, setSectionLengthSubsetCode = None, setSectionLengthSubsetDescription = None, setSort1 = None, setSort2 = None, setSort3 = None, setSort4 = None, setSortNumber = None, setStaffName = None, setStudentSectionID = None, setTotalPossibleCredit = None, setRelationships = None, returnGradeReportRowID = True, returnAttemptedCredit = False, returnClassPeriod = False, returnCourseSubjectDescription = False, returnCourseTypeCode = False, returnCourseTypeDescription = False, returnCreatedTime = False, returnDepartment = False, returnDescription = False, returnEarnedCredit = False, returnGradeReportAcademicSessionID = False, returnGradeReportAcademicSessionSortNumber = False, returnGradeReportRowIDParent = False, returnModifiedTime = False, returnRowType = False, returnRowTypeCode = False, returnSectionLengthSubsetCode = False, returnSectionLengthSubsetDescription = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnSortNumber = False, returnStaffName = False, returnStudentSectionID = False, returnTotalPossibleCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportRow(GradeReportRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportRowColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowColumnID = True, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportRowColumn(GradeReportRowColumnID, EntityID = 1, returnGradeReportRowColumnID = True, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(GradeReportRowColumnID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportRowColumn(GradeReportRowColumnID, EntityID = 1, setDisplayValue = None, setGradeMarkID = None, setGradeReportColumnGroupColumnID = None, setGradeReportRowID = None, setRelationships = None, returnGradeReportRowColumnID = True, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/" + str(GradeReportRowColumnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportRowColumn(EntityID = 1, setDisplayValue = None, setGradeMarkID = None, setGradeReportColumnGroupColumnID = None, setGradeReportRowID = None, setRelationships = None, returnGradeReportRowColumnID = True, returnCreatedTime = False, returnDisplayValue = False, returnGradeMarkID = False, returnGradeReportColumnGroupColumnID = False, returnGradeReportRowID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowColumn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportRowColumn(GradeReportRowColumnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportRowDetail(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRowDetailID = True, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportRowDetail(GradeReportRowDetailID, EntityID = 1, returnGradeReportRowDetailID = True, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(GradeReportRowDetailID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportRowDetail(GradeReportRowDetailID, EntityID = 1, setDetailData = None, setGradeReportRowID = None, setGradingPeriodLabel = None, setGradingPeriodSortNumber = None, setLabel = None, setSortNumber = None, setRelationships = None, returnGradeReportRowDetailID = True, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/" + str(GradeReportRowDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportRowDetail(EntityID = 1, setDetailData = None, setGradeReportRowID = None, setGradingPeriodLabel = None, setGradingPeriodSortNumber = None, setLabel = None, setSortNumber = None, setRelationships = None, returnGradeReportRowDetailID = True, returnCreatedTime = False, returnDetailData = False, returnGradeReportRowID = False, returnGradingPeriodLabel = False, returnGradingPeriodSortNumber = False, returnLabel = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRowDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportRowDetail(GradeReportRowDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportRunHistory(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRunHistoryID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportRunHistory(GradeReportRunHistoryID, EntityID = 1, returnGradeReportRunHistoryID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(GradeReportRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportRunHistory(GradeReportRunHistoryID, EntityID = 1, setAddressLine1 = None, setAddressLine2 = None, setCEEBACT = None, setCity = None, setCode = None, setEntityID = None, setFamilyPrintType = None, setFamilyPrintTypeCode = None, setFaxNumber = None, setFooterMessage = None, setFormattedFullAddress = None, setGradeReportTemplateID = None, setIsTexasTranscript = None, setName = None, setOverwriteExistingReportCard = None, setParameterDescription = None, setPhoneNumber = None, setPostalCode = None, setPostReportCardToFASA = None, setPrintCompletedGradingPeriodComments = None, setReportCardFileName = None, setRequireFamilyAccessElectronicSignature = None, setStateProvince = None, setStatusType = None, setStatusTypeCode = None, setRelationships = None, returnGradeReportRunHistoryID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/" + str(GradeReportRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportRunHistory(EntityID = 1, setAddressLine1 = None, setAddressLine2 = None, setCEEBACT = None, setCity = None, setCode = None, setEntityID = None, setFamilyPrintType = None, setFamilyPrintTypeCode = None, setFaxNumber = None, setFooterMessage = None, setFormattedFullAddress = None, setGradeReportTemplateID = None, setIsTexasTranscript = None, setName = None, setOverwriteExistingReportCard = None, setParameterDescription = None, setPhoneNumber = None, setPostalCode = None, setPostReportCardToFASA = None, setPrintCompletedGradingPeriodComments = None, setReportCardFileName = None, setRequireFamilyAccessElectronicSignature = None, setStateProvince = None, setStatusType = None, setStatusTypeCode = None, setRelationships = None, returnGradeReportRunHistoryID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnCEEBACT = False, returnCity = False, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFaxNumber = False, returnFooterMessage = False, returnFormattedFullAddress = False, returnGradeReportTemplateID = False, returnIsTexasTranscript = False, returnModifiedTime = False, returnName = False, returnOverwriteExistingReportCard = False, returnParameterDescription = False, returnPhoneNumber = False, returnPostalCode = False, returnPostReportCardToFASA = False, returnPrintCompletedGradingPeriodComments = False, returnReportCardFileName = False, returnRequireFamilyAccessElectronicSignature = False, returnStateProvince = False, returnStatusType = False, returnStatusTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportRunHistory(GradeReportRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportRunHistoryAttachment(EntityID = 1, page = 1, pageSize = 100, returnGradeReportRunHistoryAttachmentID = True, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, EntityID = 1, returnGradeReportRunHistoryAttachmentID = True, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(GradeReportRunHistoryAttachmentID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, EntityID = 1, setAttachmentID = None, setGradeReportRunHistoryID = None, setGuardianSignedTime = None, setNameIDGuardianSignedBy = None, setStudentID = None, setRelationships = None, returnGradeReportRunHistoryAttachmentID = True, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/" + str(GradeReportRunHistoryAttachmentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportRunHistoryAttachment(EntityID = 1, setAttachmentID = None, setGradeReportRunHistoryID = None, setGuardianSignedTime = None, setNameIDGuardianSignedBy = None, setStudentID = None, setRelationships = None, returnGradeReportRunHistoryAttachmentID = True, returnAttachmentCanBeViewedByStudentFamilyFamilyAccess = False, returnAttachmentID = False, returnCreatedTime = False, returnGradeReportRunHistoryID = False, returnGuardianSignedTime = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnSignedByGuardian = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportRunHistoryAttachment/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportRunHistoryAttachment(GradeReportRunHistoryAttachmentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportStudent(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportStudent(GradeReportStudentID, EntityID = 1, returnGradeReportStudentID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(GradeReportStudentID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportStudent(GradeReportStudentID, EntityID = 1, setAddressLine1 = None, setAddressLine2 = None, setAdvisorName = None, setBirthDate = None, setCity = None, setDoubleColumnHeaderField1 = None, setDoubleColumnHeaderField10 = None, setDoubleColumnHeaderField2 = None, setDoubleColumnHeaderField3 = None, setDoubleColumnHeaderField4 = None, setDoubleColumnHeaderField5 = None, setDoubleColumnHeaderField6 = None, setDoubleColumnHeaderField7 = None, setDoubleColumnHeaderField8 = None, setDoubleColumnHeaderField9 = None, setEmailAddress = None, setEthnicityAndRace = None, setFirstName = None, setFormattedFullAddress = None, setFormattedName = None, setGender = None, setGenderCode = None, setGradeReportRunHistoryID = None, setGraduationDate = None, setHomeroom = None, setLastName = None, setMiddleName = None, setNameIDPrimaryGuardian = None, setNameSuffix = None, setNameTitle = None, setPostalCode = None, setPrimaryGuardianEmailAddress = None, setPrimaryGuardianFirstName = None, setPrimaryGuardianFormattedName = None, setPrimaryGuardianLastName = None, setPrimaryGuardianMiddleName = None, setPrimaryGuardianNameSuffix = None, setPrimaryGuardianNameTitle = None, setPrimaryGuardianPhoneNumber = None, setPromotionStatus = None, setPromotionStatusCode = None, setSingleColumnHeaderField1 = None, setSingleColumnHeaderField2 = None, setSingleColumnHeaderField3 = None, setSingleColumnHeaderField4 = None, setSingleColumnHeaderField5 = None, setSort1 = None, setSort2 = None, setSort3 = None, setSort4 = None, setStateProvince = None, setStudentFamilyID = None, setStudentFamilyRank = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnGradeReportStudentID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/" + str(GradeReportStudentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportStudent(EntityID = 1, setAddressLine1 = None, setAddressLine2 = None, setAdvisorName = None, setBirthDate = None, setCity = None, setDoubleColumnHeaderField1 = None, setDoubleColumnHeaderField10 = None, setDoubleColumnHeaderField2 = None, setDoubleColumnHeaderField3 = None, setDoubleColumnHeaderField4 = None, setDoubleColumnHeaderField5 = None, setDoubleColumnHeaderField6 = None, setDoubleColumnHeaderField7 = None, setDoubleColumnHeaderField8 = None, setDoubleColumnHeaderField9 = None, setEmailAddress = None, setEthnicityAndRace = None, setFirstName = None, setFormattedFullAddress = None, setFormattedName = None, setGender = None, setGenderCode = None, setGradeReportRunHistoryID = None, setGraduationDate = None, setHomeroom = None, setLastName = None, setMiddleName = None, setNameIDPrimaryGuardian = None, setNameSuffix = None, setNameTitle = None, setPostalCode = None, setPrimaryGuardianEmailAddress = None, setPrimaryGuardianFirstName = None, setPrimaryGuardianFormattedName = None, setPrimaryGuardianLastName = None, setPrimaryGuardianMiddleName = None, setPrimaryGuardianNameSuffix = None, setPrimaryGuardianNameTitle = None, setPrimaryGuardianPhoneNumber = None, setPromotionStatus = None, setPromotionStatusCode = None, setSingleColumnHeaderField1 = None, setSingleColumnHeaderField2 = None, setSingleColumnHeaderField3 = None, setSingleColumnHeaderField4 = None, setSingleColumnHeaderField5 = None, setSort1 = None, setSort2 = None, setSort3 = None, setSort4 = None, setStateProvince = None, setStudentFamilyID = None, setStudentFamilyRank = None, setStudentID = None, setStudentNumber = None, setRelationships = None, returnGradeReportStudentID = True, returnAddressLine1 = False, returnAddressLine2 = False, returnAdvisorName = False, returnBirthDate = False, returnCity = False, returnCreatedTime = False, returnDoubleColumnHeaderField1 = False, returnDoubleColumnHeaderField10 = False, returnDoubleColumnHeaderField2 = False, returnDoubleColumnHeaderField3 = False, returnDoubleColumnHeaderField4 = False, returnDoubleColumnHeaderField5 = False, returnDoubleColumnHeaderField6 = False, returnDoubleColumnHeaderField7 = False, returnDoubleColumnHeaderField8 = False, returnDoubleColumnHeaderField9 = False, returnEmailAddress = False, returnEthnicityAndRace = False, returnFirstName = False, returnFormattedFullAddress = False, returnFormattedName = False, returnGender = False, returnGenderCode = False, returnGradeReportRunHistoryID = False, returnGraduationDate = False, returnHomeroom = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameIDPrimaryGuardian = False, returnNameSuffix = False, returnNameTitle = False, returnPostalCode = False, returnPrimaryGuardianEmailAddress = False, returnPrimaryGuardianFirstName = False, returnPrimaryGuardianFormattedName = False, returnPrimaryGuardianLastName = False, returnPrimaryGuardianMiddleName = False, returnPrimaryGuardianNameSuffix = False, returnPrimaryGuardianNameTitle = False, returnPrimaryGuardianPhoneNumber = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnSingleColumnHeaderField1 = False, returnSingleColumnHeaderField2 = False, returnSingleColumnHeaderField3 = False, returnSingleColumnHeaderField4 = False, returnSingleColumnHeaderField5 = False, returnSort1 = False, returnSort2 = False, returnSort3 = False, returnSort4 = False, returnStateProvince = False, returnStudentFamilyID = False, returnStudentFamilyRank = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportStudent(GradeReportStudentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportStudentAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentAttendanceTermID = True, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, EntityID = 1, returnGradeReportStudentAttendanceTermID = True, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(GradeReportStudentAttendanceTermID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, EntityID = 1, setAttendanceTermCode = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysTardy = None, setDaysUnexcused = None, setGradeReportAcademicSessionID = None, setSortNumber = None, setRelationships = None, returnGradeReportStudentAttendanceTermID = True, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/" + str(GradeReportStudentAttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportStudentAttendanceTerm(EntityID = 1, setAttendanceTermCode = None, setDaysAbsent = None, setDaysExcused = None, setDaysOther = None, setDaysTardy = None, setDaysUnexcused = None, setGradeReportAcademicSessionID = None, setSortNumber = None, setRelationships = None, returnGradeReportStudentAttendanceTermID = True, returnAttendanceTermCode = False, returnCreatedTime = False, returnDaysAbsent = False, returnDaysExcused = False, returnDaysOther = False, returnDaysTardy = False, returnDaysUnexcused = False, returnGradeReportAcademicSessionID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportStudentAttendanceTerm(GradeReportStudentAttendanceTermID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportStudentTestRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentTestRowID = True, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportStudentTestRow(GradeReportStudentTestRowID, EntityID = 1, returnGradeReportStudentTestRowID = True, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(GradeReportStudentTestRowID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportStudentTestRow(GradeReportStudentTestRowID, EntityID = 1, setDateTaken = None, setGradeReportStudentTestTypeID = None, setSortNumber = None, setTestColumn1 = None, setTestColumn10 = None, setTestColumn2 = None, setTestColumn3 = None, setTestColumn4 = None, setTestColumn5 = None, setTestColumn6 = None, setTestColumn7 = None, setTestColumn8 = None, setTestColumn9 = None, setRelationships = None, returnGradeReportStudentTestRowID = True, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/" + str(GradeReportStudentTestRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportStudentTestRow(EntityID = 1, setDateTaken = None, setGradeReportStudentTestTypeID = None, setSortNumber = None, setTestColumn1 = None, setTestColumn10 = None, setTestColumn2 = None, setTestColumn3 = None, setTestColumn4 = None, setTestColumn5 = None, setTestColumn6 = None, setTestColumn7 = None, setTestColumn8 = None, setTestColumn9 = None, setRelationships = None, returnGradeReportStudentTestRowID = True, returnCreatedTime = False, returnDateTaken = False, returnGradeReportStudentTestTypeID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumn1 = False, returnTestColumn10 = False, returnTestColumn2 = False, returnTestColumn3 = False, returnTestColumn4 = False, returnTestColumn5 = False, returnTestColumn6 = False, returnTestColumn7 = False, returnTestColumn8 = False, returnTestColumn9 = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportStudentTestRow(GradeReportStudentTestRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportStudentTestType(EntityID = 1, page = 1, pageSize = 100, returnGradeReportStudentTestTypeID = True, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportStudentTestType(GradeReportStudentTestTypeID, EntityID = 1, returnGradeReportStudentTestTypeID = True, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(GradeReportStudentTestTypeID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportStudentTestType(GradeReportStudentTestTypeID, EntityID = 1, setGradeReportStudentID = None, setSortNumber = None, setTestColumnHeader1 = None, setTestColumnHeader10 = None, setTestColumnHeader2 = None, setTestColumnHeader3 = None, setTestColumnHeader4 = None, setTestColumnHeader5 = None, setTestColumnHeader6 = None, setTestColumnHeader7 = None, setTestColumnHeader8 = None, setTestColumnHeader9 = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnGradeReportStudentTestTypeID = True, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/" + str(GradeReportStudentTestTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportStudentTestType(EntityID = 1, setGradeReportStudentID = None, setSortNumber = None, setTestColumnHeader1 = None, setTestColumnHeader10 = None, setTestColumnHeader2 = None, setTestColumnHeader3 = None, setTestColumnHeader4 = None, setTestColumnHeader5 = None, setTestColumnHeader6 = None, setTestColumnHeader7 = None, setTestColumnHeader8 = None, setTestColumnHeader9 = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnGradeReportStudentTestTypeID = True, returnCreatedTime = False, returnGradeReportStudentID = False, returnModifiedTime = False, returnSortNumber = False, returnTestColumnHeader1 = False, returnTestColumnHeader10 = False, returnTestColumnHeader2 = False, returnTestColumnHeader3 = False, returnTestColumnHeader4 = False, returnTestColumnHeader5 = False, returnTestColumnHeader6 = False, returnTestColumnHeader7 = False, returnTestColumnHeader8 = False, returnTestColumnHeader9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportStudentTestType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportStudentTestType(GradeReportStudentTestTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplate(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateID = True, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplate(GradeReportTemplateID, EntityID = 1, returnGradeReportTemplateID = True, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(GradeReportTemplateID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplate(GradeReportTemplateID, EntityID = 1, setAcademicSessionType = None, setAcademicSessionTypeCode = None, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBlankSignatureLabel = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setCommentPrintType = None, setCommentPrintTypeCode = None, setConfigEntityYearID = None, setCourseDescriptionFormat = None, setCourseDescriptionFormatCode = None, setCourseFilter = None, setCourseFilterCode = None, setDescription = None, setDisplayPeriodCodeSort1 = None, setDisplayPeriodCodeSort2 = None, setDisplayPeriodCodeSort3 = None, setDisplayPeriodCodeSort4 = None, setFamilyPrintType = None, setFamilyPrintTypeCode = None, setFreeFormGradingLegend = None, setGPAField1 = None, setGPAField1Code = None, setGPAField2 = None, setGPAField2Code = None, setGPAField3 = None, setGPAField3Code = None, setGPAField4 = None, setGPAField4Code = None, setGPAField5 = None, setGPAField5Code = None, setGPAField6 = None, setGPAField6Code = None, setGPAField7 = None, setGPAField7Code = None, setGradeReportAcademicSessionTemplateGroupID = None, setGradeReportColumnGroupIDSecondary = None, setGradeReportTemplateIDClonedFrom = None, setGradingSort = None, setGradingSortCode = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setIncludeCurrentYearClasses = None, setIncludeInProgressGrades = None, setIncludePhoneInEntityAddress = None, setIncludePhoneInGuardianAddress = None, setIncludeTranscriptNotes = None, setIncludeTransferCourses = None, setMediaIDLogo = None, setNoReceivingFamily = None, setOfficialSignatureLabel = None, setPrintAllCourseRowHeaders = None, setPrintAttendanceTotals = None, setPrintBlankSignatureLine = None, setPrintComments = None, setPrintElectronicSignature = None, setPrintEndorsements = None, setPrintFreeFormComments = None, setPrintGPA = None, setPrintGradeScaleAtTop = None, setPrintHighFrequencyWords = None, setPrintIndividualAttendanceTerms = None, setPrintLettersAndSounds = None, setPrintYearToDateTotals = None, setReceivesForms = None, setReportRunInfoID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setStudentSort1 = None, setStudentSort1Code = None, setStudentSort2 = None, setStudentSort2Code = None, setStudentSort3 = None, setStudentSort3Code = None, setStudentSort4 = None, setStudentSort4Code = None, setTeacherNameFormat = None, setTeacherNameFormatCode = None, setTemplateType = None, setTemplateTypeCode = None, setUseFreeFormGradingLegend = None, setUseGradeMarkDescriptionGradingLegend = None, setUseGradeMarkRangeGradingLegend = None, setUseStudentSectionLinking = None, setRelationships = None, returnGradeReportTemplateID = True, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/" + str(GradeReportTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplate(EntityID = 1, setAcademicSessionType = None, setAcademicSessionTypeCode = None, setAdvisorNameFormat = None, setAdvisorNameFormatCode = None, setBlankSignatureLabel = None, setColumnHeaderLabel1 = None, setColumnHeaderLabel10 = None, setColumnHeaderLabel2 = None, setColumnHeaderLabel3 = None, setColumnHeaderLabel4 = None, setColumnHeaderLabel5 = None, setColumnHeaderLabel6 = None, setColumnHeaderLabel7 = None, setColumnHeaderLabel8 = None, setColumnHeaderLabel9 = None, setCommentPrintType = None, setCommentPrintTypeCode = None, setConfigEntityYearID = None, setCourseDescriptionFormat = None, setCourseDescriptionFormatCode = None, setCourseFilter = None, setCourseFilterCode = None, setDescription = None, setDisplayPeriodCodeSort1 = None, setDisplayPeriodCodeSort2 = None, setDisplayPeriodCodeSort3 = None, setDisplayPeriodCodeSort4 = None, setFamilyPrintType = None, setFamilyPrintTypeCode = None, setFreeFormGradingLegend = None, setGPAField1 = None, setGPAField1Code = None, setGPAField2 = None, setGPAField2Code = None, setGPAField3 = None, setGPAField3Code = None, setGPAField4 = None, setGPAField4Code = None, setGPAField5 = None, setGPAField5Code = None, setGPAField6 = None, setGPAField6Code = None, setGPAField7 = None, setGPAField7Code = None, setGradeReportAcademicSessionTemplateGroupID = None, setGradeReportColumnGroupIDSecondary = None, setGradeReportTemplateIDClonedFrom = None, setGradingSort = None, setGradingSortCode = None, setGuardianNameFormat = None, setGuardianNameFormatCode = None, setIncludeCurrentYearClasses = None, setIncludeInProgressGrades = None, setIncludePhoneInEntityAddress = None, setIncludePhoneInGuardianAddress = None, setIncludeTranscriptNotes = None, setIncludeTransferCourses = None, setMediaIDLogo = None, setNoReceivingFamily = None, setOfficialSignatureLabel = None, setPrintAllCourseRowHeaders = None, setPrintAttendanceTotals = None, setPrintBlankSignatureLine = None, setPrintComments = None, setPrintElectronicSignature = None, setPrintEndorsements = None, setPrintFreeFormComments = None, setPrintGPA = None, setPrintGradeScaleAtTop = None, setPrintHighFrequencyWords = None, setPrintIndividualAttendanceTerms = None, setPrintLettersAndSounds = None, setPrintYearToDateTotals = None, setReceivesForms = None, setReportRunInfoID = None, setStudentNameFormat = None, setStudentNameFormatCode = None, setStudentSort1 = None, setStudentSort1Code = None, setStudentSort2 = None, setStudentSort2Code = None, setStudentSort3 = None, setStudentSort3Code = None, setStudentSort4 = None, setStudentSort4Code = None, setTeacherNameFormat = None, setTeacherNameFormatCode = None, setTemplateType = None, setTemplateTypeCode = None, setUseFreeFormGradingLegend = None, setUseGradeMarkDescriptionGradingLegend = None, setUseGradeMarkRangeGradingLegend = None, setUseStudentSectionLinking = None, setRelationships = None, returnGradeReportTemplateID = True, returnAcademicSessionType = False, returnAcademicSessionTypeCode = False, returnAdvisorNameFormat = False, returnAdvisorNameFormatCode = False, returnBlankSignatureLabel = False, returnColumnHeaderLabel1 = False, returnColumnHeaderLabel10 = False, returnColumnHeaderLabel2 = False, returnColumnHeaderLabel3 = False, returnColumnHeaderLabel4 = False, returnColumnHeaderLabel5 = False, returnColumnHeaderLabel6 = False, returnColumnHeaderLabel7 = False, returnColumnHeaderLabel8 = False, returnColumnHeaderLabel9 = False, returnCommentPrintType = False, returnCommentPrintTypeCode = False, returnConfigEntityYearID = False, returnCourseDescriptionFormat = False, returnCourseDescriptionFormatCode = False, returnCourseFilter = False, returnCourseFilterCode = False, returnCreatedTime = False, returnDescription = False, returnDisplayPeriodCodeSort1 = False, returnDisplayPeriodCodeSort2 = False, returnDisplayPeriodCodeSort3 = False, returnDisplayPeriodCodeSort4 = False, returnFamilyPrintType = False, returnFamilyPrintTypeCode = False, returnFreeFormGradingLegend = False, returnGPAField1 = False, returnGPAField1Code = False, returnGPAField2 = False, returnGPAField2Code = False, returnGPAField3 = False, returnGPAField3Code = False, returnGPAField4 = False, returnGPAField4Code = False, returnGPAField5 = False, returnGPAField5Code = False, returnGPAField6 = False, returnGPAField6Code = False, returnGPAField7 = False, returnGPAField7Code = False, returnGPALabel1 = False, returnGPALabel2 = False, returnGPALabel3 = False, returnGPALabel4 = False, returnGPALabel5 = False, returnGPALabel6 = False, returnGPALabel7 = False, returnGradeReportAcademicSessionTemplateGroupID = False, returnGradeReportColumnGroupIDSecondary = False, returnGradeReportTemplateIDClonedFrom = False, returnGradingSort = False, returnGradingSortCode = False, returnGuardianNameFormat = False, returnGuardianNameFormatCode = False, returnHasLogo = False, returnHideSignatureSection = False, returnIncludeCurrentYearClasses = False, returnIncludeInProgressGrades = False, returnIncludePhoneInEntityAddress = False, returnIncludePhoneInGuardianAddress = False, returnIncludeTranscriptNotes = False, returnIncludeTransferCourses = False, returnMediaIDLogo = False, returnModifiedTime = False, returnNoReceivingFamily = False, returnOfficialSignatureLabel = False, returnPrintAllCourseRowHeaders = False, returnPrintAttendanceTotals = False, returnPrintBlankSignatureLine = False, returnPrintComments = False, returnPrintElectronicSignature = False, returnPrintEndorsements = False, returnPrintFreeFormComments = False, returnPrintGPA = False, returnPrintGradeScaleAtTop = False, returnPrintHighFrequencyWords = False, returnPrintIndividualAttendanceTerms = False, returnPrintLettersAndSounds = False, returnPrintYearToDateTotals = False, returnReceivesForms = False, returnReportRunInfoID = False, returnStudentNameFormat = False, returnStudentNameFormatCode = False, returnStudentSort1 = False, returnStudentSort1Code = False, returnStudentSort2 = False, returnStudentSort2Code = False, returnStudentSort3 = False, returnStudentSort3Code = False, returnStudentSort4 = False, returnStudentSort4Code = False, returnTeacherNameFormat = False, returnTeacherNameFormatCode = False, returnTemplateType = False, returnTemplateTypeCode = False, returnUseFreeFormGradingLegend = False, returnUseFullGPASection = False, returnUseFullGradesSection = False, returnUseGradeMarkDescriptionGradingLegend = False, returnUseGradeMarkRangeGradingLegend = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStudentSectionLinking = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplate(GradeReportTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateCommentSet(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateCommentSetID = True, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, EntityID = 1, returnGradeReportTemplateCommentSetID = True, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(GradeReportTemplateCommentSetID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, EntityID = 1, setCommentSetID = None, setGradeReportTemplateCommentSetIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateCommentSetID = True, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/" + str(GradeReportTemplateCommentSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateCommentSet(EntityID = 1, setCommentSetID = None, setGradeReportTemplateCommentSetIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateCommentSetID = True, returnCommentSetID = False, returnCreatedTime = False, returnGradeReportTemplateCommentSetIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateCommentSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateCommentSet(GradeReportTemplateCommentSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateEndorsement(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateEndorsementID = True, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, EntityID = 1, returnGradeReportTemplateEndorsementID = True, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(GradeReportTemplateEndorsementID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, EntityID = 1, setEndorsementID = None, setGradeReportTemplateID = None, setGradYearHigh = None, setGradYearLow = None, setOrderNumber = None, setRelationships = None, returnGradeReportTemplateEndorsementID = True, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/" + str(GradeReportTemplateEndorsementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateEndorsement(EntityID = 1, setEndorsementID = None, setGradeReportTemplateID = None, setGradYearHigh = None, setGradYearLow = None, setOrderNumber = None, setRelationships = None, returnGradeReportTemplateEndorsementID = True, returnCreatedTime = False, returnEndorsementID = False, returnGradeReportTemplateID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateEndorsement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateEndorsement(GradeReportTemplateEndorsementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateGPABucket(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGPABucketID = True, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, EntityID = 1, returnGradeReportTemplateGPABucketID = True, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(GradeReportTemplateGPABucketID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, EntityID = 1, setGPABucketID = None, setGradeReportTemplateGPABucketIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateGPABucketID = True, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/" + str(GradeReportTemplateGPABucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateGPABucket(EntityID = 1, setGPABucketID = None, setGradeReportTemplateGPABucketIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateGPABucketID = True, returnCreatedTime = False, returnGPABucketID = False, returnGradeReportTemplateGPABucketIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPABucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateGPABucket(GradeReportTemplateGPABucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGPAMethodID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, EntityID = 1, returnGradeReportTemplateGPAMethodID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(GradeReportTemplateGPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, EntityID = 1, setGPAMethodID = None, setGradeReportTemplateGPAMethodIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateGPAMethodID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/" + str(GradeReportTemplateGPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateGPAMethod(EntityID = 1, setGPAMethodID = None, setGradeReportTemplateGPAMethodIDClonedFrom = None, setGradeReportTemplateID = None, setRelationships = None, returnGradeReportTemplateGPAMethodID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeReportTemplateGPAMethodIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateGPAMethod(GradeReportTemplateGPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateGradeMark(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, EntityID = 1, returnGradeReportTemplateGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(GradeReportTemplateGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, EntityID = 1, setGradeMarkID = None, setGradeReportTemplateGradeMarkIDClonedFrom = None, setGradeReportTemplateID = None, setType = None, setTypeCode = None, setRelationships = None, returnGradeReportTemplateGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/" + str(GradeReportTemplateGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateGradeMark(EntityID = 1, setGradeMarkID = None, setGradeReportTemplateGradeMarkIDClonedFrom = None, setGradeReportTemplateID = None, setType = None, setTypeCode = None, setRelationships = None, returnGradeReportTemplateGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnGradeReportTemplateGradeMarkIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateGradeMark(GradeReportTemplateGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateHeaderColumn(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateHeaderColumnID = True, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, EntityID = 1, returnGradeReportTemplateHeaderColumnID = True, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(GradeReportTemplateHeaderColumnID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, EntityID = 1, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setGPABucketID = None, setGPAMethodID = None, setGradeReportTemplateHeaderColumnIDClonedFrom = None, setGradeReportTemplateHeaderRowID = None, setLabelOverride = None, setRankMethodID = None, setSortNumber = None, setRelationships = None, returnGradeReportTemplateHeaderColumnID = True, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/" + str(GradeReportTemplateHeaderColumnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateHeaderColumn(EntityID = 1, setFieldType = None, setFieldTypeCode = None, setFreeformText = None, setGPABucketID = None, setGPAMethodID = None, setGradeReportTemplateHeaderColumnIDClonedFrom = None, setGradeReportTemplateHeaderRowID = None, setLabelOverride = None, setRankMethodID = None, setSortNumber = None, setRelationships = None, returnGradeReportTemplateHeaderColumnID = True, returnCreatedTime = False, returnFieldType = False, returnFieldTypeCode = False, returnFreeformText = False, returnGPABucketID = False, returnGPAMethodID = False, returnGradeReportTemplateHeaderColumnIDClonedFrom = False, returnGradeReportTemplateHeaderRowID = False, returnLabelOverride = False, returnModifiedTime = False, returnRankMethodID = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderColumn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateHeaderColumn(GradeReportTemplateHeaderColumnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateHeaderRow(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, EntityID = 1, returnGradeReportTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(GradeReportTemplateHeaderRowID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, EntityID = 1, setColumnCount = None, setGradeReportTemplateHeaderRowIDClonedFrom = None, setGradeReportTemplateID = None, setSortNumber = None, setRelationships = None, returnGradeReportTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/" + str(GradeReportTemplateHeaderRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateHeaderRow(EntityID = 1, setColumnCount = None, setGradeReportTemplateHeaderRowIDClonedFrom = None, setGradeReportTemplateID = None, setSortNumber = None, setRelationships = None, returnGradeReportTemplateHeaderRowID = True, returnColumnCount = False, returnCreatedTime = False, returnGradeReportTemplateHeaderRowIDClonedFrom = False, returnGradeReportTemplateID = False, returnModifiedTime = False, returnSortNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateHeaderRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateHeaderRow(GradeReportTemplateHeaderRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradeReportTemplateTestType(EntityID = 1, page = 1, pageSize = 100, returnGradeReportTemplateTestTypeID = True, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradeReportTemplateTestType(GradeReportTemplateTestTypeID, EntityID = 1, returnGradeReportTemplateTestTypeID = True, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(GradeReportTemplateTestTypeID), verb = "get", return_params_list = return_params_list)

def modifyGradeReportTemplateTestType(GradeReportTemplateTestTypeID, EntityID = 1, setFieldGUIDTestColumn1 = None, setFieldGUIDTestColumn10 = None, setFieldGUIDTestColumn2 = None, setFieldGUIDTestColumn3 = None, setFieldGUIDTestColumn4 = None, setFieldGUIDTestColumn5 = None, setFieldGUIDTestColumn6 = None, setFieldGUIDTestColumn7 = None, setFieldGUIDTestColumn8 = None, setFieldGUIDTestColumn9 = None, setGradeReportTemplateID = None, setGradeReportTemplateTestTypeIDClonedFrom = None, setPrintHighestScoreOnly = None, setSortNumber = None, setTestColumnHeaderOverride1 = None, setTestColumnHeaderOverride10 = None, setTestColumnHeaderOverride2 = None, setTestColumnHeaderOverride3 = None, setTestColumnHeaderOverride4 = None, setTestColumnHeaderOverride5 = None, setTestColumnHeaderOverride6 = None, setTestColumnHeaderOverride7 = None, setTestColumnHeaderOverride8 = None, setTestColumnHeaderOverride9 = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnGradeReportTemplateTestTypeID = True, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/" + str(GradeReportTemplateTestTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradeReportTemplateTestType(EntityID = 1, setFieldGUIDTestColumn1 = None, setFieldGUIDTestColumn10 = None, setFieldGUIDTestColumn2 = None, setFieldGUIDTestColumn3 = None, setFieldGUIDTestColumn4 = None, setFieldGUIDTestColumn5 = None, setFieldGUIDTestColumn6 = None, setFieldGUIDTestColumn7 = None, setFieldGUIDTestColumn8 = None, setFieldGUIDTestColumn9 = None, setGradeReportTemplateID = None, setGradeReportTemplateTestTypeIDClonedFrom = None, setPrintHighestScoreOnly = None, setSortNumber = None, setTestColumnHeaderOverride1 = None, setTestColumnHeaderOverride10 = None, setTestColumnHeaderOverride2 = None, setTestColumnHeaderOverride3 = None, setTestColumnHeaderOverride4 = None, setTestColumnHeaderOverride5 = None, setTestColumnHeaderOverride6 = None, setTestColumnHeaderOverride7 = None, setTestColumnHeaderOverride8 = None, setTestColumnHeaderOverride9 = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setRelationships = None, returnGradeReportTemplateTestTypeID = True, returnCreatedTime = False, returnFieldGUIDTestColumn1 = False, returnFieldGUIDTestColumn10 = False, returnFieldGUIDTestColumn2 = False, returnFieldGUIDTestColumn3 = False, returnFieldGUIDTestColumn4 = False, returnFieldGUIDTestColumn5 = False, returnFieldGUIDTestColumn6 = False, returnFieldGUIDTestColumn7 = False, returnFieldGUIDTestColumn8 = False, returnFieldGUIDTestColumn9 = False, returnGradeReportTemplateID = False, returnGradeReportTemplateTestTypeIDClonedFrom = False, returnModifiedTime = False, returnPrintHighestScoreOnly = False, returnSortNumber = False, returnTestColumnHeaderOverride1 = False, returnTestColumnHeaderOverride10 = False, returnTestColumnHeaderOverride2 = False, returnTestColumnHeaderOverride3 = False, returnTestColumnHeaderOverride4 = False, returnTestColumnHeaderOverride5 = False, returnTestColumnHeaderOverride6 = False, returnTestColumnHeaderOverride7 = False, returnTestColumnHeaderOverride8 = False, returnTestColumnHeaderOverride9 = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradeReportTemplateTestType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradeReportTemplateTestType(GradeReportTemplateTestTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodID = True, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradingPeriod(GradingPeriodID, EntityID = 1, returnGradingPeriodID = True, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(GradingPeriodID), verb = "get", return_params_list = return_params_list)

def modifyGradingPeriod(GradingPeriodID, EntityID = 1, setDateOverrideTeacherGracePeriod = None, setDescription = None, setEndDate = None, setEntityGroupKey = None, setGradingPeriodIDClonedFrom = None, setGradingPeriodSetID = None, setNumber = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnGradingPeriodID = True, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/" + str(GradingPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradingPeriod(EntityID = 1, setDateOverrideTeacherGracePeriod = None, setDescription = None, setEndDate = None, setEntityGroupKey = None, setGradingPeriodIDClonedFrom = None, setGradingPeriodSetID = None, setNumber = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnGradingPeriodID = True, returnAfterSectionLengthEndLastGradingPeriod = False, returnBeforeSectionLengthStartFirstGradingPeriod = False, returnCalculatedEndDateWithExtension = False, returnClosedGradingPeriodGradeChangeID = False, returnClosedGradingPeriodGradeChangeIDForNotReviewedRequests = False, returnCompletedFieldText = False, returnCompletedText = False, returnCreatedTime = False, returnCurrentActiveStatus = False, returnDateOverrideTeacherGracePeriod = False, returnDateOverrideTeacherGracePeriodDisplay = False, returnDescription = False, returnDisplayAssignments = False, returnDisplayGradeBuckets = False, returnEndDate = False, returnEndDateCopy = False, returnEntityGroupKey = False, returnExtendedEndDateGreaterThanToday = False, returnExtensionDays = False, returnExtensionEndTime = False, returnGradeBucketLabels = False, returnGradingPeriodIDClonedFrom = False, returnGradingPeriodIDClonedTo = False, returnGradingPeriodSetID = False, returnIncludeMissingAssignments = False, returnIncludeMissingAssignmentsOrIsCurrentGradingPeriod = False, returnIsActiveOrExtended = False, returnIsCompleted = False, returnModifiedTime = False, returnNumber = False, returnNumberDescription = False, returnOptionsHeaderText = False, returnProgressReportGradingPeriodNumberDateDisplay = False, returnSectionIDForActiveStatus = False, returnSectionLengthID = False, returnStartDate = False, returnStartDateCopy = False, returnStatusDisplay = False, returnStatusDisplayWithExtensionDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinGradingPeriod = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradingPeriod(GradingPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradingPeriodGradeBucket(GradingPeriodGradeBucketID, EntityID = 1, returnGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(GradingPeriodGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyGradingPeriodGradeBucket(GradingPeriodGradeBucketID, EntityID = 1, setEntityGroupKey = None, setFactorBasedGPACountAs = None, setGradeBucketID = None, setGradingPeriodGradeBucketIDClonedFrom = None, setGradingPeriodIDEnd = None, setGradingPeriodIDStart = None, setIsUpToDate = None, setRelationships = None, returnGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/" + str(GradingPeriodGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradingPeriodGradeBucket(EntityID = 1, setEntityGroupKey = None, setFactorBasedGPACountAs = None, setGradeBucketID = None, setGradingPeriodGradeBucketIDClonedFrom = None, setGradingPeriodIDEnd = None, setGradingPeriodIDStart = None, setIsUpToDate = None, setRelationships = None, returnGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnFactorBasedGPACountAs = False, returnGradeBucketID = False, returnGradeBucketLabelWithDates = False, returnGradingPeriodEndDateAddSnapshotGraceDays = False, returnGradingPeriodGradeBucketExistsInSpecifcEntity = False, returnGradingPeriodGradeBucketIDClonedFrom = False, returnGradingPeriodIDEnd = False, returnGradingPeriodIDStart = False, returnHasGradeBucketTypeCategories = False, returnIsAHistoricRecord = False, returnIsUpToDate = False, returnMaxExtraCredit = False, returnModifiedTime = False, returnNumberOfGradeBucketsToWeight = False, returnStatus = False, returnUseMaxExtraCredit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradingPeriodGradeBucket(GradingPeriodGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradingPeriodSet(EntityID = 1, page = 1, pageSize = 100, returnGradingPeriodSetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradingPeriodSet(GradingPeriodSetID, EntityID = 1, returnGradingPeriodSetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(GradingPeriodSetID), verb = "get", return_params_list = return_params_list)

def modifyGradingPeriodSet(GradingPeriodSetID, EntityID = 1, setCode = None, setCourseLengthID = None, setDescription = None, setEntityGroupKey = None, setGradingPeriodSetIDClonedFrom = None, setIsDefault = None, setRelationships = None, returnGradingPeriodSetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/" + str(GradingPeriodSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradingPeriodSet(EntityID = 1, setCode = None, setCourseLengthID = None, setDescription = None, setEntityGroupKey = None, setGradingPeriodSetIDClonedFrom = None, setIsDefault = None, setRelationships = None, returnGradingPeriodSetID = True, returnCode = False, returnCodeDescription = False, returnCourseLengthID = False, returnCreatedTime = False, returnDescription = False, returnEntityGroupKey = False, returnGradingPeriodSetIDClonedFrom = False, returnGradingPeriodSetIDClonedTo = False, returnIsDefault = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradingPeriodSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradingPeriodSet(GradingPeriodSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradReqRankGPACourseType(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankGPACourseTypeID = True, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradReqRankGPACourseType(GradReqRankGPACourseTypeID, EntityID = 1, returnGradReqRankGPACourseTypeID = True, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(GradReqRankGPACourseTypeID), verb = "get", return_params_list = return_params_list)

def modifyGradReqRankGPACourseType(GradReqRankGPACourseTypeID, EntityID = 1, setCourseTypeID = None, setGradReqRankGPAMethodEntityID = None, setRelationships = None, returnGradReqRankGPACourseTypeID = True, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/" + str(GradReqRankGPACourseTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradReqRankGPACourseType(EntityID = 1, setCourseTypeID = None, setGradReqRankGPAMethodEntityID = None, setRelationships = None, returnGradReqRankGPACourseTypeID = True, returnCourseTypeID = False, returnCreatedTime = False, returnGradReqRankGPAMethodEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPACourseType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradReqRankGPACourseType(GradReqRankGPACourseTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradReqRankGPAMethodEntity(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankGPAMethodEntityID = True, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, EntityID = 1, returnGradReqRankGPAMethodEntityID = True, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(GradReqRankGPAMethodEntityID), verb = "get", return_params_list = return_params_list)

def modifyGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, EntityID = 1, setGPAMethodEntityID = None, setGradeBucketFlagIDLocalCredit = None, setGradeBucketIDTermOne = None, setGradeBucketIDTermTwo = None, setGradPlanSetting = None, setGradPlanSettingCode = None, setPlanID = None, setRelationships = None, returnGradReqRankGPAMethodEntityID = True, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/" + str(GradReqRankGPAMethodEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradReqRankGPAMethodEntity(EntityID = 1, setGPAMethodEntityID = None, setGradeBucketFlagIDLocalCredit = None, setGradeBucketIDTermOne = None, setGradeBucketIDTermTwo = None, setGradPlanSetting = None, setGradPlanSettingCode = None, setPlanID = None, setRelationships = None, returnGradReqRankGPAMethodEntityID = True, returnCreatedTime = False, returnGPAMethodEntityID = False, returnGradeBucketFlagIDLocalCredit = False, returnGradeBucketIDTermOne = False, returnGradeBucketIDTermTwo = False, returnGradPlanSetting = False, returnGradPlanSettingCode = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankGPAMethodEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradReqRankGPAMethodEntity(GradReqRankGPAMethodEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradReqRankHighSchoolGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankHighSchoolGradeLevelID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, EntityID = 1, returnGradReqRankHighSchoolGradeLevelID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(GradReqRankHighSchoolGradeLevelID), verb = "get", return_params_list = return_params_list)

def modifyGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, EntityID = 1, setGPAMethodID = None, setGradeLevelID = None, setRelationships = None, returnGradReqRankHighSchoolGradeLevelID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/" + str(GradReqRankHighSchoolGradeLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradReqRankHighSchoolGradeLevel(EntityID = 1, setGPAMethodID = None, setGradeLevelID = None, setRelationships = None, returnGradReqRankHighSchoolGradeLevelID = True, returnCreatedTime = False, returnGPAMethodID = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankHighSchoolGradeLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradReqRankHighSchoolGradeLevel(GradReqRankHighSchoolGradeLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradReqRankSchoolYearIncludeLocalCredit(EntityID = 1, page = 1, pageSize = 100, returnGradReqRankSchoolYearIncludeLocalCreditID = True, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, EntityID = 1, returnGradReqRankSchoolYearIncludeLocalCreditID = True, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(GradReqRankSchoolYearIncludeLocalCreditID), verb = "get", return_params_list = return_params_list)

def modifyGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, EntityID = 1, setGPAMethodID = None, setSchoolYearID = None, setRelationships = None, returnGradReqRankSchoolYearIncludeLocalCreditID = True, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/" + str(GradReqRankSchoolYearIncludeLocalCreditID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradReqRankSchoolYearIncludeLocalCredit(EntityID = 1, setGPAMethodID = None, setSchoolYearID = None, setRelationships = None, returnGradReqRankSchoolYearIncludeLocalCreditID = True, returnCreatedTime = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqRankSchoolYearIncludeLocalCredit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradReqRankSchoolYearIncludeLocalCredit(GradReqRankSchoolYearIncludeLocalCreditID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryGradReqSubjectType(EntityID = 1, page = 1, pageSize = 100, returnGradReqSubjectTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getGradReqSubjectType(GradReqSubjectTypeID, EntityID = 1, returnGradReqSubjectTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(GradReqSubjectTypeID), verb = "get", return_params_list = return_params_list)

def modifyGradReqSubjectType(GradReqSubjectTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnGradReqSubjectTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/" + str(GradReqSubjectTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createGradReqSubjectType(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setRelationships = None, returnGradReqSubjectTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/GradReqSubjectType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteGradReqSubjectType(GradReqSubjectTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRuleGPA(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGPAID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRuleGPA(HonorRollRuleGPAID, EntityID = 1, returnHonorRollRuleGPAID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(HonorRollRuleGPAID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRuleGPA(HonorRollRuleGPAID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGPABucketID = None, setGPAMethodID = None, setGPAType = None, setGPATypeCode = None, setHonorRollRuleGPAIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setMaximumGPA = None, setMinimumGPA = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGPAID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/" + str(HonorRollRuleGPAID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRuleGPA(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGPABucketID = None, setGPAMethodID = None, setGPAType = None, setGPATypeCode = None, setHonorRollRuleGPAIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setMaximumGPA = None, setMinimumGPA = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGPAID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnHonorRollRuleGPAIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnMaximumGPA = False, returnMinimumGPA = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGPA/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRuleGPA(HonorRollRuleGPAID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRuleGradeMark(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkID = True, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, EntityID = 1, returnHonorRollRuleGradeMarkID = True, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(HonorRollRuleGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, EntityID = 1, setAllowException = None, setCourseStandardFilterXML = None, setEntityGroupKey = None, setEntityID = None, setExclusionThreshold = None, setHonorRollRuleGradeMarkIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setInclusionType = None, setInclusionTypeCode = None, setSchoolYearID = None, setTotalAllowableExceptions = None, setRelationships = None, returnHonorRollRuleGradeMarkID = True, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/" + str(HonorRollRuleGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRuleGradeMark(EntityID = 1, setAllowException = None, setCourseStandardFilterXML = None, setEntityGroupKey = None, setEntityID = None, setExclusionThreshold = None, setHonorRollRuleGradeMarkIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setInclusionType = None, setInclusionTypeCode = None, setSchoolYearID = None, setTotalAllowableExceptions = None, setRelationships = None, returnHonorRollRuleGradeMarkID = True, returnAllowException = False, returnCourseStandardFilterXML = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnExclusionThreshold = False, returnHonorRollRuleGradeMarkIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnInclusionType = False, returnInclusionTypeCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRuleGradeMark(HonorRollRuleGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRuleGradeMarkGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, EntityID = 1, returnHonorRollRuleGradeMarkGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(HonorRollRuleGradeMarkGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeBucketID = None, setHonorRollRuleGradeMarkGradeBucketIDClonedFrom = None, setHonorRollRuleGradeMarkID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGradeMarkGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/" + str(HonorRollRuleGradeMarkGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRuleGradeMarkGradeBucket(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeBucketID = None, setHonorRollRuleGradeMarkGradeBucketIDClonedFrom = None, setHonorRollRuleGradeMarkID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGradeMarkGradeBucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeBucketID = False, returnHonorRollRuleGradeMarkGradeBucketIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRuleGradeMarkGradeBucket(HonorRollRuleGradeMarkGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRuleGradeMarkGradeMark(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRuleGradeMarkGradeMarkID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, EntityID = 1, returnHonorRollRuleGradeMarkGradeMarkID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(HonorRollRuleGradeMarkGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeMarkID = None, setHonorRollRuleGradeMarkGradeMarkIDClonedFrom = None, setHonorRollRuleGradeMarkID = None, setIsException = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGradeMarkGradeMarkID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/" + str(HonorRollRuleGradeMarkGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRuleGradeMarkGradeMark(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setGradeMarkID = None, setHonorRollRuleGradeMarkGradeMarkIDClonedFrom = None, setHonorRollRuleGradeMarkID = None, setIsException = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRuleGradeMarkGradeMarkID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnGradeMarkID = False, returnHonorRollRuleGradeMarkGradeMarkIDClonedFrom = False, returnHonorRollRuleGradeMarkID = False, returnIsException = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRuleGradeMarkGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRuleGradeMarkGradeMark(HonorRollRuleGradeMarkGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRulePriorHonorRoll(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRulePriorHonorRollID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, EntityID = 1, returnHonorRollRulePriorHonorRollID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(HonorRollRulePriorHonorRollID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollLevelTotal = None, setHonorRollRulePriorHonorRollIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRulePriorHonorRollID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/" + str(HonorRollRulePriorHonorRollID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRulePriorHonorRoll(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollLevelTotal = None, setHonorRollRulePriorHonorRollIDClonedFrom = None, setHonorRollRunLevelRuleID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRulePriorHonorRollID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollLevelTotal = False, returnHonorRollRulePriorHonorRollIDClonedFrom = False, returnHonorRollRunLevelRuleID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRoll/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRulePriorHonorRoll(HonorRollRulePriorHonorRollID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRulePriorHonorRollLevel(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRulePriorHonorRollLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, EntityID = 1, returnHonorRollRulePriorHonorRollLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(HonorRollRulePriorHonorRollLevelID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRulePriorHonorRollID = None, setHonorRollRulePriorHonorRollLevelIDClonedFrom = None, setHonorRollRunLevelHistoryID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRulePriorHonorRollLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/" + str(HonorRollRulePriorHonorRollLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRulePriorHonorRollLevel(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRulePriorHonorRollID = None, setHonorRollRulePriorHonorRollLevelIDClonedFrom = None, setHonorRollRunLevelHistoryID = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRulePriorHonorRollLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRulePriorHonorRollID = False, returnHonorRollRulePriorHonorRollLevelIDClonedFrom = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRulePriorHonorRollLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRulePriorHonorRollLevel(HonorRollRulePriorHonorRollLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRun(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunID = True, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRun(HonorRollRunID, EntityID = 1, returnHonorRollRunID = True, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(HonorRollRunID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRun(HonorRollRunID, EntityID = 1, setAllowMultipleHonorRollLevels = None, setDisplayGPAForHonorRoll = None, setEntityGroupKey = None, setEntityID = None, setGPABucketIDToDisplay = None, setGPAMethodIDToDisplay = None, setGPATypeToDisplay = None, setGPATypeToDisplayCode = None, setHonorRollRunIDClonedFrom = None, setIsActive = None, setName = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunID = True, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/" + str(HonorRollRunID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRun(EntityID = 1, setAllowMultipleHonorRollLevels = None, setDisplayGPAForHonorRoll = None, setEntityGroupKey = None, setEntityID = None, setGPABucketIDToDisplay = None, setGPAMethodIDToDisplay = None, setGPATypeToDisplay = None, setGPATypeToDisplayCode = None, setHonorRollRunIDClonedFrom = None, setIsActive = None, setName = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunID = True, returnAllowMultipleHonorRollLevels = False, returnContainsGPARule = False, returnCreatedTime = False, returnDisplayGPAForHonorRoll = False, returnEntityGroupKey = False, returnEntityID = False, returnGPABucketIDToDisplay = False, returnGPAMethodIDToDisplay = False, returnGPATypeToDisplay = False, returnGPATypeToDisplayCode = False, returnHonorRollRunIDClonedFrom = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRun/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRun(HonorRollRunID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRunHistory(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRunHistory(HonorRollRunHistoryID, EntityID = 1, returnHonorRollRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(HonorRollRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRunHistory(HonorRollRunHistoryID, EntityID = 1, setCalculation = None, setCalculationCode = None, setDate = None, setDescription = None, setGPAAsOfDate = None, setHonorRollRunID = None, setStudentFilterParameter = None, setRelationships = None, returnHonorRollRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/" + str(HonorRollRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRunHistory(EntityID = 1, setCalculation = None, setCalculationCode = None, setDate = None, setDescription = None, setGPAAsOfDate = None, setHonorRollRunID = None, setStudentFilterParameter = None, setRelationships = None, returnHonorRollRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnGPAAsOfDate = False, returnHonorRollRunID = False, returnModifiedTime = False, returnNameDescription = False, returnStudentFilterParameter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRunHistory(HonorRollRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRunLevel(HonorRollRunLevelID, EntityID = 1, returnHonorRollRunLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(HonorRollRunLevelID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRunLevel(HonorRollRunLevelID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRunID = None, setHonorRollRunLevelIDClonedFrom = None, setName = None, setOrder = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/" + str(HonorRollRunLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRunLevel(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRunID = None, setHonorRollRunLevelIDClonedFrom = None, setName = None, setOrder = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunLevelID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunID = False, returnHonorRollRunLevelIDClonedFrom = False, returnHonorRollRunNameName = False, returnModifiedTime = False, returnName = False, returnOrder = False, returnRulesParameterDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRunLevel(HonorRollRunLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRunLevelHistory(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelHistoryID = True, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, EntityID = 1, returnHonorRollRunLevelHistoryID = True, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(HonorRollRunLevelHistoryID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, EntityID = 1, setHonorRollRunHistoryID = None, setHonorRollRunLevelID = None, setParameterDescription = None, setRelationships = None, returnHonorRollRunLevelHistoryID = True, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/" + str(HonorRollRunLevelHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRunLevelHistory(EntityID = 1, setHonorRollRunHistoryID = None, setHonorRollRunLevelID = None, setParameterDescription = None, setRelationships = None, returnHonorRollRunLevelHistoryID = True, returnCreatedTime = False, returnEntitySchoolYearHonorRollRunLevelName = False, returnHonorRollRunHistoryID = False, returnHonorRollRunLevelID = False, returnModifiedTime = False, returnParameterDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRunLevelHistory(HonorRollRunLevelHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHonorRollRunLevelRule(EntityID = 1, page = 1, pageSize = 100, returnHonorRollRunLevelRuleID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHonorRollRunLevelRule(HonorRollRunLevelRuleID, EntityID = 1, returnHonorRollRunLevelRuleID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(HonorRollRunLevelRuleID), verb = "get", return_params_list = return_params_list)

def modifyHonorRollRunLevelRule(HonorRollRunLevelRuleID, EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRunLevelID = None, setHonorRollRunLevelRuleIDClonedFrom = None, setParameterDescription = None, setRuleType = None, setRuleTypeCode = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunLevelRuleID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/" + str(HonorRollRunLevelRuleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHonorRollRunLevelRule(EntityID = 1, setEntityGroupKey = None, setEntityID = None, setHonorRollRunLevelID = None, setHonorRollRunLevelRuleIDClonedFrom = None, setParameterDescription = None, setRuleType = None, setRuleTypeCode = None, setSchoolYearID = None, setRelationships = None, returnHonorRollRunLevelRuleID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityID = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelRuleIDClonedFrom = False, returnModifiedTime = False, returnParameterDescription = False, returnRuleType = False, returnRuleTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/HonorRollRunLevelRule/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHonorRollRunLevelRule(HonorRollRunLevelRuleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPointSet(EntityID = 1, page = 1, pageSize = 100, returnPointSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPointSet(PointSetID, EntityID = 1, returnPointSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(PointSetID), verb = "get", return_params_list = return_params_list)

def modifyPointSet(PointSetID, EntityID = 1, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setName = None, setRelationships = None, returnPointSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/" + str(PointSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPointSet(EntityID = 1, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setName = None, setRelationships = None, returnPointSetID = True, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnNameDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePointSet(PointSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPointSetEntity(EntityID = 1, page = 1, pageSize = 100, returnPointSetEntityID = True, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPointSetEntity(PointSetEntityID, EntityID = 1, returnPointSetEntityID = True, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(PointSetEntityID), verb = "get", return_params_list = return_params_list)

def modifyPointSetEntity(PointSetEntityID, EntityID = 1, setApplyFactorBasedAddOn = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setIsDefault = None, setPointSetEntityIDClonedFrom = None, setPointSetID = None, setSchoolYearID = None, setRelationships = None, returnPointSetEntityID = True, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/" + str(PointSetEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPointSetEntity(EntityID = 1, setApplyFactorBasedAddOn = None, setDisplayOrder = None, setEntityGroupKey = None, setEntityID = None, setIsDefault = None, setPointSetEntityIDClonedFrom = None, setPointSetID = None, setSchoolYearID = None, setRelationships = None, returnPointSetEntityID = True, returnApplyFactorBasedAddOn = False, returnCreatedTime = False, returnDisplayOrder = False, returnEntityGroupKey = False, returnEntityID = False, returnIsDefault = False, returnModifiedTime = False, returnPointSetEntityIDClonedFrom = False, returnPointSetID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/PointSetEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePointSetEntity(PointSetEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryQueuedGPACalculation(EntityID = 1, page = 1, pageSize = 100, returnQueuedGPACalculationID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getQueuedGPACalculation(QueuedGPACalculationID, EntityID = 1, returnQueuedGPACalculationID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(QueuedGPACalculationID), verb = "get", return_params_list = return_params_list)

def modifyQueuedGPACalculation(QueuedGPACalculationID, EntityID = 1, setEndTime = None, setEntityID = None, setHostName = None, setProcessID = None, setSchoolYearID = None, setSkipCredits = None, setSourcePrimaryKey = None, setSourceType = None, setStartTime = None, setStatus = None, setThreadName = None, setUserIDImpersonator = None, setRelationships = None, returnQueuedGPACalculationID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/" + str(QueuedGPACalculationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createQueuedGPACalculation(EntityID = 1, setEndTime = None, setEntityID = None, setHostName = None, setProcessID = None, setSchoolYearID = None, setSkipCredits = None, setSourcePrimaryKey = None, setSourceType = None, setStartTime = None, setStatus = None, setThreadName = None, setUserIDImpersonator = None, setRelationships = None, returnQueuedGPACalculationID = True, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSchoolYearID = False, returnSkipCredits = False, returnSourcePrimaryKey = False, returnSourceType = False, returnSourceTypeCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/QueuedGPACalculation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteQueuedGPACalculation(QueuedGPACalculationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRankMethod(EntityID = 1, page = 1, pageSize = 100, returnRankMethodID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRankMethod(RankMethodID, EntityID = 1, returnRankMethodID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(RankMethodID), verb = "get", return_params_list = return_params_list)

def modifyRankMethod(RankMethodID, EntityID = 1, setDistrictGroupKey = None, setGPABucketID = None, setGPAMethodID = None, setGPAType = None, setGPATypeCode = None, setIncludeNonRankedStudents = None, setIsActive = None, setName = None, setValueRangeHigh = None, setValueRangeLow = None, setValueRangeType = None, setValueRangeTypeCode = None, setRelationships = None, returnRankMethodID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/" + str(RankMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRankMethod(EntityID = 1, setDistrictGroupKey = None, setGPABucketID = None, setGPAMethodID = None, setGPAType = None, setGPATypeCode = None, setIncludeNonRankedStudents = None, setIsActive = None, setName = None, setValueRangeHigh = None, setValueRangeLow = None, setValueRangeType = None, setValueRangeTypeCode = None, setRelationships = None, returnRankMethodID = True, returnCreatedTime = False, returnDistrictGroupKey = False, returnGPABucketID = False, returnGPAMethodID = False, returnGPAType = False, returnGPATypeCode = False, returnIncludeNonRankedStudents = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueRangeHigh = False, returnValueRangeLow = False, returnValueRangeType = False, returnValueRangeTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRankMethod(RankMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRankMethodStudentRangeSetup(EntityID = 1, page = 1, pageSize = 100, returnRankMethodStudentRangeSetupID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, EntityID = 1, returnRankMethodStudentRangeSetupID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(RankMethodStudentRangeSetupID), verb = "get", return_params_list = return_params_list)

def modifyRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, EntityID = 1, setConfigEntityGroupYearID = None, setRankMethodID = None, setStudentRangeID = None, setRelationships = None, returnRankMethodStudentRangeSetupID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/" + str(RankMethodStudentRangeSetupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRankMethodStudentRangeSetup(EntityID = 1, setConfigEntityGroupYearID = None, setRankMethodID = None, setStudentRangeID = None, setRelationships = None, returnRankMethodStudentRangeSetupID = True, returnConfigEntityGroupYearID = False, returnCreatedTime = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankMethodStudentRangeSetup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRankMethodStudentRangeSetup(RankMethodStudentRangeSetupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRankRunHistory(EntityID = 1, page = 1, pageSize = 100, returnRankRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRankRunHistory(RankRunHistoryID, EntityID = 1, returnRankRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(RankRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyRankRunHistory(RankRunHistoryID, EntityID = 1, setCalculation = None, setCalculationCode = None, setDate = None, setDescription = None, setGPAAsOfDate = None, setGradeLevelIDCohort = None, setRankMethodID = None, setStudentGroup = None, setStudentGroupCode = None, setStudentRangeID = None, setRelationships = None, returnRankRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/" + str(RankRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRankRunHistory(EntityID = 1, setCalculation = None, setCalculationCode = None, setDate = None, setDescription = None, setGPAAsOfDate = None, setGradeLevelIDCohort = None, setRankMethodID = None, setStudentGroup = None, setStudentGroupCode = None, setStudentRangeID = None, setRelationships = None, returnRankRunHistoryID = True, returnCalculation = False, returnCalculationCode = False, returnCreatedTime = False, returnDate = False, returnDescription = False, returnFullGroupingDescription = False, returnGPAAsOfDate = False, returnGradeLevelIDCohort = False, returnModifiedTime = False, returnRankMethodID = False, returnStudentGroup = False, returnStudentGroupCode = False, returnStudentRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/RankRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRankRunHistory(RankRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySectionLengthGPABucket(EntityID = 1, page = 1, pageSize = 100, returnSectionLengthGPABucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSectionLengthGPABucket(SectionLengthGPABucketID, EntityID = 1, returnSectionLengthGPABucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(SectionLengthGPABucketID), verb = "get", return_params_list = return_params_list)

def modifySectionLengthGPABucket(SectionLengthGPABucketID, EntityID = 1, setEntityGroupKey = None, setGPABucketEntityID = None, setIsUpToDate = None, setSectionLengthGPABucketIDClonedFrom = None, setSectionLengthID = None, setRelationships = None, returnSectionLengthGPABucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/" + str(SectionLengthGPABucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSectionLengthGPABucket(EntityID = 1, setEntityGroupKey = None, setGPABucketEntityID = None, setIsUpToDate = None, setSectionLengthGPABucketIDClonedFrom = None, setSectionLengthID = None, setRelationships = None, returnSectionLengthGPABucketID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnGPABucketEntityID = False, returnIsUpToDate = False, returnModifiedTime = False, returnSectionLengthGPABucketIDClonedFrom = False, returnSectionLengthID = False, returnStatus = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/SectionLengthGPABucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSectionLengthGPABucket(SectionLengthGPABucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentCommentBucket(StudentCommentBucketID, EntityID = 1, returnStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(StudentCommentBucketID), verb = "get", return_params_list = return_params_list)

def modifyStudentCommentBucket(StudentCommentBucketID, EntityID = 1, setCommentBucketID = None, setCommentCodeID = None, setGradingPeriodID = None, setStudentSectionID = None, setRelationships = None, returnStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/" + str(StudentCommentBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentCommentBucket(EntityID = 1, setCommentBucketID = None, setCommentCodeID = None, setGradingPeriodID = None, setStudentSectionID = None, setRelationships = None, returnStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentCodeID = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentCommentBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentCommentBucket(StudentCommentBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentFreeFormCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentFreeFormCommentBucketID = True, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, EntityID = 1, returnStudentFreeFormCommentBucketID = True, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(StudentFreeFormCommentBucketID), verb = "get", return_params_list = return_params_list)

def modifyStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, EntityID = 1, setComment = None, setGradingPeriodID = None, setStudentSectionID = None, setRelationships = None, returnStudentFreeFormCommentBucketID = True, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/" + str(StudentFreeFormCommentBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentFreeFormCommentBucket(EntityID = 1, setComment = None, setGradingPeriodID = None, setStudentSectionID = None, setRelationships = None, returnStudentFreeFormCommentBucketID = True, returnComment = False, returnCreatedTime = False, returnGradingPeriodID = False, returnModifiedTime = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentFreeFormCommentBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentFreeFormCommentBucket(StudentFreeFormCommentBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGPABucket(EntityID = 1, page = 1, pageSize = 100, returnStudentGPABucketID = True, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGPABucket(StudentGPABucketID, EntityID = 1, returnStudentGPABucketID = True, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(StudentGPABucketID), verb = "get", return_params_list = return_params_list)

def modifyStudentGPABucket(StudentGPABucketID, EntityID = 1, setBonusGPAPoints = None, setEntityID = None, setGPACredits = None, setGPAPoints = None, setGradReqRankGPAStatus = None, setGradReqRankGPAStatusCode = None, setPointsAndCreditsMultiplier = None, setSchoolYearID = None, setStudentGradeBucketID = None, setStudentSectionGPABucketGroupID = None, setUseOverride = None, setRelationships = None, returnStudentGPABucketID = True, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/" + str(StudentGPABucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGPABucket(EntityID = 1, setBonusGPAPoints = None, setEntityID = None, setGPACredits = None, setGPAPoints = None, setGradReqRankGPAStatus = None, setGradReqRankGPAStatusCode = None, setPointsAndCreditsMultiplier = None, setSchoolYearID = None, setStudentGradeBucketID = None, setStudentSectionGPABucketGroupID = None, setUseOverride = None, setRelationships = None, returnStudentGPABucketID = True, returnBonusGPAPoints = False, returnCreatedTime = False, returnDisplayGPACredits = False, returnDisplayGPAPoints = False, returnEntityID = False, returnGPACredits = False, returnGPAPoints = False, returnGPAWithBonus = False, returnGradReqRankGPAStatus = False, returnGradReqRankGPAStatusCode = False, returnHasAllGradesRequiredForGPACalculation = False, returnModifiedTime = False, returnPointsAndCreditsMultiplier = False, returnSchoolYearID = False, returnStudentGradeBucketID = False, returnStudentSectionGPABucketGroupID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGPABucket(StudentGPABucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentGPABucketGroupID = True, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGPABucketGroup(StudentGPABucketGroupID, EntityID = 1, returnStudentGPABucketGroupID = True, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(StudentGPABucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyStudentGPABucketGroup(StudentGPABucketGroupID, EntityID = 1, setGPABucketID = None, setGPAMethodID = None, setGradReqRankGPABreakdown = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnStudentGPABucketGroupID = True, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/" + str(StudentGPABucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGPABucketGroup(EntityID = 1, setGPABucketID = None, setGPAMethodID = None, setGradReqRankGPABreakdown = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnStudentGPABucketGroupID = True, returnBonusGPA = False, returnBonusGPAWithoutRounding = False, returnCreatedTime = False, returnCurrentDefaultDistrictID = False, returnEarnedCredits = False, returnElectiveBonusGPA = False, returnElectiveFactor = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnFactorBonusGPA = False, returnFactorBonusGPAWithoutRounding = False, returnFailedCredits = False, returnFinalGPARoundingDecimals = False, returnGPA = False, returnGPABucketID = False, returnGPACalculationRoundingDecimals = False, returnGPACredits = False, returnGPACreditsWithoutRounding = False, returnGPAMethodID = False, returnGPAPoints = False, returnGPAPointsWithoutRounding = False, returnGPAWithBonus = False, returnGPAWithFactorBonus = False, returnGradReqRankGPABreakdown = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGPABucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGPABucketGroup(StudentGPABucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketID = True, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradeBucket(StudentGradeBucketID, EntityID = 1, returnStudentGradeBucketID = True, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(StudentGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradeBucket(StudentGradeBucketID, EntityID = 1, setCalculatedCalculationTypeCode = None, setCalculatedClosedGradingPeriodGradeChangeStatus = None, setCalculatedClosedGradingPeriodGradeChangeStatusCode = None, setCalculatedPoints = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setCompleteByTeacher = None, setCompleteByTeacherCode = None, setCompletionDate = None, setCompletionDateOverride = None, setDoNotPost = None, setEarnedCreditAttempted = None, setEarnedCredits = None, setEarnedCreditsPossible = None, setEarnedPoints = None, setEntityID = None, setFailedCredits = None, setGradeMarkID = None, setGradeMarkIDOutOfDistrictTransferWithdraw = None, setGradeMarkIDOverride = None, setGradeMarkIDToApply = None, setGradeMarkIDToUse = None, setGradeMarkIDToUseIgnoreDoNotPost = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setGradeMarkToUseIgnoreDoNotPost = None, setGradingPeriodEndDateHasPassed = None, setGradingPeriodGradeBucketID = None, setHasUnscoredRequiredFeederBucket = None, setIsAdminOverride = None, setIsComplete = None, setIsTransferBucket = None, setIsUsingPointsBasedScale = None, setNoGradebookOverride = None, setOverrideComment = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPercentWithAdjustmentIgnoreMinimum = None, setPercentWithAdjustmentNoCap = None, setPossiblePoints = None, setReportCardGradeMarkToUse = None, setSchoolYearID = None, setSectionID = None, setStartingPercent = None, setStudentGradeBucketFlag = None, setStudentSectionID = None, setUseCompletionDateOverride = None, setRelationships = None, returnStudentGradeBucketID = True, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/" + str(StudentGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradeBucket(EntityID = 1, setCalculatedCalculationTypeCode = None, setCalculatedClosedGradingPeriodGradeChangeStatus = None, setCalculatedClosedGradingPeriodGradeChangeStatusCode = None, setCalculatedPoints = None, setClosedGradingPeriodGradeChangeStatus = None, setClosedGradingPeriodGradeChangeStatusCode = None, setCompleteByTeacher = None, setCompleteByTeacherCode = None, setCompletionDate = None, setCompletionDateOverride = None, setDoNotPost = None, setEarnedCreditAttempted = None, setEarnedCredits = None, setEarnedCreditsPossible = None, setEarnedPoints = None, setEntityID = None, setFailedCredits = None, setGradeMarkID = None, setGradeMarkIDOutOfDistrictTransferWithdraw = None, setGradeMarkIDOverride = None, setGradeMarkIDToApply = None, setGradeMarkIDToUse = None, setGradeMarkIDToUseIgnoreDoNotPost = None, setGradeMarkOverrideComment = None, setGradeMarkToUse = None, setGradeMarkToUseIgnoreDoNotPost = None, setGradingPeriodEndDateHasPassed = None, setGradingPeriodGradeBucketID = None, setHasUnscoredRequiredFeederBucket = None, setIsAdminOverride = None, setIsComplete = None, setIsTransferBucket = None, setIsUsingPointsBasedScale = None, setNoGradebookOverride = None, setOverrideComment = None, setPercent = None, setPercentAdjustment = None, setPercentAdjustmentComment = None, setPercentWithAdjustment = None, setPercentWithAdjustmentIgnoreMinimum = None, setPercentWithAdjustmentNoCap = None, setPossiblePoints = None, setReportCardGradeMarkToUse = None, setSchoolYearID = None, setSectionID = None, setStartingPercent = None, setStudentGradeBucketFlag = None, setStudentSectionID = None, setUseCompletionDateOverride = None, setRelationships = None, returnStudentGradeBucketID = True, returnAbsentCount = False, returnCalculatedCalculationTypeCode = False, returnCalculatedClosedGradingPeriodGradeChangeStatus = False, returnCalculatedClosedGradingPeriodGradeChangeStatusCode = False, returnCalculatedPoints = False, returnClosedGradingPeriodGradeChangeStatus = False, returnClosedGradingPeriodGradeChangeStatusCode = False, returnCompleteByTeacher = False, returnCompleteByTeacherCode = False, returnCompletionDate = False, returnCompletionDateOverride = False, returnConfigEarnedCredits = False, returnConfigFailedCredits = False, returnCreatedTime = False, returnDoNotPost = False, returnEarnedCreditAttempted = False, returnEarnedCredits = False, returnEarnedCreditsPossible = False, returnEarnedPoints = False, returnEntityID = False, returnExcusedCount = False, returnFailedCredits = False, returnGradeMarkID = False, returnGradeMarkIDOutOfDistrictTransferWithdraw = False, returnGradeMarkIDOverride = False, returnGradeMarkIDToApply = False, returnGradeMarkIDToUse = False, returnGradeMarkIDToUseIgnoreDoNotPost = False, returnGradeMarkOverrideComment = False, returnGradeMarkToUse = False, returnGradeMarkToUseExists = False, returnGradeMarkToUseIgnoreDoNotPost = False, returnGradingPeriodEndDateHasPassed = False, returnGradingPeriodGradeBucketID = False, returnHasAcademicStandardGrades = False, returnHasAssignments = False, returnHasStudentSectionGradingScaleGradeBucket = False, returnHasStudentSectionLinkConflict = False, returnHasSubjectGrades = False, returnHasUnscoredRequiredFeederBucket = False, returnIsAdminOverride = False, returnIsComplete = False, returnIsTransferBucket = False, returnIsUsingPointsBasedScale = False, returnModifiedTime = False, returnNoGradebookOrAdminOverride = False, returnNoGradebookOverride = False, returnOtherCount = False, returnOverrideComment = False, returnPercent = False, returnPercentAdjustment = False, returnPercentAdjustmentComment = False, returnPercentHasChangedWithinSpecifiedAmountOfTime = False, returnPercentWithAdjustment = False, returnPercentWithAdjustmentFormatted = False, returnPercentWithAdjustmentIgnoreMinimum = False, returnPercentWithAdjustmentNoCap = False, returnPercentWithAdjustmentWithGradeMarkToUse = False, returnPercentWithAdjustmentWithGradeMarkToUseIgnoreDoNotPost = False, returnPercentWithAdjustmentWithGradeMarkToUseNoCap = False, returnPercentWithGradeMarkIgnoreDoNotPost = False, returnPossiblePoints = False, returnReportCardGradeMarkToUse = False, returnSchoolYearID = False, returnSectionID = False, returnStartingPercent = False, returnStudentCommentBucketCount = False, returnStudentFreeFormCommentBucketCount = False, returnStudentGradeBucketFlag = False, returnStudentGradeBucketStatus = False, returnStudentSectionID = False, returnTardyCount = False, returnUnexcusedCount = False, returnUseCompletionDateOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWeightPercentForGradeBucket = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradeBucket(StudentGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnStudentGradeBucketFlagID = True, returnCreatedTime = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False, returnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentGradeBucketFlag(StudentGradeBucketFlagID, EntityID = 1, returnStudentGradeBucketFlagID = True, returnCreatedTime = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False, returnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(StudentGradeBucketFlagID), verb = "get", return_params_list = return_params_list)

def modifyStudentGradeBucketFlag(StudentGradeBucketFlagID, EntityID = 1, setGradeBucketFlagID = None, setStudentGradeBucketID = None, setRelationships = None, setAPIOptionFlags = None, returnStudentGradeBucketFlagID = True, returnCreatedTime = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False, returnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/" + str(StudentGradeBucketFlagID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentGradeBucketFlag(EntityID = 1, setGradeBucketFlagID = None, setStudentGradeBucketID = None, setRelationships = None, setAPIOptionFlags = None, returnStudentGradeBucketFlagID = True, returnCreatedTime = False, returnGradeBucketFlagID = False, returnModifiedTime = False, returnStudentGradeBucketID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False, returnAPIOptionFlags = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentGradeBucketFlag/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentGradeBucketFlag(StudentGradeBucketFlagID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentHonorRollRunLevel(StudentHonorRollRunLevelID, EntityID = 1, returnStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(StudentHonorRollRunLevelID), verb = "get", return_params_list = return_params_list)

def modifyStudentHonorRollRunLevel(StudentHonorRollRunLevelID, EntityID = 1, setGPAValue = None, setHonorRollRunLevelHistoryID = None, setStudentID = None, setRelationships = None, returnStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/" + str(StudentHonorRollRunLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentHonorRollRunLevel(EntityID = 1, setGPAValue = None, setHonorRollRunLevelHistoryID = None, setStudentID = None, setRelationships = None, returnStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnHonorRollRunLevelHistoryID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentHonorRollRunLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentHonorRollRunLevel(StudentHonorRollRunLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentRange(EntityID = 1, page = 1, pageSize = 100, returnStudentRangeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnFilter = False, returnIsActive = False, returnModifiedTime = False, returnRank = False, returnSchoolID = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnStatus = False, returnStatusCode = False, returnStudentTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentRange(StudentRangeID, EntityID = 1, returnStudentRangeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnFilter = False, returnIsActive = False, returnModifiedTime = False, returnRank = False, returnSchoolID = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnStatus = False, returnStatusCode = False, returnStudentTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(StudentRangeID), verb = "get", return_params_list = return_params_list)

def modifyStudentRange(StudentRangeID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEntityID = None, setFilter = None, setIsActive = None, setRank = None, setSchoolID = None, setSchoolYearID = None, setSearchConditionFilter = None, setStatus = None, setStatusCode = None, setStudentTypeID = None, setRelationships = None, returnStudentRangeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnFilter = False, returnIsActive = False, returnModifiedTime = False, returnRank = False, returnSchoolID = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnStatus = False, returnStatusCode = False, returnStudentTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/" + str(StudentRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentRange(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEntityID = None, setFilter = None, setIsActive = None, setRank = None, setSchoolID = None, setSchoolYearID = None, setSearchConditionFilter = None, setStatus = None, setStatusCode = None, setStudentTypeID = None, setRelationships = None, returnStudentRangeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEntityID = False, returnFilter = False, returnIsActive = False, returnModifiedTime = False, returnRank = False, returnSchoolID = False, returnSchoolYearID = False, returnSearchConditionFilter = False, returnStatus = False, returnStatusCode = False, returnStudentTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentRange(StudentRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentRank(EntityID = 1, page = 1, pageSize = 100, returnStudentRankID = True, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentRank(StudentRankID, EntityID = 1, returnStudentRankID = True, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(StudentRankID), verb = "get", return_params_list = return_params_list)

def modifyStudentRank(StudentRankID, EntityID = 1, setIsManualRank = None, setIsProspectiveRank = None, setNumberInRank = None, setNumberOutOf = None, setRankRunHistoryID = None, setSchoolYearIDCohort = None, setStudentID = None, setUseOverride = None, setValue = None, setRelationships = None, returnStudentRankID = True, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/" + str(StudentRankID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentRank(EntityID = 1, setIsManualRank = None, setIsProspectiveRank = None, setNumberInRank = None, setNumberOutOf = None, setRankRunHistoryID = None, setSchoolYearIDCohort = None, setStudentID = None, setUseOverride = None, setValue = None, setRelationships = None, returnStudentRankID = True, returnCreatedTime = False, returnDisplayRank = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNumberInRank = False, returnNumberOutOf = False, returnRankRunHistoryID = False, returnSchoolYearIDCohort = False, returnStudentID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentRank/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentRank(StudentRankID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSectionGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGPABucketGroupID = True, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, EntityID = 1, returnStudentSectionGPABucketGroupID = True, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(StudentSectionGPABucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, EntityID = 1, setEntityID = None, setSchoolYearID = None, setStudentGPABucketGroupID = None, setStudentSectionID = None, setTotalAddOnPoints = None, setTotalGPACredits = None, setTotalGPAPoints = None, setUseGPATotalOverride = None, setRelationships = None, returnStudentSectionGPABucketGroupID = True, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/" + str(StudentSectionGPABucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSectionGPABucketGroup(EntityID = 1, setEntityID = None, setSchoolYearID = None, setStudentGPABucketGroupID = None, setStudentSectionID = None, setTotalAddOnPoints = None, setTotalGPACredits = None, setTotalGPAPoints = None, setUseGPATotalOverride = None, setRelationships = None, returnStudentSectionGPABucketGroupID = True, returnBonusGPA = False, returnCreatedTime = False, returnElectiveBonusGPA = False, returnElectiveGPACredits = False, returnElectiveGPAPoints = False, returnEntityID = False, returnFactorBasedGPACountTotal = False, returnGPACredits = False, returnGPAPoints = False, returnIsGPAElective = False, returnModifiedTime = False, returnRequiredBonusGPA = False, returnRequiredGPACredits = False, returnRequiredGPAPoints = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentSectionID = False, returnTotalAddOnPoints = False, returnTotalGPACredits = False, returnTotalGPAPoints = False, returnUseGPATotalOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPABucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSectionGPABucketGroup(StudentSectionGPABucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStudentSectionGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnStudentSectionGPAMethodID = True, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStudentSectionGPAMethod(StudentSectionGPAMethodID, EntityID = 1, returnStudentSectionGPAMethodID = True, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(StudentSectionGPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyStudentSectionGPAMethod(StudentSectionGPAMethodID, EntityID = 1, setGPACredits = None, setGPAMethodEntityID = None, setPointSetEntityID = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnStudentSectionGPAMethodID = True, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/" + str(StudentSectionGPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStudentSectionGPAMethod(EntityID = 1, setGPACredits = None, setGPAMethodEntityID = None, setPointSetEntityID = None, setStudentSectionID = None, setUseOverride = None, setRelationships = None, returnStudentSectionGPAMethodID = True, returnCreatedTime = False, returnCumulativeGPACredits = False, returnCumulativeGPAPoints = False, returnGPACredits = False, returnGPAMethodEntityID = False, returnModifiedTime = False, returnPointSetEntityID = False, returnStudentSectionID = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/StudentSectionGPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStudentSectionGPAMethod(StudentSectionGPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFactorBasedAddOn(EntityID = 1, page = 1, pageSize = 100, returnTempFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFactorBasedAddOn(TempFactorBasedAddOnID, EntityID = 1, returnTempFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(TempFactorBasedAddOnID), verb = "get", return_params_list = return_params_list)

def modifyTempFactorBasedAddOn(TempFactorBasedAddOnID, EntityID = 1, setFactor = None, setGPABucketEntityDisplayName = None, setGradeReferenceDisplayName = None, setGradingEndDateCutoffForCumulative = None, setOriginalGradingEndDateCutoffForCumulative = None, setTempFactorBasedAddOnClonedFromID = None, setRelationships = None, returnTempFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/" + str(TempFactorBasedAddOnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFactorBasedAddOn(EntityID = 1, setFactor = None, setGPABucketEntityDisplayName = None, setGradeReferenceDisplayName = None, setGradingEndDateCutoffForCumulative = None, setOriginalGradingEndDateCutoffForCumulative = None, setTempFactorBasedAddOnClonedFromID = None, setRelationships = None, returnTempFactorBasedAddOnID = True, returnCreatedTime = False, returnFactor = False, returnGPABucketEntityDisplayName = False, returnGradeReferenceDisplayName = False, returnGradingEndDateCutoffForCumulative = False, returnModifiedTime = False, returnOriginalGradingEndDateCutoffForCumulative = False, returnTempFactorBasedAddOnClonedFromID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFactorBasedAddOn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFactorBasedAddOn(TempFactorBasedAddOnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempFailedGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnTempFailedGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempFailedGradingPeriod(TempFailedGradingPeriodID, EntityID = 1, returnTempFailedGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(TempFailedGradingPeriodID), verb = "get", return_params_list = return_params_list)

def modifyTempFailedGradingPeriod(TempFailedGradingPeriodID, EntityID = 1, setDescription = None, setEndDate = None, setGradingPeriodID = None, setGradingPeriodSetCode = None, setGradingPeriodSetCodeDescription = None, setGradingPeriodSetID = None, setIsUpdated = None, setNote = None, setNumber = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setStartDate = None, setTempGradingPeriodID = None, setRelationships = None, returnTempFailedGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/" + str(TempFailedGradingPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempFailedGradingPeriod(EntityID = 1, setDescription = None, setEndDate = None, setGradingPeriodID = None, setGradingPeriodSetCode = None, setGradingPeriodSetCodeDescription = None, setGradingPeriodSetID = None, setIsUpdated = None, setNote = None, setNumber = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setStartDate = None, setTempGradingPeriodID = None, setRelationships = None, returnTempFailedGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNote = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnTempGradingPeriodID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempFailedGradingPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempFailedGradingPeriod(TempFailedGradingPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeBucketFlagDetailGPAMethod(EntityID = 1, page = 1, pageSize = 100, returnTempGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnGPAMethodDescription = False, returnGradeBucketFlagCodeName = False, returnModifiedTime = False, returnPointSetDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, EntityID = 1, returnTempGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnGPAMethodDescription = False, returnGradeBucketFlagCodeName = False, returnModifiedTime = False, returnPointSetDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(TempGradeBucketFlagDetailGPAMethodID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, EntityID = 1, setGPAMethodDescription = None, setGradeBucketFlagCodeName = None, setPointSetDescription = None, setRelationships = None, returnTempGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnGPAMethodDescription = False, returnGradeBucketFlagCodeName = False, returnModifiedTime = False, returnPointSetDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/" + str(TempGradeBucketFlagDetailGPAMethodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeBucketFlagDetailGPAMethod(EntityID = 1, setGPAMethodDescription = None, setGradeBucketFlagCodeName = None, setPointSetDescription = None, setRelationships = None, returnTempGradeBucketFlagDetailGPAMethodID = True, returnCreatedTime = False, returnGPAMethodDescription = False, returnGradeBucketFlagCodeName = False, returnModifiedTime = False, returnPointSetDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeBucketFlagDetailGPAMethod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeBucketFlagDetailGPAMethod(TempGradeBucketFlagDetailGPAMethodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeMarkPointSetError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeMarkPointSetErrorID = True, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, EntityID = 1, returnTempGradeMarkPointSetErrorID = True, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(TempGradeMarkPointSetErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, EntityID = 1, setErrorString = None, setGPAMethodName = None, setGradeMarkCode = None, setPointSetName = None, setRelationships = None, returnTempGradeMarkPointSetErrorID = True, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/" + str(TempGradeMarkPointSetErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeMarkPointSetError(EntityID = 1, setErrorString = None, setGPAMethodName = None, setGradeMarkCode = None, setPointSetName = None, setRelationships = None, returnTempGradeMarkPointSetErrorID = True, returnCreatedTime = False, returnErrorString = False, returnGPAMethodName = False, returnGradeMarkCode = False, returnModifiedTime = False, returnPointSetName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeMarkPointSetError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeMarkPointSetError(TempGradeMarkPointSetErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeReportAttendanceTerm(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, EntityID = 1, returnTempGradeReportAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(TempGradeReportAttendanceTermID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, EntityID = 1, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarDescription = None, setEndDate = None, setEntityName = None, setSchoolYearDescription = None, setStartDate = None, setRelationships = None, returnTempGradeReportAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/" + str(TempGradeReportAttendanceTermID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeReportAttendanceTerm(EntityID = 1, setAttendanceTermCode = None, setAttendanceTermID = None, setCalendarDescription = None, setEndDate = None, setEntityName = None, setSchoolYearDescription = None, setStartDate = None, setRelationships = None, returnTempGradeReportAttendanceTermID = True, returnAttendanceTermCode = False, returnAttendanceTermID = False, returnCalendarDescription = False, returnCreatedTime = False, returnEndDate = False, returnEntityName = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportAttendanceTerm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeReportAttendanceTerm(TempGradeReportAttendanceTermID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeReportGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportGradeBucketID = True, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeReportGradeBucket(TempGradeReportGradeBucketID, EntityID = 1, returnTempGradeReportGradeBucketID = True, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(TempGradeReportGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeReportGradeBucket(TempGradeReportGradeBucketID, EntityID = 1, setEntityName = None, setGradeBucketLabel = None, setGradingPeriodGradeBucketID = None, setSchoolYearDescription = None, setSectionLengthDescription = None, setRelationships = None, returnTempGradeReportGradeBucketID = True, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/" + str(TempGradeReportGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeReportGradeBucket(EntityID = 1, setEntityName = None, setGradeBucketLabel = None, setGradingPeriodGradeBucketID = None, setSchoolYearDescription = None, setSectionLengthDescription = None, setRelationships = None, returnTempGradeReportGradeBucketID = True, returnCreatedTime = False, returnEntityName = False, returnGradeBucketLabel = False, returnGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSectionLengthDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeReportGradeBucket(TempGradeReportGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeReportTemplate(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportTemplateID = True, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeReportTemplate(TempGradeReportTemplateID, EntityID = 1, returnTempGradeReportTemplateID = True, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(TempGradeReportTemplateID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeReportTemplate(TempGradeReportTemplateID, EntityID = 1, setEntityCodeNameClonedFrom = None, setEntityCodeNameClonedTo = None, setEntityID = None, setErrorCount = None, setHasErrors = None, setNewGradeReportTemplateDescription = None, setOriginalGradeReportTemplateDescription = None, setSchoolYearID = None, setRelationships = None, returnTempGradeReportTemplateID = True, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/" + str(TempGradeReportTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeReportTemplate(EntityID = 1, setEntityCodeNameClonedFrom = None, setEntityCodeNameClonedTo = None, setEntityID = None, setErrorCount = None, setHasErrors = None, setNewGradeReportTemplateDescription = None, setOriginalGradeReportTemplateDescription = None, setSchoolYearID = None, setRelationships = None, returnTempGradeReportTemplateID = True, returnCreatedTime = False, returnEntityCodeNameClonedFrom = False, returnEntityCodeNameClonedTo = False, returnEntityID = False, returnErrorCount = False, returnHasErrors = False, returnModifiedTime = False, returnNewGradeReportTemplateDescription = False, returnOriginalGradeReportTemplateDescription = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeReportTemplate(TempGradeReportTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeReportTemplateError(EntityID = 1, page = 1, pageSize = 100, returnTempGradeReportTemplateErrorID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeReportTemplateError(TempGradeReportTemplateErrorID, EntityID = 1, returnTempGradeReportTemplateErrorID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(TempGradeReportTemplateErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeReportTemplateError(TempGradeReportTemplateErrorID, EntityID = 1, setError = None, setErrorDetail = None, setTempGradeReportTemplateID = None, setRelationships = None, returnTempGradeReportTemplateErrorID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/" + str(TempGradeReportTemplateErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeReportTemplateError(EntityID = 1, setError = None, setErrorDetail = None, setTempGradeReportTemplateID = None, setRelationships = None, returnTempGradeReportTemplateErrorID = True, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnModifiedTime = False, returnTempGradeReportTemplateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradeReportTemplateError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeReportTemplateError(TempGradeReportTemplateErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingPeriod(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingPeriod(TempGradingPeriodID, EntityID = 1, returnTempGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(TempGradingPeriodID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingPeriod(TempGradingPeriodID, EntityID = 1, setDescription = None, setEndDate = None, setGradingPeriodID = None, setGradingPeriodSetCode = None, setGradingPeriodSetCodeDescription = None, setGradingPeriodSetID = None, setIsUpdated = None, setNumber = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnTempGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/" + str(TempGradingPeriodID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingPeriod(EntityID = 1, setDescription = None, setEndDate = None, setGradingPeriodID = None, setGradingPeriodSetCode = None, setGradingPeriodSetCodeDescription = None, setGradingPeriodSetID = None, setIsUpdated = None, setNumber = None, setOriginalEndDate = None, setOriginalStartDate = None, setProcessAction = None, setProcessActionCode = None, setSectionLengthCode = None, setSectionLengthCodeDescription = None, setSectionLengthID = None, setStartDate = None, setRelationships = None, returnTempGradingPeriodID = True, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnGradingPeriodID = False, returnGradingPeriodSetCode = False, returnGradingPeriodSetCodeDescription = False, returnGradingPeriodSetID = False, returnIsUpdated = False, returnModifiedTime = False, returnNumber = False, returnOriginalEndDate = False, returnOriginalStartDate = False, returnProcessAction = False, returnProcessActionCode = False, returnSectionLengthCode = False, returnSectionLengthCodeDescription = False, returnSectionLengthID = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriod/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingPeriod(TempGradingPeriodID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingPeriodError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodErrorID = True, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingPeriodError(TempGradingPeriodErrorID, EntityID = 1, returnTempGradingPeriodErrorID = True, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(TempGradingPeriodErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingPeriodError(TempGradingPeriodErrorID, EntityID = 1, setAcademicStandard = None, setAssignmentName = None, setCategory = None, setCourseDescription = None, setDueDate = None, setError = None, setSectionNumber = None, setSubject = None, setTeacherName = None, setRelationships = None, returnTempGradingPeriodErrorID = True, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/" + str(TempGradingPeriodErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingPeriodError(EntityID = 1, setAcademicStandard = None, setAssignmentName = None, setCategory = None, setCourseDescription = None, setDueDate = None, setError = None, setSectionNumber = None, setSubject = None, setTeacherName = None, setRelationships = None, returnTempGradingPeriodErrorID = True, returnAcademicStandard = False, returnAssignmentName = False, returnCategory = False, returnCourseDescription = False, returnCreatedTime = False, returnDueDate = False, returnError = False, returnModifiedTime = False, returnSectionNumber = False, returnSubject = False, returnTeacherName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingPeriodError(TempGradingPeriodErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingPeriodUpdateProcessError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingPeriodUpdateProcessErrorID = True, returnCreatedTime = False, returnErrorDetail = False, returnModifiedTime = False, returnProcessName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, EntityID = 1, returnTempGradingPeriodUpdateProcessErrorID = True, returnCreatedTime = False, returnErrorDetail = False, returnModifiedTime = False, returnProcessName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(TempGradingPeriodUpdateProcessErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, EntityID = 1, setErrorDetail = None, setProcessName = None, setRelationships = None, returnTempGradingPeriodUpdateProcessErrorID = True, returnCreatedTime = False, returnErrorDetail = False, returnModifiedTime = False, returnProcessName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/" + str(TempGradingPeriodUpdateProcessErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingPeriodUpdateProcessError(EntityID = 1, setErrorDetail = None, setProcessName = None, setRelationships = None, returnTempGradingPeriodUpdateProcessErrorID = True, returnCreatedTime = False, returnErrorDetail = False, returnModifiedTime = False, returnProcessName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingPeriodUpdateProcessError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingPeriodUpdateProcessError(TempGradingPeriodUpdateProcessErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradingUtilityError(EntityID = 1, page = 1, pageSize = 100, returnTempGradingUtilityErrorID = True, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradingUtilityError(TempGradingUtilityErrorID, EntityID = 1, returnTempGradingUtilityErrorID = True, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(TempGradingUtilityErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempGradingUtilityError(TempGradingUtilityErrorID, EntityID = 1, setError = None, setGrade = None, setHonorRollName = None, setStudentName = None, setValue = None, setRelationships = None, returnTempGradingUtilityErrorID = True, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/" + str(TempGradingUtilityErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradingUtilityError(EntityID = 1, setError = None, setGrade = None, setHonorRollName = None, setStudentName = None, setValue = None, setRelationships = None, returnTempGradingUtilityErrorID = True, returnCreatedTime = False, returnError = False, returnGrade = False, returnHonorRollName = False, returnModifiedTime = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempGradingUtilityError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradingUtilityError(TempGradingUtilityErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHonorRollGradeMarkMethodRange(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeID = True, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, EntityID = 1, returnTempHonorRollGradeMarkMethodRangeID = True, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(TempHonorRollGradeMarkMethodRangeID), verb = "get", return_params_list = return_params_list)

def modifyTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, EntityID = 1, setHonorRollGradeMarkMethodID = None, setHonorRollGradeMarkMethodRangeID = None, setIsActive = None, setName = None, setPriorityOrder = None, setTotalAllowableExceptions = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeID = True, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/" + str(TempHonorRollGradeMarkMethodRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHonorRollGradeMarkMethodRange(EntityID = 1, setHonorRollGradeMarkMethodID = None, setHonorRollGradeMarkMethodRangeID = None, setIsActive = None, setName = None, setPriorityOrder = None, setTotalAllowableExceptions = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeID = True, returnCreatedTime = False, returnHonorRollGradeMarkMethodID = False, returnHonorRollGradeMarkMethodRangeID = False, returnIsActive = False, returnModifiedTime = False, returnName = False, returnPriorityOrder = False, returnTotalAllowableExceptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHonorRollGradeMarkMethodRange(TempHonorRollGradeMarkMethodRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHonorRollGradeMarkMethodRangeCourseGroup(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, EntityID = 1, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(TempHonorRollGradeMarkMethodRangeCourseGroupID), verb = "get", return_params_list = return_params_list)

def modifyTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, EntityID = 1, setCourseGroupID = None, setHonorRollGradeMarkMethodRangeCourseGroupID = None, setHonorRollGradeMarkMethodRangeID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/" + str(TempHonorRollGradeMarkMethodRangeCourseGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHonorRollGradeMarkMethodRangeCourseGroup(EntityID = 1, setCourseGroupID = None, setHonorRollGradeMarkMethodRangeCourseGroupID = None, setHonorRollGradeMarkMethodRangeID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeCourseGroupID = True, returnCourseGroupID = False, returnCreatedTime = False, returnHonorRollGradeMarkMethodRangeCourseGroupID = False, returnHonorRollGradeMarkMethodRangeID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeCourseGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHonorRollGradeMarkMethodRangeCourseGroup(TempHonorRollGradeMarkMethodRangeCourseGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHonorRollGradeMarkMethodRangeGradeMark(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, EntityID = 1, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(TempHonorRollGradeMarkMethodRangeGradeMarkID), verb = "get", return_params_list = return_params_list)

def modifyTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, EntityID = 1, setGradeMarkID = None, setHonorRollGradeMarkMethodRangeGradeMarkID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/" + str(TempHonorRollGradeMarkMethodRangeGradeMarkID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHonorRollGradeMarkMethodRangeGradeMark(EntityID = 1, setGradeMarkID = None, setHonorRollGradeMarkMethodRangeGradeMarkID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeGradeMarkID = True, returnCreatedTime = False, returnGradeMarkID = False, returnHonorRollGradeMarkMethodRangeGradeMarkID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradeMark/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHonorRollGradeMarkMethodRangeGradeMark(TempHonorRollGradeMarkMethodRangeGradeMarkID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, EntityID = 1, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, EntityID = 1, setGradingPeriodGradeBucketID = None, setHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/" + str(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(EntityID = 1, setGradingPeriodGradeBucketID = None, setHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = None, setTempHonorRollGradeMarkMethodRangeID = None, setRelationships = None, returnTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = True, returnCreatedTime = False, returnGradingPeriodGradeBucketID = False, returnHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID = False, returnModifiedTime = False, returnTempHonorRollGradeMarkMethodRangeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucket(TempHonorRollGradeMarkMethodRangeGradingPeriodGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHonorRollMethodRange(EntityID = 1, page = 1, pageSize = 100, returnTempHonorRollMethodRangeID = True, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHonorRollMethodRange(TempHonorRollMethodRangeID, EntityID = 1, returnTempHonorRollMethodRangeID = True, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(TempHonorRollMethodRangeID), verb = "get", return_params_list = return_params_list)

def modifyTempHonorRollMethodRange(TempHonorRollMethodRangeID, EntityID = 1, setGPAHigh = None, setGPALow = None, setHonorRollMethodRangeID = None, setIsUsed = None, setName = None, setRelationships = None, returnTempHonorRollMethodRangeID = True, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/" + str(TempHonorRollMethodRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHonorRollMethodRange(EntityID = 1, setGPAHigh = None, setGPALow = None, setHonorRollMethodRangeID = None, setIsUsed = None, setName = None, setRelationships = None, returnTempHonorRollMethodRangeID = True, returnCreatedTime = False, returnGPAHigh = False, returnGPALow = False, returnHonorRollMethodRangeID = False, returnIsUsed = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempHonorRollMethodRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHonorRollMethodRange(TempHonorRollMethodRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempMassChangeSystemDatesError(EntityID = 1, page = 1, pageSize = 100, returnTempMassChangeSystemDatesErrorID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnIsParent = False, returnModifiedTime = False, returnOriginalPrimaryKey = False, returnParentPrimaryKey = False, returnSortOrder = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, EntityID = 1, returnTempMassChangeSystemDatesErrorID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnIsParent = False, returnModifiedTime = False, returnOriginalPrimaryKey = False, returnParentPrimaryKey = False, returnSortOrder = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(TempMassChangeSystemDatesErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, EntityID = 1, setDescription = None, setError = None, setIsParent = None, setOriginalPrimaryKey = None, setParentPrimaryKey = None, setSortOrder = None, setTableType = None, setTableTypeCode = None, setRelationships = None, returnTempMassChangeSystemDatesErrorID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnIsParent = False, returnModifiedTime = False, returnOriginalPrimaryKey = False, returnParentPrimaryKey = False, returnSortOrder = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/" + str(TempMassChangeSystemDatesErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempMassChangeSystemDatesError(EntityID = 1, setDescription = None, setError = None, setIsParent = None, setOriginalPrimaryKey = None, setParentPrimaryKey = None, setSortOrder = None, setTableType = None, setTableTypeCode = None, setRelationships = None, returnTempMassChangeSystemDatesErrorID = True, returnCreatedTime = False, returnDescription = False, returnError = False, returnIsParent = False, returnModifiedTime = False, returnOriginalPrimaryKey = False, returnParentPrimaryKey = False, returnSortOrder = False, returnTableType = False, returnTableTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempMassChangeSystemDatesError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempMassChangeSystemDatesError(TempMassChangeSystemDatesErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentCommentBucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentCommentBucket(TempStudentCommentBucketID, EntityID = 1, returnTempStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(TempStudentCommentBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentCommentBucket(TempStudentCommentBucketID, EntityID = 1, setCommentBucketID = None, setCommentBucketName = None, setCurrentCommentCode = None, setDisplayOrder = None, setGradingPeriodDescription = None, setGradingPeriodID = None, setNewCommentCode = None, setNewCommentCodeID = None, setSectionLengthCode = None, setStudentCommentBucketID = None, setStudentName = None, setStudentSectionDescription = None, setStudentSectionID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/" + str(TempStudentCommentBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentCommentBucket(EntityID = 1, setCommentBucketID = None, setCommentBucketName = None, setCurrentCommentCode = None, setDisplayOrder = None, setGradingPeriodDescription = None, setGradingPeriodID = None, setNewCommentCode = None, setNewCommentCodeID = None, setSectionLengthCode = None, setStudentCommentBucketID = None, setStudentName = None, setStudentSectionDescription = None, setStudentSectionID = None, setWorkflowAction = None, setWorkflowActionCode = None, setRelationships = None, returnTempStudentCommentBucketID = True, returnCommentBucketID = False, returnCommentBucketName = False, returnCreatedTime = False, returnCurrentCommentCode = False, returnDisplayOrder = False, returnGradingPeriodDescription = False, returnGradingPeriodID = False, returnModifiedTime = False, returnNewCommentCode = False, returnNewCommentCodeID = False, returnSectionLengthCode = False, returnStudentCommentBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowAction = False, returnWorkflowActionCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentCommentBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentCommentBucket(TempStudentCommentBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentGPABucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGPABucketID = True, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentGPABucket(TempStudentGPABucketID, EntityID = 1, returnTempStudentGPABucketID = True, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(TempStudentGPABucketID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentGPABucket(TempStudentGPABucketID, EntityID = 1, setCorrectBonusGPAPoints = None, setCorrectGPACredits = None, setCorrectGPAPoints = None, setCourseName = None, setCurrentBonusGPAPoints = None, setCurrentGPACredits = None, setCurrentGPAPoints = None, setEntityID = None, setGPABucketCodeDescription = None, setGPABucketID = None, setGPAMethodCodeDescription = None, setGPAMethodID = None, setGradeBucketCodeDescription = None, setGradingPeriodGradeBucketID = None, setIsDelete = None, setIsGradReqRankGPA = None, setSchoolYearDescription = None, setSchoolYearID = None, setSchoolYearIDForPostSave = None, setStudentGPABucketGroupID = None, setStudentGPABucketGroupIsFromTemp = None, setStudentGPABucketID = None, setStudentGradeBucketID = None, setStudentGradeBucketIsFromTemp = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionGPABucketGroupID = None, setStudentSectionGPABucketGroupIsFromTemp = None, setStudentSectionID = None, setRelationships = None, returnTempStudentGPABucketID = True, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/" + str(TempStudentGPABucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentGPABucket(EntityID = 1, setCorrectBonusGPAPoints = None, setCorrectGPACredits = None, setCorrectGPAPoints = None, setCourseName = None, setCurrentBonusGPAPoints = None, setCurrentGPACredits = None, setCurrentGPAPoints = None, setEntityID = None, setGPABucketCodeDescription = None, setGPABucketID = None, setGPAMethodCodeDescription = None, setGPAMethodID = None, setGradeBucketCodeDescription = None, setGradingPeriodGradeBucketID = None, setIsDelete = None, setIsGradReqRankGPA = None, setSchoolYearDescription = None, setSchoolYearID = None, setSchoolYearIDForPostSave = None, setStudentGPABucketGroupID = None, setStudentGPABucketGroupIsFromTemp = None, setStudentGPABucketID = None, setStudentGradeBucketID = None, setStudentGradeBucketIsFromTemp = None, setStudentID = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionGPABucketGroupID = None, setStudentSectionGPABucketGroupIsFromTemp = None, setStudentSectionID = None, setRelationships = None, returnTempStudentGPABucketID = True, returnCorrectBonusGPAPoints = False, returnCorrectGPACredits = False, returnCorrectGPAPoints = False, returnCourseName = False, returnCreatedTime = False, returnCurrentBonusGPAPoints = False, returnCurrentGPACredits = False, returnCurrentGPAPoints = False, returnEntityID = False, returnGPABucketCodeDescription = False, returnGPABucketID = False, returnGPAMethodCodeDescription = False, returnGPAMethodID = False, returnGradeBucketCodeDescription = False, returnGradingPeriodGradeBucketID = False, returnIsDelete = False, returnIsGradReqRankGPA = False, returnModifiedTime = False, returnSchoolYearDescription = False, returnSchoolYearID = False, returnSchoolYearIDForPostSave = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentGPABucketID = False, returnStudentGradeBucketID = False, returnStudentGradeBucketIsFromTemp = False, returnStudentID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionGPABucketGroupID = False, returnStudentSectionGPABucketGroupIsFromTemp = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentGPABucket(TempStudentGPABucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGPABucketGroupID = True, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentGPABucketGroup(TempStudentGPABucketGroupID, EntityID = 1, returnTempStudentGPABucketGroupID = True, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(TempStudentGPABucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentGPABucketGroup(TempStudentGPABucketGroupID, EntityID = 1, setGPABucketID = None, setGPAMethodID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnTempStudentGPABucketGroupID = True, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/" + str(TempStudentGPABucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentGPABucketGroup(EntityID = 1, setGPABucketID = None, setGPAMethodID = None, setSchoolYearID = None, setStudentID = None, setRelationships = None, returnTempStudentGPABucketGroupID = True, returnCreatedTime = False, returnGPABucketID = False, returnGPAMethodID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGPABucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentGPABucketGroup(TempStudentGPABucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentGradeBucket(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradeBucketID = True, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentGradeBucket(TempStudentGradeBucketID, EntityID = 1, returnTempStudentGradeBucketID = True, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(TempStudentGradeBucketID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentGradeBucket(TempStudentGradeBucketID, EntityID = 1, setCompleteByTeacherCode = None, setDoNotPost = None, setEntityID = None, setGradeBucketCode = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkIDReverse = None, setGradingPeriodGradeBucketID = None, setIsTransferBucket = None, setIsTransferCourse = None, setNewCode = None, setOldCode = None, setOverallPercent = None, setOverallStatus = None, setPercentWithAdjustment = None, setSchoolYearID = None, setSectionID = None, setStudentGradeBucketID = None, setStudentName = None, setStudentSectionID = None, setStudentSectionName = None, setRelationships = None, returnTempStudentGradeBucketID = True, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/" + str(TempStudentGradeBucketID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentGradeBucket(EntityID = 1, setCompleteByTeacherCode = None, setDoNotPost = None, setEntityID = None, setGradeBucketCode = None, setGradeMarkID = None, setGradeMarkIDOverride = None, setGradeMarkIDReverse = None, setGradingPeriodGradeBucketID = None, setIsTransferBucket = None, setIsTransferCourse = None, setNewCode = None, setOldCode = None, setOverallPercent = None, setOverallStatus = None, setPercentWithAdjustment = None, setSchoolYearID = None, setSectionID = None, setStudentGradeBucketID = None, setStudentName = None, setStudentSectionID = None, setStudentSectionName = None, setRelationships = None, returnTempStudentGradeBucketID = True, returnCompleteByTeacherCode = False, returnCreatedTime = False, returnDoNotPost = False, returnEntityID = False, returnGradeBucketCode = False, returnGradeMarkID = False, returnGradeMarkIDOverride = False, returnGradeMarkIDReverse = False, returnGradingPeriodGradeBucketID = False, returnIsTransferBucket = False, returnIsTransferCourse = False, returnModifiedTime = False, returnNewCode = False, returnOldCode = False, returnOverallPercent = False, returnOverallStatus = False, returnPercentWithAdjustment = False, returnSchoolYearID = False, returnSectionID = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionID = False, returnStudentSectionName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucket/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentGradeBucket(TempStudentGradeBucketID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentGradeBucketFlag(EntityID = 1, page = 1, pageSize = 100, returnTempStudentGradeBucketFlagID = True, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsException = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, EntityID = 1, returnTempStudentGradeBucketFlagID = True, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsException = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(TempStudentGradeBucketFlagID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, EntityID = 1, setCourseSectionCode = None, setExceptionReason = None, setGradeBucketFlagCode = None, setGradeBucketFlagID = None, setGradeBucketLabel = None, setGradeMarkCode = None, setIsException = None, setSectionLengthCode = None, setStudentGradeBucketID = None, setStudentName = None, setStudentSectionDescription = None, setRelationships = None, returnTempStudentGradeBucketFlagID = True, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsException = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/" + str(TempStudentGradeBucketFlagID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentGradeBucketFlag(EntityID = 1, setCourseSectionCode = None, setExceptionReason = None, setGradeBucketFlagCode = None, setGradeBucketFlagID = None, setGradeBucketLabel = None, setGradeMarkCode = None, setIsException = None, setSectionLengthCode = None, setStudentGradeBucketID = None, setStudentName = None, setStudentSectionDescription = None, setRelationships = None, returnTempStudentGradeBucketFlagID = True, returnCourseSectionCode = False, returnCreatedTime = False, returnExceptionReason = False, returnGradeBucketFlagCode = False, returnGradeBucketFlagID = False, returnGradeBucketLabel = False, returnGradeMarkCode = False, returnIsException = False, returnModifiedTime = False, returnSectionLengthCode = False, returnStudentGradeBucketID = False, returnStudentName = False, returnStudentSectionDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentGradeBucketFlag/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentGradeBucketFlag(TempStudentGradeBucketFlagID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentHonorRollRunLevel(EntityID = 1, page = 1, pageSize = 100, returnTempStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, EntityID = 1, returnTempStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(TempStudentHonorRollRunLevelID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, EntityID = 1, setGPAValue = None, setGrade = None, setHonorRollRunLevelID = None, setHonorRollRunLevelName = None, setHonorRollRunLevelOrder = None, setStudentID = None, setStudentName = None, setRelationships = None, returnTempStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/" + str(TempStudentHonorRollRunLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentHonorRollRunLevel(EntityID = 1, setGPAValue = None, setGrade = None, setHonorRollRunLevelID = None, setHonorRollRunLevelName = None, setHonorRollRunLevelOrder = None, setStudentID = None, setStudentName = None, setRelationships = None, returnTempStudentHonorRollRunLevelID = True, returnCreatedTime = False, returnGPAValue = False, returnGrade = False, returnHonorRollRunLevelID = False, returnHonorRollRunLevelName = False, returnHonorRollRunLevelOrder = False, returnModifiedTime = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentHonorRollRunLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentHonorRollRunLevel(TempStudentHonorRollRunLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentRank(EntityID = 1, page = 1, pageSize = 100, returnTempStudentRankID = True, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentRank(TempStudentRankID, EntityID = 1, returnTempStudentRankID = True, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(TempStudentRankID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentRank(TempStudentRankID, EntityID = 1, setCohortNumericYear = None, setGPA = None, setGraduationRequirementYear = None, setIsManualRank = None, setIsProspectiveRank = None, setNoRank = None, setRank = None, setRankMethodID = None, setSchoolYearIDCohort = None, setStudentGrade = None, setStudentID = None, setStudentName = None, setStudentRankID = None, setStudentRankSort = None, setTotalStudents = None, setUseOverride = None, setRelationships = None, returnTempStudentRankID = True, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/" + str(TempStudentRankID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentRank(EntityID = 1, setCohortNumericYear = None, setGPA = None, setGraduationRequirementYear = None, setIsManualRank = None, setIsProspectiveRank = None, setNoRank = None, setRank = None, setRankMethodID = None, setSchoolYearIDCohort = None, setStudentGrade = None, setStudentID = None, setStudentName = None, setStudentRankID = None, setStudentRankSort = None, setTotalStudents = None, setUseOverride = None, setRelationships = None, returnTempStudentRankID = True, returnCohortNumericYear = False, returnCreatedTime = False, returnGPA = False, returnGraduationRequirementYear = False, returnIsManualRank = False, returnIsProspectiveRank = False, returnModifiedTime = False, returnNoRank = False, returnRank = False, returnRankMethodID = False, returnSchoolYearIDCohort = False, returnStudentGrade = False, returnStudentID = False, returnStudentName = False, returnStudentRankID = False, returnStudentRankSort = False, returnTotalStudents = False, returnUseOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentRank/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentRank(TempStudentRankID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSection(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSection(TempStudentSectionID, EntityID = 1, returnTempStudentSectionID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(TempStudentSectionID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSection(TempStudentSectionID, EntityID = 1, setCourse = None, setSectionCode = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setRelationships = None, returnTempStudentSectionID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/" + str(TempStudentSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSection(EntityID = 1, setCourse = None, setSectionCode = None, setStudentNameLFM = None, setStudentNumber = None, setStudentSectionID = None, setRelationships = None, returnTempStudentSectionID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnSectionCode = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSection(TempStudentSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSectionFailedUpdate(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionFailedUpdateID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, EntityID = 1, returnTempStudentSectionFailedUpdateID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(TempStudentSectionFailedUpdateID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, EntityID = 1, setCourse = None, setNote = None, setSection = None, setStudentNameLFM = None, setRelationships = None, returnTempStudentSectionFailedUpdateID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/" + str(TempStudentSectionFailedUpdateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSectionFailedUpdate(EntityID = 1, setCourse = None, setNote = None, setSection = None, setStudentNameLFM = None, setRelationships = None, returnTempStudentSectionFailedUpdateID = True, returnCourse = False, returnCreatedTime = False, returnModifiedTime = False, returnNote = False, returnSection = False, returnStudentNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionFailedUpdate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSectionFailedUpdate(TempStudentSectionFailedUpdateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentSectionGPABucketGroup(EntityID = 1, page = 1, pageSize = 100, returnTempStudentSectionGPABucketGroupID = True, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, EntityID = 1, returnTempStudentSectionGPABucketGroupID = True, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(TempStudentSectionGPABucketGroupID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, EntityID = 1, setEntityID = None, setGPABucketID = None, setGPAMethodID = None, setIsCumulative = None, setSchoolYearID = None, setStudentGPABucketGroupID = None, setStudentGPABucketGroupIsFromTemp = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnTempStudentSectionGPABucketGroupID = True, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/" + str(TempStudentSectionGPABucketGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentSectionGPABucketGroup(EntityID = 1, setEntityID = None, setGPABucketID = None, setGPAMethodID = None, setIsCumulative = None, setSchoolYearID = None, setStudentGPABucketGroupID = None, setStudentGPABucketGroupIsFromTemp = None, setStudentID = None, setStudentSectionID = None, setRelationships = None, returnTempStudentSectionGPABucketGroupID = True, returnCreatedTime = False, returnEntityID = False, returnGPABucketID = False, returnGPAMethodID = False, returnIsCumulative = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentGPABucketGroupID = False, returnStudentGPABucketGroupIsFromTemp = False, returnStudentID = False, returnStudentSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempStudentSectionGPABucketGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentSectionGPABucketGroup(TempStudentSectionGPABucketGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempTransferCourse(EntityID = 1, page = 1, pageSize = 100, returnTempTransferCourseID = True, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempTransferCourse(TempTransferCourseID, EntityID = 1, returnTempTransferCourseID = True, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(TempTransferCourseID), verb = "get", return_params_list = return_params_list)

def modifyTempTransferCourse(TempTransferCourseID, EntityID = 1, setCourseCredits = None, setCourseDescription = None, setCourseID = None, setCourseSection = None, setEarnedCreditOverride = None, setEndDate = None, setEntityCode = None, setEntityID = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLinking = None, setGradedCourse = None, setGradeReferenceID = None, setGradingPeriodSetID = None, setGradYear = None, setSchoolYear = None, setSchoolYearID = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentID = None, setTotalEarnedCredits = None, setTotalFailedCredits = None, setUseAddOnGPA = None, setUseEarnedCreditOverride = None, setUseEarnedCreditPercentOverride = None, setRelationships = None, returnTempTransferCourseID = True, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/" + str(TempTransferCourseID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempTransferCourse(EntityID = 1, setCourseCredits = None, setCourseDescription = None, setCourseID = None, setCourseSection = None, setEarnedCreditOverride = None, setEndDate = None, setEntityCode = None, setEntityID = None, setExcludeFromReportCardsAndTranscripts = None, setExcludeFromStudentSectionLinking = None, setGradedCourse = None, setGradeReferenceID = None, setGradingPeriodSetID = None, setGradYear = None, setSchoolYear = None, setSchoolYearID = None, setSectionID = None, setSectionLengthID = None, setSectionLengthSubsetID = None, setStartDate = None, setStudentID = None, setTotalEarnedCredits = None, setTotalFailedCredits = None, setUseAddOnGPA = None, setUseEarnedCreditOverride = None, setUseEarnedCreditPercentOverride = None, setRelationships = None, returnTempTransferCourseID = True, returnCourseCredits = False, returnCourseDescription = False, returnCourseID = False, returnCourseSection = False, returnCreatedTime = False, returnEarnedCreditOverride = False, returnEndDate = False, returnEntityCode = False, returnEntityID = False, returnExcludeFromReportCardsAndTranscripts = False, returnExcludeFromStudentSectionLinking = False, returnGradedCourse = False, returnGradeReferenceID = False, returnGradingPeriodSetID = False, returnGradYear = False, returnModifiedTime = False, returnSchoolYear = False, returnSchoolYearID = False, returnSectionID = False, returnSectionLengthID = False, returnSectionLengthSubsetID = False, returnStartDate = False, returnStudentID = False, returnTotalEarnedCredits = False, returnTotalFailedCredits = False, returnUseAddOnGPA = False, returnUseEarnedCreditOverride = False, returnUseEarnedCreditPercentOverride = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TempTransferCourse/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempTransferCourse(TempTransferCourseID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTranscriptNote(EntityID = 1, page = 1, pageSize = 100, returnTranscriptNoteID = True, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTranscriptNote(TranscriptNoteID, EntityID = 1, returnTranscriptNoteID = True, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(TranscriptNoteID), verb = "get", return_params_list = return_params_list)

def modifyTranscriptNote(TranscriptNoteID, EntityID = 1, setDateAdded = None, setNote = None, setStudentID = None, setRelationships = None, returnTranscriptNoteID = True, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/" + str(TranscriptNoteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTranscriptNote(EntityID = 1, setDateAdded = None, setNote = None, setStudentID = None, setRelationships = None, returnTranscriptNoteID = True, returnCreatedTime = False, returnDateAdded = False, returnModifiedTime = False, returnNote = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptNote/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTranscriptNote(TranscriptNoteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTranscriptSent(EntityID = 1, page = 1, pageSize = 100, returnTranscriptSentID = True, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTranscriptSent(TranscriptSentID, EntityID = 1, returnTranscriptSentID = True, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(TranscriptSentID), verb = "get", return_params_list = return_params_list)

def modifyTranscriptSent(TranscriptSentID, EntityID = 1, setComment = None, setDateSent = None, setInstitutionID = None, setStudentID = None, setRelationships = None, returnTranscriptSentID = True, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/" + str(TranscriptSentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTranscriptSent(EntityID = 1, setComment = None, setDateSent = None, setInstitutionID = None, setStudentID = None, setRelationships = None, returnTranscriptSentID = True, returnComment = False, returnCreatedTime = False, returnDateSent = False, returnInstitutionID = False, returnModifiedTime = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Grading/TranscriptSent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTranscriptSent(TranscriptSentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")