# This module contains Curriculum functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardID = True, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandard(AcademicStandardID, EntityID = 1, returnAcademicStandardID = True, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandard(AcademicStandardID, EntityID = 1, setAcademicStandardDefaultID = None, setAcademicStandardGradeRangeID = None, setAcademicStandardIDParent = None, setDescription = None, setDescriptionToUse = None, setDisplayAs = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setIsHighFrequencyWord = None, setIsLettersAndSounds = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setParentGuid = None, setSequence = None, setStateNumber = None, setRelationships = None, returnAcademicStandardID = True, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandard(EntityID = 1, setAcademicStandardDefaultID = None, setAcademicStandardGradeRangeID = None, setAcademicStandardIDParent = None, setDescription = None, setDescriptionToUse = None, setDisplayAs = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setIsHighFrequencyWord = None, setIsLettersAndSounds = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setParentGuid = None, setSequence = None, setStateNumber = None, setRelationships = None, returnAcademicStandardID = True, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandard(AcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardDefaultID = True, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, returnAcademicStandardDefaultID = True, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, setAcademicStandardDefaultIDParent = None, setAcademicStandardGradeRangeDefaultID = None, setDescription = None, setIsHighFrequencyWord = None, setKey = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setParentGuid = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardDefaultID = True, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardDefault(EntityID = 1, setAcademicStandardDefaultIDParent = None, setAcademicStandardGradeRangeDefaultID = None, setDescription = None, setIsHighFrequencyWord = None, setKey = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setParentGuid = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardDefaultID = True, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardGradeRange(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradeRangeID = True, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, returnAcademicStandardGradeRangeID = True, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setKey = None, setSequence = None, setRelationships = None, returnAcademicStandardGradeRangeID = True, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardGradeRange(EntityID = 1, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setKey = None, setSequence = None, setRelationships = None, returnAcademicStandardGradeRangeID = True, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardGradeRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardGradeRangeDefaultID = True, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, returnAcademicStandardGradeRangeDefaultID = True, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, setAcademicStandardSubjectDefaultID = None, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardGradeRangeDefaultID = True, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardGradeRangeDefault(EntityID = 1, setAcademicStandardSubjectDefaultID = None, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardGradeRangeDefaultID = True, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardHierarchyDepthID = True, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, returnAcademicStandardHierarchyDepthID = True, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, setAcademicStandardID = None, setAcademicStandardIDAtLevel = None, setDistrictGroupKey = None, setHierarchyDepthID = None, setRelationships = None, returnAcademicStandardHierarchyDepthID = True, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardHierarchyDepth(EntityID = 1, setAcademicStandardID = None, setAcademicStandardIDAtLevel = None, setDistrictGroupKey = None, setHierarchyDepthID = None, setRelationships = None, returnAcademicStandardHierarchyDepthID = True, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardSet(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSetID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardSet(AcademicStandardSetID, EntityID = 1, returnAcademicStandardSetID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardSet(AcademicStandardSetID, EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEnteredByDistrict = None, setIsActive = None, setKey = None, setStateCode = None, setRelationships = None, returnAcademicStandardSetID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardSet(EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEnteredByDistrict = None, setIsActive = None, setKey = None, setStateCode = None, setRelationships = None, returnAcademicStandardSetID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardSet(AcademicStandardSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardSetDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSetDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, returnAcademicStandardSetDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardSetDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardSetDefault(EntityID = 1, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardSetDefaultID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardSubject(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSubjectID = True, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, returnAcademicStandardSubjectID = True, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, setAcademicStandardSetID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setKey = None, setSequence = None, setYear = None, setRelationships = None, returnAcademicStandardSubjectID = True, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardSubject(EntityID = 1, setAcademicStandardSetID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setKey = None, setSequence = None, setYear = None, setRelationships = None, returnAcademicStandardSubjectID = True, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAcademicStandardSubjectDefault(EntityID = 1, page = 1, pageSize = 100, returnAcademicStandardSubjectDefaultID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, returnAcademicStandardSubjectDefaultID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "get", return_params_list = return_params_list)

def modifyAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardSubjectDefaultID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAcademicStandardSubjectDefault(EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setDescription = None, setKey = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAcademicStandardSubjectDefaultID = True, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAssessmentToolMN(EntityID = 1, page = 1, pageSize = 100, returnAssessmentToolMNID = True, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAssessmentToolMN(AssessmentToolMNID, EntityID = 1, returnAssessmentToolMNID = True, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "get", return_params_list = return_params_list)

def modifyAssessmentToolMN(AssessmentToolMNID, EntityID = 1, setAssessmentToolMNIDClonedFrom = None, setCurriculumYearID = None, setStateAssessmentToolMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnAssessmentToolMNID = True, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAssessmentToolMN(EntityID = 1, setAssessmentToolMNIDClonedFrom = None, setCurriculumYearID = None, setStateAssessmentToolMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnAssessmentToolMNID = True, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAssessmentToolMN(AssessmentToolMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculum(EntityID = 1, page = 1, pageSize = 100, returnCurriculumID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculum(CurriculumID, EntityID = 1, returnCurriculumID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "get", return_params_list = return_params_list)

def modifyCurriculum(CurriculumID, EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEarnedCredits = None, setGradReqRankGPAIgnoreDuplicateCheck = None, setGradReqSubjectTypeID = None, setIsActive = None, setIsAllowedToBeSelectedInCareerPlan = None, setRelationships = None, returnCurriculumID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculum(EntityID = 1, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEarnedCredits = None, setGradReqRankGPAIgnoreDuplicateCheck = None, setGradReqSubjectTypeID = None, setIsActive = None, setIsAllowedToBeSelectedInCareerPlan = None, setRelationships = None, returnCurriculumID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculum(CurriculumID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCurriculumAcademicStandardID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, returnCurriculumAcademicStandardID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, setAcademicStandardID = None, setCurriculumID = None, setDistrictGroupKey = None, setIsGraded = None, setRelationships = None, returnCurriculumAcademicStandardID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumAcademicStandard(EntityID = 1, setAcademicStandardID = None, setCurriculumID = None, setDistrictGroupKey = None, setIsGraded = None, setRelationships = None, returnCurriculumAcademicStandardID = True, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumCustomRequirement(EntityID = 1, page = 1, pageSize = 100, returnCurriculumCustomRequirementID = True, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, returnCurriculumCustomRequirementID = True, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, setCurriculumID = None, setCustomRequirementID = None, setDistrictGroupKey = None, setSchoolYearHigh = None, setSchoolYearLow = None, setRelationships = None, returnCurriculumCustomRequirementID = True, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumCustomRequirement(EntityID = 1, setCurriculumID = None, setCustomRequirementID = None, setDistrictGroupKey = None, setSchoolYearHigh = None, setSchoolYearLow = None, setRelationships = None, returnCurriculumCustomRequirementID = True, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumGradeLevel(EntityID = 1, page = 1, pageSize = 100, returnCurriculumGradeLevelID = True, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, returnCurriculumGradeLevelID = True, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, setCurriculumID = None, setDistrictGroupKey = None, setGradeLevelID = None, setRelationships = None, returnCurriculumGradeLevelID = True, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumGradeLevel(EntityID = 1, setCurriculumID = None, setDistrictGroupKey = None, setGradeLevelID = None, setRelationships = None, returnCurriculumGradeLevelID = True, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumProgramMN(EntityID = 1, page = 1, pageSize = 100, returnCurriculumProgramMNID = True, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, returnCurriculumProgramMNID = True, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, setCurriculumProgramMNIDClonedFrom = None, setCurriculumYearID = None, setStateCurriculumProgramMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnCurriculumProgramMNID = True, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumProgramMN(EntityID = 1, setCurriculumProgramMNIDClonedFrom = None, setCurriculumYearID = None, setStateCurriculumProgramMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnCurriculumProgramMNID = True, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumSubject(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubjectID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumSubject(CurriculumSubjectID, EntityID = 1, returnCurriculumSubjectID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumSubject(CurriculumSubjectID, EntityID = 1, setCurriculumID = None, setCurriculumSubjectIDClonedFrom = None, setDistrictGroupKey = None, setIsDefault = None, setSubjectID = None, setRelationships = None, returnCurriculumSubjectID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumSubject(EntityID = 1, setCurriculumID = None, setCurriculumSubjectIDClonedFrom = None, setDistrictGroupKey = None, setIsDefault = None, setSubjectID = None, setRelationships = None, returnCurriculumSubjectID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumSubject(CurriculumSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumSubjectAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnCurriculumSubjectAcademicStandardID = True, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, returnCurriculumSubjectAcademicStandardID = True, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, setCurriculumAcademicStandardID = None, setCurriculumSubjectID = None, setRelationships = None, returnCurriculumSubjectAcademicStandardID = True, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumSubjectAcademicStandard(EntityID = 1, setCurriculumAcademicStandardID = None, setCurriculumSubjectID = None, setRelationships = None, returnCurriculumSubjectAcademicStandardID = True, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCurriculumYear(EntityID = 1, page = 1, pageSize = 100, returnCurriculumYearID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCurriculumYear(CurriculumYearID, EntityID = 1, returnCurriculumYearID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "get", return_params_list = return_params_list)

def modifyCurriculumYear(CurriculumYearID, EntityID = 1, setCurriculumID = None, setCurriculumYearIDClonedFrom = None, setDescription = None, setDistrictGroupKey = None, setFederalAdvancedPlacementCourseTypeID = None, setFederalSubjectTypeID = None, setIsAdultBasicEducation = None, setIsEndOfCourse = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsFederalProgram = None, setIsGraduationRequirement = None, setIsStateProgram = None, setReportToFitnessGram = None, setSchoolYearID = None, setStateCourseCodeMNID = None, setStateEarlyEducationLocationMNID = None, setStateStandardAddressedCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSubjectAreaCodeMNID = None, setRelationships = None, returnCurriculumYearID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCurriculumYear(EntityID = 1, setCurriculumID = None, setCurriculumYearIDClonedFrom = None, setDescription = None, setDistrictGroupKey = None, setFederalAdvancedPlacementCourseTypeID = None, setFederalSubjectTypeID = None, setIsAdultBasicEducation = None, setIsEndOfCourse = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsFederalProgram = None, setIsGraduationRequirement = None, setIsStateProgram = None, setReportToFitnessGram = None, setSchoolYearID = None, setStateCourseCodeMNID = None, setStateEarlyEducationLocationMNID = None, setStateStandardAddressedCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSubjectAreaCodeMNID = None, setRelationships = None, returnCurriculumYearID = True, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCurriculumYear(CurriculumYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarlyEducationInstructionalApproachMN(EntityID = 1, page = 1, pageSize = 100, returnEarlyEducationInstructionalApproachMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, returnEarlyEducationInstructionalApproachMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "get", return_params_list = return_params_list)

def modifyEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, setCurriculumYearID = None, setEarlyEducationInstructionalApproachMNIDClonedFrom = None, setStateEarlyEducationInstructionalApproachMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnEarlyEducationInstructionalApproachMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarlyEducationInstructionalApproachMN(EntityID = 1, setCurriculumYearID = None, setEarlyEducationInstructionalApproachMNIDClonedFrom = None, setStateEarlyEducationInstructionalApproachMNID = None, setStateImplementationStatusMNID = None, setRelationships = None, returnEarlyEducationInstructionalApproachMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEarlyEducationProgramMN(EntityID = 1, page = 1, pageSize = 100, returnEarlyEducationProgramMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, returnEarlyEducationProgramMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "get", return_params_list = return_params_list)

def modifyEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, setCurriculumYearID = None, setEarlyEducationProgramMNIDClonedFrom = None, setStateEarlyEducationProgramMNID = None, setRelationships = None, returnEarlyEducationProgramMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEarlyEducationProgramMN(EntityID = 1, setCurriculumYearID = None, setEarlyEducationProgramMNIDClonedFrom = None, setStateEarlyEducationProgramMNID = None, setRelationships = None, returnEarlyEducationProgramMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnHierarchyDepthID = True, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getHierarchyDepth(HierarchyDepthID, EntityID = 1, returnHierarchyDepthID = True, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "get", return_params_list = return_params_list)

def modifyHierarchyDepth(HierarchyDepthID, EntityID = 1, setAcademicStandardSetID = None, setCode = None, setDepthLevel = None, setDescription = None, setDistrictGroupKey = None, setRelationships = None, returnHierarchyDepthID = True, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createHierarchyDepth(EntityID = 1, setAcademicStandardSetID = None, setCode = None, setDepthLevel = None, setDescription = None, setDistrictGroupKey = None, setRelationships = None, returnHierarchyDepthID = True, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteHierarchyDepth(HierarchyDepthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPrerequisite(EntityID = 1, page = 1, pageSize = 100, returnPrerequisiteID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPrerequisite(PrerequisiteID, EntityID = 1, returnPrerequisiteID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "get", return_params_list = return_params_list)

def modifyPrerequisite(PrerequisiteID, EntityID = 1, setCode = None, setCurriculumID = None, setDescription = None, setDistrictGroupKey = None, setEarnedCredits = None, setSchoolYearHigh = None, setSchoolYearLow = None, setRelationships = None, returnPrerequisiteID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPrerequisite(EntityID = 1, setCode = None, setCurriculumID = None, setDescription = None, setDistrictGroupKey = None, setEarnedCredits = None, setSchoolYearHigh = None, setSchoolYearLow = None, setRelationships = None, returnPrerequisiteID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePrerequisite(PrerequisiteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPrerequisiteCurriculum(EntityID = 1, page = 1, pageSize = 100, returnPrerequisiteCurriculumID = True, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, returnPrerequisiteCurriculumID = True, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "get", return_params_list = return_params_list)

def modifyPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, setCurriculumIDRequired = None, setPrerequisiteID = None, setRelationships = None, returnPrerequisiteCurriculumID = True, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPrerequisiteCurriculum(EntityID = 1, setCurriculumIDRequired = None, setPrerequisiteID = None, setRelationships = None, returnPrerequisiteCurriculumID = True, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySiteBasedInitiativeMN(EntityID = 1, page = 1, pageSize = 100, returnSiteBasedInitiativeMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, returnSiteBasedInitiativeMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "get", return_params_list = return_params_list)

def modifySiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, setCurriculumYearID = None, setSiteBasedInitiativeMNIDClonedFrom = None, setStateImplementationStatusMNID = None, setStateSiteBasedInitiativeMNID = None, setRelationships = None, returnSiteBasedInitiativeMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSiteBasedInitiativeMN(EntityID = 1, setCurriculumYearID = None, setSiteBasedInitiativeMNIDClonedFrom = None, setStateImplementationStatusMNID = None, setStateSiteBasedInitiativeMNID = None, setRelationships = None, returnSiteBasedInitiativeMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStandardPlacementMN(EntityID = 1, page = 1, pageSize = 100, returnStandardPlacementMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStandardPlacementMN(StandardPlacementMNID, EntityID = 1, returnStandardPlacementMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "get", return_params_list = return_params_list)

def modifyStandardPlacementMN(StandardPlacementMNID, EntityID = 1, setCurriculumYearID = None, setStateStandardCodeMNID = None, setRelationships = None, returnStandardPlacementMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStandardPlacementMN(EntityID = 1, setCurriculumYearID = None, setStateStandardCodeMNID = None, setRelationships = None, returnStandardPlacementMNID = True, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStandardPlacementMN(StandardPlacementMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubject(EntityID = 1, page = 1, pageSize = 100, returnSubjectID = True, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubject(SubjectID, EntityID = 1, returnSubjectID = True, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "get", return_params_list = return_params_list)

def modifySubject(SubjectID, EntityID = 1, setBackgroundColor = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setSchoolYearID = None, setSubjectIDClonedFrom = None, setTextColor = None, setRelationships = None, returnSubjectID = True, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubject(EntityID = 1, setBackgroundColor = None, setCode = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setSchoolYearID = None, setSubjectIDClonedFrom = None, setTextColor = None, setRelationships = None, returnSubjectID = True, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubject(SubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAcademicStandard(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardID = True, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAcademicStandard(TempAcademicStandardID, EntityID = 1, returnTempAcademicStandardID = True, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "get", return_params_list = return_params_list)

def modifyTempAcademicStandard(TempAcademicStandardID, EntityID = 1, setDescription = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setImportedFrom = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLevel = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTempAcademicStandardGradeRangeID = None, setTempAcademicStandardIDParent = None, setTempAcademicStandardSetID = None, setRelationships = None, returnTempAcademicStandardID = True, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAcademicStandard(EntityID = 1, setDescription = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setImportedFrom = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLevel = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTempAcademicStandardGradeRangeID = None, setTempAcademicStandardIDParent = None, setTempAcademicStandardSetID = None, setRelationships = None, returnTempAcademicStandardID = True, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAcademicStandard(TempAcademicStandardID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAcademicStandardGradeRange(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardGradeRangeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, returnTempAcademicStandardGradeRangeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "get", return_params_list = return_params_list)

def modifyTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, setCode = None, setDescription = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setImportedFrom = None, setSequence = None, setTempAcademicStandardSubjectID = None, setRelationships = None, returnTempAcademicStandardGradeRangeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAcademicStandardGradeRange(EntityID = 1, setCode = None, setDescription = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setImportedFrom = None, setSequence = None, setTempAcademicStandardSubjectID = None, setRelationships = None, returnTempAcademicStandardGradeRangeID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAcademicStandardSet(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardSetID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, returnTempAcademicStandardSetID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "get", return_params_list = return_params_list)

def modifyTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEnteredByDistrict = None, setImportedFrom = None, setIsActive = None, setStateCode = None, setRelationships = None, returnTempAcademicStandardSetID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAcademicStandardSet(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setEnteredByDistrict = None, setImportedFrom = None, setIsActive = None, setStateCode = None, setRelationships = None, returnTempAcademicStandardSetID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAcademicStandardSubject(EntityID = 1, page = 1, pageSize = 100, returnTempAcademicStandardSubjectID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, returnTempAcademicStandardSubjectID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "get", return_params_list = return_params_list)

def modifyTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, setCode = None, setDescription = None, setEnteredByDistrict = None, setImportedFrom = None, setSequence = None, setTempAcademicStandardSetID = None, setYear = None, setRelationships = None, returnTempAcademicStandardSubjectID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAcademicStandardSubject(EntityID = 1, setCode = None, setDescription = None, setEnteredByDistrict = None, setImportedFrom = None, setSequence = None, setTempAcademicStandardSetID = None, setYear = None, setRelationships = None, returnTempAcademicStandardSubjectID = True, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempGradeRangeCopyResult(EntityID = 1, page = 1, pageSize = 100, returnTempGradeRangeCopyResultID = True, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, returnTempGradeRangeCopyResultID = True, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "get", return_params_list = return_params_list)

def modifyTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, setAcademicStandardSubjectCode = None, setErrorText = None, setGradeRangeCode = None, setIsError = None, setRelationships = None, returnTempGradeRangeCopyResultID = True, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempGradeRangeCopyResult(EntityID = 1, setAcademicStandardSubjectCode = None, setErrorText = None, setGradeRangeCode = None, setIsError = None, setRelationships = None, returnTempGradeRangeCopyResultID = True, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempHierarchyDepth(EntityID = 1, page = 1, pageSize = 100, returnTempHierarchyDepthID = True, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, returnTempHierarchyDepthID = True, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "get", return_params_list = return_params_list)

def modifyTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, setAcademicStandardSetCode = None, setAcademicStandardSetDescription = None, setCode = None, setDepthLevel = None, setDescription = None, setRelationships = None, returnTempHierarchyDepthID = True, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempHierarchyDepth(EntityID = 1, setAcademicStandardSetCode = None, setAcademicStandardSetDescription = None, setCode = None, setDepthLevel = None, setDescription = None, setRelationships = None, returnTempHierarchyDepthID = True, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")