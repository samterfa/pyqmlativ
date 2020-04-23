# This module contains Reporting functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBurstAction(searchConditions = [], EntityID = 1, returnBurstActionID = False, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BurstAction in the district.

    This function returns a dataframe of every BurstAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBurstAction(BurstActionID, EntityID = 1, returnBurstActionID = False, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(BurstActionID), verb = "get", return_params_list = return_params)

def modifyBurstAction(BurstActionID, EntityID = 1, setBurstActionID = None, setActionHandler = None, setActionHandlerXML = None, setCanBeReverted = None, setCreatedTime = None, setIsPrintAction = None, setModifiedTime = None, setName = None, setObjectID = None, setParameterSxlPath = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBurstActionID = False, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(BurstActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBurstAction(EntityID = 1, setBurstActionID = None, setActionHandler = None, setActionHandlerXML = None, setCanBeReverted = None, setCreatedTime = None, setIsPrintAction = None, setModifiedTime = None, setName = None, setObjectID = None, setParameterSxlPath = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBurstActionID = False, returnActionHandler = False, returnActionHandlerXML = False, returnCanBeReverted = False, returnCreatedTime = False, returnIsPrintAction = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnParameterSxlPath = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBurstAction(BurstActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/BurstAction/" + str(BurstActionID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigSystem in the district.

    This function returns a dataframe of every ConfigSystem in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setCreatedTime = None, setDaysToSaveReportResults = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setCreatedTime = None, setDaysToSaveReportResults = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigSystemID = False, returnCreatedTime = False, returnDaysToSaveReportResults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryDataMiningReport(searchConditions = [], EntityID = 1, returnDataMiningReportID = False, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReport in the district.

    This function returns a dataframe of every DataMiningReport in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReport(DataMiningReportID, EntityID = 1, returnDataMiningReportID = False, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(DataMiningReportID), verb = "get", return_params_list = return_params)

def modifyDataMiningReport(DataMiningReportID, EntityID = 1, setDataMiningReportID = None, setCreatedTime = None, setCurrentUserCanEdit = None, setCurrentUserCanRead = None, setCurrentUserCanRun = None, setDelimiter = None, setDelimiterCode = None, setHasFieldsThatCanBeTotaled = None, setIncludeSectionHeaders = None, setIsFixedWidth = None, setModifiedTime = None, setName = None, setReportID = None, setReportSchemaObject = None, setSubjectID = None, setTextQualifier = None, setTextQualifierCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportID = False, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(DataMiningReportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReport(EntityID = 1, setDataMiningReportID = None, setCreatedTime = None, setCurrentUserCanEdit = None, setCurrentUserCanRead = None, setCurrentUserCanRun = None, setDelimiter = None, setDelimiterCode = None, setHasFieldsThatCanBeTotaled = None, setIncludeSectionHeaders = None, setIsFixedWidth = None, setModifiedTime = None, setName = None, setReportID = None, setReportSchemaObject = None, setSubjectID = None, setTextQualifier = None, setTextQualifierCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportID = False, returnCreatedTime = False, returnCurrentUserCanEdit = False, returnCurrentUserCanRead = False, returnCurrentUserCanRun = False, returnDelimiter = False, returnDelimiterCode = False, returnHasFieldsThatCanBeTotaled = False, returnIncludeSectionHeaders = False, returnIsFixedWidth = False, returnModifiedTime = False, returnName = False, returnReportID = False, returnReportSchemaObject = False, returnSubjectID = False, returnTextQualifier = False, returnTextQualifierCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReport(DataMiningReportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReport/" + str(DataMiningReportID), verb = "delete")


def getEveryDataMiningReportField(searchConditions = [], EntityID = 1, returnDataMiningReportFieldID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportField in the district.

    This function returns a dataframe of every DataMiningReportField in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportField(DataMiningReportFieldID, EntityID = 1, returnDataMiningReportFieldID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(DataMiningReportFieldID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportField(DataMiningReportFieldID, EntityID = 1, setDataMiningReportFieldID = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setDisplayOrder = None, setEndPosition = None, setIsNumeric = None, setLabel = None, setModifiedTime = None, setShowTotal = None, setStartPosition = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWidth = None, setWidthInPixels = None, returnDataMiningReportFieldID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(DataMiningReportFieldID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportField(EntityID = 1, setDataMiningReportFieldID = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setDisplayOrder = None, setEndPosition = None, setIsNumeric = None, setLabel = None, setModifiedTime = None, setShowTotal = None, setStartPosition = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWidth = None, setWidthInPixels = None, returnDataMiningReportFieldID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDisplayOrder = False, returnEndPosition = False, returnIsNumeric = False, returnLabel = False, returnModifiedTime = False, returnShowTotal = False, returnStartPosition = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWidth = False, returnWidthInPixels = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportField(DataMiningReportFieldID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportField/" + str(DataMiningReportFieldID), verb = "delete")


def getEveryDataMiningReportFieldFilter(searchConditions = [], EntityID = 1, returnDataMiningReportFieldFilterID = False, returnComparisonType = False, returnComparisonTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportFieldFilter in the district.

    This function returns a dataframe of every DataMiningReportFieldFilter in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1, returnDataMiningReportFieldFilterID = False, returnComparisonType = False, returnComparisonTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(DataMiningReportFieldFilterID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1, setDataMiningReportFieldFilterID = None, setComparisonType = None, setComparisonTypeCode = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setDistinctMultiSelectFieldPath = None, setDistinctMultiSelectModule = None, setDistinctMultiSelectObject = None, setDistinctMultiSelectSchemaObject = None, setFilterType = None, setFilterTypeCode = None, setFilterValue = None, setFormatedDisplayValue = None, setHigh = None, setIsPrompt = None, setList = None, setListAsJsonDictionaryString = None, setListAsJsonListString = None, setListBackingData = None, setListDisplayValue = None, setLow = None, setModifiedTime = None, setPromptIsRequired = None, setPromptLabel = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportFieldFilterID = False, returnComparisonType = False, returnComparisonTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(DataMiningReportFieldFilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportFieldFilter(EntityID = 1, setDataMiningReportFieldFilterID = None, setComparisonType = None, setComparisonTypeCode = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setDistinctMultiSelectFieldPath = None, setDistinctMultiSelectModule = None, setDistinctMultiSelectObject = None, setDistinctMultiSelectSchemaObject = None, setFilterType = None, setFilterTypeCode = None, setFilterValue = None, setFormatedDisplayValue = None, setHigh = None, setIsPrompt = None, setList = None, setListAsJsonDictionaryString = None, setListAsJsonListString = None, setListBackingData = None, setListDisplayValue = None, setLow = None, setModifiedTime = None, setPromptIsRequired = None, setPromptLabel = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportFieldFilterID = False, returnComparisonType = False, returnComparisonTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnDistinctMultiSelectFieldPath = False, returnDistinctMultiSelectModule = False, returnDistinctMultiSelectObject = False, returnDistinctMultiSelectSchemaObject = False, returnFilterType = False, returnFilterTypeCode = False, returnFilterValue = False, returnFormatedDisplayValue = False, returnHigh = False, returnIsPrompt = False, returnList = False, returnListAsJsonDictionaryString = False, returnListAsJsonListString = False, returnListBackingData = False, returnListDisplayValue = False, returnLow = False, returnModifiedTime = False, returnPromptIsRequired = False, returnPromptLabel = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportFieldFilter(DataMiningReportFieldFilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldFilter/" + str(DataMiningReportFieldFilterID), verb = "delete")


def getEveryDataMiningReportFieldParameter(searchConditions = [], EntityID = 1, returnDataMiningReportFieldParameterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportFieldParameter in the district.

    This function returns a dataframe of every DataMiningReportFieldParameter in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1, returnDataMiningReportFieldParameterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(DataMiningReportFieldParameterID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1, setDataMiningReportFieldParameterID = None, setCreatedTime = None, setDataMiningReportID = None, setDataType = None, setDataTypeString = None, setIsPrompt = None, setModifiedTime = None, setParameterName = None, setPromptLabel = None, setPromptLabelOrParameterName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setValueString = None, returnDataMiningReportFieldParameterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(DataMiningReportFieldParameterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportFieldParameter(EntityID = 1, setDataMiningReportFieldParameterID = None, setCreatedTime = None, setDataMiningReportID = None, setDataType = None, setDataTypeString = None, setIsPrompt = None, setModifiedTime = None, setParameterName = None, setPromptLabel = None, setPromptLabelOrParameterName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setValueString = None, returnDataMiningReportFieldParameterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnDataType = False, returnDataTypeString = False, returnIsPrompt = False, returnModifiedTime = False, returnParameterName = False, returnPromptLabel = False, returnPromptLabelOrParameterName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnValueString = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportFieldParameter(DataMiningReportFieldParameterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldParameter/" + str(DataMiningReportFieldParameterID), verb = "delete")


def getEveryDataMiningReportFieldSort(searchConditions = [], EntityID = 1, returnDataMiningReportFieldSortID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportFieldSort in the district.

    This function returns a dataframe of every DataMiningReportFieldSort in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1, returnDataMiningReportFieldSortID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(DataMiningReportFieldSortID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1, setDataMiningReportFieldSortID = None, setBreakType = None, setBreakTypeCode = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setLength = None, setModifiedTime = None, setShowCount = None, setShowSubtotals = None, setSortDirection = None, setSortDirectionCode = None, setSortOrder = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportFieldSortID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(DataMiningReportFieldSortID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportFieldSort(EntityID = 1, setDataMiningReportFieldSortID = None, setBreakType = None, setBreakTypeCode = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setLength = None, setModifiedTime = None, setShowCount = None, setShowSubtotals = None, setSortDirection = None, setSortDirectionCode = None, setSortOrder = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportFieldSortID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnLength = False, returnModifiedTime = False, returnShowCount = False, returnShowSubtotals = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportFieldSort(DataMiningReportFieldSortID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportFieldSort/" + str(DataMiningReportFieldSortID), verb = "delete")


def getEveryDataMiningReportSortBreak(searchConditions = [], EntityID = 1, returnDataMiningReportSortBreakID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportSortBreak in the district.

    This function returns a dataframe of every DataMiningReportSortBreak in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1, returnDataMiningReportSortBreakID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(DataMiningReportSortBreakID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1, setDataMiningReportSortBreakID = None, setBreakType = None, setBreakTypeCode = None, setCreatedTime = None, setDataMiningReportFieldSortID = None, setHasDoubleUnderline = None, setHasSeparator = None, setModifiedTime = None, setSortBreakID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSortBreakID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(DataMiningReportSortBreakID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportSortBreak(EntityID = 1, setDataMiningReportSortBreakID = None, setBreakType = None, setBreakTypeCode = None, setCreatedTime = None, setDataMiningReportFieldSortID = None, setHasDoubleUnderline = None, setHasSeparator = None, setModifiedTime = None, setSortBreakID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSortBreakID = False, returnBreakType = False, returnBreakTypeCode = False, returnCreatedTime = False, returnDataMiningReportFieldSortID = False, returnHasDoubleUnderline = False, returnHasSeparator = False, returnModifiedTime = False, returnSortBreakID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportSortBreak(DataMiningReportSortBreakID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSortBreak/" + str(DataMiningReportSortBreakID), verb = "delete")


def getEveryDataMiningReportSubtopic(searchConditions = [], EntityID = 1, returnDataMiningReportSubtopicID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowCount = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportSubtopic in the district.

    This function returns a dataframe of every DataMiningReportSubtopic in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1, returnDataMiningReportSubtopicID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowCount = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(DataMiningReportSubtopicID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1, setDataMiningReportSubtopicID = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setHasRecord = None, setHasRecordCode = None, setHasRecordIsEditable = None, setModifiedTime = None, setOnlyShowTotals = None, setShowCount = None, setShowSubtotals = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSubtopicID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowCount = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(DataMiningReportSubtopicID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportSubtopic(EntityID = 1, setDataMiningReportSubtopicID = None, setCreatedTime = None, setCurrentUserCanRead = None, setDataMiningReportID = None, setHasRecord = None, setHasRecordCode = None, setHasRecordIsEditable = None, setModifiedTime = None, setOnlyShowTotals = None, setShowCount = None, setShowSubtotals = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSubtopicID = False, returnCreatedTime = False, returnCurrentUserCanRead = False, returnDataMiningReportID = False, returnHasRecord = False, returnHasRecordCode = False, returnHasRecordIsEditable = False, returnModifiedTime = False, returnOnlyShowTotals = False, returnShowCount = False, returnShowSubtotals = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportSubtopic(DataMiningReportSubtopicID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopic/" + str(DataMiningReportSubtopicID), verb = "delete")


def getEveryDataMiningReportSubtopicStandardFilter(searchConditions = [], EntityID = 1, returnDataMiningReportSubtopicStandardFilterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMiningReportSubtopicStandardFilter in the district.

    This function returns a dataframe of every DataMiningReportSubtopicStandardFilter in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1, returnDataMiningReportSubtopicStandardFilterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(DataMiningReportSubtopicStandardFilterID), verb = "get", return_params_list = return_params)

def modifyDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1, setDataMiningReportSubtopicStandardFilterID = None, setCreatedTime = None, setDataMiningReportID = None, setIsEnabled = None, setModifiedTime = None, setSubtopicStandardFilterID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSubtopicStandardFilterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(DataMiningReportSubtopicStandardFilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMiningReportSubtopicStandardFilter(EntityID = 1, setDataMiningReportSubtopicStandardFilterID = None, setCreatedTime = None, setDataMiningReportID = None, setIsEnabled = None, setModifiedTime = None, setSubtopicStandardFilterID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMiningReportSubtopicStandardFilterID = False, returnCreatedTime = False, returnDataMiningReportID = False, returnIsEnabled = False, returnModifiedTime = False, returnSubtopicStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMiningReportSubtopicStandardFilter(DataMiningReportSubtopicStandardFilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/DataMiningReportSubtopicStandardFilter/" + str(DataMiningReportSubtopicStandardFilterID), verb = "delete")


def getEveryPage(searchConditions = [], EntityID = 1, returnPageID = False, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Page in the district.

    This function returns a dataframe of every Page in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPage(PageID, EntityID = 1, returnPageID = False, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(PageID), verb = "get", return_params_list = return_params)

def modifyPage(PageID, EntityID = 1, setPageID = None, setCreatedTime = None, setModifiedTime = None, setPageNumber = None, setReportQueueID = None, setTables = None, setTotalHeightInPoints = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPageID = False, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(PageID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPage(EntityID = 1, setPageID = None, setCreatedTime = None, setModifiedTime = None, setPageNumber = None, setReportQueueID = None, setTables = None, setTotalHeightInPoints = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPageID = False, returnCreatedTime = False, returnModifiedTime = False, returnPageNumber = False, returnReportQueueID = False, returnTables = False, returnTotalHeightInPoints = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePage(PageID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Page/" + str(PageID), verb = "delete")


def getEveryPageBurst(searchConditions = [], EntityID = 1, returnPageBurstID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PageBurst in the district.

    This function returns a dataframe of every PageBurst in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPageBurst(PageBurstID, EntityID = 1, returnPageBurstID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(PageBurstID), verb = "get", return_params_list = return_params)

def modifyPageBurst(PageBurstID, EntityID = 1, setPageBurstID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setPageID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPageBurstID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(PageBurstID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPageBurst(EntityID = 1, setPageBurstID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setPageID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPageBurstID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnPageID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePageBurst(PageBurstID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PageBurst/" + str(PageBurstID), verb = "delete")


def getEveryPromptTemplate(searchConditions = [], EntityID = 1, returnPromptTemplateID = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PromptTemplate in the district.

    This function returns a dataframe of every PromptTemplate in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPromptTemplate(PromptTemplateID, EntityID = 1, returnPromptTemplateID = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(PromptTemplateID), verb = "get", return_params_list = return_params)

def modifyPromptTemplate(PromptTemplateID, EntityID = 1, setPromptTemplateID = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserHasAccess = None, setCurrentUserIsOwnerOrCreator = None, setCurrentUserIsOwnerOrCreatorNonOperation = None, setDescription = None, setEntityID = None, setModifiedDate = None, setModifiedTime = None, setName = None, setPromptValues = None, setPromptValuesJson = None, setPromptXML = None, setPublished = None, setReportDefinition = None, setReportDefinitionXml = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnPromptTemplateID = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(PromptTemplateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPromptTemplate(EntityID = 1, setPromptTemplateID = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserHasAccess = None, setCurrentUserIsOwnerOrCreator = None, setCurrentUserIsOwnerOrCreatorNonOperation = None, setDescription = None, setEntityID = None, setModifiedDate = None, setModifiedTime = None, setName = None, setPromptValues = None, setPromptValuesJson = None, setPromptXML = None, setPublished = None, setReportDefinition = None, setReportDefinitionXml = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnPromptTemplateID = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserHasAccess = False, returnCurrentUserIsOwnerOrCreator = False, returnCurrentUserIsOwnerOrCreatorNonOperation = False, returnDescription = False, returnEntityID = False, returnModifiedDate = False, returnModifiedTime = False, returnName = False, returnPromptValues = False, returnPromptValuesJson = False, returnPromptXML = False, returnPublished = False, returnReportDefinition = False, returnReportDefinitionXml = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePromptTemplate(PromptTemplateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/PromptTemplate/" + str(PromptTemplateID), verb = "delete")


def getEveryReport(searchConditions = [], EntityID = 1, returnReportID = False, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDefinitionWasModified = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasErrors = False, returnHasNoUnpublishedChanges = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptForFiscalYear = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Report in the district.

    This function returns a dataframe of every Report in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReport(ReportID, EntityID = 1, returnReportID = False, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDefinitionWasModified = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasErrors = False, returnHasNoUnpublishedChanges = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptForFiscalYear = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(ReportID), verb = "get", return_params_list = return_params)

def modifyReport(ReportID, EntityID = 1, setReportID = None, setAllowOthersToClone = None, setBottomMargin = None, setBurstActionIDPrintAction = None, setCanBeAddedToScreens = None, setCanBePublished = None, setCanBeScheduled = None, setCanRevert = None, setContainsStateSpecificFields = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserCanClone = None, setCurrentUserCanDelete = None, setCurrentUserCanRead = None, setCurrentUserCanSetStateID = None, setCurrentUserCanUpdate = None, setCurrentUserCanUpdateOverrideFields = None, setCurrentUserIsEffectiveOwner = None, setDefinitionWasModified = None, setDescription = None, setDescriptionOverride = None, setDisplayInMainMenuAndListScreens = None, setDisplayInMainMenuAndListScreensOverride = None, setEffectiveDescription = None, setEffectiveDisplayInMainMenuAndListScreens = None, setEffectiveFileExtensionOverride = None, setEncodingType = None, setEncodingTypeCode = None, setFileExtensionNewOverride = None, setFileExtensionOverride = None, setHasErrors = None, setHasNoUnpublishedChanges = None, setHasUnpublishedChanges = None, setIsCrystalReport = None, setIsEligibleForPrintAction = None, setIsSkywardMaintained = None, setIsSkywardReport = None, setIsSummaryReport = None, setJsonData = None, setKeepDataSources = None, setLastRunTime = None, setLeftMargin = None, setMediaIDCrystalRPT = None, setModifiedTime = None, setModuleIDBase = None, setModulePath = None, setModules = None, setName = None, setNotPublished = None, setObjectIDBase = None, setObjectName = None, setOriginReportSkywardID = None, setOverrideDescription = None, setOverrideDisplayInMainMenuAndListScreens = None, setOverrideFileExtensionOverride = None, setPageHeight = None, setPageOrientation = None, setPageOrientationCode = None, setPageSize = None, setPageSizeCode = None, setPageWidth = None, setPortal = None, setPortalCode = None, setPromptForFiscalYear = None, setPromptList = None, setPublished = None, setPublishedCalculatedInCSharp = None, setPublishedDefinitionText = None, setPublishedReportDefinition = None, setPublishedTime = None, setReportType = None, setReportTypeCode = None, setRightMargin = None, setRunCount = None, setSaveUntil = None, setSkywardHash = None, setSkywardID = None, setSkywardReportSystemVersion = None, setStateID = None, setStateSpecificFields = None, setStateSpecificFieldsDisplay = None, setTopMargin = None, setUpdatesMadeToMasterReport = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, setWorkingDefinitionText = None, setWorkingReportDefinition = None, returnReportID = False, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDefinitionWasModified = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasErrors = False, returnHasNoUnpublishedChanges = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptForFiscalYear = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(ReportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReport(EntityID = 1, setReportID = None, setAllowOthersToClone = None, setBottomMargin = None, setBurstActionIDPrintAction = None, setCanBeAddedToScreens = None, setCanBePublished = None, setCanBeScheduled = None, setCanRevert = None, setContainsStateSpecificFields = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserCanClone = None, setCurrentUserCanDelete = None, setCurrentUserCanRead = None, setCurrentUserCanSetStateID = None, setCurrentUserCanUpdate = None, setCurrentUserCanUpdateOverrideFields = None, setCurrentUserIsEffectiveOwner = None, setDefinitionWasModified = None, setDescription = None, setDescriptionOverride = None, setDisplayInMainMenuAndListScreens = None, setDisplayInMainMenuAndListScreensOverride = None, setEffectiveDescription = None, setEffectiveDisplayInMainMenuAndListScreens = None, setEffectiveFileExtensionOverride = None, setEncodingType = None, setEncodingTypeCode = None, setFileExtensionNewOverride = None, setFileExtensionOverride = None, setHasErrors = None, setHasNoUnpublishedChanges = None, setHasUnpublishedChanges = None, setIsCrystalReport = None, setIsEligibleForPrintAction = None, setIsSkywardMaintained = None, setIsSkywardReport = None, setIsSummaryReport = None, setJsonData = None, setKeepDataSources = None, setLastRunTime = None, setLeftMargin = None, setMediaIDCrystalRPT = None, setModifiedTime = None, setModuleIDBase = None, setModulePath = None, setModules = None, setName = None, setNotPublished = None, setObjectIDBase = None, setObjectName = None, setOriginReportSkywardID = None, setOverrideDescription = None, setOverrideDisplayInMainMenuAndListScreens = None, setOverrideFileExtensionOverride = None, setPageHeight = None, setPageOrientation = None, setPageOrientationCode = None, setPageSize = None, setPageSizeCode = None, setPageWidth = None, setPortal = None, setPortalCode = None, setPromptForFiscalYear = None, setPromptList = None, setPublished = None, setPublishedCalculatedInCSharp = None, setPublishedDefinitionText = None, setPublishedReportDefinition = None, setPublishedTime = None, setReportType = None, setReportTypeCode = None, setRightMargin = None, setRunCount = None, setSaveUntil = None, setSkywardHash = None, setSkywardID = None, setSkywardReportSystemVersion = None, setStateID = None, setStateSpecificFields = None, setStateSpecificFieldsDisplay = None, setTopMargin = None, setUpdatesMadeToMasterReport = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, setWorkingDefinitionText = None, setWorkingReportDefinition = None, returnReportID = False, returnAllowOthersToClone = False, returnBottomMargin = False, returnBurstActionIDPrintAction = False, returnCanBeAddedToScreens = False, returnCanBePublished = False, returnCanBeScheduled = False, returnCanRevert = False, returnContainsStateSpecificFields = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanClone = False, returnCurrentUserCanDelete = False, returnCurrentUserCanRead = False, returnCurrentUserCanSetStateID = False, returnCurrentUserCanUpdate = False, returnCurrentUserCanUpdateOverrideFields = False, returnCurrentUserIsEffectiveOwner = False, returnDefinitionWasModified = False, returnDescription = False, returnDescriptionOverride = False, returnDisplayInMainMenuAndListScreens = False, returnDisplayInMainMenuAndListScreensOverride = False, returnEffectiveDescription = False, returnEffectiveDisplayInMainMenuAndListScreens = False, returnEffectiveFileExtensionOverride = False, returnEncodingType = False, returnEncodingTypeCode = False, returnFileExtensionNewOverride = False, returnFileExtensionOverride = False, returnHasErrors = False, returnHasNoUnpublishedChanges = False, returnHasUnpublishedChanges = False, returnIsCrystalReport = False, returnIsEligibleForPrintAction = False, returnIsSkywardMaintained = False, returnIsSkywardReport = False, returnIsSummaryReport = False, returnJsonData = False, returnKeepDataSources = False, returnLastRunTime = False, returnLeftMargin = False, returnMediaIDCrystalRPT = False, returnModifiedTime = False, returnModuleIDBase = False, returnModulePath = False, returnModules = False, returnName = False, returnNotPublished = False, returnObjectIDBase = False, returnObjectName = False, returnOriginReportSkywardID = False, returnOverrideDescription = False, returnOverrideDisplayInMainMenuAndListScreens = False, returnOverrideFileExtensionOverride = False, returnPageHeight = False, returnPageOrientation = False, returnPageOrientationCode = False, returnPageSize = False, returnPageSizeCode = False, returnPageWidth = False, returnPortal = False, returnPortalCode = False, returnPromptForFiscalYear = False, returnPromptList = False, returnPublished = False, returnPublishedCalculatedInCSharp = False, returnPublishedDefinitionText = False, returnPublishedReportDefinition = False, returnPublishedTime = False, returnReportType = False, returnReportTypeCode = False, returnRightMargin = False, returnRunCount = False, returnSaveUntil = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardReportSystemVersion = False, returnStateID = False, returnStateSpecificFields = False, returnStateSpecificFieldsDisplay = False, returnTopMargin = False, returnUpdatesMadeToMasterReport = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, returnWorkingDefinitionText = False, returnWorkingReportDefinition = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReport(ReportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Report/" + str(ReportID), verb = "delete")


def getEveryReportError(searchConditions = [], EntityID = 1, returnReportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportError in the district.

    This function returns a dataframe of every ReportError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportError(ReportErrorID, EntityID = 1, returnReportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(ReportErrorID), verb = "get", return_params_list = return_params)

def modifyReportError(ReportErrorID, EntityID = 1, setReportErrorID = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(ReportErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportError(EntityID = 1, setReportErrorID = None, setCreatedTime = None, setErrorMessage = None, setModifiedTime = None, setReportID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnModifiedTime = False, returnReportID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportError(ReportErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportError/" + str(ReportErrorID), verb = "delete")


def getEveryReportMenuModule(searchConditions = [], EntityID = 1, returnReportMenuModuleID = False, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportMenuModule in the district.

    This function returns a dataframe of every ReportMenuModule in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportMenuModule(ReportMenuModuleID, EntityID = 1, returnReportMenuModuleID = False, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(ReportMenuModuleID), verb = "get", return_params_list = return_params)

def modifyReportMenuModule(ReportMenuModuleID, EntityID = 1, setReportMenuModuleID = None, setCreatedTime = None, setEffectiveIsPrimary = None, setIsPrimary = None, setIsPrimaryOverride = None, setIsSkywardReportMenuModule = None, setMenuModuleID = None, setModifiedTime = None, setReportID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportMenuModuleID = False, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(ReportMenuModuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportMenuModule(EntityID = 1, setReportMenuModuleID = None, setCreatedTime = None, setEffectiveIsPrimary = None, setIsPrimary = None, setIsPrimaryOverride = None, setIsSkywardReportMenuModule = None, setMenuModuleID = None, setModifiedTime = None, setReportID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportMenuModuleID = False, returnCreatedTime = False, returnEffectiveIsPrimary = False, returnIsPrimary = False, returnIsPrimaryOverride = False, returnIsSkywardReportMenuModule = False, returnMenuModuleID = False, returnModifiedTime = False, returnReportID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportMenuModule(ReportMenuModuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportMenuModule/" + str(ReportMenuModuleID), verb = "delete")


def getEveryReportQueue(searchConditions = [], EntityID = 1, returnReportQueueID = False, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnIsViewableReport = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportQueue in the district.

    This function returns a dataframe of every ReportQueue in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportQueue(ReportQueueID, EntityID = 1, returnReportQueueID = False, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnIsViewableReport = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(ReportQueueID), verb = "get", return_params_list = return_params)

def modifyReportQueue(ReportQueueID, EntityID = 1, setReportQueueID = None, setApplication = None, setBurstObjectIDs = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedFiscalYearSelectedOrCurrent = None, setCachedSchoolYear = None, setCachedSchoolYearSelectedOrCurrent = None, setCanCancel = None, setConcatenatedPromptValues = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserCanView = None, setDataSource = None, setDataSourceCode = None, setEncoding = None, setEncodingType = None, setEncodingTypeCode = None, setEndTime = None, setEntityID = None, setEntityIDList = None, setFiscalYearID = None, setFiscalYearIDSelectedOrCurrent = None, setFTPResultID = None, setHasContent = None, setHasContentDownloadable = None, setHasContentViewable = None, setHasPrintAction = None, setHideFiscalYear = None, setHideSchoolYear = None, setHostname = None, setIsCrystalReport = None, setIsEligibleForNonPrintBurstAction = None, setIsFromPublishedVersion = None, setIsViewableReport = None, setLastActivity = None, setLogID = None, setMediaID = None, setMediaIDCsv = None, setMediaIDDownload = None, setMediaIDPrint = None, setModifiedTime = None, setPageCount = None, setPageCountWhenCompleted = None, setProcessID = None, setPromptTemplateID = None, setPromptValues = None, setQueryDuration = None, setQueryStartTime = None, setQueue = None, setQueueCode = None, setQueuedDuration = None, setReferrerPath = None, setRenderingDuration = None, setRenderingStartTime = None, setReportDefinition = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportQueueIDSummaryReport = None, setReportQueueIDSummaryReportSource = None, setReportType = None, setReportTypeCode = None, setSaveUntil = None, setScheduledReportID = None, setSchoolYearID = None, setSchoolYearIDSelectedOrCurrent = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setStatus = None, setStatusAction = None, setStatusActionXML = None, setStatusCode = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueID = False, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnIsViewableReport = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(ReportQueueID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportQueue(EntityID = 1, setReportQueueID = None, setApplication = None, setBurstObjectIDs = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedFiscalYearSelectedOrCurrent = None, setCachedSchoolYear = None, setCachedSchoolYearSelectedOrCurrent = None, setCanCancel = None, setConcatenatedPromptValues = None, setCreatedTime = None, setCrystalParameterData = None, setCurrentUserCanView = None, setDataSource = None, setDataSourceCode = None, setEncoding = None, setEncodingType = None, setEncodingTypeCode = None, setEndTime = None, setEntityID = None, setEntityIDList = None, setFiscalYearID = None, setFiscalYearIDSelectedOrCurrent = None, setFTPResultID = None, setHasContent = None, setHasContentDownloadable = None, setHasContentViewable = None, setHasPrintAction = None, setHideFiscalYear = None, setHideSchoolYear = None, setHostname = None, setIsCrystalReport = None, setIsEligibleForNonPrintBurstAction = None, setIsFromPublishedVersion = None, setIsViewableReport = None, setLastActivity = None, setLogID = None, setMediaID = None, setMediaIDCsv = None, setMediaIDDownload = None, setMediaIDPrint = None, setModifiedTime = None, setPageCount = None, setPageCountWhenCompleted = None, setProcessID = None, setPromptTemplateID = None, setPromptValues = None, setQueryDuration = None, setQueryStartTime = None, setQueue = None, setQueueCode = None, setQueuedDuration = None, setReferrerPath = None, setRenderingDuration = None, setRenderingStartTime = None, setReportDefinition = None, setReportFileExtensionOverride = None, setReportID = None, setReportName = None, setReportQueueIDSummaryReport = None, setReportQueueIDSummaryReportSource = None, setReportType = None, setReportTypeCode = None, setSaveUntil = None, setScheduledReportID = None, setSchoolYearID = None, setSchoolYearIDSelectedOrCurrent = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setStatus = None, setStatusAction = None, setStatusActionXML = None, setStatusCode = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueID = False, returnApplication = False, returnBurstObjectIDs = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedFiscalYearSelectedOrCurrent = False, returnCachedSchoolYear = False, returnCachedSchoolYearSelectedOrCurrent = False, returnCanCancel = False, returnConcatenatedPromptValues = False, returnCreatedTime = False, returnCrystalParameterData = False, returnCurrentUserCanView = False, returnDataSource = False, returnDataSourceCode = False, returnEncoding = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEndTime = False, returnEntityID = False, returnEntityIDList = False, returnFiscalYearID = False, returnFiscalYearIDSelectedOrCurrent = False, returnFTPResultID = False, returnHasContent = False, returnHasContentDownloadable = False, returnHasContentViewable = False, returnHasPrintAction = False, returnHideFiscalYear = False, returnHideSchoolYear = False, returnHostname = False, returnIsCrystalReport = False, returnIsEligibleForNonPrintBurstAction = False, returnIsFromPublishedVersion = False, returnIsViewableReport = False, returnLastActivity = False, returnLogID = False, returnMediaID = False, returnMediaIDCsv = False, returnMediaIDDownload = False, returnMediaIDPrint = False, returnModifiedTime = False, returnPageCount = False, returnPageCountWhenCompleted = False, returnProcessID = False, returnPromptTemplateID = False, returnPromptValues = False, returnQueryDuration = False, returnQueryStartTime = False, returnQueue = False, returnQueueCode = False, returnQueuedDuration = False, returnReferrerPath = False, returnRenderingDuration = False, returnRenderingStartTime = False, returnReportDefinition = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportName = False, returnReportQueueIDSummaryReport = False, returnReportQueueIDSummaryReportSource = False, returnReportType = False, returnReportTypeCode = False, returnSaveUntil = False, returnScheduledReportID = False, returnSchoolYearID = False, returnSchoolYearIDSelectedOrCurrent = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnStatus = False, returnStatusAction = False, returnStatusActionXML = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportQueue(ReportQueueID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueue/" + str(ReportQueueID), verb = "delete")


def getEveryReportQueueBurstAction(searchConditions = [], EntityID = 1, returnReportQueueBurstActionID = False, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportQueueBurstAction in the district.

    This function returns a dataframe of every ReportQueueBurstAction in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1, returnReportQueueBurstActionID = False, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(ReportQueueBurstActionID), verb = "get", return_params_list = return_params)

def modifyReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1, setReportQueueBurstActionID = None, setBurstActionID = None, setChangesetXML = None, setCreatedTime = None, setLogID = None, setModifiedTime = None, setParameters = None, setParametersXML = None, setReportQueueID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueBurstActionID = False, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(ReportQueueBurstActionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportQueueBurstAction(EntityID = 1, setReportQueueBurstActionID = None, setBurstActionID = None, setChangesetXML = None, setCreatedTime = None, setLogID = None, setModifiedTime = None, setParameters = None, setParametersXML = None, setReportQueueID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueBurstActionID = False, returnBurstActionID = False, returnChangesetXML = False, returnCreatedTime = False, returnLogID = False, returnModifiedTime = False, returnParameters = False, returnParametersXML = False, returnReportQueueID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportQueueBurstAction(ReportQueueBurstActionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueBurstAction/" + str(ReportQueueBurstActionID), verb = "delete")


def getEveryReportQueueSQL(searchConditions = [], EntityID = 1, returnReportQueueSQLID = False, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportQueueSQL in the district.

    This function returns a dataframe of every ReportQueueSQL in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportQueueSQL(ReportQueueSQLID, EntityID = 1, returnReportQueueSQLID = False, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(ReportQueueSQLID), verb = "get", return_params_list = return_params)

def modifyReportQueueSQL(ReportQueueSQLID, EntityID = 1, setReportQueueSQLID = None, setCreatedTime = None, setExecutedQuery = None, setModifiedTime = None, setReportQueueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueSQLID = False, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(ReportQueueSQLID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportQueueSQL(EntityID = 1, setReportQueueSQLID = None, setCreatedTime = None, setExecutedQuery = None, setModifiedTime = None, setReportQueueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportQueueSQLID = False, returnCreatedTime = False, returnExecutedQuery = False, returnModifiedTime = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportQueueSQL(ReportQueueSQLID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportQueueSQL/" + str(ReportQueueSQLID), verb = "delete")


def getEveryReportRole(searchConditions = [], EntityID = 1, returnReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportRole in the district.

    This function returns a dataframe of every ReportRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportRole(ReportRoleID, EntityID = 1, returnReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(ReportRoleID), verb = "get", return_params_list = return_params)

def modifyReportRole(ReportRoleID, EntityID = 1, setReportRoleID = None, setCreatedTime = None, setModifiedTime = None, setReportID = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(ReportRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportRole(EntityID = 1, setReportRoleID = None, setCreatedTime = None, setModifiedTime = None, setReportID = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportRole(ReportRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRole/" + str(ReportRoleID), verb = "delete")


def getEveryReportRunInfo(searchConditions = [], EntityID = 1, returnReportRunInfoID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportRunInfo in the district.

    This function returns a dataframe of every ReportRunInfo in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportRunInfo(ReportRunInfoID, EntityID = 1, returnReportRunInfoID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(ReportRunInfoID), verb = "get", return_params_list = return_params)

def modifyReportRunInfo(ReportRunInfoID, EntityID = 1, setReportRunInfoID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectSkywardID = None, setPromptDataSources = None, setPromptDataSourcesJson = None, setPromptDataSourcesXml = None, setReportID = None, setSecurityLocationReportSetSkywardID = None, setSourceSchemaObject = None, setSourceTypeName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportRunInfoID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(ReportRunInfoID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportRunInfo(EntityID = 1, setReportRunInfoID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectSkywardID = None, setPromptDataSources = None, setPromptDataSourcesJson = None, setPromptDataSourcesXml = None, setReportID = None, setSecurityLocationReportSetSkywardID = None, setSourceSchemaObject = None, setSourceTypeName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportRunInfoID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectSkywardID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnPromptDataSourcesXml = False, returnReportID = False, returnSecurityLocationReportSetSkywardID = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportRunInfo(ReportRunInfoID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportRunInfo/" + str(ReportRunInfoID), verb = "delete")


def getEveryReportStyle(searchConditions = [], EntityID = 1, returnReportStyleID = False, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ReportStyle in the district.

    This function returns a dataframe of every ReportStyle in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getReportStyle(ReportStyleID, EntityID = 1, returnReportStyleID = False, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(ReportStyleID), verb = "get", return_params_list = return_params)

def modifyReportStyle(ReportStyleID, EntityID = 1, setReportStyleID = None, setCreatedTime = None, setCurrentUserCanDelete = None, setCurrentUserCanMakeNotPublic = None, setCurrentUserCanMakePublic = None, setIsNotSkywardReportStyle = None, setIsPublic = None, setIsSkywardReportStyle = None, setModifiedTime = None, setName = None, setReportDefinition = None, setReportDefinitionXML = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportStyleID = False, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(ReportStyleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createReportStyle(EntityID = 1, setReportStyleID = None, setCreatedTime = None, setCurrentUserCanDelete = None, setCurrentUserCanMakeNotPublic = None, setCurrentUserCanMakePublic = None, setIsNotSkywardReportStyle = None, setIsPublic = None, setIsSkywardReportStyle = None, setModifiedTime = None, setName = None, setReportDefinition = None, setReportDefinitionXML = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnReportStyleID = False, returnCreatedTime = False, returnCurrentUserCanDelete = False, returnCurrentUserCanMakeNotPublic = False, returnCurrentUserCanMakePublic = False, returnIsNotSkywardReportStyle = False, returnIsPublic = False, returnIsSkywardReportStyle = False, returnModifiedTime = False, returnName = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteReportStyle(ReportStyleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ReportStyle/" + str(ReportStyleID), verb = "delete")


def getEveryScheduledReport(searchConditions = [], EntityID = 1, returnScheduledReportID = False, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduledReport in the district.

    This function returns a dataframe of every ScheduledReport in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduledReport(ScheduledReportID, EntityID = 1, returnScheduledReportID = False, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(ScheduledReportID), verb = "get", return_params_list = return_params)

def modifyScheduledReport(ScheduledReportID, EntityID = 1, setScheduledReportID = None, setAutomateFileName = None, setAutoUpdate = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setCrystalParameterData = None, setDaysToSaveReport = None, setDefinitionUpdatedTime = None, setEncodingType = None, setEncodingTypeCode = None, setEntityID = None, setEntityIDList = None, setExportFileName = None, setFiscalYearID = None, setFTPConnectionID = None, setIsCrystalReport = None, setMediaIDCrystalRPT = None, setMessageMasterID = None, setModifiedTime = None, setName = None, setNetworkLocation = None, setNotifyByEmail = None, setNotifyByMessageCenter = None, setOverwriteExistingFile = None, setPromptValues = None, setPromptXML = None, setReportDefinition = None, setReportDefinitionXML = None, setReportFileExtensionOverride = None, setReportID = None, setReportIsCurrent = None, setReportName = None, setReportType = None, setReportTypeCode = None, setRunCount = None, setSaveToFtp = None, setSaveToNetworkLocation = None, setScheduledTaskID = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnScheduledReportID = False, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(ScheduledReportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduledReport(EntityID = 1, setScheduledReportID = None, setAutomateFileName = None, setAutoUpdate = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setCrystalParameterData = None, setDaysToSaveReport = None, setDefinitionUpdatedTime = None, setEncodingType = None, setEncodingTypeCode = None, setEntityID = None, setEntityIDList = None, setExportFileName = None, setFiscalYearID = None, setFTPConnectionID = None, setIsCrystalReport = None, setMediaIDCrystalRPT = None, setMessageMasterID = None, setModifiedTime = None, setName = None, setNetworkLocation = None, setNotifyByEmail = None, setNotifyByMessageCenter = None, setOverwriteExistingFile = None, setPromptValues = None, setPromptXML = None, setReportDefinition = None, setReportDefinitionXML = None, setReportFileExtensionOverride = None, setReportID = None, setReportIsCurrent = None, setReportName = None, setReportType = None, setReportTypeCode = None, setRunCount = None, setSaveToFtp = None, setSaveToNetworkLocation = None, setScheduledTaskID = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setSkywardReportSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnScheduledReportID = False, returnAutomateFileName = False, returnAutoUpdate = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnCrystalParameterData = False, returnDaysToSaveReport = False, returnDefinitionUpdatedTime = False, returnEncodingType = False, returnEncodingTypeCode = False, returnEntityID = False, returnEntityIDList = False, returnExportFileName = False, returnFiscalYearID = False, returnFTPConnectionID = False, returnIsCrystalReport = False, returnMediaIDCrystalRPT = False, returnMessageMasterID = False, returnModifiedTime = False, returnName = False, returnNetworkLocation = False, returnNotifyByEmail = False, returnNotifyByMessageCenter = False, returnOverwriteExistingFile = False, returnPromptValues = False, returnPromptXML = False, returnReportDefinition = False, returnReportDefinitionXML = False, returnReportFileExtensionOverride = False, returnReportID = False, returnReportIsCurrent = False, returnReportName = False, returnReportType = False, returnReportTypeCode = False, returnRunCount = False, returnSaveToFtp = False, returnSaveToNetworkLocation = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnSkywardReportSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduledReport(ScheduledReportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/ScheduledReport/" + str(ScheduledReportID), verb = "delete")


def getEverySecurityLocationReportSet(searchConditions = [], EntityID = 1, returnSecurityLocationReportSetID = False, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SecurityLocationReportSet in the district.

    This function returns a dataframe of every SecurityLocationReportSet in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1, returnSecurityLocationReportSetID = False, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(SecurityLocationReportSetID), verb = "get", return_params_list = return_params)

def modifySecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1, setSecurityLocationReportSetID = None, setAcceptsDataObject = None, setCreatedTime = None, setDataObjectID = None, setFullLocation = None, setIsSkywardLoaded = None, setModifiedTime = None, setModule = None, setName = None, setObject = None, setPrimaryKeySource = None, setScreen = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationReportSetID = False, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(SecurityLocationReportSetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSecurityLocationReportSet(EntityID = 1, setSecurityLocationReportSetID = None, setAcceptsDataObject = None, setCreatedTime = None, setDataObjectID = None, setFullLocation = None, setIsSkywardLoaded = None, setModifiedTime = None, setModule = None, setName = None, setObject = None, setPrimaryKeySource = None, setScreen = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationReportSetID = False, returnAcceptsDataObject = False, returnCreatedTime = False, returnDataObjectID = False, returnFullLocation = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnPrimaryKeySource = False, returnScreen = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSecurityLocationReportSet(SecurityLocationReportSetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSet/" + str(SecurityLocationReportSetID), verb = "delete")


def getEverySecurityLocationReportSetReportRunInfo(searchConditions = [], EntityID = 1, returnSecurityLocationReportSetReportRunInfoID = False, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SecurityLocationReportSetReportRunInfo in the district.

    This function returns a dataframe of every SecurityLocationReportSetReportRunInfo in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1, returnSecurityLocationReportSetReportRunInfoID = False, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(SecurityLocationReportSetReportRunInfoID), verb = "get", return_params_list = return_params)

def modifySecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1, setSecurityLocationReportSetReportRunInfoID = None, setCreatedTime = None, setInUse = None, setIsSkywardLoaded = None, setModifiedTime = None, setReportRunInfoID = None, setSecurityLocationReportSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationReportSetReportRunInfoID = False, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(SecurityLocationReportSetReportRunInfoID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSecurityLocationReportSetReportRunInfo(EntityID = 1, setSecurityLocationReportSetReportRunInfoID = None, setCreatedTime = None, setInUse = None, setIsSkywardLoaded = None, setModifiedTime = None, setReportRunInfoID = None, setSecurityLocationReportSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSecurityLocationReportSetReportRunInfoID = False, returnCreatedTime = False, returnInUse = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnReportRunInfoID = False, returnSecurityLocationReportSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSecurityLocationReportSetReportRunInfo(SecurityLocationReportSetReportRunInfoID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SecurityLocationReportSetReportRunInfo/" + str(SecurityLocationReportSetReportRunInfoID), verb = "delete")


def getEverySort(searchConditions = [], EntityID = 1, returnSortID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Sort in the district.

    This function returns a dataframe of every Sort in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSort(SortID, EntityID = 1, returnSortID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(SortID), verb = "get", return_params_list = return_params)

def modifySort(SortID, EntityID = 1, setSortID = None, setCreatedTime = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSortDirection = None, setSortDirectionCode = None, setSortGroupID = None, setSortOrder = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(SortID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSort(EntityID = 1, setSortID = None, setCreatedTime = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSortDirection = None, setSortDirectionCode = None, setSortGroupID = None, setSortOrder = None, setSubtopicFieldID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSortDirection = False, returnSortDirectionCode = False, returnSortGroupID = False, returnSortOrder = False, returnSubtopicFieldID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSort(SortID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Sort/" + str(SortID), verb = "delete")


def getEverySortBreak(searchConditions = [], EntityID = 1, returnSortBreakID = False, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SortBreak in the district.

    This function returns a dataframe of every SortBreak in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSortBreak(SortBreakID, EntityID = 1, returnSortBreakID = False, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(SortBreakID), verb = "get", return_params_list = return_params)

def modifySortBreak(SortBreakID, EntityID = 1, setSortBreakID = None, setCharacterPosition = None, setCreatedTime = None, setDataObjectFieldPathID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortBreakID = False, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(SortBreakID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSortBreak(EntityID = 1, setSortBreakID = None, setCharacterPosition = None, setCreatedTime = None, setDataObjectFieldPathID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortBreakID = False, returnCharacterPosition = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSortBreak(SortBreakID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortBreak/" + str(SortBreakID), verb = "delete")


def getEverySortGroup(searchConditions = [], EntityID = 1, returnSortGroupID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SortGroup in the district.

    This function returns a dataframe of every SortGroup in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSortGroup(SortGroupID, EntityID = 1, returnSortGroupID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(SortGroupID), verb = "get", return_params_list = return_params)

def modifySortGroup(SortGroupID, EntityID = 1, setSortGroupID = None, setCreatedTime = None, setIsDefault = None, setModifiedTime = None, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortGroupID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(SortGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSortGroup(EntityID = 1, setSortGroupID = None, setCreatedTime = None, setIsDefault = None, setModifiedTime = None, setName = None, setObjectID = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSortGroupID = False, returnCreatedTime = False, returnIsDefault = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSortGroup(SortGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SortGroup/" + str(SortGroupID), verb = "delete")


def getEverySubject(searchConditions = [], EntityID = 1, returnSubjectID = False, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPromptForFiscalYear = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Subject in the district.

    This function returns a dataframe of every Subject in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubject(SubjectID, EntityID = 1, returnSubjectID = False, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPromptForFiscalYear = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(SubjectID), verb = "get", return_params_list = return_params)

def modifySubject(SubjectID, EntityID = 1, setSubjectID = None, setAllowAccountBreaks = None, setCreatedTime = None, setCurrentUserHasAccess = None, setModifiedTime = None, setName = None, setObjectID = None, setPromptForFiscalYear = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectID = False, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPromptForFiscalYear = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(SubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubject(EntityID = 1, setSubjectID = None, setAllowAccountBreaks = None, setCreatedTime = None, setCurrentUserHasAccess = None, setModifiedTime = None, setName = None, setObjectID = None, setPromptForFiscalYear = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectID = False, returnAllowAccountBreaks = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPromptForFiscalYear = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubject(SubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subject/" + str(SubjectID), verb = "delete")


def getEverySubjectSecurityLocation(searchConditions = [], EntityID = 1, returnSubjectSecurityLocationID = False, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubjectSecurityLocation in the district.

    This function returns a dataframe of every SubjectSecurityLocation in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1, returnSubjectSecurityLocationID = False, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(SubjectSecurityLocationID), verb = "get", return_params_list = return_params)

def modifySubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1, setSubjectSecurityLocationID = None, setCreatedTime = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectSecurityLocationID = False, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(SubjectSecurityLocationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubjectSecurityLocation(EntityID = 1, setSubjectSecurityLocationID = None, setCreatedTime = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectSecurityLocationID = False, returnCreatedTime = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubjectSecurityLocation(SubjectSecurityLocationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubjectSecurityLocation/" + str(SubjectSecurityLocationID), verb = "delete")


def getEverySubtopic(searchConditions = [], EntityID = 1, returnSubtopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnCustomizationID = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Subtopic in the district.

    This function returns a dataframe of every Subtopic in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubtopic(SubtopicID, EntityID = 1, returnSubtopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnCustomizationID = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(SubtopicID), verb = "get", return_params_list = return_params)

def modifySubtopic(SubtopicID, EntityID = 1, setSubtopicID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setCustomizationID = None, setDataObjectFieldPathIDDefaultSort = None, setDefaultSortDirection = None, setDefaultSortDirectionCode = None, setDisplayOrder = None, setFieldAreaPath = None, setFieldPrefix = None, setIsOneToMany = None, setIsSkywardLoaded = None, setModifiedTime = None, setName = None, setObjectID = None, setOneToManyRelationshipPath = None, setRelationshipPath = None, setSkywardHash = None, setSkywardID = None, setTopicID = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnCustomizationID = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(SubtopicID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubtopic(EntityID = 1, setSubtopicID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setCustomizationID = None, setDataObjectFieldPathIDDefaultSort = None, setDefaultSortDirection = None, setDefaultSortDirectionCode = None, setDisplayOrder = None, setFieldAreaPath = None, setFieldPrefix = None, setIsOneToMany = None, setIsSkywardLoaded = None, setModifiedTime = None, setName = None, setObjectID = None, setOneToManyRelationshipPath = None, setRelationshipPath = None, setSkywardHash = None, setSkywardID = None, setTopicID = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnCustomizationID = False, returnDataObjectFieldPathIDDefaultSort = False, returnDefaultSortDirection = False, returnDefaultSortDirectionCode = False, returnDisplayOrder = False, returnFieldAreaPath = False, returnFieldPrefix = False, returnIsOneToMany = False, returnIsSkywardLoaded = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnOneToManyRelationshipPath = False, returnRelationshipPath = False, returnSkywardHash = False, returnSkywardID = False, returnTopicID = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubtopic(SubtopicID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Subtopic/" + str(SubtopicID), verb = "delete")


def getEverySubtopicField(searchConditions = [], EntityID = 1, returnSubtopicFieldID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubtopicField in the district.

    This function returns a dataframe of every SubtopicField in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubtopicField(SubtopicFieldID, EntityID = 1, returnSubtopicFieldID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(SubtopicFieldID), verb = "get", return_params_list = return_params)

def modifySubtopicField(SubtopicFieldID, EntityID = 1, setSubtopicFieldID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setDataObjectFieldPathID = None, setFriendlyNameWithPrefix = None, setFullFieldPath = None, setIsBoolean = None, setIsCalculatedInCSharp = None, setIsDateTime = None, setIsEnum = None, setIsFilterable = None, setIsNotEnumOrBoolean = None, setIsNumeric = None, setIsString = None, setIsTimeSpan = None, setMaxSortBreakPosition = None, setModifiedTime = None, setSubtopicID = None, setSystemType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicFieldID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(SubtopicFieldID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubtopicField(EntityID = 1, setSubtopicFieldID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setDataObjectFieldPathID = None, setFriendlyNameWithPrefix = None, setFullFieldPath = None, setIsBoolean = None, setIsCalculatedInCSharp = None, setIsDateTime = None, setIsEnum = None, setIsFilterable = None, setIsNotEnumOrBoolean = None, setIsNumeric = None, setIsString = None, setIsTimeSpan = None, setMaxSortBreakPosition = None, setModifiedTime = None, setSubtopicID = None, setSystemType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicFieldID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnDataObjectFieldPathID = False, returnFriendlyNameWithPrefix = False, returnFullFieldPath = False, returnIsBoolean = False, returnIsCalculatedInCSharp = False, returnIsDateTime = False, returnIsEnum = False, returnIsFilterable = False, returnIsNotEnumOrBoolean = False, returnIsNumeric = False, returnIsString = False, returnIsTimeSpan = False, returnMaxSortBreakPosition = False, returnModifiedTime = False, returnSubtopicID = False, returnSystemType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubtopicField(SubtopicFieldID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicField/" + str(SubtopicFieldID), verb = "delete")


def getEverySubtopicStandardFilter(searchConditions = [], EntityID = 1, returnSubtopicStandardFilterID = False, returnCreatedTime = False, returnDisplayOnReport = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubtopicStandardFilter in the district.

    This function returns a dataframe of every SubtopicStandardFilter in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1, returnSubtopicStandardFilterID = False, returnCreatedTime = False, returnDisplayOnReport = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(SubtopicStandardFilterID), verb = "get", return_params_list = return_params)

def modifySubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1, setSubtopicStandardFilterID = None, setCreatedTime = None, setDisplayOnReport = None, setIsRequired = None, setModifiedTime = None, setPath = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicStandardFilterID = False, returnCreatedTime = False, returnDisplayOnReport = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(SubtopicStandardFilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubtopicStandardFilter(EntityID = 1, setSubtopicStandardFilterID = None, setCreatedTime = None, setDisplayOnReport = None, setIsRequired = None, setModifiedTime = None, setPath = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setSubtopicID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubtopicStandardFilterID = False, returnCreatedTime = False, returnDisplayOnReport = False, returnIsRequired = False, returnModifiedTime = False, returnPath = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnSubtopicID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubtopicStandardFilter(SubtopicStandardFilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SubtopicStandardFilter/" + str(SubtopicStandardFilterID), verb = "delete")


def getEverySummaryReportParameter(searchConditions = [], EntityID = 1, returnSummaryReportParameterID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SummaryReportParameter in the district.

    This function returns a dataframe of every SummaryReportParameter in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSummaryReportParameter(SummaryReportParameterID, EntityID = 1, returnSummaryReportParameterID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(SummaryReportParameterID), verb = "get", return_params_list = return_params)

def modifySummaryReportParameter(SummaryReportParameterID, EntityID = 1, setSummaryReportParameterID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setReportQueueID = None, setUsedBy = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSummaryReportParameterID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(SummaryReportParameterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSummaryReportParameter(EntityID = 1, setSummaryReportParameterID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setReportQueueID = None, setUsedBy = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSummaryReportParameterID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnReportQueueID = False, returnUsedBy = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSummaryReportParameter(SummaryReportParameterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportParameter/" + str(SummaryReportParameterID), verb = "delete")


def getEverySummaryReportPrompt(searchConditions = [], EntityID = 1, returnSummaryReportPromptID = False, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SummaryReportPrompt in the district.

    This function returns a dataframe of every SummaryReportPrompt in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSummaryReportPrompt(SummaryReportPromptID, EntityID = 1, returnSummaryReportPromptID = False, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(SummaryReportPromptID), verb = "get", return_params_list = return_params)

def modifySummaryReportPrompt(SummaryReportPromptID, EntityID = 1, setSummaryReportPromptID = None, setCreatedTime = None, setLabel = None, setModifiedTime = None, setOrder = None, setReportQueueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSummaryReportPromptID = False, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(SummaryReportPromptID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSummaryReportPrompt(EntityID = 1, setSummaryReportPromptID = None, setCreatedTime = None, setLabel = None, setModifiedTime = None, setOrder = None, setReportQueueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSummaryReportPromptID = False, returnCreatedTime = False, returnLabel = False, returnModifiedTime = False, returnOrder = False, returnReportQueueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSummaryReportPrompt(SummaryReportPromptID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportPrompt/" + str(SummaryReportPromptID), verb = "delete")


def getEverySummaryReportSection(searchConditions = [], EntityID = 1, returnSummaryReportSectionID = False, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SummaryReportSection in the district.

    This function returns a dataframe of every SummaryReportSection in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSummaryReportSection(SummaryReportSectionID, EntityID = 1, returnSummaryReportSectionID = False, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(SummaryReportSectionID), verb = "get", return_params_list = return_params)

def modifySummaryReportSection(SummaryReportSectionID, EntityID = 1, setSummaryReportSectionID = None, setCreatedTime = None, setDisplayName = None, setHiddenType = None, setHiddenTypeCode = None, setModifiedTime = None, setOrder = None, setPath = None, setReportQueueID = None, setSummaryReportSectionIDParent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSummaryReportSectionID = False, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(SummaryReportSectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSummaryReportSection(EntityID = 1, setSummaryReportSectionID = None, setCreatedTime = None, setDisplayName = None, setHiddenType = None, setHiddenTypeCode = None, setModifiedTime = None, setOrder = None, setPath = None, setReportQueueID = None, setSummaryReportSectionIDParent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSummaryReportSectionID = False, returnCreatedTime = False, returnDisplayName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnOrder = False, returnPath = False, returnReportQueueID = False, returnSummaryReportSectionIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSummaryReportSection(SummaryReportSectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSection/" + str(SummaryReportSectionID), verb = "delete")


def getEverySummaryReportSectionColumn(searchConditions = [], EntityID = 1, returnSummaryReportSectionColumnID = False, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SummaryReportSectionColumn in the district.

    This function returns a dataframe of every SummaryReportSectionColumn in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1, returnSummaryReportSectionColumnID = False, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(SummaryReportSectionColumnID), verb = "get", return_params_list = return_params)

def modifySummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1, setSummaryReportSectionColumnID = None, setCreatedTime = None, setDataType = None, setDisplayName = None, setFieldName = None, setHiddenType = None, setHiddenTypeCode = None, setModifiedTime = None, setSummaryReportSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSummaryReportSectionColumnID = False, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(SummaryReportSectionColumnID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSummaryReportSectionColumn(EntityID = 1, setSummaryReportSectionColumnID = None, setCreatedTime = None, setDataType = None, setDisplayName = None, setFieldName = None, setHiddenType = None, setHiddenTypeCode = None, setModifiedTime = None, setSummaryReportSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSummaryReportSectionColumnID = False, returnCreatedTime = False, returnDataType = False, returnDisplayName = False, returnFieldName = False, returnHiddenType = False, returnHiddenTypeCode = False, returnModifiedTime = False, returnSummaryReportSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSummaryReportSectionColumn(SummaryReportSectionColumnID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/SummaryReportSectionColumn/" + str(SummaryReportSectionColumnID), verb = "delete")


def getEveryTempReportRole(searchConditions = [], EntityID = 1, returnTempReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnReportIsSkywardReport = False, returnReportName = False, returnReportPortal = False, returnReportPrimaryMenuModuleDisplayName = False, returnReportReportType = False, returnReportRoleID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempReportRole in the district.

    This function returns a dataframe of every TempReportRole in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempReportRole(TempReportRoleID, EntityID = 1, returnTempReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnReportIsSkywardReport = False, returnReportName = False, returnReportPortal = False, returnReportPrimaryMenuModuleDisplayName = False, returnReportReportType = False, returnReportRoleID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(TempReportRoleID), verb = "get", return_params_list = return_params)

def modifyTempReportRole(TempReportRoleID, EntityID = 1, setTempReportRoleID = None, setCreatedTime = None, setModifiedTime = None, setReportID = None, setReportIsSkywardReport = None, setReportName = None, setReportPortal = None, setReportPrimaryMenuModuleDisplayName = None, setReportReportType = None, setReportRoleID = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnReportIsSkywardReport = False, returnReportName = False, returnReportPortal = False, returnReportPrimaryMenuModuleDisplayName = False, returnReportReportType = False, returnReportRoleID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(TempReportRoleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempReportRole(EntityID = 1, setTempReportRoleID = None, setCreatedTime = None, setModifiedTime = None, setReportID = None, setReportIsSkywardReport = None, setReportName = None, setReportPortal = None, setReportPrimaryMenuModuleDisplayName = None, setReportReportType = None, setReportRoleID = None, setRoleID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempReportRoleID = False, returnCreatedTime = False, returnModifiedTime = False, returnReportID = False, returnReportIsSkywardReport = False, returnReportName = False, returnReportPortal = False, returnReportPrimaryMenuModuleDisplayName = False, returnReportReportType = False, returnReportRoleID = False, returnRoleID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempReportRole(TempReportRoleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempReportRole/" + str(TempReportRoleID), verb = "delete")


def getEveryTempSubtopicRelationshipOption(searchConditions = [], EntityID = 1, returnTempSubtopicRelationshipOptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnRelationshipPath = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempSubtopicRelationshipOption in the district.

    This function returns a dataframe of every TempSubtopicRelationshipOption in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempSubtopicRelationshipOption(TempSubtopicRelationshipOptionID, EntityID = 1, returnTempSubtopicRelationshipOptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnRelationshipPath = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(TempSubtopicRelationshipOptionID), verb = "get", return_params_list = return_params)

def modifyTempSubtopicRelationshipOption(TempSubtopicRelationshipOptionID, EntityID = 1, setTempSubtopicRelationshipOptionID = None, setCreatedTime = None, setModifiedTime = None, setRelationshipPath = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSubtopicRelationshipOptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnRelationshipPath = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(TempSubtopicRelationshipOptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempSubtopicRelationshipOption(EntityID = 1, setTempSubtopicRelationshipOptionID = None, setCreatedTime = None, setModifiedTime = None, setRelationshipPath = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempSubtopicRelationshipOptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnRelationshipPath = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempSubtopicRelationshipOption(TempSubtopicRelationshipOptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempSubtopicRelationshipOption/" + str(TempSubtopicRelationshipOptionID), verb = "delete")


def getEveryTempUploadDataMiningReportLog(searchConditions = [], EntityID = 1, returnTempUploadDataMiningReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempUploadDataMiningReportLog in the district.

    This function returns a dataframe of every TempUploadDataMiningReportLog in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempUploadDataMiningReportLog(TempUploadDataMiningReportLogID, EntityID = 1, returnTempUploadDataMiningReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(TempUploadDataMiningReportLogID), verb = "get", return_params_list = return_params)

def modifyTempUploadDataMiningReportLog(TempUploadDataMiningReportLogID, EntityID = 1, setTempUploadDataMiningReportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setResult = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUploadDataMiningReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(TempUploadDataMiningReportLogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempUploadDataMiningReportLog(EntityID = 1, setTempUploadDataMiningReportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setResult = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUploadDataMiningReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempUploadDataMiningReportLog(TempUploadDataMiningReportLogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/TempUploadDataMiningReportLog/" + str(TempUploadDataMiningReportLogID), verb = "delete")


def getEveryTopic(searchConditions = [], EntityID = 1, returnTopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnNameWithParentTopicName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Topic in the district.

    This function returns a dataframe of every Topic in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTopic(TopicID, EntityID = 1, returnTopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnNameWithParentTopicName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(TopicID), verb = "get", return_params_list = return_params)

def modifyTopic(TopicID, EntityID = 1, setTopicID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setModifiedTime = None, setName = None, setNameWithParentTopicName = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setTopicIDParent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnNameWithParentTopicName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(TopicID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTopic(EntityID = 1, setTopicID = None, setCreatedTime = None, setCurrentUserHasAccess = None, setModifiedTime = None, setName = None, setNameWithParentTopicName = None, setSkywardHash = None, setSkywardID = None, setSubjectID = None, setTopicIDParent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTopicID = False, returnCreatedTime = False, returnCurrentUserHasAccess = False, returnModifiedTime = False, returnName = False, returnNameWithParentTopicName = False, returnSkywardHash = False, returnSkywardID = False, returnSubjectID = False, returnTopicIDParent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTopic(TopicID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/Topic/" + str(TopicID), verb = "delete")


def getEveryUploadReportLog(searchConditions = [], EntityID = 1, returnUploadReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UploadReportLog in the district.

    This function returns a dataframe of every UploadReportLog in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUploadReportLog(UploadReportLogID, EntityID = 1, returnUploadReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(UploadReportLogID), verb = "get", return_params_list = return_params)

def modifyUploadReportLog(UploadReportLogID, EntityID = 1, setUploadReportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setReportID = None, setResult = None, setResultCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnUploadReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(UploadReportLogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUploadReportLog(EntityID = 1, setUploadReportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setReportID = None, setResult = None, setResultCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnUploadReportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnReportID = False, returnResult = False, returnResultCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUploadReportLog(UploadReportLogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UploadReportLog/" + str(UploadReportLogID), verb = "delete")


def getEveryUserReportPrompt(searchConditions = [], EntityID = 1, returnUserReportPromptID = False, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserReportPrompt in the district.

    This function returns a dataframe of every UserReportPrompt in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserReportPrompt(UserReportPromptID, EntityID = 1, returnUserReportPromptID = False, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(UserReportPromptID), verb = "get", return_params_list = return_params)

def modifyUserReportPrompt(UserReportPromptID, EntityID = 1, setUserReportPromptID = None, setCreatedTime = None, setCrystalPromptValues = None, setCrystalPromptXML = None, setEntityID = None, setModifiedTime = None, setPromptTemplateID = None, setReportID = None, setSkywardPromptValues = None, setSkywardPromptXML = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserReportPromptID = False, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(UserReportPromptID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserReportPrompt(EntityID = 1, setUserReportPromptID = None, setCreatedTime = None, setCrystalPromptValues = None, setCrystalPromptXML = None, setEntityID = None, setModifiedTime = None, setPromptTemplateID = None, setReportID = None, setSkywardPromptValues = None, setSkywardPromptXML = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserReportPromptID = False, returnCreatedTime = False, returnCrystalPromptValues = False, returnCrystalPromptXML = False, returnEntityID = False, returnModifiedTime = False, returnPromptTemplateID = False, returnReportID = False, returnSkywardPromptValues = False, returnSkywardPromptXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserReportPrompt(UserReportPromptID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserReportPrompt/" + str(UserReportPromptID), verb = "delete")


def getEveryUserSetting(searchConditions = [], EntityID = 1, returnUserSettingID = False, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserSetting in the district.

    This function returns a dataframe of every UserSetting in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserSetting(UserSettingID, EntityID = 1, returnUserSettingID = False, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(UserSettingID), verb = "get", return_params_list = return_params)

def modifyUserSetting(UserSettingID, EntityID = 1, setUserSettingID = None, setCreatedTime = None, setDataMiningLeftFieldSelectionPanelWidth = None, setDataMiningMiddleFieldSelectionPanelWidth = None, setDataMiningShowLeftFieldSelectionPanel = None, setModifiedTime = None, setShowSideBar = None, setSideBarWidth = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserSettingID = False, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(UserSettingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserSetting(EntityID = 1, setUserSettingID = None, setCreatedTime = None, setDataMiningLeftFieldSelectionPanelWidth = None, setDataMiningMiddleFieldSelectionPanelWidth = None, setDataMiningShowLeftFieldSelectionPanel = None, setModifiedTime = None, setShowSideBar = None, setSideBarWidth = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserSettingID = False, returnCreatedTime = False, returnDataMiningLeftFieldSelectionPanelWidth = False, returnDataMiningMiddleFieldSelectionPanelWidth = False, returnDataMiningShowLeftFieldSelectionPanel = False, returnModifiedTime = False, returnShowSideBar = False, returnSideBarWidth = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserSetting(UserSettingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Reporting/UserSetting/" + str(UserSettingID), verb = "delete")