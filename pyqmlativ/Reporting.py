# This module contains Reporting functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryBurstAction(EntityID = 1, page = 1, pageSize = 100, returnBurstActionID = True, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getBurstAction(BurstActionID, EntityID = 1, returnBurstActionID = True, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(BurstActionID), verb = "get", return_params_list = return_params_list)

def modifyBurstAction(BurstActionID, EntityID = 1, setActionHandlerXML = None, setCanBeReverted = None, setIsPrintAction = None, setName = None, setObjectID = None, setParameterSxlPath = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnBurstActionID = True, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(BurstActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createBurstAction(EntityID = 1, setActionHandlerXML = None, setCanBeReverted = None, setIsPrintAction = None, setName = None, setObjectID = None, setParameterSxlPath = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnBurstActionID = True, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteBurstAction(BurstActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setDaysToSaveReportResults = None, setRelationships = None, returnConfigSystemID = True, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setDaysToSaveReportResults = None, setRelationships = None, returnConfigSystemID = True, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReport(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportID = True, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReport(DataMiningReportID, EntityID = 1, returnDataMiningReportID = True, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(DataMiningReportID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReport(DataMiningReportID, EntityID = 1, setDelimiter = None, setDelimiterCode = None, setHasFieldsThatCanBeTotaled = None, setIncludeSectionHeaders = None, setIsFixedWidth = None, setReportID = None, setSubjectID = None, setTextQualifier = None, setTextQualifierCode = None, setRelationships = None, returnDataMiningReportID = True, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(DataMiningReportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReport(EntityID = 1, setDelimiter = None, setDelimiterCode = None, setHasFieldsThatCanBeTotaled = None, setIncludeSectionHeaders = None, setIsFixedWidth = None, setReportID = None, setSubjectID = None, setTextQualifier = None, setTextQualifierCode = None, setRelationships = None, returnDataMiningReportID = True, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReport(DataMiningReportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportField(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportFieldID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportField(DataMiningReportFieldID, EntityID = 1, returnDataMiningReportFieldID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(DataMiningReportFieldID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportField(DataMiningReportFieldID, EntityID = 1, setDataMiningReportID = None, setDisplayOrder = None, setLabel = None, setShowTotal = None, setStartPosition = None, setSubtopicFieldID = None, setWidth = None, setRelationships = None, returnDataMiningReportFieldID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(DataMiningReportFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportField(EntityID = 1, setDataMiningReportID = None, setDisplayOrder = None, setLabel = None, setShowTotal = None, setStartPosition = None, setSubtopicFieldID = None, setWidth = None, setRelationships = None, returnDataMiningReportFieldID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportField(DataMiningReportFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportFieldFilter(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportFieldFilterID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1, returnDataMiningReportFieldFilterID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(DataMiningReportFieldFilterID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1, setDataMiningReportID = None, setFilterType = None, setFilterTypeCode = None, setHigh = None, setIsPrompt = None, setListAsJsonDictionaryString = None, setListAsJsonListString = None, setListBackingData = None, setLow = None, setPromptIsRequired = None, setPromptLabel = None, setSubtopicFieldID = None, setRelationships = None, returnDataMiningReportFieldFilterID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(DataMiningReportFieldFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportFieldFilter(EntityID = 1, setDataMiningReportID = None, setFilterType = None, setFilterTypeCode = None, setHigh = None, setIsPrompt = None, setListAsJsonDictionaryString = None, setListAsJsonListString = None, setListBackingData = None, setLow = None, setPromptIsRequired = None, setPromptLabel = None, setSubtopicFieldID = None, setRelationships = None, returnDataMiningReportFieldFilterID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportFieldParameter(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportFieldParameterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1, returnDataMiningReportFieldParameterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(DataMiningReportFieldParameterID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1, setDataMiningReportID = None, setDataType = None, setDataTypeString = None, setIsPrompt = None, setParameterName = None, setPromptLabel = None, setValue = None, setValueString = None, setRelationships = None, returnDataMiningReportFieldParameterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(DataMiningReportFieldParameterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportFieldParameter(EntityID = 1, setDataMiningReportID = None, setDataType = None, setDataTypeString = None, setIsPrompt = None, setParameterName = None, setPromptLabel = None, setValue = None, setValueString = None, setRelationships = None, returnDataMiningReportFieldParameterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportFieldSort(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportFieldSortID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1, returnDataMiningReportFieldSortID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(DataMiningReportFieldSortID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1, setBreakType = None, setBreakTypeCode = None, setDataMiningReportID = None, setLength = None, setShowCount = None, setShowSubtotals = None, setSortDirection = None, setSortDirectionCode = None, setSortOrder = None, setSubtopicFieldID = None, setRelationships = None, returnDataMiningReportFieldSortID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(DataMiningReportFieldSortID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportFieldSort(EntityID = 1, setBreakType = None, setBreakTypeCode = None, setDataMiningReportID = None, setLength = None, setShowCount = None, setShowSubtotals = None, setSortDirection = None, setSortDirectionCode = None, setSortOrder = None, setSubtopicFieldID = None, setRelationships = None, returnDataMiningReportFieldSortID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportSortBreak(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportSortBreakID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1, returnDataMiningReportSortBreakID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(DataMiningReportSortBreakID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1, setBreakType = None, setBreakTypeCode = None, setDataMiningReportFieldSortID = None, setHasDoubleUnderline = None, setHasSeparator = None, setSortBreakID = None, setRelationships = None, returnDataMiningReportSortBreakID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(DataMiningReportSortBreakID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportSortBreak(EntityID = 1, setBreakType = None, setBreakTypeCode = None, setDataMiningReportFieldSortID = None, setHasDoubleUnderline = None, setHasSeparator = None, setSortBreakID = None, setRelationships = None, returnDataMiningReportSortBreakID = True, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportSubtopic(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportSubtopicID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1, returnDataMiningReportSubtopicID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(DataMiningReportSubtopicID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1, setDataMiningReportID = None, setHasRecord = None, setHasRecordCode = None, setOnlyShowTotals = None, setShowSubtotals = None, setSubtopicID = None, setRelationships = None, returnDataMiningReportSubtopicID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(DataMiningReportSubtopicID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportSubtopic(EntityID = 1, setDataMiningReportID = None, setHasRecord = None, setHasRecordCode = None, setOnlyShowTotals = None, setShowSubtotals = None, setSubtopicID = None, setRelationships = None, returnDataMiningReportSubtopicID = True, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDataMiningReportSubtopicStandardFilter(EntityID = 1, page = 1, pageSize = 100, returnDataMiningReportSubtopicStandardFilterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1, returnDataMiningReportSubtopicStandardFilterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(DataMiningReportSubtopicStandardFilterID), verb = "get", return_params_list = return_params_list)

def modifyDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1, setDataMiningReportID = None, setIsEnabled = None, setSubtopicStandardFilterID = None, setRelationships = None, returnDataMiningReportSubtopicStandardFilterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(DataMiningReportSubtopicStandardFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDataMiningReportSubtopicStandardFilter(EntityID = 1, setDataMiningReportID = None, setIsEnabled = None, setSubtopicStandardFilterID = None, setRelationships = None, returnDataMiningReportSubtopicStandardFilterID = True, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPage(EntityID = 1, page = 1, pageSize = 100, returnPageID = True, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPage(PageID, EntityID = 1, returnPageID = True, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(PageID), verb = "get", return_params_list = return_params_list)

def modifyPage(PageID, EntityID = 1, setPageNumber = None, setReportQueueID = None, setRelationships = None, returnPageID = True, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(PageID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPage(EntityID = 1, setPageNumber = None, setReportQueueID = None, setRelationships = None, returnPageID = True, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePage(PageID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPageBurst(EntityID = 1, page = 1, pageSize = 100, returnPageBurstID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPageBurst(PageBurstID, EntityID = 1, returnPageBurstID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(PageBurstID), verb = "get", return_params_list = return_params_list)

def modifyPageBurst(PageBurstID, EntityID = 1, setObjectID = None, setObjectPrimaryKey = None, setPageID = None, setRelationships = None, returnPageBurstID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(PageBurstID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPageBurst(EntityID = 1, setObjectID = None, setObjectPrimaryKey = None, setPageID = None, setRelationships = None, returnPageBurstID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePageBurst(PageBurstID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPromptTemplate(EntityID = 1, page = 1, pageSize = 100, returnPromptTemplateID = True, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPromptTemplate(PromptTemplateID, EntityID = 1, returnPromptTemplateID = True, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(PromptTemplateID), verb = "get", return_params_list = return_params_list)

def modifyPromptTemplate(PromptTemplateID, EntityID = 1, setDescription = None, setEntityID = None, setName = None, setPromptValuesJson = None, setPublished = None, setReportID = None, setUserIDOwner = None, setRelationships = None, returnPromptTemplateID = True, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(PromptTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPromptTemplate(EntityID = 1, setDescription = None, setEntityID = None, setName = None, setPromptValuesJson = None, setPublished = None, setReportID = None, setUserIDOwner = None, setRelationships = None, returnPromptTemplateID = True, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePromptTemplate(PromptTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReport(EntityID = 1, page = 1, pageSize = 100, returnReportID = True, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReport(ReportID, EntityID = 1, returnReportID = True, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(ReportID), verb = "get", return_params_list = return_params_list)

def modifyReport(ReportID, EntityID = 1, setAllowOthersToClone = None, setBottomMargin = None, setBurstActionIDPrintAction = None, setCrystalParameterData = None, setDescription = None, setDescriptionOverride = None, setDisplayInMainMenuAndListScreens = None, setDisplayInMainMenuAndListScreensOverride = None, setEncodingType = None, setEncodingTypeCode = None, setFileExtensionNewOverride = None, setFileExtensionOverride = None, setHasUnpublishedChanges = None, setIsSkywardMaintained = None, setJsonData = None, setKeepDataSources = None, setLeftMargin = None, setMediaIDCrystalRPT = None, setModuleIDBase = None, setName = None, setObjectIDBase = None, setOriginReportSkywardID = None, setOverrideDisplayInMainMenuAndListScreens = None, setPageHeight = None, setPageOrientationCode = None, setPageSizeCode = None, setPageWidth = None, setPortal = None, setPortalCode = None, setPublishedTime = None, setReportType = None, setReportTypeCode = None, setRightMargin = None, setSaveUntil = None, setSkywardHash = None, setSkywardID = None, setSkywardReportSystemVersion = None, setStateID = None, setTopMargin = None, setUserIDOwner = None, setRelationships = None, returnReportID = True, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(ReportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReport(EntityID = 1, setAllowOthersToClone = None, setBottomMargin = None, setBurstActionIDPrintAction = None, setCrystalParameterData = None, setDescription = None, setDescriptionOverride = None, setDisplayInMainMenuAndListScreens = None, setDisplayInMainMenuAndListScreensOverride = None, setEncodingType = None, setEncodingTypeCode = None, setFileExtensionNewOverride = None, setFileExtensionOverride = None, setHasUnpublishedChanges = None, setIsSkywardMaintained = None, setJsonData = None, setKeepDataSources = None, setLeftMargin = None, setMediaIDCrystalRPT = None, setModuleIDBase = None, setName = None, setObjectIDBase = None, setOriginReportSkywardID = None, setOverrideDisplayInMainMenuAndListScreens = None, setPageHeight = None, setPageOrientationCode = None, setPageSizeCode = None, setPageWidth = None, setPortal = None, setPortalCode = None, setPublishedTime = None, setReportType = None, setReportTypeCode = None, setRightMargin = None, setSaveUntil = None, setSkywardHash = None, setSkywardID = None, setSkywardReportSystemVersion = None, setStateID = None, setTopMargin = None, setUserIDOwner = None, setRelationships = None, returnReportID = True, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReport(ReportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportMenuModule(EntityID = 1, page = 1, pageSize = 100, returnReportMenuModuleID = True, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportMenuModule(ReportMenuModuleID, EntityID = 1, returnReportMenuModuleID = True, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(ReportMenuModuleID), verb = "get", return_params_list = return_params_list)

def modifyReportMenuModule(ReportMenuModuleID, EntityID = 1, setIsPrimary = None, setIsPrimaryOverride = None, setMenuModuleID = None, setReportID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnReportMenuModuleID = True, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(ReportMenuModuleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportMenuModule(EntityID = 1, setIsPrimary = None, setIsPrimaryOverride = None, setMenuModuleID = None, setReportID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnReportMenuModuleID = True, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportMenuModule(ReportMenuModuleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportQueue(EntityID = 1, page = 1, pageSize = 100, returnReportQueueID = True, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasExpiredContent = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportQueue(ReportQueueID, EntityID = 1, returnReportQueueID = True, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasExpiredContent = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(ReportQueueID), verb = "get", return_params_list = return_params_list)

def modifyReportQueue(ReportQueueID, EntityID = 1, setApplication = None, setCrystalParameterData = None, setDataSource = None, setDataSourceCode = None, setEncodingType = None, setEncodingTypeCode = None, setEndTime = None, setEntityID = None, setFiscalYearID = None, setFiscalYearIDSelectedOrCurrent = None, setFTPResultID = None, setHostname = None, setIsFromPublishedVersion = None, setLastActivity = None, setLogID = None, setMediaID = None, setMediaIDCsv = None, setMediaIDDownload = None, setMediaIDPrint = None, setPageCountWhenCompleted = None, setProcessID = None, setPromptTemplateID = None, setQueryStartTime = None, setQueue = None, setReferrerPath = None, setRenderingStartTime = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportQueueIDSummaryReportSource = None, setReportType = None, setReportTypeCode = None, setSaveUntil = None, setScheduledReportID = None, setSchoolYearID = None, setSchoolYearIDSelectedOrCurrent = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setStatus = None, setStatusActionXML = None, setThreadName = None, setRelationships = None, returnReportQueueID = True, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasExpiredContent = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(ReportQueueID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportQueue(EntityID = 1, setApplication = None, setCrystalParameterData = None, setDataSource = None, setDataSourceCode = None, setEncodingType = None, setEncodingTypeCode = None, setEndTime = None, setEntityID = None, setFiscalYearID = None, setFiscalYearIDSelectedOrCurrent = None, setFTPResultID = None, setHostname = None, setIsFromPublishedVersion = None, setLastActivity = None, setLogID = None, setMediaID = None, setMediaIDCsv = None, setMediaIDDownload = None, setMediaIDPrint = None, setPageCountWhenCompleted = None, setProcessID = None, setPromptTemplateID = None, setQueryStartTime = None, setQueue = None, setReferrerPath = None, setRenderingStartTime = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportQueueIDSummaryReportSource = None, setReportType = None, setReportTypeCode = None, setSaveUntil = None, setScheduledReportID = None, setSchoolYearID = None, setSchoolYearIDSelectedOrCurrent = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setStatus = None, setStatusActionXML = None, setThreadName = None, setRelationships = None, returnReportQueueID = True, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasExpiredContent = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportQueue(ReportQueueID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportQueueBurstAction(EntityID = 1, page = 1, pageSize = 100, returnReportQueueBurstActionID = True, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1, returnReportQueueBurstActionID = True, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(ReportQueueBurstActionID), verb = "get", return_params_list = return_params_list)

def modifyReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1, setBurstActionID = None, setChangesetXML = None, setLogID = None, setParametersXML = None, setReportQueueID = None, setStatus = None, setRelationships = None, returnReportQueueBurstActionID = True, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(ReportQueueBurstActionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportQueueBurstAction(EntityID = 1, setBurstActionID = None, setChangesetXML = None, setLogID = None, setParametersXML = None, setReportQueueID = None, setStatus = None, setRelationships = None, returnReportQueueBurstActionID = True, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportQueueSQL(EntityID = 1, page = 1, pageSize = 100, returnReportQueueSQLID = True, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportQueueSQL(ReportQueueSQLID, EntityID = 1, returnReportQueueSQLID = True, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(ReportQueueSQLID), verb = "get", return_params_list = return_params_list)

def modifyReportQueueSQL(ReportQueueSQLID, EntityID = 1, setExecutedQuery = None, setReportQueueID = None, setRelationships = None, returnReportQueueSQLID = True, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(ReportQueueSQLID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportQueueSQL(EntityID = 1, setExecutedQuery = None, setReportQueueID = None, setRelationships = None, returnReportQueueSQLID = True, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportQueueSQL(ReportQueueSQLID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportRole(EntityID = 1, page = 1, pageSize = 100, returnReportRoleID = True, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportRole(ReportRoleID, EntityID = 1, returnReportRoleID = True, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(ReportRoleID), verb = "get", return_params_list = return_params_list)

def modifyReportRole(ReportRoleID, EntityID = 1, setReportID = None, setRoleID = None, setRelationships = None, returnReportRoleID = True, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(ReportRoleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportRole(EntityID = 1, setReportID = None, setRoleID = None, setRelationships = None, returnReportRoleID = True, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportRole(ReportRoleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportRunInfo(EntityID = 1, page = 1, pageSize = 100, returnReportRunInfoID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportRunInfo(ReportRunInfoID, EntityID = 1, returnReportRunInfoID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(ReportRunInfoID), verb = "get", return_params_list = return_params_list)

def modifyReportRunInfo(ReportRunInfoID, EntityID = 1, setObjectID = None, setPromptDataSourcesJson = None, setPromptDataSourcesXml = None, setReportID = None, setRelationships = None, returnReportRunInfoID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(ReportRunInfoID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportRunInfo(EntityID = 1, setObjectID = None, setPromptDataSourcesJson = None, setPromptDataSourcesXml = None, setReportID = None, setRelationships = None, returnReportRunInfoID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportRunInfo(ReportRunInfoID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryReportStyle(EntityID = 1, page = 1, pageSize = 100, returnReportStyleID = True, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getReportStyle(ReportStyleID, EntityID = 1, returnReportStyleID = True, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(ReportStyleID), verb = "get", return_params_list = return_params_list)

def modifyReportStyle(ReportStyleID, EntityID = 1, setIsPublic = None, setName = None, setReportDefinitionXML = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnReportStyleID = True, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(ReportStyleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createReportStyle(EntityID = 1, setIsPublic = None, setName = None, setReportDefinitionXML = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnReportStyleID = True, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteReportStyle(ReportStyleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryScheduledReport(EntityID = 1, page = 1, pageSize = 100, returnScheduledReportID = True, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getScheduledReport(ScheduledReportID, EntityID = 1, returnScheduledReportID = True, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(ScheduledReportID), verb = "get", return_params_list = return_params_list)

def modifyScheduledReport(ScheduledReportID, EntityID = 1, setAutomateFileName = None, setAutoUpdate = None, setDaysToSaveReport = None, setDefinitionUpdatedTime = None, setEncodingType = None, setEncodingTypeCode = None, setEntityID = None, setExportFileName = None, setFTPConnectionID = None, setMediaIDCrystalRPT = None, setMessageMasterID = None, setName = None, setNetworkLocation = None, setNotifyByEmail = None, setNotifyByMessageCenter = None, setOverwriteExistingFile = None, setReportDefinitionXML = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportType = None, setReportTypeCode = None, setScheduledTaskID = None, setSectionID = None, setSkywardReportSystemVersion = None, setRelationships = None, returnScheduledReportID = True, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(ScheduledReportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createScheduledReport(EntityID = 1, setAutomateFileName = None, setAutoUpdate = None, setDaysToSaveReport = None, setDefinitionUpdatedTime = None, setEncodingType = None, setEncodingTypeCode = None, setEntityID = None, setExportFileName = None, setFTPConnectionID = None, setMediaIDCrystalRPT = None, setMessageMasterID = None, setName = None, setNetworkLocation = None, setNotifyByEmail = None, setNotifyByMessageCenter = None, setOverwriteExistingFile = None, setReportDefinitionXML = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportType = None, setReportTypeCode = None, setScheduledTaskID = None, setSectionID = None, setSkywardReportSystemVersion = None, setRelationships = None, returnScheduledReportID = True, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteScheduledReport(ScheduledReportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySecurityLocationReportSet(EntityID = 1, page = 1, pageSize = 100, returnSecurityLocationReportSetID = True, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1, returnSecurityLocationReportSetID = True, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(SecurityLocationReportSetID), verb = "get", return_params_list = return_params_list)

def modifySecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1, setDataObjectID = None, setIsSkywardLoaded = None, setName = None, setPrimaryKeySource = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSecurityLocationReportSetID = True, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(SecurityLocationReportSetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSecurityLocationReportSet(EntityID = 1, setDataObjectID = None, setIsSkywardLoaded = None, setName = None, setPrimaryKeySource = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSecurityLocationReportSetID = True, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySecurityLocationReportSetReportRunInfo(EntityID = 1, page = 1, pageSize = 100, returnSecurityLocationReportSetReportRunInfoID = True, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1, returnSecurityLocationReportSetReportRunInfoID = True, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(SecurityLocationReportSetReportRunInfoID), verb = "get", return_params_list = return_params_list)

def modifySecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1, setIsSkywardLoaded = None, setReportRunInfoID = None, setSecurityLocationReportSetID = None, setRelationships = None, returnSecurityLocationReportSetReportRunInfoID = True, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(SecurityLocationReportSetReportRunInfoID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSecurityLocationReportSetReportRunInfo(EntityID = 1, setIsSkywardLoaded = None, setReportRunInfoID = None, setSecurityLocationReportSetID = None, setRelationships = None, returnSecurityLocationReportSetReportRunInfoID = True, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySort(EntityID = 1, page = 1, pageSize = 100, returnSortID = True, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSort(SortID, EntityID = 1, returnSortID = True, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(SortID), verb = "get", return_params_list = return_params_list)

def modifySort(SortID, EntityID = 1, setSkywardHash = None, setSkywardID = None, setSortDirection = None, setSortDirectionCode = None, setSortGroupID = None, setSortOrder = None, setSubtopicFieldID = None, setRelationships = None, returnSortID = True, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(SortID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSort(EntityID = 1, setSkywardHash = None, setSkywardID = None, setSortDirection = None, setSortDirectionCode = None, setSortGroupID = None, setSortOrder = None, setSubtopicFieldID = None, setRelationships = None, returnSortID = True, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSort(SortID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySortBreak(EntityID = 1, page = 1, pageSize = 100, returnSortBreakID = True, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSortBreak(SortBreakID, EntityID = 1, returnSortBreakID = True, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(SortBreakID), verb = "get", return_params_list = return_params_list)

def modifySortBreak(SortBreakID, EntityID = 1, setCharacterPosition = None, setDataObjectFieldPathID = None, setSkywardHash = None, setSkywardID = None, setSubtopicID = None, setRelationships = None, returnSortBreakID = True, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(SortBreakID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSortBreak(EntityID = 1, setCharacterPosition = None, setDataObjectFieldPathID = None, setSkywardHash = None, setSkywardID = None, setSubtopicID = None, setRelationships = None, returnSortBreakID = True, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSortBreak(SortBreakID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySortGroup(EntityID = 1, page = 1, pageSize = 100, returnSortGroupID = True, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSortGroup(SortGroupID, EntityID = 1, returnSortGroupID = True, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(SortGroupID), verb = "get", return_params_list = return_params_list)

def modifySortGroup(SortGroupID, EntityID = 1, setIsDefault = None, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSortGroupID = True, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(SortGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSortGroup(EntityID = 1, setIsDefault = None, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSortGroupID = True, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSortGroup(SortGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubject(EntityID = 1, page = 1, pageSize = 100, returnSubjectID = True, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubject(SubjectID, EntityID = 1, returnSubjectID = True, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(SubjectID), verb = "get", return_params_list = return_params_list)

def modifySubject(SubjectID, EntityID = 1, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSubjectID = True, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(SubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubject(EntityID = 1, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnSubjectID = True, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubject(SubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubjectSecurityLocation(EntityID = 1, page = 1, pageSize = 100, returnSubjectSecurityLocationID = True, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1, returnSubjectSecurityLocationID = True, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(SubjectSecurityLocationID), verb = "get", return_params_list = return_params_list)

def modifySubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setRelationships = None, returnSubjectSecurityLocationID = True, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(SubjectSecurityLocationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubjectSecurityLocation(EntityID = 1, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setRelationships = None, returnSubjectSecurityLocationID = True, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubtopic(EntityID = 1, page = 1, pageSize = 100, returnSubtopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubtopic(SubtopicID, EntityID = 1, returnSubtopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(SubtopicID), verb = "get", return_params_list = return_params_list)

def modifySubtopic(SubtopicID, EntityID = 1, setDataObjectFieldPathIDDefaultSort = None, setDefaultSortDirection = None, setDefaultSortDirectionCode = None, setDisplayOrder = None, setFieldAreaPath = None, setFieldPrefix = None, setIsOneToMany = None, setName = None, setObjectID = None, setOneToManyRelationshipPath = None, setRelationshipPath = None, setSkywardHash = None, setSkywardID = None, setTopicID = None, setRelationships = None, returnSubtopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(SubtopicID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubtopic(EntityID = 1, setDataObjectFieldPathIDDefaultSort = None, setDefaultSortDirection = None, setDefaultSortDirectionCode = None, setDisplayOrder = None, setFieldAreaPath = None, setFieldPrefix = None, setIsOneToMany = None, setName = None, setObjectID = None, setOneToManyRelationshipPath = None, setRelationshipPath = None, setSkywardHash = None, setSkywardID = None, setTopicID = None, setRelationships = None, returnSubtopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubtopic(SubtopicID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubtopicField(EntityID = 1, page = 1, pageSize = 100, returnSubtopicFieldID = True, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubtopicField(SubtopicFieldID, EntityID = 1, returnSubtopicFieldID = True, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(SubtopicFieldID), verb = "get", return_params_list = return_params_list)

def modifySubtopicField(SubtopicFieldID, EntityID = 1, setDataObjectFieldPathID = None, setSubtopicID = None, setRelationships = None, returnSubtopicFieldID = True, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(SubtopicFieldID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubtopicField(EntityID = 1, setDataObjectFieldPathID = None, setSubtopicID = None, setRelationships = None, returnSubtopicFieldID = True, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubtopicField(SubtopicFieldID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySubtopicStandardFilter(EntityID = 1, page = 1, pageSize = 100, returnSubtopicStandardFilterID = True, returnCreatedTime = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1, returnSubtopicStandardFilterID = True, returnCreatedTime = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(SubtopicStandardFilterID), verb = "get", return_params_list = return_params_list)

def modifySubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1, setIsRequired = None, setPath = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setSubtopicID = None, setRelationships = None, returnSubtopicStandardFilterID = True, returnCreatedTime = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(SubtopicStandardFilterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSubtopicStandardFilter(EntityID = 1, setIsRequired = None, setPath = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setSubtopicID = None, setRelationships = None, returnSubtopicStandardFilterID = True, returnCreatedTime = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySummaryReportParameter(EntityID = 1, page = 1, pageSize = 100, returnSummaryReportParameterID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSummaryReportParameter(SummaryReportParameterID, EntityID = 1, returnSummaryReportParameterID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(SummaryReportParameterID), verb = "get", return_params_list = return_params_list)

def modifySummaryReportParameter(SummaryReportParameterID, EntityID = 1, setName = None, setReportQueueID = None, setUsedBy = None, setValue = None, setRelationships = None, returnSummaryReportParameterID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(SummaryReportParameterID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSummaryReportParameter(EntityID = 1, setName = None, setReportQueueID = None, setUsedBy = None, setValue = None, setRelationships = None, returnSummaryReportParameterID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSummaryReportParameter(SummaryReportParameterID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySummaryReportPrompt(EntityID = 1, page = 1, pageSize = 100, returnSummaryReportPromptID = True, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSummaryReportPrompt(SummaryReportPromptID, EntityID = 1, returnSummaryReportPromptID = True, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(SummaryReportPromptID), verb = "get", return_params_list = return_params_list)

def modifySummaryReportPrompt(SummaryReportPromptID, EntityID = 1, setLabel = None, setOrder = None, setReportQueueID = None, setValue = None, setRelationships = None, returnSummaryReportPromptID = True, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(SummaryReportPromptID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSummaryReportPrompt(EntityID = 1, setLabel = None, setOrder = None, setReportQueueID = None, setValue = None, setRelationships = None, returnSummaryReportPromptID = True, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSummaryReportPrompt(SummaryReportPromptID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySummaryReportSection(EntityID = 1, page = 1, pageSize = 100, returnSummaryReportSectionID = True, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSummaryReportSection(SummaryReportSectionID, EntityID = 1, returnSummaryReportSectionID = True, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(SummaryReportSectionID), verb = "get", return_params_list = return_params_list)

def modifySummaryReportSection(SummaryReportSectionID, EntityID = 1, setDisplayName = None, setHiddenType = None, setOrder = None, setPath = None, setReportQueueID = None, setSummaryReportSectionIDParent = None, setRelationships = None, returnSummaryReportSectionID = True, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(SummaryReportSectionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSummaryReportSection(EntityID = 1, setDisplayName = None, setHiddenType = None, setOrder = None, setPath = None, setReportQueueID = None, setSummaryReportSectionIDParent = None, setRelationships = None, returnSummaryReportSectionID = True, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSummaryReportSection(SummaryReportSectionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySummaryReportSectionColumn(EntityID = 1, page = 1, pageSize = 100, returnSummaryReportSectionColumnID = True, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1, returnSummaryReportSectionColumnID = True, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(SummaryReportSectionColumnID), verb = "get", return_params_list = return_params_list)

def modifySummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1, setDataType = None, setDisplayName = None, setFieldName = None, setHiddenType = None, setSummaryReportSectionID = None, setRelationships = None, returnSummaryReportSectionColumnID = True, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(SummaryReportSectionColumnID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSummaryReportSectionColumn(EntityID = 1, setDataType = None, setDisplayName = None, setFieldName = None, setHiddenType = None, setSummaryReportSectionID = None, setRelationships = None, returnSummaryReportSectionColumnID = True, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTopic(EntityID = 1, page = 1, pageSize = 100, returnTopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTopic(TopicID, EntityID = 1, returnTopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(TopicID), verb = "get", return_params_list = return_params_list)

def modifyTopic(TopicID, EntityID = 1, setName = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setTopicIDParent = None, setRelationships = None, returnTopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(TopicID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTopic(EntityID = 1, setName = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setTopicIDParent = None, setRelationships = None, returnTopicID = True, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTopic(TopicID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUploadReportLog(EntityID = 1, page = 1, pageSize = 100, returnUploadReportLogID = True, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUploadReportLog(UploadReportLogID, EntityID = 1, returnUploadReportLogID = True, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(UploadReportLogID), verb = "get", return_params_list = return_params_list)

def modifyUploadReportLog(UploadReportLogID, EntityID = 1, setFileName = None, setLogID = None, setMessage = None, setReportID = None, setResult = None, setResultCode = None, setWorkflowInstanceID = None, setRelationships = None, returnUploadReportLogID = True, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(UploadReportLogID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUploadReportLog(EntityID = 1, setFileName = None, setLogID = None, setMessage = None, setReportID = None, setResult = None, setResultCode = None, setWorkflowInstanceID = None, setRelationships = None, returnUploadReportLogID = True, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUploadReportLog(UploadReportLogID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserReportPrompt(EntityID = 1, page = 1, pageSize = 100, returnUserReportPromptID = True, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserReportPrompt(UserReportPromptID, EntityID = 1, returnUserReportPromptID = True, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(UserReportPromptID), verb = "get", return_params_list = return_params_list)

def modifyUserReportPrompt(UserReportPromptID, EntityID = 1, setCrystalPromptXML = None, setEntityID = None, setPromptTemplateID = None, setReportID = None, setRelationships = None, returnUserReportPromptID = True, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(UserReportPromptID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserReportPrompt(EntityID = 1, setCrystalPromptXML = None, setEntityID = None, setPromptTemplateID = None, setReportID = None, setRelationships = None, returnUserReportPromptID = True, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserReportPrompt(UserReportPromptID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryUserSetting(EntityID = 1, page = 1, pageSize = 100, returnUserSettingID = True, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getUserSetting(UserSettingID, EntityID = 1, returnUserSettingID = True, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(UserSettingID), verb = "get", return_params_list = return_params_list)

def modifyUserSetting(UserSettingID, EntityID = 1, setDataMiningLeftFieldSelectionPanelWidth = None, setDataMiningMiddleFieldSelectionPanelWidth = None, setDataMiningShowLeftFieldSelectionPanel = None, setShowSideBar = None, setSideBarWidth = None, setRelationships = None, returnUserSettingID = True, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(UserSettingID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createUserSetting(EntityID = 1, setDataMiningLeftFieldSelectionPanelWidth = None, setDataMiningMiddleFieldSelectionPanelWidth = None, setDataMiningShowLeftFieldSelectionPanel = None, setShowSideBar = None, setSideBarWidth = None, setRelationships = None, returnUserSettingID = True, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteUserSetting(UserSettingID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")