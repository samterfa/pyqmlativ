# This module contains SkySys functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryApplySchemaChangeAllChangesConfirmation(searchConditions = [], EntityID = 1, returnApplySchemaChangeAllChangesConfirmationID = False, returnApplySchemaChangeRunID = False, returnChangeType = False, returnCreatedTime = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModuleID = False, returnModulePendingName = False, returnObjectID = False, returnObjectPendingName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ApplySchemaChangeAllChangesConfirmation in the district.

    This function returns a dataframe of every ApplySchemaChangeAllChangesConfirmation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getApplySchemaChangeAllChangesConfirmation(ApplySchemaChangeAllChangesConfirmationID, EntityID = 1, returnApplySchemaChangeAllChangesConfirmationID = False, returnApplySchemaChangeRunID = False, returnChangeType = False, returnCreatedTime = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModuleID = False, returnModulePendingName = False, returnObjectID = False, returnObjectPendingName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(ApplySchemaChangeAllChangesConfirmationID), verb = "get", return_params_list = return_params)

def modifyApplySchemaChangeAllChangesConfirmation(ApplySchemaChangeAllChangesConfirmationID, EntityID = 1, setApplySchemaChangeAllChangesConfirmationID = None, setApplySchemaChangeRunID = None, setChangeType = None, setCreatedTime = None, setFieldID = None, setFieldPendingName = None, setModifiedTime = None, setModuleID = None, setModulePendingName = None, setObjectID = None, setObjectPendingName = None, setRelationshipID = None, setRelationshipPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeAllChangesConfirmationID = False, returnApplySchemaChangeRunID = False, returnChangeType = False, returnCreatedTime = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModuleID = False, returnModulePendingName = False, returnObjectID = False, returnObjectPendingName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(ApplySchemaChangeAllChangesConfirmationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createApplySchemaChangeAllChangesConfirmation(EntityID = 1, setApplySchemaChangeAllChangesConfirmationID = None, setApplySchemaChangeRunID = None, setChangeType = None, setCreatedTime = None, setFieldID = None, setFieldPendingName = None, setModifiedTime = None, setModuleID = None, setModulePendingName = None, setObjectID = None, setObjectPendingName = None, setRelationshipID = None, setRelationshipPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeAllChangesConfirmationID = False, returnApplySchemaChangeRunID = False, returnChangeType = False, returnCreatedTime = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModuleID = False, returnModulePendingName = False, returnObjectID = False, returnObjectPendingName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteApplySchemaChangeAllChangesConfirmation(ApplySchemaChangeAllChangesConfirmationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeAllChangesConfirmation/" + str(ApplySchemaChangeAllChangesConfirmationID), verb = "delete")


def getEveryApplySchemaChangeFieldSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeFieldSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldChangeType = False, returnFieldCurrentName = False, returnFieldHasChangedRelationships = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ApplySchemaChangeFieldSelection in the district.

    This function returns a dataframe of every ApplySchemaChangeFieldSelection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getApplySchemaChangeFieldSelection(ApplySchemaChangeFieldSelectionID, EntityID = 1, returnApplySchemaChangeFieldSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldChangeType = False, returnFieldCurrentName = False, returnFieldHasChangedRelationships = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(ApplySchemaChangeFieldSelectionID), verb = "get", return_params_list = return_params)

def modifyApplySchemaChangeFieldSelection(ApplySchemaChangeFieldSelectionID, EntityID = 1, setApplySchemaChangeFieldSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setFieldChangeType = None, setFieldCurrentName = None, setFieldHasChangedRelationships = None, setFieldID = None, setFieldPendingName = None, setModifiedTime = None, setModulePendingName = None, setObjectPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeFieldSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldChangeType = False, returnFieldCurrentName = False, returnFieldHasChangedRelationships = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(ApplySchemaChangeFieldSelectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createApplySchemaChangeFieldSelection(EntityID = 1, setApplySchemaChangeFieldSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setFieldChangeType = None, setFieldCurrentName = None, setFieldHasChangedRelationships = None, setFieldID = None, setFieldPendingName = None, setModifiedTime = None, setModulePendingName = None, setObjectPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeFieldSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldChangeType = False, returnFieldCurrentName = False, returnFieldHasChangedRelationships = False, returnFieldID = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteApplySchemaChangeFieldSelection(ApplySchemaChangeFieldSelectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeFieldSelection/" + str(ApplySchemaChangeFieldSelectionID), verb = "delete")


def getEveryApplySchemaChangeObjectSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeObjectSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectChangeType = False, returnObjectCurrentName = False, returnObjectHasChangedFields = False, returnObjectHasChangedRelationships = False, returnObjectID = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ApplySchemaChangeObjectSelection in the district.

    This function returns a dataframe of every ApplySchemaChangeObjectSelection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getApplySchemaChangeObjectSelection(ApplySchemaChangeObjectSelectionID, EntityID = 1, returnApplySchemaChangeObjectSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectChangeType = False, returnObjectCurrentName = False, returnObjectHasChangedFields = False, returnObjectHasChangedRelationships = False, returnObjectID = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(ApplySchemaChangeObjectSelectionID), verb = "get", return_params_list = return_params)

def modifyApplySchemaChangeObjectSelection(ApplySchemaChangeObjectSelectionID, EntityID = 1, setApplySchemaChangeObjectSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setModifiedTime = None, setModulePendingName = None, setObjectChangeType = None, setObjectCurrentName = None, setObjectHasChangedFields = None, setObjectHasChangedRelationships = None, setObjectID = None, setObjectPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeObjectSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectChangeType = False, returnObjectCurrentName = False, returnObjectHasChangedFields = False, returnObjectHasChangedRelationships = False, returnObjectID = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(ApplySchemaChangeObjectSelectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createApplySchemaChangeObjectSelection(EntityID = 1, setApplySchemaChangeObjectSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setModifiedTime = None, setModulePendingName = None, setObjectChangeType = None, setObjectCurrentName = None, setObjectHasChangedFields = None, setObjectHasChangedRelationships = None, setObjectID = None, setObjectPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeObjectSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectChangeType = False, returnObjectCurrentName = False, returnObjectHasChangedFields = False, returnObjectHasChangedRelationships = False, returnObjectID = False, returnObjectPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteApplySchemaChangeObjectSelection(ApplySchemaChangeObjectSelectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeObjectSelection/" + str(ApplySchemaChangeObjectSelectionID), verb = "delete")


def getEveryApplySchemaChangeRelationshipSelection(searchConditions = [], EntityID = 1, returnApplySchemaChangeRelationshipSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnRelationshipChangeType = False, returnRelationshipCurrentName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ApplySchemaChangeRelationshipSelection in the district.

    This function returns a dataframe of every ApplySchemaChangeRelationshipSelection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getApplySchemaChangeRelationshipSelection(ApplySchemaChangeRelationshipSelectionID, EntityID = 1, returnApplySchemaChangeRelationshipSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnRelationshipChangeType = False, returnRelationshipCurrentName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(ApplySchemaChangeRelationshipSelectionID), verb = "get", return_params_list = return_params)

def modifyApplySchemaChangeRelationshipSelection(ApplySchemaChangeRelationshipSelectionID, EntityID = 1, setApplySchemaChangeRelationshipSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setFieldPendingName = None, setModifiedTime = None, setModulePendingName = None, setObjectPendingName = None, setRelationshipChangeType = None, setRelationshipCurrentName = None, setRelationshipID = None, setRelationshipPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeRelationshipSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnRelationshipChangeType = False, returnRelationshipCurrentName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(ApplySchemaChangeRelationshipSelectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createApplySchemaChangeRelationshipSelection(EntityID = 1, setApplySchemaChangeRelationshipSelectionID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setFieldPendingName = None, setModifiedTime = None, setModulePendingName = None, setObjectPendingName = None, setRelationshipChangeType = None, setRelationshipCurrentName = None, setRelationshipID = None, setRelationshipPendingName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeRelationshipSelectionID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnFieldPendingName = False, returnModifiedTime = False, returnModulePendingName = False, returnObjectPendingName = False, returnRelationshipChangeType = False, returnRelationshipCurrentName = False, returnRelationshipID = False, returnRelationshipPendingName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteApplySchemaChangeRelationshipSelection(ApplySchemaChangeRelationshipSelectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRelationshipSelection/" + str(ApplySchemaChangeRelationshipSelectionID), verb = "delete")


def getEveryApplySchemaChangeRun(searchConditions = [], EntityID = 1, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnExecutedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ApplySchemaChangeRun in the district.

    This function returns a dataframe of every ApplySchemaChangeRun in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getApplySchemaChangeRun(ApplySchemaChangeRunID, EntityID = 1, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnExecutedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(ApplySchemaChangeRunID), verb = "get", return_params_list = return_params)

def modifyApplySchemaChangeRun(ApplySchemaChangeRunID, EntityID = 1, setApplySchemaChangeRunID = None, setCreatedTime = None, setExecutedTime = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnExecutedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(ApplySchemaChangeRunID), verb = "post", return_params_list = return_params, payload = payload_params)

def createApplySchemaChangeRun(EntityID = 1, setApplySchemaChangeRunID = None, setCreatedTime = None, setExecutedTime = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnExecutedTime = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteApplySchemaChangeRun(ApplySchemaChangeRunID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ApplySchemaChangeRun/" + str(ApplySchemaChangeRunID), verb = "delete")


def getEveryAttachment(searchConditions = [], EntityID = 1, returnAttachmentID = False, returnAttachmentTypeID = False, returnComment = False, returnCreatedTime = False, returnCurrentUserCanReadAttachmentsOfThisAttachmentType = False, returnMediaID = False, returnModifiedTime = False, returnObjectID = False, returnSourceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Attachment in the district.

    This function returns a dataframe of every Attachment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttachment(AttachmentID, EntityID = 1, returnAttachmentID = False, returnAttachmentTypeID = False, returnComment = False, returnCreatedTime = False, returnCurrentUserCanReadAttachmentsOfThisAttachmentType = False, returnMediaID = False, returnModifiedTime = False, returnObjectID = False, returnSourceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(AttachmentID), verb = "get", return_params_list = return_params)

def modifyAttachment(AttachmentID, EntityID = 1, setAttachmentID = None, setAttachmentTypeID = None, setComment = None, setCreatedTime = None, setCurrentUserCanReadAttachmentsOfThisAttachmentType = None, setMediaID = None, setModifiedTime = None, setObjectID = None, setSourceID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttachmentID = False, returnAttachmentTypeID = False, returnComment = False, returnCreatedTime = False, returnCurrentUserCanReadAttachmentsOfThisAttachmentType = False, returnMediaID = False, returnModifiedTime = False, returnObjectID = False, returnSourceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(AttachmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttachment(EntityID = 1, setAttachmentID = None, setAttachmentTypeID = None, setComment = None, setCreatedTime = None, setCurrentUserCanReadAttachmentsOfThisAttachmentType = None, setMediaID = None, setModifiedTime = None, setObjectID = None, setSourceID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttachmentID = False, returnAttachmentTypeID = False, returnComment = False, returnCreatedTime = False, returnCurrentUserCanReadAttachmentsOfThisAttachmentType = False, returnMediaID = False, returnModifiedTime = False, returnObjectID = False, returnSourceID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttachment(AttachmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Attachment/" + str(AttachmentID), verb = "delete")


def getEveryAttachmentType(searchConditions = [], EntityID = 1, returnAttachmentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserCanCreateAttachmentsOfThisAttachmentType = False, returnCustomizationID = False, returnDescription = False, returnEffectiveIsDefault = False, returnEffectiveShowInActivityAccess = False, returnEffectiveShowInAdministrativeAccess = False, returnEffectiveShowInEmployeeAccess = False, returnEffectiveShowInFamilyAccess = False, returnEffectiveShowInNewStudentEnrollment = False, returnEffectiveShowInStudentAccess = False, returnEffectiveShowInStudentServices = False, returnEffectiveShowInTeacherAccess = False, returnIncludeWithEmail = False, returnIsDefault = False, returnModifiedTime = False, returnObjectID = False, returnShowInActivityAccess = False, returnShowInAdministrativeAccess = False, returnShowInEmployeeAccess = False, returnShowInFamilyAccess = False, returnShowInNewStudentEnrollment = False, returnShowInStudentAccess = False, returnShowInStudentServices = False, returnShowInTeacherAccess = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardShowInActivityAccess = False, returnSkywardShowInAdministrativeAccess = False, returnSkywardShowInEmployeeAccess = False, returnSkywardShowInFamilyAccess = False, returnSkywardShowInNewStudentEnrollment = False, returnSkywardShowInStudentAccess = False, returnSkywardShowInStudentServices = False, returnSkywardShowInTeacherAccess = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AttachmentType in the district.

    This function returns a dataframe of every AttachmentType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAttachmentType(AttachmentTypeID, EntityID = 1, returnAttachmentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserCanCreateAttachmentsOfThisAttachmentType = False, returnCustomizationID = False, returnDescription = False, returnEffectiveIsDefault = False, returnEffectiveShowInActivityAccess = False, returnEffectiveShowInAdministrativeAccess = False, returnEffectiveShowInEmployeeAccess = False, returnEffectiveShowInFamilyAccess = False, returnEffectiveShowInNewStudentEnrollment = False, returnEffectiveShowInStudentAccess = False, returnEffectiveShowInStudentServices = False, returnEffectiveShowInTeacherAccess = False, returnIncludeWithEmail = False, returnIsDefault = False, returnModifiedTime = False, returnObjectID = False, returnShowInActivityAccess = False, returnShowInAdministrativeAccess = False, returnShowInEmployeeAccess = False, returnShowInFamilyAccess = False, returnShowInNewStudentEnrollment = False, returnShowInStudentAccess = False, returnShowInStudentServices = False, returnShowInTeacherAccess = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardShowInActivityAccess = False, returnSkywardShowInAdministrativeAccess = False, returnSkywardShowInEmployeeAccess = False, returnSkywardShowInFamilyAccess = False, returnSkywardShowInNewStudentEnrollment = False, returnSkywardShowInStudentAccess = False, returnSkywardShowInStudentServices = False, returnSkywardShowInTeacherAccess = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(AttachmentTypeID), verb = "get", return_params_list = return_params)

def modifyAttachmentType(AttachmentTypeID, EntityID = 1, setAttachmentTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentUserCanCreateAttachmentsOfThisAttachmentType = None, setCustomizationID = None, setDescription = None, setEffectiveIsDefault = None, setEffectiveShowInActivityAccess = None, setEffectiveShowInAdministrativeAccess = None, setEffectiveShowInEmployeeAccess = None, setEffectiveShowInFamilyAccess = None, setEffectiveShowInNewStudentEnrollment = None, setEffectiveShowInStudentAccess = None, setEffectiveShowInStudentServices = None, setEffectiveShowInTeacherAccess = None, setIncludeWithEmail = None, setIsDefault = None, setModifiedTime = None, setObjectID = None, setShowInActivityAccess = None, setShowInAdministrativeAccess = None, setShowInEmployeeAccess = None, setShowInFamilyAccess = None, setShowInNewStudentEnrollment = None, setShowInStudentAccess = None, setShowInStudentServices = None, setShowInTeacherAccess = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSkywardShowInActivityAccess = None, setSkywardShowInAdministrativeAccess = None, setSkywardShowInEmployeeAccess = None, setSkywardShowInFamilyAccess = None, setSkywardShowInNewStudentEnrollment = None, setSkywardShowInStudentAccess = None, setSkywardShowInStudentServices = None, setSkywardShowInTeacherAccess = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttachmentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserCanCreateAttachmentsOfThisAttachmentType = False, returnCustomizationID = False, returnDescription = False, returnEffectiveIsDefault = False, returnEffectiveShowInActivityAccess = False, returnEffectiveShowInAdministrativeAccess = False, returnEffectiveShowInEmployeeAccess = False, returnEffectiveShowInFamilyAccess = False, returnEffectiveShowInNewStudentEnrollment = False, returnEffectiveShowInStudentAccess = False, returnEffectiveShowInStudentServices = False, returnEffectiveShowInTeacherAccess = False, returnIncludeWithEmail = False, returnIsDefault = False, returnModifiedTime = False, returnObjectID = False, returnShowInActivityAccess = False, returnShowInAdministrativeAccess = False, returnShowInEmployeeAccess = False, returnShowInFamilyAccess = False, returnShowInNewStudentEnrollment = False, returnShowInStudentAccess = False, returnShowInStudentServices = False, returnShowInTeacherAccess = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardShowInActivityAccess = False, returnSkywardShowInAdministrativeAccess = False, returnSkywardShowInEmployeeAccess = False, returnSkywardShowInFamilyAccess = False, returnSkywardShowInNewStudentEnrollment = False, returnSkywardShowInStudentAccess = False, returnSkywardShowInStudentServices = False, returnSkywardShowInTeacherAccess = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(AttachmentTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAttachmentType(EntityID = 1, setAttachmentTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentUserCanCreateAttachmentsOfThisAttachmentType = None, setCustomizationID = None, setDescription = None, setEffectiveIsDefault = None, setEffectiveShowInActivityAccess = None, setEffectiveShowInAdministrativeAccess = None, setEffectiveShowInEmployeeAccess = None, setEffectiveShowInFamilyAccess = None, setEffectiveShowInNewStudentEnrollment = None, setEffectiveShowInStudentAccess = None, setEffectiveShowInStudentServices = None, setEffectiveShowInTeacherAccess = None, setIncludeWithEmail = None, setIsDefault = None, setModifiedTime = None, setObjectID = None, setShowInActivityAccess = None, setShowInAdministrativeAccess = None, setShowInEmployeeAccess = None, setShowInFamilyAccess = None, setShowInNewStudentEnrollment = None, setShowInStudentAccess = None, setShowInStudentServices = None, setShowInTeacherAccess = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSkywardShowInActivityAccess = None, setSkywardShowInAdministrativeAccess = None, setSkywardShowInEmployeeAccess = None, setSkywardShowInFamilyAccess = None, setSkywardShowInNewStudentEnrollment = None, setSkywardShowInStudentAccess = None, setSkywardShowInStudentServices = None, setSkywardShowInTeacherAccess = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAttachmentTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserCanCreateAttachmentsOfThisAttachmentType = False, returnCustomizationID = False, returnDescription = False, returnEffectiveIsDefault = False, returnEffectiveShowInActivityAccess = False, returnEffectiveShowInAdministrativeAccess = False, returnEffectiveShowInEmployeeAccess = False, returnEffectiveShowInFamilyAccess = False, returnEffectiveShowInNewStudentEnrollment = False, returnEffectiveShowInStudentAccess = False, returnEffectiveShowInStudentServices = False, returnEffectiveShowInTeacherAccess = False, returnIncludeWithEmail = False, returnIsDefault = False, returnModifiedTime = False, returnObjectID = False, returnShowInActivityAccess = False, returnShowInAdministrativeAccess = False, returnShowInEmployeeAccess = False, returnShowInFamilyAccess = False, returnShowInNewStudentEnrollment = False, returnShowInStudentAccess = False, returnShowInStudentServices = False, returnShowInTeacherAccess = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardShowInActivityAccess = False, returnSkywardShowInAdministrativeAccess = False, returnSkywardShowInEmployeeAccess = False, returnSkywardShowInFamilyAccess = False, returnSkywardShowInNewStudentEnrollment = False, returnSkywardShowInStudentAccess = False, returnSkywardShowInStudentServices = False, returnSkywardShowInTeacherAccess = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAttachmentType(AttachmentTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/AttachmentType/" + str(AttachmentTypeID), verb = "delete")


def getEveryBenchmarkingQuestion(searchConditions = [], EntityID = 1, returnBenchmarkingQuestionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingQuestion in the district.

    This function returns a dataframe of every BenchmarkingQuestion in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingQuestion(BenchmarkingQuestionID, EntityID = 1, returnBenchmarkingQuestionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(BenchmarkingQuestionID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingQuestion(BenchmarkingQuestionID, EntityID = 1, setBenchmarkingQuestionID = None, setCreatedTime = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setText = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingQuestionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(BenchmarkingQuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingQuestion(EntityID = 1, setBenchmarkingQuestionID = None, setCreatedTime = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setText = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingQuestionID = False, returnCreatedTime = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingQuestion(BenchmarkingQuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestion/" + str(BenchmarkingQuestionID), verb = "delete")


def getEveryBenchmarkingQuestionAnswer(searchConditions = [], EntityID = 1, returnBenchmarkingQuestionAnswerID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyInstanceID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNumericValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingQuestionAnswer in the district.

    This function returns a dataframe of every BenchmarkingQuestionAnswer in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingQuestionAnswer(BenchmarkingQuestionAnswerID, EntityID = 1, returnBenchmarkingQuestionAnswerID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyInstanceID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNumericValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(BenchmarkingQuestionAnswerID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingQuestionAnswer(BenchmarkingQuestionAnswerID, EntityID = 1, setBenchmarkingQuestionAnswerID = None, setBenchmarkingQuestionID = None, setBenchmarkingSurveyInstanceID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setNumericValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingQuestionAnswerID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyInstanceID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNumericValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(BenchmarkingQuestionAnswerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingQuestionAnswer(EntityID = 1, setBenchmarkingQuestionAnswerID = None, setBenchmarkingQuestionID = None, setBenchmarkingSurveyInstanceID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setNumericValue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingQuestionAnswerID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyInstanceID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNumericValue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingQuestionAnswer(BenchmarkingQuestionAnswerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingQuestionAnswer/" + str(BenchmarkingQuestionAnswerID), verb = "delete")


def getEveryBenchmarkingSurvey(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyID = False, returnBannerMessage = False, returnCreatedTime = False, returnEndTime = False, returnHeaderMessage = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingSurvey in the district.

    This function returns a dataframe of every BenchmarkingSurvey in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingSurvey(BenchmarkingSurveyID, EntityID = 1, returnBenchmarkingSurveyID = False, returnBannerMessage = False, returnCreatedTime = False, returnEndTime = False, returnHeaderMessage = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(BenchmarkingSurveyID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingSurvey(BenchmarkingSurveyID, EntityID = 1, setBenchmarkingSurveyID = None, setBannerMessage = None, setCreatedTime = None, setEndTime = None, setHeaderMessage = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingSurveyID = False, returnBannerMessage = False, returnCreatedTime = False, returnEndTime = False, returnHeaderMessage = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(BenchmarkingSurveyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingSurvey(EntityID = 1, setBenchmarkingSurveyID = None, setBannerMessage = None, setCreatedTime = None, setEndTime = None, setHeaderMessage = None, setModifiedTime = None, setSecurityLocationID = None, setSkywardHash = None, setSkywardID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingSurveyID = False, returnBannerMessage = False, returnCreatedTime = False, returnEndTime = False, returnHeaderMessage = False, returnModifiedTime = False, returnSecurityLocationID = False, returnSkywardHash = False, returnSkywardID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingSurvey(BenchmarkingSurveyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurvey/" + str(BenchmarkingSurveyID), verb = "delete")


def getEveryBenchmarkingSurveyDelay(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyDelayID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnResumeTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingSurveyDelay in the district.

    This function returns a dataframe of every BenchmarkingSurveyDelay in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingSurveyDelay(BenchmarkingSurveyDelayID, EntityID = 1, returnBenchmarkingSurveyDelayID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnResumeTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(BenchmarkingSurveyDelayID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingSurveyDelay(BenchmarkingSurveyDelayID, EntityID = 1, setBenchmarkingSurveyDelayID = None, setBenchmarkingSurveyID = None, setCreatedTime = None, setModifiedTime = None, setResumeTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnBenchmarkingSurveyDelayID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnResumeTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(BenchmarkingSurveyDelayID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingSurveyDelay(EntityID = 1, setBenchmarkingSurveyDelayID = None, setBenchmarkingSurveyID = None, setCreatedTime = None, setModifiedTime = None, setResumeTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnBenchmarkingSurveyDelayID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnResumeTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingSurveyDelay(BenchmarkingSurveyDelayID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyDelay/" + str(BenchmarkingSurveyDelayID), verb = "delete")


def getEveryBenchmarkingSurveyInstance(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyInstanceID = False, returnBenchmarkingSurveyID = False, returnComment = False, returnContactEmail = False, returnCreatedTime = False, returnModifiedTime = False, returnTakenOnMobile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingSurveyInstance in the district.

    This function returns a dataframe of every BenchmarkingSurveyInstance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingSurveyInstance(BenchmarkingSurveyInstanceID, EntityID = 1, returnBenchmarkingSurveyInstanceID = False, returnBenchmarkingSurveyID = False, returnComment = False, returnContactEmail = False, returnCreatedTime = False, returnModifiedTime = False, returnTakenOnMobile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(BenchmarkingSurveyInstanceID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingSurveyInstance(BenchmarkingSurveyInstanceID, EntityID = 1, setBenchmarkingSurveyInstanceID = None, setBenchmarkingSurveyID = None, setComment = None, setContactEmail = None, setCreatedTime = None, setModifiedTime = None, setTakenOnMobile = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnBenchmarkingSurveyInstanceID = False, returnBenchmarkingSurveyID = False, returnComment = False, returnContactEmail = False, returnCreatedTime = False, returnModifiedTime = False, returnTakenOnMobile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(BenchmarkingSurveyInstanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingSurveyInstance(EntityID = 1, setBenchmarkingSurveyInstanceID = None, setBenchmarkingSurveyID = None, setComment = None, setContactEmail = None, setCreatedTime = None, setModifiedTime = None, setTakenOnMobile = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnBenchmarkingSurveyInstanceID = False, returnBenchmarkingSurveyID = False, returnComment = False, returnContactEmail = False, returnCreatedTime = False, returnModifiedTime = False, returnTakenOnMobile = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingSurveyInstance(BenchmarkingSurveyInstanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyInstance/" + str(BenchmarkingSurveyInstanceID), verb = "delete")


def getEveryBenchmarkingSurveyQuestion(searchConditions = [], EntityID = 1, returnBenchmarkingSurveyQuestionID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BenchmarkingSurveyQuestion in the district.

    This function returns a dataframe of every BenchmarkingSurveyQuestion in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBenchmarkingSurveyQuestion(BenchmarkingSurveyQuestionID, EntityID = 1, returnBenchmarkingSurveyQuestionID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(BenchmarkingSurveyQuestionID), verb = "get", return_params_list = return_params)

def modifyBenchmarkingSurveyQuestion(BenchmarkingSurveyQuestionID, EntityID = 1, setBenchmarkingSurveyQuestionID = None, setBenchmarkingQuestionID = None, setBenchmarkingSurveyID = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingSurveyQuestionID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(BenchmarkingSurveyQuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBenchmarkingSurveyQuestion(EntityID = 1, setBenchmarkingSurveyQuestionID = None, setBenchmarkingQuestionID = None, setBenchmarkingSurveyID = None, setCreatedTime = None, setModifiedTime = None, setOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBenchmarkingSurveyQuestionID = False, returnBenchmarkingQuestionID = False, returnBenchmarkingSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBenchmarkingSurveyQuestion(BenchmarkingSurveyQuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BenchmarkingSurveyQuestion/" + str(BenchmarkingSurveyQuestionID), verb = "delete")


def getEveryBrowse(searchConditions = [], EntityID = 1, returnBrowseID = False, returnApplyEntityDistrictFilter = False, returnApplyFiscalYearFilter = False, returnApplySchoolYearFilter = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnEffectiveDataModule = False, returnEffectiveDataObject = False, returnFormattedBrowsePath = False, returnIsReference = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnObjectScreenNamePath = False, returnScreen = False, returnScreenNamePath = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUseAudit = False, returnUseOldPagingSystem = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Browse in the district.

    This function returns a dataframe of every Browse in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowse(BrowseID, EntityID = 1, returnBrowseID = False, returnApplyEntityDistrictFilter = False, returnApplyFiscalYearFilter = False, returnApplySchoolYearFilter = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnEffectiveDataModule = False, returnEffectiveDataObject = False, returnFormattedBrowsePath = False, returnIsReference = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnObjectScreenNamePath = False, returnScreen = False, returnScreenNamePath = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUseAudit = False, returnUseOldPagingSystem = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(BrowseID), verb = "get", return_params_list = return_params)

def modifyBrowse(BrowseID, EntityID = 1, setBrowseID = None, setApplyEntityDistrictFilter = None, setApplyFiscalYearFilter = None, setApplySchoolYearFilter = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setEffectiveDataModule = None, setEffectiveDataObject = None, setFormattedBrowsePath = None, setIsReference = None, setModifiedTime = None, setModule = None, setName = None, setObject = None, setObjectScreenNamePath = None, setScreen = None, setScreenNamePath = None, setSkywardHash = None, setSkywardID = None, setTask = None, setUseAudit = None, setUseOldPagingSystem = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseID = False, returnApplyEntityDistrictFilter = False, returnApplyFiscalYearFilter = False, returnApplySchoolYearFilter = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnEffectiveDataModule = False, returnEffectiveDataObject = False, returnFormattedBrowsePath = False, returnIsReference = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnObjectScreenNamePath = False, returnScreen = False, returnScreenNamePath = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUseAudit = False, returnUseOldPagingSystem = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(BrowseID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowse(EntityID = 1, setBrowseID = None, setApplyEntityDistrictFilter = None, setApplyFiscalYearFilter = None, setApplySchoolYearFilter = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setEffectiveDataModule = None, setEffectiveDataObject = None, setFormattedBrowsePath = None, setIsReference = None, setModifiedTime = None, setModule = None, setName = None, setObject = None, setObjectScreenNamePath = None, setScreen = None, setScreenNamePath = None, setSkywardHash = None, setSkywardID = None, setTask = None, setUseAudit = None, setUseOldPagingSystem = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseID = False, returnApplyEntityDistrictFilter = False, returnApplyFiscalYearFilter = False, returnApplySchoolYearFilter = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnEffectiveDataModule = False, returnEffectiveDataObject = False, returnFormattedBrowsePath = False, returnIsReference = False, returnModifiedTime = False, returnModule = False, returnName = False, returnObject = False, returnObjectScreenNamePath = False, returnScreen = False, returnScreenNamePath = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUseAudit = False, returnUseOldPagingSystem = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowse(BrowseID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Browse/" + str(BrowseID), verb = "delete")


def getEveryBrowseFilter(searchConditions = [], EntityID = 1, returnBrowseFilterID = False, returnBrowseFilterIDClonedFrom = False, returnBrowseID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnFilterID = False, returnFilterTemplate = False, returnFilterTemplateData = False, returnIsAutoCreated = False, returnIsBase = False, returnIsCurrent = False, returnIsDefault = False, returnIsEnabled = False, returnModifiedTime = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseFilter in the district.

    This function returns a dataframe of every BrowseFilter in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseFilter(BrowseFilterID, EntityID = 1, returnBrowseFilterID = False, returnBrowseFilterIDClonedFrom = False, returnBrowseID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnFilterID = False, returnFilterTemplate = False, returnFilterTemplateData = False, returnIsAutoCreated = False, returnIsBase = False, returnIsCurrent = False, returnIsDefault = False, returnIsEnabled = False, returnModifiedTime = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(BrowseFilterID), verb = "get", return_params_list = return_params)

def modifyBrowseFilter(BrowseFilterID, EntityID = 1, setBrowseFilterID = None, setBrowseFilterIDClonedFrom = None, setBrowseID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setFilterID = None, setFilterTemplate = None, setFilterTemplateData = None, setIsAutoCreated = None, setIsBase = None, setIsCurrent = None, setIsDefault = None, setIsEnabled = None, setModifiedTime = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setType = None, setTypeCode = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFilterID = False, returnBrowseFilterIDClonedFrom = False, returnBrowseID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnFilterID = False, returnFilterTemplate = False, returnFilterTemplateData = False, returnIsAutoCreated = False, returnIsBase = False, returnIsCurrent = False, returnIsDefault = False, returnIsEnabled = False, returnModifiedTime = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(BrowseFilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseFilter(EntityID = 1, setBrowseFilterID = None, setBrowseFilterIDClonedFrom = None, setBrowseID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setFilterID = None, setFilterTemplate = None, setFilterTemplateData = None, setIsAutoCreated = None, setIsBase = None, setIsCurrent = None, setIsDefault = None, setIsEnabled = None, setModifiedTime = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setType = None, setTypeCode = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFilterID = False, returnBrowseFilterIDClonedFrom = False, returnBrowseID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnFilterID = False, returnFilterTemplate = False, returnFilterTemplateData = False, returnIsAutoCreated = False, returnIsBase = False, returnIsCurrent = False, returnIsDefault = False, returnIsEnabled = False, returnModifiedTime = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseFilter(BrowseFilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilter/" + str(BrowseFilterID), verb = "delete")


def getEveryBrowseFilterLastUsed(searchConditions = [], EntityID = 1, returnBrowseFilterLastUsedID = False, returnBrowseFilterID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseFilterLastUsed in the district.

    This function returns a dataframe of every BrowseFilterLastUsed in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseFilterLastUsed(BrowseFilterLastUsedID, EntityID = 1, returnBrowseFilterLastUsedID = False, returnBrowseFilterID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(BrowseFilterLastUsedID), verb = "get", return_params_list = return_params)

def modifyBrowseFilterLastUsed(BrowseFilterLastUsedID, EntityID = 1, setBrowseFilterLastUsedID = None, setBrowseFilterID = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFilterLastUsedID = False, returnBrowseFilterID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(BrowseFilterLastUsedID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseFilterLastUsed(EntityID = 1, setBrowseFilterLastUsedID = None, setBrowseFilterID = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseFilterLastUsedID = False, returnBrowseFilterID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseFilterLastUsed(BrowseFilterLastUsedID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseFilterLastUsed/" + str(BrowseFilterLastUsedID), verb = "delete")


def getEveryBrowseMenu(searchConditions = [], EntityID = 1, returnBrowseMenuID = False, returnAppendDataObjectNameToDisplayName = False, returnBrowseID = False, returnCondition = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayInBrowse = False, returnDisplayInDetails = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnEffectiveTarget = False, returnFilter = False, returnImage = False, returnImageCode = False, returnImageText = False, returnIncludeInRowMoreMenu = False, returnIsDefault = False, returnIsEnabled = False, returnIsRowMenu = False, returnIsSkywardBrowseMenu = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPostData = False, returnPrimaryKeyBindSource = False, returnRenderCondition = False, returnScreen = False, returnSkywardDescription = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardTarget = False, returnTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseMenu in the district.

    This function returns a dataframe of every BrowseMenu in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseMenu(BrowseMenuID, EntityID = 1, returnBrowseMenuID = False, returnAppendDataObjectNameToDisplayName = False, returnBrowseID = False, returnCondition = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayInBrowse = False, returnDisplayInDetails = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnEffectiveTarget = False, returnFilter = False, returnImage = False, returnImageCode = False, returnImageText = False, returnIncludeInRowMoreMenu = False, returnIsDefault = False, returnIsEnabled = False, returnIsRowMenu = False, returnIsSkywardBrowseMenu = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPostData = False, returnPrimaryKeyBindSource = False, returnRenderCondition = False, returnScreen = False, returnSkywardDescription = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardTarget = False, returnTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(BrowseMenuID), verb = "get", return_params_list = return_params)

def modifyBrowseMenu(BrowseMenuID, EntityID = 1, setBrowseMenuID = None, setAppendDataObjectNameToDisplayName = None, setBrowseID = None, setCondition = None, setCreatedTime = None, setData = None, setDescription = None, setDisplayInBrowse = None, setDisplayInDetails = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setEffectiveTarget = None, setFilter = None, setImage = None, setImageCode = None, setImageText = None, setIncludeInRowMoreMenu = None, setIsDefault = None, setIsEnabled = None, setIsRowMenu = None, setIsSkywardBrowseMenu = None, setModifiedTime = None, setModule = None, setObject = None, setPostData = None, setPrimaryKeyBindSource = None, setRenderCondition = None, setScreen = None, setSkywardDescription = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSkywardTarget = None, setTarget = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseMenuID = False, returnAppendDataObjectNameToDisplayName = False, returnBrowseID = False, returnCondition = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayInBrowse = False, returnDisplayInDetails = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnEffectiveTarget = False, returnFilter = False, returnImage = False, returnImageCode = False, returnImageText = False, returnIncludeInRowMoreMenu = False, returnIsDefault = False, returnIsEnabled = False, returnIsRowMenu = False, returnIsSkywardBrowseMenu = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPostData = False, returnPrimaryKeyBindSource = False, returnRenderCondition = False, returnScreen = False, returnSkywardDescription = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardTarget = False, returnTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(BrowseMenuID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseMenu(EntityID = 1, setBrowseMenuID = None, setAppendDataObjectNameToDisplayName = None, setBrowseID = None, setCondition = None, setCreatedTime = None, setData = None, setDescription = None, setDisplayInBrowse = None, setDisplayInDetails = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setEffectiveTarget = None, setFilter = None, setImage = None, setImageCode = None, setImageText = None, setIncludeInRowMoreMenu = None, setIsDefault = None, setIsEnabled = None, setIsRowMenu = None, setIsSkywardBrowseMenu = None, setModifiedTime = None, setModule = None, setObject = None, setPostData = None, setPrimaryKeyBindSource = None, setRenderCondition = None, setScreen = None, setSkywardDescription = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSkywardTarget = None, setTarget = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseMenuID = False, returnAppendDataObjectNameToDisplayName = False, returnBrowseID = False, returnCondition = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayInBrowse = False, returnDisplayInDetails = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnEffectiveTarget = False, returnFilter = False, returnImage = False, returnImageCode = False, returnImageText = False, returnIncludeInRowMoreMenu = False, returnIsDefault = False, returnIsEnabled = False, returnIsRowMenu = False, returnIsSkywardBrowseMenu = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPostData = False, returnPrimaryKeyBindSource = False, returnRenderCondition = False, returnScreen = False, returnSkywardDescription = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSkywardTarget = False, returnTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseMenu(BrowseMenuID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseMenu/" + str(BrowseMenuID), verb = "delete")


def getEveryBrowseView(searchConditions = [], EntityID = 1, returnBrowseViewID = False, returnBrowseID = False, returnBrowseType = False, returnBrowseViewIDClonedFrom = False, returnColumns = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnHasSelectAllCheckBox = False, returnIsDefault = False, returnIsEnabled = False, returnIsModifiedView = False, returnIsSkywardView = False, returnIsUserView = False, returnJsonData = False, returnModifiedTime = False, returnRowsPerPage = False, returnSearchColumns = False, returnShowFooter = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseView in the district.

    This function returns a dataframe of every BrowseView in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseView(BrowseViewID, EntityID = 1, returnBrowseViewID = False, returnBrowseID = False, returnBrowseType = False, returnBrowseViewIDClonedFrom = False, returnColumns = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnHasSelectAllCheckBox = False, returnIsDefault = False, returnIsEnabled = False, returnIsModifiedView = False, returnIsSkywardView = False, returnIsUserView = False, returnJsonData = False, returnModifiedTime = False, returnRowsPerPage = False, returnSearchColumns = False, returnShowFooter = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(BrowseViewID), verb = "get", return_params_list = return_params)

def modifyBrowseView(BrowseViewID, EntityID = 1, setBrowseViewID = None, setBrowseID = None, setBrowseType = None, setBrowseViewIDClonedFrom = None, setColumns = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setHasSelectAllCheckBox = None, setIsDefault = None, setIsEnabled = None, setIsModifiedView = None, setIsSkywardView = None, setIsUserView = None, setJsonData = None, setModifiedTime = None, setRowsPerPage = None, setSearchColumns = None, setShowFooter = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSorts = None, setType = None, setTypeCode = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseViewID = False, returnBrowseID = False, returnBrowseType = False, returnBrowseViewIDClonedFrom = False, returnColumns = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnHasSelectAllCheckBox = False, returnIsDefault = False, returnIsEnabled = False, returnIsModifiedView = False, returnIsSkywardView = False, returnIsUserView = False, returnJsonData = False, returnModifiedTime = False, returnRowsPerPage = False, returnSearchColumns = False, returnShowFooter = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(BrowseViewID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseView(EntityID = 1, setBrowseViewID = None, setBrowseID = None, setBrowseType = None, setBrowseViewIDClonedFrom = None, setColumns = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setEffectiveIsDefault = None, setHasSelectAllCheckBox = None, setIsDefault = None, setIsEnabled = None, setIsModifiedView = None, setIsSkywardView = None, setIsUserView = None, setJsonData = None, setModifiedTime = None, setRowsPerPage = None, setSearchColumns = None, setShowFooter = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setSorts = None, setType = None, setTypeCode = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseViewID = False, returnBrowseID = False, returnBrowseType = False, returnBrowseViewIDClonedFrom = False, returnColumns = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnEffectiveIsDefault = False, returnHasSelectAllCheckBox = False, returnIsDefault = False, returnIsEnabled = False, returnIsModifiedView = False, returnIsSkywardView = False, returnIsUserView = False, returnJsonData = False, returnModifiedTime = False, returnRowsPerPage = False, returnSearchColumns = False, returnShowFooter = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseView(BrowseViewID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseView/" + str(BrowseViewID), verb = "delete")


def getEveryBrowseViewLastUsed(searchConditions = [], EntityID = 1, returnBrowseViewLastUsedID = False, returnBrowseID = False, returnBrowseViewID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BrowseViewLastUsed in the district.

    This function returns a dataframe of every BrowseViewLastUsed in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBrowseViewLastUsed(BrowseViewLastUsedID, EntityID = 1, returnBrowseViewLastUsedID = False, returnBrowseID = False, returnBrowseViewID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(BrowseViewLastUsedID), verb = "get", return_params_list = return_params)

def modifyBrowseViewLastUsed(BrowseViewLastUsedID, EntityID = 1, setBrowseViewLastUsedID = None, setBrowseID = None, setBrowseViewID = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseViewLastUsedID = False, returnBrowseID = False, returnBrowseViewID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(BrowseViewLastUsedID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBrowseViewLastUsed(EntityID = 1, setBrowseViewLastUsedID = None, setBrowseID = None, setBrowseViewID = None, setCreatedTime = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBrowseViewLastUsedID = False, returnBrowseID = False, returnBrowseViewID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBrowseViewLastUsed(BrowseViewLastUsedID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BrowseViewLastUsed/" + str(BrowseViewLastUsedID), verb = "delete")


def getEveryBulkLoad(searchConditions = [], EntityID = 1, returnBulkLoadID = False, returnCreatedTime = False, returnMask = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BulkLoad in the district.

    This function returns a dataframe of every BulkLoad in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBulkLoad(BulkLoadID, EntityID = 1, returnBulkLoadID = False, returnCreatedTime = False, returnMask = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(BulkLoadID), verb = "get", return_params_list = return_params)

def modifyBulkLoad(BulkLoadID, EntityID = 1, setBulkLoadID = None, setCreatedTime = None, setMask = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBulkLoadID = False, returnCreatedTime = False, returnMask = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(BulkLoadID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBulkLoad(EntityID = 1, setBulkLoadID = None, setCreatedTime = None, setMask = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBulkLoadID = False, returnCreatedTime = False, returnMask = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBulkLoad(BulkLoadID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BulkLoad/" + str(BulkLoadID), verb = "delete")


def getEveryBusinessMigrationHistory(searchConditions = [], EntityID = 1, returnBusinessMigrationHistoryID = False, returnCreatedTime = False, returnFullClassName = False, returnHasRun = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BusinessMigrationHistory in the district.

    This function returns a dataframe of every BusinessMigrationHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBusinessMigrationHistory(BusinessMigrationHistoryID, EntityID = 1, returnBusinessMigrationHistoryID = False, returnCreatedTime = False, returnFullClassName = False, returnHasRun = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(BusinessMigrationHistoryID), verb = "get", return_params_list = return_params)

def modifyBusinessMigrationHistory(BusinessMigrationHistoryID, EntityID = 1, setBusinessMigrationHistoryID = None, setCreatedTime = None, setFullClassName = None, setHasRun = None, setModifiedTime = None, setOnlineInstall = None, setSkywardHash = None, setSkywardID = None, setSkywardVersion = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusinessMigrationHistoryID = False, returnCreatedTime = False, returnFullClassName = False, returnHasRun = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(BusinessMigrationHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBusinessMigrationHistory(EntityID = 1, setBusinessMigrationHistoryID = None, setCreatedTime = None, setFullClassName = None, setHasRun = None, setModifiedTime = None, setOnlineInstall = None, setSkywardHash = None, setSkywardID = None, setSkywardVersion = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusinessMigrationHistoryID = False, returnCreatedTime = False, returnFullClassName = False, returnHasRun = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBusinessMigrationHistory(BusinessMigrationHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/BusinessMigrationHistory/" + str(BusinessMigrationHistoryID), verb = "delete")


def getEveryCacheInitialization(searchConditions = [], EntityID = 1, returnCacheInitializationID = False, returnApplication = False, returnCacheName = False, returnCacheVersionCount = False, returnCreatedTime = False, returnHostName = False, returnInitializationTimeMilliseconds = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CacheInitialization in the district.

    This function returns a dataframe of every CacheInitialization in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCacheInitialization(CacheInitializationID, EntityID = 1, returnCacheInitializationID = False, returnApplication = False, returnCacheName = False, returnCacheVersionCount = False, returnCreatedTime = False, returnHostName = False, returnInitializationTimeMilliseconds = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(CacheInitializationID), verb = "get", return_params_list = return_params)

def modifyCacheInitialization(CacheInitializationID, EntityID = 1, setCacheInitializationID = None, setApplication = None, setCacheName = None, setCacheVersionCount = None, setCreatedTime = None, setHostName = None, setInitializationTimeMilliseconds = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCacheInitializationID = False, returnApplication = False, returnCacheName = False, returnCacheVersionCount = False, returnCreatedTime = False, returnHostName = False, returnInitializationTimeMilliseconds = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(CacheInitializationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCacheInitialization(EntityID = 1, setCacheInitializationID = None, setApplication = None, setCacheName = None, setCacheVersionCount = None, setCreatedTime = None, setHostName = None, setInitializationTimeMilliseconds = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCacheInitializationID = False, returnApplication = False, returnCacheName = False, returnCacheVersionCount = False, returnCreatedTime = False, returnHostName = False, returnInitializationTimeMilliseconds = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCacheInitialization(CacheInitializationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CacheInitialization/" + str(CacheInitializationID), verb = "delete")


def getEveryCharacterLimitGroup(searchConditions = [], EntityID = 1, returnCharacterLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMaxLength = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CharacterLimitGroup in the district.

    This function returns a dataframe of every CharacterLimitGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCharacterLimitGroup(CharacterLimitGroupID, EntityID = 1, returnCharacterLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMaxLength = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(CharacterLimitGroupID), verb = "get", return_params_list = return_params)

def modifyCharacterLimitGroup(CharacterLimitGroupID, EntityID = 1, setCharacterLimitGroupID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setMaxLength = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCharacterLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMaxLength = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(CharacterLimitGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCharacterLimitGroup(EntityID = 1, setCharacterLimitGroupID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setMaxLength = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCharacterLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMaxLength = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCharacterLimitGroup(CharacterLimitGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CharacterLimitGroup/" + str(CharacterLimitGroupID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnAllowMobileAccess = False, returnBrowseTimeoutEnabled = False, returnBrowseTimeoutSeconds = False, returnBrowseTimeoutSecondsMobile = False, returnCreatedTime = False, returnCurrencyIDBase = False, returnCustomRelationshipSync = False, returnCustomRelationshipSyncPollInterval = False, returnCustomViewSync = False, returnDaysToStoreAPIUsageHistory = False, returnDaysToStoreSystemLog = False, returnDaysToStoreUsageHistory = False, returnEnvironmentPurpose = False, returnEnvironmentPurposeBarColor = False, returnFileDestinationIDSkylertExport = False, returnFileDestinationIDThirdPartyExportImportLocation = False, returnLockDelayMinutes = False, returnLockMessage = False, returnLockoutText = False, returnLockTime = False, returnLogThreshold = False, returnLogThresholdCode = False, returnMaximumAttachmentSize = False, returnMediaIDLogo = False, returnModifiedTime = False, returnProductType = False, returnProductTypeCode = False, returnSecondsToLocked = False, returnSendingEmailAddress = False, returnSendingEmailAlias = False, returnSerialNumber = False, returnSMTPPassword = False, returnSMTPUsername = False, returnStateID = False, returnStatisticsExpiresTime = False, returnSystemTimeOffset = False, returnTimeZoneCode = False, returnTrainingTimeOffset = False, returnUseLicensing = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStatisticInfo = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnAllowMobileAccess = False, returnBrowseTimeoutEnabled = False, returnBrowseTimeoutSeconds = False, returnBrowseTimeoutSecondsMobile = False, returnCreatedTime = False, returnCurrencyIDBase = False, returnCustomRelationshipSync = False, returnCustomRelationshipSyncPollInterval = False, returnCustomViewSync = False, returnDaysToStoreAPIUsageHistory = False, returnDaysToStoreSystemLog = False, returnDaysToStoreUsageHistory = False, returnEnvironmentPurpose = False, returnEnvironmentPurposeBarColor = False, returnFileDestinationIDSkylertExport = False, returnFileDestinationIDThirdPartyExportImportLocation = False, returnLockDelayMinutes = False, returnLockMessage = False, returnLockoutText = False, returnLockTime = False, returnLogThreshold = False, returnLogThresholdCode = False, returnMaximumAttachmentSize = False, returnMediaIDLogo = False, returnModifiedTime = False, returnProductType = False, returnProductTypeCode = False, returnSecondsToLocked = False, returnSendingEmailAddress = False, returnSendingEmailAlias = False, returnSerialNumber = False, returnSMTPPassword = False, returnSMTPUsername = False, returnStateID = False, returnStatisticsExpiresTime = False, returnSystemTimeOffset = False, returnTimeZoneCode = False, returnTrainingTimeOffset = False, returnUseLicensing = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStatisticInfo = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setAllowMobileAccess = None, setBrowseTimeoutEnabled = None, setBrowseTimeoutSeconds = None, setBrowseTimeoutSecondsMobile = None, setCreatedTime = None, setCurrencyIDBase = None, setCustomRelationshipSync = None, setCustomRelationshipSyncPollInterval = None, setCustomViewSync = None, setDaysToStoreAPIUsageHistory = None, setDaysToStoreSystemLog = None, setDaysToStoreUsageHistory = None, setEnvironmentPurpose = None, setEnvironmentPurposeBarColor = None, setFileDestinationIDSkylertExport = None, setFileDestinationIDThirdPartyExportImportLocation = None, setLockDelayMinutes = None, setLockMessage = None, setLockoutText = None, setLockTime = None, setLogThreshold = None, setLogThresholdCode = None, setMaximumAttachmentSize = None, setMediaIDLogo = None, setModifiedTime = None, setProductType = None, setProductTypeCode = None, setSecondsToLocked = None, setSendingEmailAddress = None, setSendingEmailAlias = None, setSerialNumber = None, setSMTPPassword = None, setSMTPUsername = None, setStateID = None, setStatisticsExpiresTime = None, setSystemTimeOffset = None, setTimeZoneCode = None, setTrainingTimeOffset = None, setUseLicensing = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseStatisticInfo = None, returnConfigSystemID = False, returnAllowMobileAccess = False, returnBrowseTimeoutEnabled = False, returnBrowseTimeoutSeconds = False, returnBrowseTimeoutSecondsMobile = False, returnCreatedTime = False, returnCurrencyIDBase = False, returnCustomRelationshipSync = False, returnCustomRelationshipSyncPollInterval = False, returnCustomViewSync = False, returnDaysToStoreAPIUsageHistory = False, returnDaysToStoreSystemLog = False, returnDaysToStoreUsageHistory = False, returnEnvironmentPurpose = False, returnEnvironmentPurposeBarColor = False, returnFileDestinationIDSkylertExport = False, returnFileDestinationIDThirdPartyExportImportLocation = False, returnLockDelayMinutes = False, returnLockMessage = False, returnLockoutText = False, returnLockTime = False, returnLogThreshold = False, returnLogThresholdCode = False, returnMaximumAttachmentSize = False, returnMediaIDLogo = False, returnModifiedTime = False, returnProductType = False, returnProductTypeCode = False, returnSecondsToLocked = False, returnSendingEmailAddress = False, returnSendingEmailAlias = False, returnSerialNumber = False, returnSMTPPassword = False, returnSMTPUsername = False, returnStateID = False, returnStatisticsExpiresTime = False, returnSystemTimeOffset = False, returnTimeZoneCode = False, returnTrainingTimeOffset = False, returnUseLicensing = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStatisticInfo = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setAllowMobileAccess = None, setBrowseTimeoutEnabled = None, setBrowseTimeoutSeconds = None, setBrowseTimeoutSecondsMobile = None, setCreatedTime = None, setCurrencyIDBase = None, setCustomRelationshipSync = None, setCustomRelationshipSyncPollInterval = None, setCustomViewSync = None, setDaysToStoreAPIUsageHistory = None, setDaysToStoreSystemLog = None, setDaysToStoreUsageHistory = None, setEnvironmentPurpose = None, setEnvironmentPurposeBarColor = None, setFileDestinationIDSkylertExport = None, setFileDestinationIDThirdPartyExportImportLocation = None, setLockDelayMinutes = None, setLockMessage = None, setLockoutText = None, setLockTime = None, setLogThreshold = None, setLogThresholdCode = None, setMaximumAttachmentSize = None, setMediaIDLogo = None, setModifiedTime = None, setProductType = None, setProductTypeCode = None, setSecondsToLocked = None, setSendingEmailAddress = None, setSendingEmailAlias = None, setSerialNumber = None, setSMTPPassword = None, setSMTPUsername = None, setStateID = None, setStatisticsExpiresTime = None, setSystemTimeOffset = None, setTimeZoneCode = None, setTrainingTimeOffset = None, setUseLicensing = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseStatisticInfo = None, returnConfigSystemID = False, returnAllowMobileAccess = False, returnBrowseTimeoutEnabled = False, returnBrowseTimeoutSeconds = False, returnBrowseTimeoutSecondsMobile = False, returnCreatedTime = False, returnCurrencyIDBase = False, returnCustomRelationshipSync = False, returnCustomRelationshipSyncPollInterval = False, returnCustomViewSync = False, returnDaysToStoreAPIUsageHistory = False, returnDaysToStoreSystemLog = False, returnDaysToStoreUsageHistory = False, returnEnvironmentPurpose = False, returnEnvironmentPurposeBarColor = False, returnFileDestinationIDSkylertExport = False, returnFileDestinationIDThirdPartyExportImportLocation = False, returnLockDelayMinutes = False, returnLockMessage = False, returnLockoutText = False, returnLockTime = False, returnLogThreshold = False, returnLogThresholdCode = False, returnMaximumAttachmentSize = False, returnMediaIDLogo = False, returnModifiedTime = False, returnProductType = False, returnProductTypeCode = False, returnSecondsToLocked = False, returnSendingEmailAddress = False, returnSendingEmailAlias = False, returnSerialNumber = False, returnSMTPPassword = False, returnSMTPUsername = False, returnStateID = False, returnStatisticsExpiresTime = False, returnSystemTimeOffset = False, returnTimeZoneCode = False, returnTrainingTimeOffset = False, returnUseLicensing = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseStatisticInfo = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryCrossReference(searchConditions = [], EntityID = 1, returnCrossReferenceID = False, returnCreatedTime = False, returnFileValue = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CrossReference in the district.

    This function returns a dataframe of every CrossReference in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCrossReference(CrossReferenceID, EntityID = 1, returnCrossReferenceID = False, returnCreatedTime = False, returnFileValue = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(CrossReferenceID), verb = "get", return_params_list = return_params)

def modifyCrossReference(CrossReferenceID, EntityID = 1, setCrossReferenceID = None, setCreatedTime = None, setFileValue = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceID = None, returnCrossReferenceID = False, returnCreatedTime = False, returnFileValue = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(CrossReferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCrossReference(EntityID = 1, setCrossReferenceID = None, setCreatedTime = None, setFileValue = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceID = None, returnCrossReferenceID = False, returnCreatedTime = False, returnFileValue = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCrossReference(CrossReferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CrossReference/" + str(CrossReferenceID), verb = "delete")


def getEveryCustomScreen(searchConditions = [], EntityID = 1, returnCustomScreenID = False, returnCreatedTime = False, returnHasPendingChanges = False, returnIsProfileScreen = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPortal = False, returnPortalCode = False, returnProfileObjectName = False, returnScreenPath = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CustomScreen in the district.

    This function returns a dataframe of every CustomScreen in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCustomScreen(CustomScreenID, EntityID = 1, returnCustomScreenID = False, returnCreatedTime = False, returnHasPendingChanges = False, returnIsProfileScreen = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPortal = False, returnPortalCode = False, returnProfileObjectName = False, returnScreenPath = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(CustomScreenID), verb = "get", return_params_list = return_params)

def modifyCustomScreen(CustomScreenID, EntityID = 1, setCustomScreenID = None, setCreatedTime = None, setHasPendingChanges = None, setIsProfileScreen = None, setModifiedTime = None, setName = None, setObjectID = None, setPortal = None, setPortalCode = None, setProfileObjectName = None, setScreenPath = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomScreenID = False, returnCreatedTime = False, returnHasPendingChanges = False, returnIsProfileScreen = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPortal = False, returnPortalCode = False, returnProfileObjectName = False, returnScreenPath = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(CustomScreenID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCustomScreen(EntityID = 1, setCustomScreenID = None, setCreatedTime = None, setHasPendingChanges = None, setIsProfileScreen = None, setModifiedTime = None, setName = None, setObjectID = None, setPortal = None, setPortalCode = None, setProfileObjectName = None, setScreenPath = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomScreenID = False, returnCreatedTime = False, returnHasPendingChanges = False, returnIsProfileScreen = False, returnModifiedTime = False, returnName = False, returnObjectID = False, returnPortal = False, returnPortalCode = False, returnProfileObjectName = False, returnScreenPath = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCustomScreen(CustomScreenID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreen/" + str(CustomScreenID), verb = "delete")


def getEveryCustomScreenElement(searchConditions = [], EntityID = 1, returnCustomScreenElementID = False, returnCreatedTime = False, returnCustomScreenElementType = False, returnCustomScreenElementTypeDisplayText = False, returnCustomScreenID = False, returnData = False, returnDisplayOrder = False, returnDisplayType = False, returnGuidFieldPath = False, returnIsReadOnly = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CustomScreenElement in the district.

    This function returns a dataframe of every CustomScreenElement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCustomScreenElement(CustomScreenElementID, EntityID = 1, returnCustomScreenElementID = False, returnCreatedTime = False, returnCustomScreenElementType = False, returnCustomScreenElementTypeDisplayText = False, returnCustomScreenID = False, returnData = False, returnDisplayOrder = False, returnDisplayType = False, returnGuidFieldPath = False, returnIsReadOnly = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(CustomScreenElementID), verb = "get", return_params_list = return_params)

def modifyCustomScreenElement(CustomScreenElementID, EntityID = 1, setCustomScreenElementID = None, setCreatedTime = None, setCustomScreenElementType = None, setCustomScreenElementTypeDisplayText = None, setCustomScreenID = None, setData = None, setDisplayOrder = None, setDisplayType = None, setGuidFieldPath = None, setIsReadOnly = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomScreenElementID = False, returnCreatedTime = False, returnCustomScreenElementType = False, returnCustomScreenElementTypeDisplayText = False, returnCustomScreenID = False, returnData = False, returnDisplayOrder = False, returnDisplayType = False, returnGuidFieldPath = False, returnIsReadOnly = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(CustomScreenElementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCustomScreenElement(EntityID = 1, setCustomScreenElementID = None, setCreatedTime = None, setCustomScreenElementType = None, setCustomScreenElementTypeDisplayText = None, setCustomScreenID = None, setData = None, setDisplayOrder = None, setDisplayType = None, setGuidFieldPath = None, setIsReadOnly = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCustomScreenElementID = False, returnCreatedTime = False, returnCustomScreenElementType = False, returnCustomScreenElementTypeDisplayText = False, returnCustomScreenID = False, returnData = False, returnDisplayOrder = False, returnDisplayType = False, returnGuidFieldPath = False, returnIsReadOnly = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCustomScreenElement(CustomScreenElementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/CustomScreenElement/" + str(CustomScreenElementID), verb = "delete")


def getEveryDashboard(searchConditions = [], EntityID = 1, returnDashboardID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Dashboard in the district.

    This function returns a dataframe of every Dashboard in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDashboard(DashboardID, EntityID = 1, returnDashboardID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(DashboardID), verb = "get", return_params_list = return_params)

def modifyDashboard(DashboardID, EntityID = 1, setDashboardID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnDashboardID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(DashboardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDashboard(EntityID = 1, setDashboardID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnDashboardID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDashboard(DashboardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Dashboard/" + str(DashboardID), verb = "delete")


def getEveryDatabaseConnection(searchConditions = [], EntityID = 1, returnConnectionID = False, returnAuthScheme = False, returnClientNetAddress = False, returnClientTcpPort = False, returnConnectTime = False, returnLastRead = False, returnLastWrite = False, returnLocalNetAddress = False, returnLocalTcpPort = False, returnMostRecentSessionID = False, returnMostRecentSqlHandle = False, returnNetPacketSize = False, returnNetTransport = False, returnNumReads = False, returnNumWrites = False, returnParentConnectionID = False, returnProtocolType = False, returnSessionID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DatabaseConnection in the district.

    This function returns a dataframe of every DatabaseConnection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDatabaseConnection(ConnectionID, EntityID = 1, returnConnectionID = False, returnAuthScheme = False, returnClientNetAddress = False, returnClientTcpPort = False, returnConnectTime = False, returnLastRead = False, returnLastWrite = False, returnLocalNetAddress = False, returnLocalTcpPort = False, returnMostRecentSessionID = False, returnMostRecentSqlHandle = False, returnNetPacketSize = False, returnNetTransport = False, returnNumReads = False, returnNumWrites = False, returnParentConnectionID = False, returnProtocolType = False, returnSessionID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(ConnectionID), verb = "get", return_params_list = return_params)

def modifyDatabaseConnection(ConnectionID, EntityID = 1, setConnectionID = None, setAuthScheme = None, setClientNetAddress = None, setClientTcpPort = None, setConnectTime = None, setLastRead = None, setLastWrite = None, setLocalNetAddress = None, setLocalTcpPort = None, setMostRecentSessionID = None, setMostRecentSqlHandle = None, setNetPacketSize = None, setNetTransport = None, setNumReads = None, setNumWrites = None, setParentConnectionID = None, setProtocolType = None, setSessionID = None, returnConnectionID = False, returnAuthScheme = False, returnClientNetAddress = False, returnClientTcpPort = False, returnConnectTime = False, returnLastRead = False, returnLastWrite = False, returnLocalNetAddress = False, returnLocalTcpPort = False, returnMostRecentSessionID = False, returnMostRecentSqlHandle = False, returnNetPacketSize = False, returnNetTransport = False, returnNumReads = False, returnNumWrites = False, returnParentConnectionID = False, returnProtocolType = False, returnSessionID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(ConnectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDatabaseConnection(EntityID = 1, setConnectionID = None, setAuthScheme = None, setClientNetAddress = None, setClientTcpPort = None, setConnectTime = None, setLastRead = None, setLastWrite = None, setLocalNetAddress = None, setLocalTcpPort = None, setMostRecentSessionID = None, setMostRecentSqlHandle = None, setNetPacketSize = None, setNetTransport = None, setNumReads = None, setNumWrites = None, setParentConnectionID = None, setProtocolType = None, setSessionID = None, returnConnectionID = False, returnAuthScheme = False, returnClientNetAddress = False, returnClientTcpPort = False, returnConnectTime = False, returnLastRead = False, returnLastWrite = False, returnLocalNetAddress = False, returnLocalTcpPort = False, returnMostRecentSessionID = False, returnMostRecentSqlHandle = False, returnNetPacketSize = False, returnNetTransport = False, returnNumReads = False, returnNumWrites = False, returnParentConnectionID = False, returnProtocolType = False, returnSessionID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDatabaseConnection(ConnectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseConnection/" + str(ConnectionID), verb = "delete")


def getEveryDatabaseRequest(searchConditions = [], EntityID = 1, returnSessionID = False, returnApplicationName = False, returnBlockedBySessionID = False, returnCommand = False, returnCPUTime = False, returnDatabase = False, returnDegreesOfParallelism = False, returnElapsedTime = False, returnEstimatedComplete = False, returnExecutingStatement = False, returnFullQuery = False, returnGrantedMemory = False, returnHostname = False, returnIdealMemory = False, returnLastWaitType = False, returnOpenResultSets = False, returnOpenTransactions = False, returnPercentComplete = False, returnQueryCost = False, returnReads = False, returnRequestID = False, returnRequiredMemory = False, returnTimeoutSeconds = False, returnUsedMemory = False, returnUser = False, returnWaitTime = False, returnWaitType = False, returnWrites = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DatabaseRequest in the district.

    This function returns a dataframe of every DatabaseRequest in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDatabaseRequest(SessionID, EntityID = 1, returnSessionID = False, returnApplicationName = False, returnBlockedBySessionID = False, returnCommand = False, returnCPUTime = False, returnDatabase = False, returnDegreesOfParallelism = False, returnElapsedTime = False, returnEstimatedComplete = False, returnExecutingStatement = False, returnFullQuery = False, returnGrantedMemory = False, returnHostname = False, returnIdealMemory = False, returnLastWaitType = False, returnOpenResultSets = False, returnOpenTransactions = False, returnPercentComplete = False, returnQueryCost = False, returnReads = False, returnRequestID = False, returnRequiredMemory = False, returnTimeoutSeconds = False, returnUsedMemory = False, returnUser = False, returnWaitTime = False, returnWaitType = False, returnWrites = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(SessionID), verb = "get", return_params_list = return_params)

def modifyDatabaseRequest(SessionID, EntityID = 1, setSessionID = None, setApplicationName = None, setBlockedBySessionID = None, setCommand = None, setCPUTime = None, setDatabase = None, setDegreesOfParallelism = None, setElapsedTime = None, setEstimatedComplete = None, setExecutingStatement = None, setFullQuery = None, setGrantedMemory = None, setHostname = None, setIdealMemory = None, setLastWaitType = None, setOpenResultSets = None, setOpenTransactions = None, setPercentComplete = None, setQueryCost = None, setReads = None, setRequestID = None, setRequiredMemory = None, setTimeoutSeconds = None, setUsedMemory = None, setUser = None, setWaitTime = None, setWaitType = None, setWrites = None, returnSessionID = False, returnApplicationName = False, returnBlockedBySessionID = False, returnCommand = False, returnCPUTime = False, returnDatabase = False, returnDegreesOfParallelism = False, returnElapsedTime = False, returnEstimatedComplete = False, returnExecutingStatement = False, returnFullQuery = False, returnGrantedMemory = False, returnHostname = False, returnIdealMemory = False, returnLastWaitType = False, returnOpenResultSets = False, returnOpenTransactions = False, returnPercentComplete = False, returnQueryCost = False, returnReads = False, returnRequestID = False, returnRequiredMemory = False, returnTimeoutSeconds = False, returnUsedMemory = False, returnUser = False, returnWaitTime = False, returnWaitType = False, returnWrites = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(SessionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDatabaseRequest(EntityID = 1, setSessionID = None, setApplicationName = None, setBlockedBySessionID = None, setCommand = None, setCPUTime = None, setDatabase = None, setDegreesOfParallelism = None, setElapsedTime = None, setEstimatedComplete = None, setExecutingStatement = None, setFullQuery = None, setGrantedMemory = None, setHostname = None, setIdealMemory = None, setLastWaitType = None, setOpenResultSets = None, setOpenTransactions = None, setPercentComplete = None, setQueryCost = None, setReads = None, setRequestID = None, setRequiredMemory = None, setTimeoutSeconds = None, setUsedMemory = None, setUser = None, setWaitTime = None, setWaitType = None, setWrites = None, returnSessionID = False, returnApplicationName = False, returnBlockedBySessionID = False, returnCommand = False, returnCPUTime = False, returnDatabase = False, returnDegreesOfParallelism = False, returnElapsedTime = False, returnEstimatedComplete = False, returnExecutingStatement = False, returnFullQuery = False, returnGrantedMemory = False, returnHostname = False, returnIdealMemory = False, returnLastWaitType = False, returnOpenResultSets = False, returnOpenTransactions = False, returnPercentComplete = False, returnQueryCost = False, returnReads = False, returnRequestID = False, returnRequiredMemory = False, returnTimeoutSeconds = False, returnUsedMemory = False, returnUser = False, returnWaitTime = False, returnWaitType = False, returnWrites = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDatabaseRequest(SessionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseRequest/" + str(SessionID), verb = "delete")


def getEveryDatabaseSession(searchConditions = [], EntityID = 1, returnSessionID = False, returnAuthenticatingDatabaseID = False, returnClientInterfaceName = False, returnClientVersion = False, returnCpuTime = False, returnDatabaseID = False, returnHostName = False, returnHostProcessID = False, returnIsUserProcess = False, returnLastRequestEndTime = False, returnLastRequestStartTime = False, returnLastSuccessfullLogon = False, returnLastUnsuccessfullLogon = False, returnLogicalReads = False, returnLoginName = False, returnLoginTime = False, returnMemoryUsage = False, returnNtDomain = False, returnNtUserName = False, returnOpenTransactionCount = False, returnOriginalLoginName = False, returnPrevError = False, returnProgramName = False, returnReads = False, returnRowCount = False, returnStatus = False, returnTotalElapsedTime = False, returnTotalScheduledTime = False, returnTransactionIsolationLevel = False, returnUnsuccessfulLogons = False, returnWrites = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DatabaseSession in the district.

    This function returns a dataframe of every DatabaseSession in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDatabaseSession(SessionID, EntityID = 1, returnSessionID = False, returnAuthenticatingDatabaseID = False, returnClientInterfaceName = False, returnClientVersion = False, returnCpuTime = False, returnDatabaseID = False, returnHostName = False, returnHostProcessID = False, returnIsUserProcess = False, returnLastRequestEndTime = False, returnLastRequestStartTime = False, returnLastSuccessfullLogon = False, returnLastUnsuccessfullLogon = False, returnLogicalReads = False, returnLoginName = False, returnLoginTime = False, returnMemoryUsage = False, returnNtDomain = False, returnNtUserName = False, returnOpenTransactionCount = False, returnOriginalLoginName = False, returnPrevError = False, returnProgramName = False, returnReads = False, returnRowCount = False, returnStatus = False, returnTotalElapsedTime = False, returnTotalScheduledTime = False, returnTransactionIsolationLevel = False, returnUnsuccessfulLogons = False, returnWrites = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(SessionID), verb = "get", return_params_list = return_params)

def modifyDatabaseSession(SessionID, EntityID = 1, setSessionID = None, setAuthenticatingDatabaseID = None, setClientInterfaceName = None, setClientVersion = None, setCpuTime = None, setDatabaseID = None, setHostName = None, setHostProcessID = None, setIsUserProcess = None, setLastRequestEndTime = None, setLastRequestStartTime = None, setLastSuccessfullLogon = None, setLastUnsuccessfullLogon = None, setLogicalReads = None, setLoginName = None, setLoginTime = None, setMemoryUsage = None, setNtDomain = None, setNtUserName = None, setOpenTransactionCount = None, setOriginalLoginName = None, setPrevError = None, setProgramName = None, setReads = None, setRowCount = None, setStatus = None, setTotalElapsedTime = None, setTotalScheduledTime = None, setTransactionIsolationLevel = None, setUnsuccessfulLogons = None, setWrites = None, returnSessionID = False, returnAuthenticatingDatabaseID = False, returnClientInterfaceName = False, returnClientVersion = False, returnCpuTime = False, returnDatabaseID = False, returnHostName = False, returnHostProcessID = False, returnIsUserProcess = False, returnLastRequestEndTime = False, returnLastRequestStartTime = False, returnLastSuccessfullLogon = False, returnLastUnsuccessfullLogon = False, returnLogicalReads = False, returnLoginName = False, returnLoginTime = False, returnMemoryUsage = False, returnNtDomain = False, returnNtUserName = False, returnOpenTransactionCount = False, returnOriginalLoginName = False, returnPrevError = False, returnProgramName = False, returnReads = False, returnRowCount = False, returnStatus = False, returnTotalElapsedTime = False, returnTotalScheduledTime = False, returnTransactionIsolationLevel = False, returnUnsuccessfulLogons = False, returnWrites = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(SessionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDatabaseSession(EntityID = 1, setSessionID = None, setAuthenticatingDatabaseID = None, setClientInterfaceName = None, setClientVersion = None, setCpuTime = None, setDatabaseID = None, setHostName = None, setHostProcessID = None, setIsUserProcess = None, setLastRequestEndTime = None, setLastRequestStartTime = None, setLastSuccessfullLogon = None, setLastUnsuccessfullLogon = None, setLogicalReads = None, setLoginName = None, setLoginTime = None, setMemoryUsage = None, setNtDomain = None, setNtUserName = None, setOpenTransactionCount = None, setOriginalLoginName = None, setPrevError = None, setProgramName = None, setReads = None, setRowCount = None, setStatus = None, setTotalElapsedTime = None, setTotalScheduledTime = None, setTransactionIsolationLevel = None, setUnsuccessfulLogons = None, setWrites = None, returnSessionID = False, returnAuthenticatingDatabaseID = False, returnClientInterfaceName = False, returnClientVersion = False, returnCpuTime = False, returnDatabaseID = False, returnHostName = False, returnHostProcessID = False, returnIsUserProcess = False, returnLastRequestEndTime = False, returnLastRequestStartTime = False, returnLastSuccessfullLogon = False, returnLastUnsuccessfullLogon = False, returnLogicalReads = False, returnLoginName = False, returnLoginTime = False, returnMemoryUsage = False, returnNtDomain = False, returnNtUserName = False, returnOpenTransactionCount = False, returnOriginalLoginName = False, returnPrevError = False, returnProgramName = False, returnReads = False, returnRowCount = False, returnStatus = False, returnTotalElapsedTime = False, returnTotalScheduledTime = False, returnTransactionIsolationLevel = False, returnUnsuccessfulLogons = False, returnWrites = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDatabaseSession(SessionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseSession/" + str(SessionID), verb = "delete")


def getEveryDatabaseTransaction(searchConditions = [], EntityID = 1, returnTransactionID = False, returnName = False, returnTransactionBeginTime = False, returnTransactionState = False, returnTransactionType = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DatabaseTransaction in the district.

    This function returns a dataframe of every DatabaseTransaction in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDatabaseTransaction(TransactionID, EntityID = 1, returnTransactionID = False, returnName = False, returnTransactionBeginTime = False, returnTransactionState = False, returnTransactionType = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(TransactionID), verb = "get", return_params_list = return_params)

def modifyDatabaseTransaction(TransactionID, EntityID = 1, setTransactionID = None, setName = None, setTransactionBeginTime = None, setTransactionState = None, setTransactionType = None, returnTransactionID = False, returnName = False, returnTransactionBeginTime = False, returnTransactionState = False, returnTransactionType = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(TransactionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDatabaseTransaction(EntityID = 1, setTransactionID = None, setName = None, setTransactionBeginTime = None, setTransactionState = None, setTransactionType = None, returnTransactionID = False, returnName = False, returnTransactionBeginTime = False, returnTransactionState = False, returnTransactionType = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDatabaseTransaction(TransactionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DatabaseTransaction/" + str(TransactionID), verb = "delete")


def getEveryDataMigrationHistory(searchConditions = [], EntityID = 1, returnDataMigrationHistoryID = False, returnCreatedTime = False, returnMigrationNumber = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkipped = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DataMigrationHistory in the district.

    This function returns a dataframe of every DataMigrationHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDataMigrationHistory(DataMigrationHistoryID, EntityID = 1, returnDataMigrationHistoryID = False, returnCreatedTime = False, returnMigrationNumber = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkipped = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(DataMigrationHistoryID), verb = "get", return_params_list = return_params)

def modifyDataMigrationHistory(DataMigrationHistoryID, EntityID = 1, setDataMigrationHistoryID = None, setCreatedTime = None, setMigrationNumber = None, setModifiedTime = None, setOnlineInstall = None, setSkipped = None, setSkywardVersion = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMigrationHistoryID = False, returnCreatedTime = False, returnMigrationNumber = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkipped = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(DataMigrationHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDataMigrationHistory(EntityID = 1, setDataMigrationHistoryID = None, setCreatedTime = None, setMigrationNumber = None, setModifiedTime = None, setOnlineInstall = None, setSkipped = None, setSkywardVersion = None, setSummary = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDataMigrationHistoryID = False, returnCreatedTime = False, returnMigrationNumber = False, returnModifiedTime = False, returnOnlineInstall = False, returnSkipped = False, returnSkywardVersion = False, returnSummary = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDataMigrationHistory(DataMigrationHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/DataMigrationHistory/" + str(DataMigrationHistoryID), verb = "delete")


def getEveryEmail(searchConditions = [], EntityID = 1, returnEmailID = False, returnBody = False, returnCarbonCopy = False, returnCreatedTime = False, returnEndTime = False, returnHostname = False, returnHTMLBody = False, returnMessageID = False, returnModifiedTime = False, returnPriority = False, returnPriorityCode = False, returnProcessID = False, returnRecipient = False, returnSendingAddress = False, returnSendingAlias = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Email in the district.

    This function returns a dataframe of every Email in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEmail(EmailID, EntityID = 1, returnEmailID = False, returnBody = False, returnCarbonCopy = False, returnCreatedTime = False, returnEndTime = False, returnHostname = False, returnHTMLBody = False, returnMessageID = False, returnModifiedTime = False, returnPriority = False, returnPriorityCode = False, returnProcessID = False, returnRecipient = False, returnSendingAddress = False, returnSendingAlias = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(EmailID), verb = "get", return_params_list = return_params)

def modifyEmail(EmailID, EntityID = 1, setEmailID = None, setBody = None, setCarbonCopy = None, setCreatedTime = None, setEndTime = None, setHostname = None, setHTMLBody = None, setMessageID = None, setModifiedTime = None, setPriority = None, setPriorityCode = None, setProcessID = None, setRecipient = None, setSendingAddress = None, setSendingAlias = None, setStartTime = None, setStatus = None, setStatusCode = None, setSubject = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnEmailID = False, returnBody = False, returnCarbonCopy = False, returnCreatedTime = False, returnEndTime = False, returnHostname = False, returnHTMLBody = False, returnMessageID = False, returnModifiedTime = False, returnPriority = False, returnPriorityCode = False, returnProcessID = False, returnRecipient = False, returnSendingAddress = False, returnSendingAlias = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(EmailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEmail(EntityID = 1, setEmailID = None, setBody = None, setCarbonCopy = None, setCreatedTime = None, setEndTime = None, setHostname = None, setHTMLBody = None, setMessageID = None, setModifiedTime = None, setPriority = None, setPriorityCode = None, setProcessID = None, setRecipient = None, setSendingAddress = None, setSendingAlias = None, setStartTime = None, setStatus = None, setStatusCode = None, setSubject = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnEmailID = False, returnBody = False, returnCarbonCopy = False, returnCreatedTime = False, returnEndTime = False, returnHostname = False, returnHTMLBody = False, returnMessageID = False, returnModifiedTime = False, returnPriority = False, returnPriorityCode = False, returnProcessID = False, returnRecipient = False, returnSendingAddress = False, returnSendingAlias = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnSubject = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEmail(EmailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Email/" + str(EmailID), verb = "delete")


def getEveryEmailAttachment(searchConditions = [], EntityID = 1, returnEmailAttachmentID = False, returnCreatedTime = False, returnEmailID = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EmailAttachment in the district.

    This function returns a dataframe of every EmailAttachment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEmailAttachment(EmailAttachmentID, EntityID = 1, returnEmailAttachmentID = False, returnCreatedTime = False, returnEmailID = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(EmailAttachmentID), verb = "get", return_params_list = return_params)

def modifyEmailAttachment(EmailAttachmentID, EntityID = 1, setEmailAttachmentID = None, setCreatedTime = None, setEmailID = None, setMediaID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmailAttachmentID = False, returnCreatedTime = False, returnEmailID = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(EmailAttachmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEmailAttachment(EntityID = 1, setEmailAttachmentID = None, setCreatedTime = None, setEmailID = None, setMediaID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmailAttachmentID = False, returnCreatedTime = False, returnEmailID = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEmailAttachment(EmailAttachmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/EmailAttachment/" + str(EmailAttachmentID), verb = "delete")


def getEveryExternalLink(searchConditions = [], EntityID = 1, returnExternalLinkID = False, returnCreatedTime = False, returnDescription = False, returnDisplayInAdministrativeAccess = False, returnDisplayInEmployeeAccess = False, returnDisplayInFamilyAccess = False, returnDisplayInNewStudentEnrollment = False, returnDisplayInStudentAccess = False, returnDisplayInStudentServicesAccess = False, returnDisplayInTeacherAccess = False, returnDistrictID = False, returnIcon = False, returnIconCode = False, returnLinkText = False, returnModifiedTime = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ExternalLink in the district.

    This function returns a dataframe of every ExternalLink in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getExternalLink(ExternalLinkID, EntityID = 1, returnExternalLinkID = False, returnCreatedTime = False, returnDescription = False, returnDisplayInAdministrativeAccess = False, returnDisplayInEmployeeAccess = False, returnDisplayInFamilyAccess = False, returnDisplayInNewStudentEnrollment = False, returnDisplayInStudentAccess = False, returnDisplayInStudentServicesAccess = False, returnDisplayInTeacherAccess = False, returnDistrictID = False, returnIcon = False, returnIconCode = False, returnLinkText = False, returnModifiedTime = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(ExternalLinkID), verb = "get", return_params_list = return_params)

def modifyExternalLink(ExternalLinkID, EntityID = 1, setExternalLinkID = None, setCreatedTime = None, setDescription = None, setDisplayInAdministrativeAccess = None, setDisplayInEmployeeAccess = None, setDisplayInFamilyAccess = None, setDisplayInNewStudentEnrollment = None, setDisplayInStudentAccess = None, setDisplayInStudentServicesAccess = None, setDisplayInTeacherAccess = None, setDistrictID = None, setIcon = None, setIconCode = None, setLinkText = None, setModifiedTime = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnExternalLinkID = False, returnCreatedTime = False, returnDescription = False, returnDisplayInAdministrativeAccess = False, returnDisplayInEmployeeAccess = False, returnDisplayInFamilyAccess = False, returnDisplayInNewStudentEnrollment = False, returnDisplayInStudentAccess = False, returnDisplayInStudentServicesAccess = False, returnDisplayInTeacherAccess = False, returnDistrictID = False, returnIcon = False, returnIconCode = False, returnLinkText = False, returnModifiedTime = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(ExternalLinkID), verb = "post", return_params_list = return_params, payload = payload_params)

def createExternalLink(EntityID = 1, setExternalLinkID = None, setCreatedTime = None, setDescription = None, setDisplayInAdministrativeAccess = None, setDisplayInEmployeeAccess = None, setDisplayInFamilyAccess = None, setDisplayInNewStudentEnrollment = None, setDisplayInStudentAccess = None, setDisplayInStudentServicesAccess = None, setDisplayInTeacherAccess = None, setDistrictID = None, setIcon = None, setIconCode = None, setLinkText = None, setModifiedTime = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnExternalLinkID = False, returnCreatedTime = False, returnDescription = False, returnDisplayInAdministrativeAccess = False, returnDisplayInEmployeeAccess = False, returnDisplayInFamilyAccess = False, returnDisplayInNewStudentEnrollment = False, returnDisplayInStudentAccess = False, returnDisplayInStudentServicesAccess = False, returnDisplayInTeacherAccess = False, returnDistrictID = False, returnIcon = False, returnIconCode = False, returnLinkText = False, returnModifiedTime = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteExternalLink(ExternalLinkID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLink/" + str(ExternalLinkID), verb = "delete")


def getEveryExternalLinkEntity(searchConditions = [], EntityID = 1, returnExternalLinkEntityID = False, returnCreatedTime = False, returnEntityID = False, returnExternalLinkID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ExternalLinkEntity in the district.

    This function returns a dataframe of every ExternalLinkEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getExternalLinkEntity(ExternalLinkEntityID, EntityID = 1, returnExternalLinkEntityID = False, returnCreatedTime = False, returnEntityID = False, returnExternalLinkID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(ExternalLinkEntityID), verb = "get", return_params_list = return_params)

def modifyExternalLinkEntity(ExternalLinkEntityID, EntityID = 1, setExternalLinkEntityID = None, setCreatedTime = None, setEntityID = None, setExternalLinkID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnExternalLinkEntityID = False, returnCreatedTime = False, returnEntityID = False, returnExternalLinkID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(ExternalLinkEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createExternalLinkEntity(EntityID = 1, setExternalLinkEntityID = None, setCreatedTime = None, setEntityID = None, setExternalLinkID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnExternalLinkEntityID = False, returnCreatedTime = False, returnEntityID = False, returnExternalLinkID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteExternalLinkEntity(ExternalLinkEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ExternalLinkEntity/" + str(ExternalLinkEntityID), verb = "delete")


def getEveryFeedback(searchConditions = [], EntityID = 1, returnFeedbackID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnSubScreen = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Feedback in the district.

    This function returns a dataframe of every Feedback in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFeedback(FeedbackID, EntityID = 1, returnFeedbackID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnSubScreen = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(FeedbackID), verb = "get", return_params_list = return_params)

def modifyFeedback(FeedbackID, EntityID = 1, setFeedbackID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setSubScreen = None, setSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFeedbackID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnSubScreen = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(FeedbackID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFeedback(EntityID = 1, setFeedbackID = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setSubScreen = None, setSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFeedbackID = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnSubScreen = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFeedback(FeedbackID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Feedback/" + str(FeedbackID), verb = "delete")


def getEveryField(searchConditions = [], EntityID = 1, returnFieldID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentFieldWidth = False, returnCurrentIsRequired = False, returnCurrentName = False, returnCurrentPrecision = False, returnCurrentRelationshipOrFieldName = False, returnCurrentScale = False, returnCurrentSize = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFormattedFieldPath = False, returnHasChangedRelationships = False, returnIsDeniable = False, returnIsForeignKeyOfRelationship = False, returnIsInDB = False, returnIsPrimaryKey = False, returnIsSkywardField = False, returnModifiedTime = False, returnObjectID = False, returnPendingDisplayName = False, returnPendingFieldWidth = False, returnPendingIsRequired = False, returnPendingName = False, returnPendingPrecision = False, returnPendingRelationshipOrFieldName = False, returnPendingScale = False, returnPendingSize = False, returnPendingType = False, returnPendingTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUniqueIDString = False, returnUserCanEdit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceDataTypeCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Field in the district.

    This function returns a dataframe of every Field in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getField(FieldID, EntityID = 1, returnFieldID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentFieldWidth = False, returnCurrentIsRequired = False, returnCurrentName = False, returnCurrentPrecision = False, returnCurrentRelationshipOrFieldName = False, returnCurrentScale = False, returnCurrentSize = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFormattedFieldPath = False, returnHasChangedRelationships = False, returnIsDeniable = False, returnIsForeignKeyOfRelationship = False, returnIsInDB = False, returnIsPrimaryKey = False, returnIsSkywardField = False, returnModifiedTime = False, returnObjectID = False, returnPendingDisplayName = False, returnPendingFieldWidth = False, returnPendingIsRequired = False, returnPendingName = False, returnPendingPrecision = False, returnPendingRelationshipOrFieldName = False, returnPendingScale = False, returnPendingSize = False, returnPendingType = False, returnPendingTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUniqueIDString = False, returnUserCanEdit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceDataTypeCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(FieldID), verb = "get", return_params_list = return_params)

def modifyField(FieldID, EntityID = 1, setFieldID = None, setChangeType = None, setCreatedTime = None, setCurrentDisplayName = None, setCurrentFieldWidth = None, setCurrentIsRequired = None, setCurrentName = None, setCurrentPrecision = None, setCurrentRelationshipOrFieldName = None, setCurrentScale = None, setCurrentSize = None, setCurrentType = None, setCurrentTypeCode = None, setCustomizationID = None, setFormattedFieldPath = None, setHasChangedRelationships = None, setIsDeniable = None, setIsForeignKeyOfRelationship = None, setIsInDB = None, setIsPrimaryKey = None, setIsSkywardField = None, setModifiedTime = None, setObjectID = None, setPendingDisplayName = None, setPendingFieldWidth = None, setPendingIsRequired = None, setPendingName = None, setPendingPrecision = None, setPendingRelationshipOrFieldName = None, setPendingScale = None, setPendingSize = None, setPendingType = None, setPendingTypeCode = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUniqueIDString = None, setUserCanEdit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceDataTypeCode = None, returnFieldID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentFieldWidth = False, returnCurrentIsRequired = False, returnCurrentName = False, returnCurrentPrecision = False, returnCurrentRelationshipOrFieldName = False, returnCurrentScale = False, returnCurrentSize = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFormattedFieldPath = False, returnHasChangedRelationships = False, returnIsDeniable = False, returnIsForeignKeyOfRelationship = False, returnIsInDB = False, returnIsPrimaryKey = False, returnIsSkywardField = False, returnModifiedTime = False, returnObjectID = False, returnPendingDisplayName = False, returnPendingFieldWidth = False, returnPendingIsRequired = False, returnPendingName = False, returnPendingPrecision = False, returnPendingRelationshipOrFieldName = False, returnPendingScale = False, returnPendingSize = False, returnPendingType = False, returnPendingTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUniqueIDString = False, returnUserCanEdit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceDataTypeCode = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(FieldID), verb = "post", return_params_list = return_params, payload = payload_params)

def createField(EntityID = 1, setFieldID = None, setChangeType = None, setCreatedTime = None, setCurrentDisplayName = None, setCurrentFieldWidth = None, setCurrentIsRequired = None, setCurrentName = None, setCurrentPrecision = None, setCurrentRelationshipOrFieldName = None, setCurrentScale = None, setCurrentSize = None, setCurrentType = None, setCurrentTypeCode = None, setCustomizationID = None, setFormattedFieldPath = None, setHasChangedRelationships = None, setIsDeniable = None, setIsForeignKeyOfRelationship = None, setIsInDB = None, setIsPrimaryKey = None, setIsSkywardField = None, setModifiedTime = None, setObjectID = None, setPendingDisplayName = None, setPendingFieldWidth = None, setPendingIsRequired = None, setPendingName = None, setPendingPrecision = None, setPendingRelationshipOrFieldName = None, setPendingScale = None, setPendingSize = None, setPendingType = None, setPendingTypeCode = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUniqueIDString = None, setUserCanEdit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceDataTypeCode = None, returnFieldID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentFieldWidth = False, returnCurrentIsRequired = False, returnCurrentName = False, returnCurrentPrecision = False, returnCurrentRelationshipOrFieldName = False, returnCurrentScale = False, returnCurrentSize = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFormattedFieldPath = False, returnHasChangedRelationships = False, returnIsDeniable = False, returnIsForeignKeyOfRelationship = False, returnIsInDB = False, returnIsPrimaryKey = False, returnIsSkywardField = False, returnModifiedTime = False, returnObjectID = False, returnPendingDisplayName = False, returnPendingFieldWidth = False, returnPendingIsRequired = False, returnPendingName = False, returnPendingPrecision = False, returnPendingRelationshipOrFieldName = False, returnPendingScale = False, returnPendingSize = False, returnPendingType = False, returnPendingTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUniqueIDString = False, returnUserCanEdit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceDataTypeCode = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteField(FieldID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Field/" + str(FieldID), verb = "delete")


def getEveryFieldMapping(searchConditions = [], EntityID = 1, returnFieldMappingID = False, returnActionIfSourceValueIsBlank = False, returnActionIfSourceValueIsBlankCode = False, returnCreatedTime = False, returnFieldID = False, returnImportDataObjectSourceID = False, returnImportDataObjectSourceIDMappedValue = False, returnMappingType = False, returnMappingTypeCode = False, returnModifiedTime = False, returnSourceDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FieldMapping in the district.

    This function returns a dataframe of every FieldMapping in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFieldMapping(FieldMappingID, EntityID = 1, returnFieldMappingID = False, returnActionIfSourceValueIsBlank = False, returnActionIfSourceValueIsBlankCode = False, returnCreatedTime = False, returnFieldID = False, returnImportDataObjectSourceID = False, returnImportDataObjectSourceIDMappedValue = False, returnMappingType = False, returnMappingTypeCode = False, returnModifiedTime = False, returnSourceDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(FieldMappingID), verb = "get", return_params_list = return_params)

def modifyFieldMapping(FieldMappingID, EntityID = 1, setFieldMappingID = None, setActionIfSourceValueIsBlank = None, setActionIfSourceValueIsBlankCode = None, setCreatedTime = None, setFieldID = None, setImportDataObjectSourceID = None, setImportDataObjectSourceIDMappedValue = None, setMappingType = None, setMappingTypeCode = None, setModifiedTime = None, setSourceDisplayName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceID = None, returnFieldMappingID = False, returnActionIfSourceValueIsBlank = False, returnActionIfSourceValueIsBlankCode = False, returnCreatedTime = False, returnFieldID = False, returnImportDataObjectSourceID = False, returnImportDataObjectSourceIDMappedValue = False, returnMappingType = False, returnMappingTypeCode = False, returnModifiedTime = False, returnSourceDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(FieldMappingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFieldMapping(EntityID = 1, setFieldMappingID = None, setActionIfSourceValueIsBlank = None, setActionIfSourceValueIsBlankCode = None, setCreatedTime = None, setFieldID = None, setImportDataObjectSourceID = None, setImportDataObjectSourceIDMappedValue = None, setMappingType = None, setMappingTypeCode = None, setModifiedTime = None, setSourceDisplayName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValueSourceID = None, returnFieldMappingID = False, returnActionIfSourceValueIsBlank = False, returnActionIfSourceValueIsBlankCode = False, returnCreatedTime = False, returnFieldID = False, returnImportDataObjectSourceID = False, returnImportDataObjectSourceIDMappedValue = False, returnMappingType = False, returnMappingTypeCode = False, returnModifiedTime = False, returnSourceDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValueSourceID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFieldMapping(FieldMappingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FieldMapping/" + str(FieldMappingID), verb = "delete")


def getEveryFileDestination(searchConditions = [], EntityID = 1, returnFileDestinationID = False, returnAllowRead = False, returnAllowWrite = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnIdentifyingInformation = False, returnIsFTPConnection = False, returnIsUNCPath = False, returnModifiedTime = False, returnName = False, returnUNCPathID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FileDestination in the district.

    This function returns a dataframe of every FileDestination in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFileDestination(FileDestinationID, EntityID = 1, returnFileDestinationID = False, returnAllowRead = False, returnAllowWrite = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnIdentifyingInformation = False, returnIsFTPConnection = False, returnIsUNCPath = False, returnModifiedTime = False, returnName = False, returnUNCPathID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(FileDestinationID), verb = "get", return_params_list = return_params)

def modifyFileDestination(FileDestinationID, EntityID = 1, setFileDestinationID = None, setAllowRead = None, setAllowWrite = None, setCreatedTime = None, setDistrictID = None, setFTPConnectionID = None, setIdentifyingInformation = None, setIsFTPConnection = None, setIsUNCPath = None, setModifiedTime = None, setName = None, setUNCPathID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFileDestinationID = False, returnAllowRead = False, returnAllowWrite = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnIdentifyingInformation = False, returnIsFTPConnection = False, returnIsUNCPath = False, returnModifiedTime = False, returnName = False, returnUNCPathID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(FileDestinationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFileDestination(EntityID = 1, setFileDestinationID = None, setAllowRead = None, setAllowWrite = None, setCreatedTime = None, setDistrictID = None, setFTPConnectionID = None, setIdentifyingInformation = None, setIsFTPConnection = None, setIsUNCPath = None, setModifiedTime = None, setName = None, setUNCPathID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFileDestinationID = False, returnAllowRead = False, returnAllowWrite = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnIdentifyingInformation = False, returnIsFTPConnection = False, returnIsUNCPath = False, returnModifiedTime = False, returnName = False, returnUNCPathID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFileDestination(FileDestinationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestination/" + str(FileDestinationID), verb = "delete")


def getEveryFileDestinationResult(searchConditions = [], EntityID = 1, returnFileDestinationResultID = False, returnCreatedTime = False, returnFileDestinationID = False, returnFileName = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FileDestinationResult in the district.

    This function returns a dataframe of every FileDestinationResult in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFileDestinationResult(FileDestinationResultID, EntityID = 1, returnFileDestinationResultID = False, returnCreatedTime = False, returnFileDestinationID = False, returnFileName = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(FileDestinationResultID), verb = "get", return_params_list = return_params)

def modifyFileDestinationResult(FileDestinationResultID, EntityID = 1, setFileDestinationResultID = None, setCreatedTime = None, setFileDestinationID = None, setFileName = None, setLogID = None, setMediaIDDownload = None, setMessage = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setTransmissionType = None, setTransmissionTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFileDestinationResultID = False, returnCreatedTime = False, returnFileDestinationID = False, returnFileName = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(FileDestinationResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFileDestinationResult(EntityID = 1, setFileDestinationResultID = None, setCreatedTime = None, setFileDestinationID = None, setFileName = None, setLogID = None, setMediaIDDownload = None, setMessage = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setTransmissionType = None, setTransmissionTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFileDestinationResultID = False, returnCreatedTime = False, returnFileDestinationID = False, returnFileName = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFileDestinationResult(FileDestinationResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FileDestinationResult/" + str(FileDestinationResultID), verb = "delete")


def getEveryFilter(searchConditions = [], EntityID = 1, returnFilterID = False, returnComment = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDistrictID = False, returnEntityID = False, returnFilterDataAdvanced = False, returnFilterDataAdvancedCondition = False, returnFilterDataColumn = False, returnFilterDataColumnCondition = False, returnFilterIDClonedFrom = False, returnFiscalYearID = False, returnFriendlyFilter = False, returnIsReusable = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Filter in the district.

    This function returns a dataframe of every Filter in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFilter(FilterID, EntityID = 1, returnFilterID = False, returnComment = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDistrictID = False, returnEntityID = False, returnFilterDataAdvanced = False, returnFilterDataAdvancedCondition = False, returnFilterDataColumn = False, returnFilterDataColumnCondition = False, returnFilterIDClonedFrom = False, returnFiscalYearID = False, returnFriendlyFilter = False, returnIsReusable = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(FilterID), verb = "get", return_params_list = return_params)

def modifyFilter(FilterID, EntityID = 1, setFilterID = None, setComment = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setDistrictID = None, setEntityID = None, setFilterDataAdvanced = None, setFilterDataAdvancedCondition = None, setFilterDataColumn = None, setFilterDataColumnCondition = None, setFilterIDClonedFrom = None, setFiscalYearID = None, setFriendlyFilter = None, setIsReusable = None, setModifiedTime = None, setName = None, setSchoolYearID = None, setSkywardHash = None, setSkywardID = None, setType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnFilterID = False, returnComment = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDistrictID = False, returnEntityID = False, returnFilterDataAdvanced = False, returnFilterDataAdvancedCondition = False, returnFilterDataColumn = False, returnFilterDataColumnCondition = False, returnFilterIDClonedFrom = False, returnFiscalYearID = False, returnFriendlyFilter = False, returnIsReusable = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(FilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFilter(EntityID = 1, setFilterID = None, setComment = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setDistrictID = None, setEntityID = None, setFilterDataAdvanced = None, setFilterDataAdvancedCondition = None, setFilterDataColumn = None, setFilterDataColumnCondition = None, setFilterIDClonedFrom = None, setFiscalYearID = None, setFriendlyFilter = None, setIsReusable = None, setModifiedTime = None, setName = None, setSchoolYearID = None, setSkywardHash = None, setSkywardID = None, setType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnFilterID = False, returnComment = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDistrictID = False, returnEntityID = False, returnFilterDataAdvanced = False, returnFilterDataAdvancedCondition = False, returnFilterDataColumn = False, returnFilterDataColumnCondition = False, returnFilterIDClonedFrom = False, returnFiscalYearID = False, returnFriendlyFilter = False, returnIsReusable = False, returnModifiedTime = False, returnName = False, returnSchoolYearID = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFilter(FilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Filter/" + str(FilterID), verb = "delete")


def getEveryFTPConnection(searchConditions = [], EntityID = 1, returnFTPConnectionID = False, returnAllowInvalidCertificate = False, returnCreatedTime = False, returnDescription = False, returnHost = False, returnMediaIDSSHKey = False, returnModifiedTime = False, returnName = False, returnPassword = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnRemoteDirectory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FTPConnection in the district.

    This function returns a dataframe of every FTPConnection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFTPConnection(FTPConnectionID, EntityID = 1, returnFTPConnectionID = False, returnAllowInvalidCertificate = False, returnCreatedTime = False, returnDescription = False, returnHost = False, returnMediaIDSSHKey = False, returnModifiedTime = False, returnName = False, returnPassword = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnRemoteDirectory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(FTPConnectionID), verb = "get", return_params_list = return_params)

def modifyFTPConnection(FTPConnectionID, EntityID = 1, setFTPConnectionID = None, setAllowInvalidCertificate = None, setCreatedTime = None, setDescription = None, setHost = None, setMediaIDSSHKey = None, setModifiedTime = None, setName = None, setPassword = None, setPort = None, setProtocol = None, setProtocolCode = None, setRemoteDirectory = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, returnFTPConnectionID = False, returnAllowInvalidCertificate = False, returnCreatedTime = False, returnDescription = False, returnHost = False, returnMediaIDSSHKey = False, returnModifiedTime = False, returnName = False, returnPassword = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnRemoteDirectory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(FTPConnectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFTPConnection(EntityID = 1, setFTPConnectionID = None, setAllowInvalidCertificate = None, setCreatedTime = None, setDescription = None, setHost = None, setMediaIDSSHKey = None, setModifiedTime = None, setName = None, setPassword = None, setPort = None, setProtocol = None, setProtocolCode = None, setRemoteDirectory = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, returnFTPConnectionID = False, returnAllowInvalidCertificate = False, returnCreatedTime = False, returnDescription = False, returnHost = False, returnMediaIDSSHKey = False, returnModifiedTime = False, returnName = False, returnPassword = False, returnPort = False, returnProtocol = False, returnProtocolCode = False, returnRemoteDirectory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFTPConnection(FTPConnectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPConnection/" + str(FTPConnectionID), verb = "delete")


def getEveryFTPProcessType(searchConditions = [], EntityID = 1, returnFTPProcessTypeID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnModuleName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FTPProcessType in the district.

    This function returns a dataframe of every FTPProcessType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFTPProcessType(FTPProcessTypeID, EntityID = 1, returnFTPProcessTypeID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnModuleName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(FTPProcessTypeID), verb = "get", return_params_list = return_params)

def modifyFTPProcessType(FTPProcessTypeID, EntityID = 1, setFTPProcessTypeID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setModuleName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPProcessTypeID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnModuleName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(FTPProcessTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFTPProcessType(EntityID = 1, setFTPProcessTypeID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setModuleName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPProcessTypeID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnModuleName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFTPProcessType(FTPProcessTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessType/" + str(FTPProcessTypeID), verb = "delete")


def getEveryFTPProcessTypeConnection(searchConditions = [], EntityID = 1, returnFTPProcessTypeConnectionID = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnFTPProcessTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FTPProcessTypeConnection in the district.

    This function returns a dataframe of every FTPProcessTypeConnection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFTPProcessTypeConnection(FTPProcessTypeConnectionID, EntityID = 1, returnFTPProcessTypeConnectionID = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnFTPProcessTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(FTPProcessTypeConnectionID), verb = "get", return_params_list = return_params)

def modifyFTPProcessTypeConnection(FTPProcessTypeConnectionID, EntityID = 1, setFTPProcessTypeConnectionID = None, setCreatedTime = None, setDistrictID = None, setFTPConnectionID = None, setFTPProcessTypeID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPProcessTypeConnectionID = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnFTPProcessTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(FTPProcessTypeConnectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFTPProcessTypeConnection(EntityID = 1, setFTPProcessTypeConnectionID = None, setCreatedTime = None, setDistrictID = None, setFTPConnectionID = None, setFTPProcessTypeID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPProcessTypeConnectionID = False, returnCreatedTime = False, returnDistrictID = False, returnFTPConnectionID = False, returnFTPProcessTypeID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFTPProcessTypeConnection(FTPProcessTypeConnectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPProcessTypeConnection/" + str(FTPProcessTypeConnectionID), verb = "delete")


def getEveryFTPResult(searchConditions = [], EntityID = 1, returnFTPResultID = False, returnCreatedTime = False, returnFileName = False, returnFTPConnectionID = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FTPResult in the district.

    This function returns a dataframe of every FTPResult in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFTPResult(FTPResultID, EntityID = 1, returnFTPResultID = False, returnCreatedTime = False, returnFileName = False, returnFTPConnectionID = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(FTPResultID), verb = "get", return_params_list = return_params)

def modifyFTPResult(FTPResultID, EntityID = 1, setFTPResultID = None, setCreatedTime = None, setFileName = None, setFTPConnectionID = None, setLogID = None, setMediaIDDownload = None, setMessage = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setTransmissionType = None, setTransmissionTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPResultID = False, returnCreatedTime = False, returnFileName = False, returnFTPConnectionID = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(FTPResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFTPResult(EntityID = 1, setFTPResultID = None, setCreatedTime = None, setFileName = None, setFTPConnectionID = None, setLogID = None, setMediaIDDownload = None, setMessage = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setTransmissionType = None, setTransmissionTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFTPResultID = False, returnCreatedTime = False, returnFileName = False, returnFTPConnectionID = False, returnLogID = False, returnMediaIDDownload = False, returnMessage = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnTransmissionType = False, returnTransmissionTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFTPResult(FTPResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/FTPResult/" + str(FTPResultID), verb = "delete")


def getEveryImport(searchConditions = [], EntityID = 1, returnImportID = False, returnAcceptedFileTypes = False, returnColumnsJSON = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDefinition = False, returnDelimiter = False, returnDescription = False, returnFileHasHeaderRow = False, returnFileType = False, returnFileTypeCode = False, returnHasPromptsFromDefinition = False, returnIsFixedWidth = False, returnIsSkywardImport = False, returnModifiedTime = False, returnName = False, returnNumberOfHeaderRows = False, returnPromptList = False, returnPromptListJson = False, returnSkywardID = False, returnTextQualifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Import in the district.

    This function returns a dataframe of every Import in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImport(ImportID, EntityID = 1, returnImportID = False, returnAcceptedFileTypes = False, returnColumnsJSON = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDefinition = False, returnDelimiter = False, returnDescription = False, returnFileHasHeaderRow = False, returnFileType = False, returnFileTypeCode = False, returnHasPromptsFromDefinition = False, returnIsFixedWidth = False, returnIsSkywardImport = False, returnModifiedTime = False, returnName = False, returnNumberOfHeaderRows = False, returnPromptList = False, returnPromptListJson = False, returnSkywardID = False, returnTextQualifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(ImportID), verb = "get", return_params_list = return_params)

def modifyImport(ImportID, EntityID = 1, setImportID = None, setAcceptedFileTypes = None, setColumnsJSON = None, setCreatedTime = None, setDateFormat = None, setDateFormatCode = None, setDefinition = None, setDelimiter = None, setDescription = None, setFileHasHeaderRow = None, setFileType = None, setFileTypeCode = None, setHasPromptsFromDefinition = None, setIsFixedWidth = None, setIsSkywardImport = None, setModifiedTime = None, setName = None, setNumberOfHeaderRows = None, setPromptList = None, setPromptListJson = None, setSkywardID = None, setTextQualifier = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportID = False, returnAcceptedFileTypes = False, returnColumnsJSON = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDefinition = False, returnDelimiter = False, returnDescription = False, returnFileHasHeaderRow = False, returnFileType = False, returnFileTypeCode = False, returnHasPromptsFromDefinition = False, returnIsFixedWidth = False, returnIsSkywardImport = False, returnModifiedTime = False, returnName = False, returnNumberOfHeaderRows = False, returnPromptList = False, returnPromptListJson = False, returnSkywardID = False, returnTextQualifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(ImportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImport(EntityID = 1, setImportID = None, setAcceptedFileTypes = None, setColumnsJSON = None, setCreatedTime = None, setDateFormat = None, setDateFormatCode = None, setDefinition = None, setDelimiter = None, setDescription = None, setFileHasHeaderRow = None, setFileType = None, setFileTypeCode = None, setHasPromptsFromDefinition = None, setIsFixedWidth = None, setIsSkywardImport = None, setModifiedTime = None, setName = None, setNumberOfHeaderRows = None, setPromptList = None, setPromptListJson = None, setSkywardID = None, setTextQualifier = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportID = False, returnAcceptedFileTypes = False, returnColumnsJSON = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDefinition = False, returnDelimiter = False, returnDescription = False, returnFileHasHeaderRow = False, returnFileType = False, returnFileTypeCode = False, returnHasPromptsFromDefinition = False, returnIsFixedWidth = False, returnIsSkywardImport = False, returnModifiedTime = False, returnName = False, returnNumberOfHeaderRows = False, returnPromptList = False, returnPromptListJson = False, returnSkywardID = False, returnTextQualifier = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImport(ImportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Import/" + str(ImportID), verb = "delete")


def getEveryImportDataObjectSource(searchConditions = [], EntityID = 1, returnImportDataObjectSourceID = False, returnAction = False, returnActionCode = False, returnCanAddFieldMapping = False, returnCreatedTime = False, returnHasFieldMappings = False, returnImportID = False, returnIsPrimary = False, returnMatchAction = False, returnMatchActionCode = False, returnModifiedTime = False, returnName = False, returnNoMatchAction = False, returnNoMatchActionCode = False, returnObjectID = False, returnUniqueKey = False, returnUpdateSearchCondition = False, returnUpdateSearchXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ImportDataObjectSource in the district.

    This function returns a dataframe of every ImportDataObjectSource in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImportDataObjectSource(ImportDataObjectSourceID, EntityID = 1, returnImportDataObjectSourceID = False, returnAction = False, returnActionCode = False, returnCanAddFieldMapping = False, returnCreatedTime = False, returnHasFieldMappings = False, returnImportID = False, returnIsPrimary = False, returnMatchAction = False, returnMatchActionCode = False, returnModifiedTime = False, returnName = False, returnNoMatchAction = False, returnNoMatchActionCode = False, returnObjectID = False, returnUniqueKey = False, returnUpdateSearchCondition = False, returnUpdateSearchXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(ImportDataObjectSourceID), verb = "get", return_params_list = return_params)

def modifyImportDataObjectSource(ImportDataObjectSourceID, EntityID = 1, setImportDataObjectSourceID = None, setAction = None, setActionCode = None, setCanAddFieldMapping = None, setCreatedTime = None, setHasFieldMappings = None, setImportID = None, setIsPrimary = None, setMatchAction = None, setMatchActionCode = None, setModifiedTime = None, setName = None, setNoMatchAction = None, setNoMatchActionCode = None, setObjectID = None, setUniqueKey = None, setUpdateSearchCondition = None, setUpdateSearchXML = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportDataObjectSourceID = False, returnAction = False, returnActionCode = False, returnCanAddFieldMapping = False, returnCreatedTime = False, returnHasFieldMappings = False, returnImportID = False, returnIsPrimary = False, returnMatchAction = False, returnMatchActionCode = False, returnModifiedTime = False, returnName = False, returnNoMatchAction = False, returnNoMatchActionCode = False, returnObjectID = False, returnUniqueKey = False, returnUpdateSearchCondition = False, returnUpdateSearchXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(ImportDataObjectSourceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImportDataObjectSource(EntityID = 1, setImportDataObjectSourceID = None, setAction = None, setActionCode = None, setCanAddFieldMapping = None, setCreatedTime = None, setHasFieldMappings = None, setImportID = None, setIsPrimary = None, setMatchAction = None, setMatchActionCode = None, setModifiedTime = None, setName = None, setNoMatchAction = None, setNoMatchActionCode = None, setObjectID = None, setUniqueKey = None, setUpdateSearchCondition = None, setUpdateSearchXML = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportDataObjectSourceID = False, returnAction = False, returnActionCode = False, returnCanAddFieldMapping = False, returnCreatedTime = False, returnHasFieldMappings = False, returnImportID = False, returnIsPrimary = False, returnMatchAction = False, returnMatchActionCode = False, returnModifiedTime = False, returnName = False, returnNoMatchAction = False, returnNoMatchActionCode = False, returnObjectID = False, returnUniqueKey = False, returnUpdateSearchCondition = False, returnUpdateSearchXML = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImportDataObjectSource(ImportDataObjectSourceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportDataObjectSource/" + str(ImportDataObjectSourceID), verb = "delete")


def getEveryImportModulePath(searchConditions = [], EntityID = 1, returnImportModulePathID = False, returnCreatedTime = False, returnImportID = False, returnModifiedTime = False, returnModulePathID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ImportModulePath in the district.

    This function returns a dataframe of every ImportModulePath in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImportModulePath(ImportModulePathID, EntityID = 1, returnImportModulePathID = False, returnCreatedTime = False, returnImportID = False, returnModifiedTime = False, returnModulePathID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(ImportModulePathID), verb = "get", return_params_list = return_params)

def modifyImportModulePath(ImportModulePathID, EntityID = 1, setImportModulePathID = None, setCreatedTime = None, setImportID = None, setModifiedTime = None, setModulePathID = None, setPromptDataSources = None, setPromptDataSourcesJson = None, setSourceSchemaObject = None, setSourceTypeName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportModulePathID = False, returnCreatedTime = False, returnImportID = False, returnModifiedTime = False, returnModulePathID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(ImportModulePathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImportModulePath(EntityID = 1, setImportModulePathID = None, setCreatedTime = None, setImportID = None, setModifiedTime = None, setModulePathID = None, setPromptDataSources = None, setPromptDataSourcesJson = None, setSourceSchemaObject = None, setSourceTypeName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportModulePathID = False, returnCreatedTime = False, returnImportID = False, returnModifiedTime = False, returnModulePathID = False, returnPromptDataSources = False, returnPromptDataSourcesJson = False, returnSourceSchemaObject = False, returnSourceTypeName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImportModulePath(ImportModulePathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportModulePath/" + str(ImportModulePathID), verb = "delete")


def getEveryImportResult(searchConditions = [], EntityID = 1, returnImportResultID = False, returnCanBeDeleted = False, returnCreatedTime = False, returnFailedRecordCount = False, returnHasMediaFailedRows = False, returnImportID = False, returnLastProcessedRowNumber = False, returnMediaIDFailedRows = False, returnMediaIDOriginalImportedData = False, returnModifiedTime = False, returnResultRowCount = False, returnStatus = False, returnStatusCode = False, returnSuccessfulRecordCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWarningRecordCount = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ImportResult in the district.

    This function returns a dataframe of every ImportResult in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImportResult(ImportResultID, EntityID = 1, returnImportResultID = False, returnCanBeDeleted = False, returnCreatedTime = False, returnFailedRecordCount = False, returnHasMediaFailedRows = False, returnImportID = False, returnLastProcessedRowNumber = False, returnMediaIDFailedRows = False, returnMediaIDOriginalImportedData = False, returnModifiedTime = False, returnResultRowCount = False, returnStatus = False, returnStatusCode = False, returnSuccessfulRecordCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWarningRecordCount = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(ImportResultID), verb = "get", return_params_list = return_params)

def modifyImportResult(ImportResultID, EntityID = 1, setImportResultID = None, setCanBeDeleted = None, setCreatedTime = None, setFailedRecordCount = None, setHasMediaFailedRows = None, setImportID = None, setLastProcessedRowNumber = None, setMediaIDFailedRows = None, setMediaIDOriginalImportedData = None, setModifiedTime = None, setResultRowCount = None, setStatus = None, setStatusCode = None, setSuccessfulRecordCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWarningRecordCount = None, returnImportResultID = False, returnCanBeDeleted = False, returnCreatedTime = False, returnFailedRecordCount = False, returnHasMediaFailedRows = False, returnImportID = False, returnLastProcessedRowNumber = False, returnMediaIDFailedRows = False, returnMediaIDOriginalImportedData = False, returnModifiedTime = False, returnResultRowCount = False, returnStatus = False, returnStatusCode = False, returnSuccessfulRecordCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWarningRecordCount = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(ImportResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImportResult(EntityID = 1, setImportResultID = None, setCanBeDeleted = None, setCreatedTime = None, setFailedRecordCount = None, setHasMediaFailedRows = None, setImportID = None, setLastProcessedRowNumber = None, setMediaIDFailedRows = None, setMediaIDOriginalImportedData = None, setModifiedTime = None, setResultRowCount = None, setStatus = None, setStatusCode = None, setSuccessfulRecordCount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWarningRecordCount = None, returnImportResultID = False, returnCanBeDeleted = False, returnCreatedTime = False, returnFailedRecordCount = False, returnHasMediaFailedRows = False, returnImportID = False, returnLastProcessedRowNumber = False, returnMediaIDFailedRows = False, returnMediaIDOriginalImportedData = False, returnModifiedTime = False, returnResultRowCount = False, returnStatus = False, returnStatusCode = False, returnSuccessfulRecordCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWarningRecordCount = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImportResult(ImportResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResult/" + str(ImportResultID), verb = "delete")


def getEveryImportResultRow(searchConditions = [], EntityID = 1, returnImportResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnFailedRowFileRowNumber = False, returnImportFileRowNumber = False, returnImportResultID = False, returnModifiedTime = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ImportResultRow in the district.

    This function returns a dataframe of every ImportResultRow in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImportResultRow(ImportResultRowID, EntityID = 1, returnImportResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnFailedRowFileRowNumber = False, returnImportFileRowNumber = False, returnImportResultID = False, returnModifiedTime = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(ImportResultRowID), verb = "get", return_params_list = return_params)

def modifyImportResultRow(ImportResultRowID, EntityID = 1, setImportResultRowID = None, setCreatedTime = None, setErrorMessage = None, setFailedRowFileRowNumber = None, setImportFileRowNumber = None, setImportResultID = None, setModifiedTime = None, setResultType = None, setResultTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnFailedRowFileRowNumber = False, returnImportFileRowNumber = False, returnImportResultID = False, returnModifiedTime = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(ImportResultRowID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImportResultRow(EntityID = 1, setImportResultRowID = None, setCreatedTime = None, setErrorMessage = None, setFailedRowFileRowNumber = None, setImportFileRowNumber = None, setImportResultID = None, setModifiedTime = None, setResultType = None, setResultTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnFailedRowFileRowNumber = False, returnImportFileRowNumber = False, returnImportResultID = False, returnModifiedTime = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImportResultRow(ImportResultRowID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRow/" + str(ImportResultRowID), verb = "delete")


def getEveryImportResultRowDetail(searchConditions = [], EntityID = 1, returnImportResultRowDetailID = False, returnActionType = False, returnActionTypeCode = False, returnBeforeImportModifiedTime = False, returnCreatedTime = False, returnImportResultRowID = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ImportResultRowDetail in the district.

    This function returns a dataframe of every ImportResultRowDetail in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getImportResultRowDetail(ImportResultRowDetailID, EntityID = 1, returnImportResultRowDetailID = False, returnActionType = False, returnActionTypeCode = False, returnBeforeImportModifiedTime = False, returnCreatedTime = False, returnImportResultRowID = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(ImportResultRowDetailID), verb = "get", return_params_list = return_params)

def modifyImportResultRowDetail(ImportResultRowDetailID, EntityID = 1, setImportResultRowDetailID = None, setActionType = None, setActionTypeCode = None, setBeforeImportModifiedTime = None, setCreatedTime = None, setImportResultRowID = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportResultRowDetailID = False, returnActionType = False, returnActionTypeCode = False, returnBeforeImportModifiedTime = False, returnCreatedTime = False, returnImportResultRowID = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(ImportResultRowDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createImportResultRowDetail(EntityID = 1, setImportResultRowDetailID = None, setActionType = None, setActionTypeCode = None, setBeforeImportModifiedTime = None, setCreatedTime = None, setImportResultRowID = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnImportResultRowDetailID = False, returnActionType = False, returnActionTypeCode = False, returnBeforeImportModifiedTime = False, returnCreatedTime = False, returnImportResultRowID = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteImportResultRowDetail(ImportResultRowDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ImportResultRowDetail/" + str(ImportResultRowDetailID), verb = "delete")


def getEveryIndexStatisticsAlwaysUpdate(searchConditions = [], EntityID = 1, returnIndexStatisticsAlwaysUpdateID = False, returnSchemaName = False, returnSkywardHash = False, returnSkywardID = False, returnTableName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every IndexStatisticsAlwaysUpdate in the district.

    This function returns a dataframe of every IndexStatisticsAlwaysUpdate in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getIndexStatisticsAlwaysUpdate(IndexStatisticsAlwaysUpdateID, EntityID = 1, returnIndexStatisticsAlwaysUpdateID = False, returnSchemaName = False, returnSkywardHash = False, returnSkywardID = False, returnTableName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(IndexStatisticsAlwaysUpdateID), verb = "get", return_params_list = return_params)

def modifyIndexStatisticsAlwaysUpdate(IndexStatisticsAlwaysUpdateID, EntityID = 1, setIndexStatisticsAlwaysUpdateID = None, setSchemaName = None, setSkywardHash = None, setSkywardID = None, setTableName = None, returnIndexStatisticsAlwaysUpdateID = False, returnSchemaName = False, returnSkywardHash = False, returnSkywardID = False, returnTableName = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(IndexStatisticsAlwaysUpdateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createIndexStatisticsAlwaysUpdate(EntityID = 1, setIndexStatisticsAlwaysUpdateID = None, setSchemaName = None, setSkywardHash = None, setSkywardID = None, setTableName = None, returnIndexStatisticsAlwaysUpdateID = False, returnSchemaName = False, returnSkywardHash = False, returnSkywardID = False, returnTableName = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteIndexStatisticsAlwaysUpdate(IndexStatisticsAlwaysUpdateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/IndexStatisticsAlwaysUpdate/" + str(IndexStatisticsAlwaysUpdateID), verb = "delete")


def getEveryKiosk(searchConditions = [], EntityID = 1, returnKioskID = False, returnCreatedTime = False, returnIPAddress = False, returnIsTardyKiosk = False, returnModifiedTime = False, returnName = False, returnPrinterType = False, returnPrinterTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Kiosk in the district.

    This function returns a dataframe of every Kiosk in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getKiosk(KioskID, EntityID = 1, returnKioskID = False, returnCreatedTime = False, returnIPAddress = False, returnIsTardyKiosk = False, returnModifiedTime = False, returnName = False, returnPrinterType = False, returnPrinterTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(KioskID), verb = "get", return_params_list = return_params)

def modifyKiosk(KioskID, EntityID = 1, setKioskID = None, setCreatedTime = None, setIPAddress = None, setIsTardyKiosk = None, setModifiedTime = None, setName = None, setPrinterType = None, setPrinterTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnKioskID = False, returnCreatedTime = False, returnIPAddress = False, returnIsTardyKiosk = False, returnModifiedTime = False, returnName = False, returnPrinterType = False, returnPrinterTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(KioskID), verb = "post", return_params_list = return_params, payload = payload_params)

def createKiosk(EntityID = 1, setKioskID = None, setCreatedTime = None, setIPAddress = None, setIsTardyKiosk = None, setModifiedTime = None, setName = None, setPrinterType = None, setPrinterTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnKioskID = False, returnCreatedTime = False, returnIPAddress = False, returnIsTardyKiosk = False, returnModifiedTime = False, returnName = False, returnPrinterType = False, returnPrinterTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteKiosk(KioskID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Kiosk/" + str(KioskID), verb = "delete")


def getEveryLog(searchConditions = [], EntityID = 1, returnLogID = False, returnActivityContext = False, returnApplication = False, returnApplicationMonitoringIdentifier = False, returnBindingEscapedMessage = False, returnClassification = False, returnClassificationCode = False, returnCreatedTime = False, returnDataObjectID = False, returnDataObjectType = False, returnDetails = False, returnHostname = False, returnMessage = False, returnModifiedTime = False, returnProcessID = False, returnSeverity = False, returnSeverityCode = False, returnSourceFile = False, returnStackTrace = False, returnSystemVersion = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Log in the district.

    This function returns a dataframe of every Log in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLog(LogID, EntityID = 1, returnLogID = False, returnActivityContext = False, returnApplication = False, returnApplicationMonitoringIdentifier = False, returnBindingEscapedMessage = False, returnClassification = False, returnClassificationCode = False, returnCreatedTime = False, returnDataObjectID = False, returnDataObjectType = False, returnDetails = False, returnHostname = False, returnMessage = False, returnModifiedTime = False, returnProcessID = False, returnSeverity = False, returnSeverityCode = False, returnSourceFile = False, returnStackTrace = False, returnSystemVersion = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(LogID), verb = "get", return_params_list = return_params)

def modifyLog(LogID, EntityID = 1, setLogID = None, setActivityContext = None, setApplication = None, setApplicationMonitoringIdentifier = None, setBindingEscapedMessage = None, setClassification = None, setClassificationCode = None, setCreatedTime = None, setDataObjectID = None, setDataObjectType = None, setDetails = None, setHostname = None, setMessage = None, setModifiedTime = None, setProcessID = None, setSeverity = None, setSeverityCode = None, setSourceFile = None, setStackTrace = None, setSystemVersion = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLogID = False, returnActivityContext = False, returnApplication = False, returnApplicationMonitoringIdentifier = False, returnBindingEscapedMessage = False, returnClassification = False, returnClassificationCode = False, returnCreatedTime = False, returnDataObjectID = False, returnDataObjectType = False, returnDetails = False, returnHostname = False, returnMessage = False, returnModifiedTime = False, returnProcessID = False, returnSeverity = False, returnSeverityCode = False, returnSourceFile = False, returnStackTrace = False, returnSystemVersion = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(LogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLog(EntityID = 1, setLogID = None, setActivityContext = None, setApplication = None, setApplicationMonitoringIdentifier = None, setBindingEscapedMessage = None, setClassification = None, setClassificationCode = None, setCreatedTime = None, setDataObjectID = None, setDataObjectType = None, setDetails = None, setHostname = None, setMessage = None, setModifiedTime = None, setProcessID = None, setSeverity = None, setSeverityCode = None, setSourceFile = None, setStackTrace = None, setSystemVersion = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLogID = False, returnActivityContext = False, returnApplication = False, returnApplicationMonitoringIdentifier = False, returnBindingEscapedMessage = False, returnClassification = False, returnClassificationCode = False, returnCreatedTime = False, returnDataObjectID = False, returnDataObjectType = False, returnDetails = False, returnHostname = False, returnMessage = False, returnModifiedTime = False, returnProcessID = False, returnSeverity = False, returnSeverityCode = False, returnSourceFile = False, returnStackTrace = False, returnSystemVersion = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLog(LogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Log/" + str(LogID), verb = "delete")


def getEveryLoginHistory(searchConditions = [], EntityID = 1, returnLoginHistoryID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnEnteredUserName = False, returnHostAddress = False, returnIsSuccessfulLogin = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LoginHistory in the district.

    This function returns a dataframe of every LoginHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLoginHistory(LoginHistoryID, EntityID = 1, returnLoginHistoryID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnEnteredUserName = False, returnHostAddress = False, returnIsSuccessfulLogin = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(LoginHistoryID), verb = "get", return_params_list = return_params)

def modifyLoginHistory(LoginHistoryID, EntityID = 1, setLoginHistoryID = None, setBrowserType = None, setBrowserVersion = None, setCreatedTime = None, setDeviceType = None, setEnteredUserName = None, setHostAddress = None, setIsSuccessfulLogin = None, setModifiedTime = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLoginHistoryID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnEnteredUserName = False, returnHostAddress = False, returnIsSuccessfulLogin = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(LoginHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLoginHistory(EntityID = 1, setLoginHistoryID = None, setBrowserType = None, setBrowserVersion = None, setCreatedTime = None, setDeviceType = None, setEnteredUserName = None, setHostAddress = None, setIsSuccessfulLogin = None, setModifiedTime = None, setOperatingSystemType = None, setUserAgent = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLoginHistoryID = False, returnBrowserType = False, returnBrowserVersion = False, returnCreatedTime = False, returnDeviceType = False, returnEnteredUserName = False, returnHostAddress = False, returnIsSuccessfulLogin = False, returnModifiedTime = False, returnOperatingSystemType = False, returnUserAgent = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLoginHistory(LoginHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/LoginHistory/" + str(LoginHistoryID), verb = "delete")


def getEveryMedia(searchConditions = [], EntityID = 1, returnMediaID = False, returnBytes = False, returnCreatedTime = False, returnHash = False, returnLibraryType = False, returnLibraryTypeCode = False, returnMediaDataID = False, returnMediaDataIDLargeThumbnail = False, returnMediaDataIDSmallThumbnail = False, returnMediaTypeID = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStorageLocation = False, returnStorageLocationCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Media in the district.

    This function returns a dataframe of every Media in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMedia(MediaID, EntityID = 1, returnMediaID = False, returnBytes = False, returnCreatedTime = False, returnHash = False, returnLibraryType = False, returnLibraryTypeCode = False, returnMediaDataID = False, returnMediaDataIDLargeThumbnail = False, returnMediaDataIDSmallThumbnail = False, returnMediaTypeID = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStorageLocation = False, returnStorageLocationCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(MediaID), verb = "get", return_params_list = return_params)

def modifyMedia(MediaID, EntityID = 1, setMediaID = None, setBytes = None, setCreatedTime = None, setHash = None, setLibraryType = None, setLibraryTypeCode = None, setMediaDataID = None, setMediaDataIDLargeThumbnail = None, setMediaDataIDSmallThumbnail = None, setMediaTypeID = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setStorageLocation = None, setStorageLocationCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXDimension = None, setYDimension = None, returnMediaID = False, returnBytes = False, returnCreatedTime = False, returnHash = False, returnLibraryType = False, returnLibraryTypeCode = False, returnMediaDataID = False, returnMediaDataIDLargeThumbnail = False, returnMediaDataIDSmallThumbnail = False, returnMediaTypeID = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStorageLocation = False, returnStorageLocationCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(MediaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMedia(EntityID = 1, setMediaID = None, setBytes = None, setCreatedTime = None, setHash = None, setLibraryType = None, setLibraryTypeCode = None, setMediaDataID = None, setMediaDataIDLargeThumbnail = None, setMediaDataIDSmallThumbnail = None, setMediaTypeID = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setStorageLocation = None, setStorageLocationCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setXDimension = None, setYDimension = None, returnMediaID = False, returnBytes = False, returnCreatedTime = False, returnHash = False, returnLibraryType = False, returnLibraryTypeCode = False, returnMediaDataID = False, returnMediaDataIDLargeThumbnail = False, returnMediaDataIDSmallThumbnail = False, returnMediaTypeID = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStorageLocation = False, returnStorageLocationCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnXDimension = False, returnYDimension = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMedia(MediaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Media/" + str(MediaID), verb = "delete")


def getEveryMediaType(searchConditions = [], EntityID = 1, returnMediaTypeID = False, returnAllowAttachment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMimeType = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MediaType in the district.

    This function returns a dataframe of every MediaType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMediaType(MediaTypeID, EntityID = 1, returnMediaTypeID = False, returnAllowAttachment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMimeType = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(MediaTypeID), verb = "get", return_params_list = return_params)

def modifyMediaType(MediaTypeID, EntityID = 1, setMediaTypeID = None, setAllowAttachment = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setMimeType = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMediaTypeID = False, returnAllowAttachment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMimeType = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(MediaTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMediaType(EntityID = 1, setMediaTypeID = None, setAllowAttachment = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setMimeType = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMediaTypeID = False, returnAllowAttachment = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnMimeType = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMediaType(MediaTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MediaType/" + str(MediaTypeID), verb = "delete")


def getEveryMenuCategory(searchConditions = [], EntityID = 1, returnMenuCategoryID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveIsDefault = False, returnIsDefault = False, returnIsEnabled = False, returnIsSkywardMenuCategory = False, returnMenuModuleID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MenuCategory in the district.

    This function returns a dataframe of every MenuCategory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMenuCategory(MenuCategoryID, EntityID = 1, returnMenuCategoryID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveIsDefault = False, returnIsDefault = False, returnIsEnabled = False, returnIsSkywardMenuCategory = False, returnMenuModuleID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(MenuCategoryID), verb = "get", return_params_list = return_params)

def modifyMenuCategory(MenuCategoryID, EntityID = 1, setMenuCategoryID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveIsDefault = None, setIsDefault = None, setIsEnabled = None, setIsSkywardMenuCategory = None, setMenuModuleID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuCategoryID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveIsDefault = False, returnIsDefault = False, returnIsEnabled = False, returnIsSkywardMenuCategory = False, returnMenuModuleID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(MenuCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMenuCategory(EntityID = 1, setMenuCategoryID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveIsDefault = None, setIsDefault = None, setIsEnabled = None, setIsSkywardMenuCategory = None, setMenuModuleID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setSkywardIsDefault = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuCategoryID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveIsDefault = False, returnIsDefault = False, returnIsEnabled = False, returnIsSkywardMenuCategory = False, returnMenuModuleID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIsDefault = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMenuCategory(MenuCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuCategory/" + str(MenuCategoryID), verb = "delete")


def getEveryMenuModule(searchConditions = [], EntityID = 1, returnMenuModuleID = False, returnCreatedTime = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnImage = False, returnImageCode = False, returnIsEnabled = False, returnIsSkywardMenuModule = False, returnModifiedTime = False, returnModuleSkywardID = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MenuModule in the district.

    This function returns a dataframe of every MenuModule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMenuModule(MenuModuleID, EntityID = 1, returnMenuModuleID = False, returnCreatedTime = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnImage = False, returnImageCode = False, returnIsEnabled = False, returnIsSkywardMenuModule = False, returnModifiedTime = False, returnModuleSkywardID = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(MenuModuleID), verb = "get", return_params_list = return_params)

def modifyMenuModule(MenuModuleID, EntityID = 1, setMenuModuleID = None, setCreatedTime = None, setDescription = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setImage = None, setImageCode = None, setIsEnabled = None, setIsSkywardMenuModule = None, setModifiedTime = None, setModuleSkywardID = None, setSkywardDescription = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuModuleID = False, returnCreatedTime = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnImage = False, returnImageCode = False, returnIsEnabled = False, returnIsSkywardMenuModule = False, returnModifiedTime = False, returnModuleSkywardID = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(MenuModuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMenuModule(EntityID = 1, setMenuModuleID = None, setCreatedTime = None, setDescription = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setImage = None, setImageCode = None, setIsEnabled = None, setIsSkywardMenuModule = None, setModifiedTime = None, setModuleSkywardID = None, setSkywardDescription = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuModuleID = False, returnCreatedTime = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnImage = False, returnImageCode = False, returnIsEnabled = False, returnIsSkywardMenuModule = False, returnModifiedTime = False, returnModuleSkywardID = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMenuModule(MenuModuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuModule/" + str(MenuModuleID), verb = "delete")


def getEveryMenuScreen(searchConditions = [], EntityID = 1, returnMenuScreenID = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnIsEnabled = False, returnIsForMenuSecurity = False, returnIsSkywardMenuScreen = False, returnMenuCategoryID = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnOptionType = False, returnOptionTypeCode = False, returnPostData = False, returnProfileID = False, returnScreen = False, returnShouldShowInMenu = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every MenuScreen in the district.

    This function returns a dataframe of every MenuScreen in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getMenuScreen(MenuScreenID, EntityID = 1, returnMenuScreenID = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnIsEnabled = False, returnIsForMenuSecurity = False, returnIsSkywardMenuScreen = False, returnMenuCategoryID = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnOptionType = False, returnOptionTypeCode = False, returnPostData = False, returnProfileID = False, returnScreen = False, returnShouldShowInMenu = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(MenuScreenID), verb = "get", return_params_list = return_params)

def modifyMenuScreen(MenuScreenID, EntityID = 1, setMenuScreenID = None, setCreatedTime = None, setData = None, setDescription = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setIsEnabled = None, setIsForMenuSecurity = None, setIsSkywardMenuScreen = None, setMenuCategoryID = None, setModifiedTime = None, setModule = None, setObject = None, setOptionType = None, setOptionTypeCode = None, setPostData = None, setProfileID = None, setScreen = None, setShouldShowInMenu = None, setSkywardDescription = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuScreenID = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnIsEnabled = False, returnIsForMenuSecurity = False, returnIsSkywardMenuScreen = False, returnMenuCategoryID = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnOptionType = False, returnOptionTypeCode = False, returnPostData = False, returnProfileID = False, returnScreen = False, returnShouldShowInMenu = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(MenuScreenID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMenuScreen(EntityID = 1, setMenuScreenID = None, setCreatedTime = None, setData = None, setDescription = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDescription = None, setIsEnabled = None, setIsForMenuSecurity = None, setIsSkywardMenuScreen = None, setMenuCategoryID = None, setModifiedTime = None, setModule = None, setObject = None, setOptionType = None, setOptionTypeCode = None, setPostData = None, setProfileID = None, setScreen = None, setShouldShowInMenu = None, setSkywardDescription = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnMenuScreenID = False, returnCreatedTime = False, returnData = False, returnDescription = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDescription = False, returnIsEnabled = False, returnIsForMenuSecurity = False, returnIsSkywardMenuScreen = False, returnMenuCategoryID = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnOptionType = False, returnOptionTypeCode = False, returnPostData = False, returnProfileID = False, returnScreen = False, returnShouldShowInMenu = False, returnSkywardDescription = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMenuScreen(MenuScreenID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/MenuScreen/" + str(MenuScreenID), verb = "delete")


def getEveryModule(searchConditions = [], EntityID = 1, returnModuleID = False, returnChangeType = False, returnContainsAtLeastOneNonTempDataObject = False, returnCreatedTime = False, returnCurrentName = False, returnDisplayName = False, returnEffectiveName = False, returnHasChangedFields = False, returnHasChangedObjects = False, returnHasChangedRelationships = False, returnIsInDB = False, returnIsSkywardModule = False, returnModifiedTime = False, returnPendingName = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Module in the district.

    This function returns a dataframe of every Module in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getModule(ModuleID, EntityID = 1, returnModuleID = False, returnChangeType = False, returnContainsAtLeastOneNonTempDataObject = False, returnCreatedTime = False, returnCurrentName = False, returnDisplayName = False, returnEffectiveName = False, returnHasChangedFields = False, returnHasChangedObjects = False, returnHasChangedRelationships = False, returnIsInDB = False, returnIsSkywardModule = False, returnModifiedTime = False, returnPendingName = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(ModuleID), verb = "get", return_params_list = return_params)

def modifyModule(ModuleID, EntityID = 1, setModuleID = None, setChangeType = None, setContainsAtLeastOneNonTempDataObject = None, setCreatedTime = None, setCurrentName = None, setDisplayName = None, setEffectiveName = None, setHasChangedFields = None, setHasChangedObjects = None, setHasChangedRelationships = None, setIsInDB = None, setIsSkywardModule = None, setModifiedTime = None, setPendingName = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnModuleID = False, returnChangeType = False, returnContainsAtLeastOneNonTempDataObject = False, returnCreatedTime = False, returnCurrentName = False, returnDisplayName = False, returnEffectiveName = False, returnHasChangedFields = False, returnHasChangedObjects = False, returnHasChangedRelationships = False, returnIsInDB = False, returnIsSkywardModule = False, returnModifiedTime = False, returnPendingName = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(ModuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createModule(EntityID = 1, setModuleID = None, setChangeType = None, setContainsAtLeastOneNonTempDataObject = None, setCreatedTime = None, setCurrentName = None, setDisplayName = None, setEffectiveName = None, setHasChangedFields = None, setHasChangedObjects = None, setHasChangedRelationships = None, setIsInDB = None, setIsSkywardModule = None, setModifiedTime = None, setPendingName = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnModuleID = False, returnChangeType = False, returnContainsAtLeastOneNonTempDataObject = False, returnCreatedTime = False, returnCurrentName = False, returnDisplayName = False, returnEffectiveName = False, returnHasChangedFields = False, returnHasChangedObjects = False, returnHasChangedRelationships = False, returnIsInDB = False, returnIsSkywardModule = False, returnModifiedTime = False, returnPendingName = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteModule(ModuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Module/" + str(ModuleID), verb = "delete")


def getEveryModulePath(searchConditions = [], EntityID = 1, returnModulePathID = False, returnAliasAction = False, returnAliasIsWorkflow = False, returnAliasModule = False, returnAliasObject = False, returnAverageLoadTimeMilliseconds = False, returnController = False, returnControllerDataObjectTypeIdentifier = False, returnControllerScreen = False, returnControllerSkywardID = False, returnCreateAccess = False, returnCreateAccessCode = False, returnCreatedTime = False, returnDataObjectTypeIdentifier = False, returnDataObjectTypeName = False, returnDataObjectTypeNameObjectID = False, returnDeleteAccess = False, returnDeleteAccessCode = False, returnFullAlias = False, returnIsAnonymous = False, returnIsFullPageLoad = False, returnIsListScreen = False, returnIsProfileScreen = False, returnIsSession = False, returnIsSkywardDefined = False, returnMassCreateAccess = False, returnMassCreateAccessCode = False, returnMassDeleteAccess = False, returnMassDeleteAccessCode = False, returnMassUpdateAccess = False, returnMassUpdateAccessCode = False, returnMaximumLoadTimeMilliseconds = False, returnMinimumLoadTimeMilliseconds = False, returnMobileCreateAccess = False, returnMobileCreateAccessCode = False, returnMobileDeleteAccess = False, returnMobileDeleteAccessCode = False, returnMobileMassCreateAccess = False, returnMobileMassCreateAccessCode = False, returnMobileMassDeleteAccess = False, returnMobileMassDeleteAccessCode = False, returnMobileMassUpdateAccess = False, returnMobileMassUpdateAccessCode = False, returnMobileReadAccess = False, returnMobileReadAccessCode = False, returnMobileUpdateAccess = False, returnMobileUpdateAccessCode = False, returnModifiedTime = False, returnModule = False, returnModuleController = False, returnNonReadOnlyImpersonationBlacklist = False, returnPageLoadCount = False, returnPortal = False, returnPortalCode = False, returnProfile_Module = False, returnProfile_Object = False, returnProfileID = False, returnReadAccess = False, returnReadAccessCode = False, returnReadOnlyImpersonationWhitelist = False, returnScreen = False, returnScreenLayoutChanges = False, returnScreenXML = False, returnShowReportType = False, returnShowReportTypeCode = False, returnSkipAntiForgeryTokenCheck = False, returnSkipLicense = False, returnSkywardHash = False, returnSkywardID = False, returnUpdateAccess = False, returnUpdateAccessCode = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidateSessionForFullPageLoad = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ModulePath in the district.

    This function returns a dataframe of every ModulePath in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getModulePath(ModulePathID, EntityID = 1, returnModulePathID = False, returnAliasAction = False, returnAliasIsWorkflow = False, returnAliasModule = False, returnAliasObject = False, returnAverageLoadTimeMilliseconds = False, returnController = False, returnControllerDataObjectTypeIdentifier = False, returnControllerScreen = False, returnControllerSkywardID = False, returnCreateAccess = False, returnCreateAccessCode = False, returnCreatedTime = False, returnDataObjectTypeIdentifier = False, returnDataObjectTypeName = False, returnDataObjectTypeNameObjectID = False, returnDeleteAccess = False, returnDeleteAccessCode = False, returnFullAlias = False, returnIsAnonymous = False, returnIsFullPageLoad = False, returnIsListScreen = False, returnIsProfileScreen = False, returnIsSession = False, returnIsSkywardDefined = False, returnMassCreateAccess = False, returnMassCreateAccessCode = False, returnMassDeleteAccess = False, returnMassDeleteAccessCode = False, returnMassUpdateAccess = False, returnMassUpdateAccessCode = False, returnMaximumLoadTimeMilliseconds = False, returnMinimumLoadTimeMilliseconds = False, returnMobileCreateAccess = False, returnMobileCreateAccessCode = False, returnMobileDeleteAccess = False, returnMobileDeleteAccessCode = False, returnMobileMassCreateAccess = False, returnMobileMassCreateAccessCode = False, returnMobileMassDeleteAccess = False, returnMobileMassDeleteAccessCode = False, returnMobileMassUpdateAccess = False, returnMobileMassUpdateAccessCode = False, returnMobileReadAccess = False, returnMobileReadAccessCode = False, returnMobileUpdateAccess = False, returnMobileUpdateAccessCode = False, returnModifiedTime = False, returnModule = False, returnModuleController = False, returnNonReadOnlyImpersonationBlacklist = False, returnPageLoadCount = False, returnPortal = False, returnPortalCode = False, returnProfile_Module = False, returnProfile_Object = False, returnProfileID = False, returnReadAccess = False, returnReadAccessCode = False, returnReadOnlyImpersonationWhitelist = False, returnScreen = False, returnScreenLayoutChanges = False, returnScreenXML = False, returnShowReportType = False, returnShowReportTypeCode = False, returnSkipAntiForgeryTokenCheck = False, returnSkipLicense = False, returnSkywardHash = False, returnSkywardID = False, returnUpdateAccess = False, returnUpdateAccessCode = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidateSessionForFullPageLoad = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(ModulePathID), verb = "get", return_params_list = return_params)

def modifyModulePath(ModulePathID, EntityID = 1, setModulePathID = None, setAliasAction = None, setAliasIsWorkflow = None, setAliasModule = None, setAliasObject = None, setAverageLoadTimeMilliseconds = None, setController = None, setControllerDataObjectTypeIdentifier = None, setControllerScreen = None, setControllerSkywardID = None, setCreateAccess = None, setCreateAccessCode = None, setCreatedTime = None, setDataObjectTypeIdentifier = None, setDataObjectTypeName = None, setDataObjectTypeNameObjectID = None, setDeleteAccess = None, setDeleteAccessCode = None, setFullAlias = None, setIsAnonymous = None, setIsFullPageLoad = None, setIsListScreen = None, setIsProfileScreen = None, setIsSession = None, setIsSkywardDefined = None, setMassCreateAccess = None, setMassCreateAccessCode = None, setMassDeleteAccess = None, setMassDeleteAccessCode = None, setMassUpdateAccess = None, setMassUpdateAccessCode = None, setMaximumLoadTimeMilliseconds = None, setMinimumLoadTimeMilliseconds = None, setMobileCreateAccess = None, setMobileCreateAccessCode = None, setMobileDeleteAccess = None, setMobileDeleteAccessCode = None, setMobileMassCreateAccess = None, setMobileMassCreateAccessCode = None, setMobileMassDeleteAccess = None, setMobileMassDeleteAccessCode = None, setMobileMassUpdateAccess = None, setMobileMassUpdateAccessCode = None, setMobileReadAccess = None, setMobileReadAccessCode = None, setMobileUpdateAccess = None, setMobileUpdateAccessCode = None, setModifiedTime = None, setModule = None, setModuleController = None, setNonReadOnlyImpersonationBlacklist = None, setPageLoadCount = None, setPortal = None, setPortalCode = None, setProfile_Module = None, setProfile_Object = None, setProfileID = None, setReadAccess = None, setReadAccessCode = None, setReadOnlyImpersonationWhitelist = None, setScreen = None, setScreenLayoutChanges = None, setScreenXML = None, setShowReportType = None, setShowReportTypeCode = None, setSkipAntiForgeryTokenCheck = None, setSkipLicense = None, setSkywardHash = None, setSkywardID = None, setUpdateAccess = None, setUpdateAccessCode = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidateSessionForFullPageLoad = None, returnModulePathID = False, returnAliasAction = False, returnAliasIsWorkflow = False, returnAliasModule = False, returnAliasObject = False, returnAverageLoadTimeMilliseconds = False, returnController = False, returnControllerDataObjectTypeIdentifier = False, returnControllerScreen = False, returnControllerSkywardID = False, returnCreateAccess = False, returnCreateAccessCode = False, returnCreatedTime = False, returnDataObjectTypeIdentifier = False, returnDataObjectTypeName = False, returnDataObjectTypeNameObjectID = False, returnDeleteAccess = False, returnDeleteAccessCode = False, returnFullAlias = False, returnIsAnonymous = False, returnIsFullPageLoad = False, returnIsListScreen = False, returnIsProfileScreen = False, returnIsSession = False, returnIsSkywardDefined = False, returnMassCreateAccess = False, returnMassCreateAccessCode = False, returnMassDeleteAccess = False, returnMassDeleteAccessCode = False, returnMassUpdateAccess = False, returnMassUpdateAccessCode = False, returnMaximumLoadTimeMilliseconds = False, returnMinimumLoadTimeMilliseconds = False, returnMobileCreateAccess = False, returnMobileCreateAccessCode = False, returnMobileDeleteAccess = False, returnMobileDeleteAccessCode = False, returnMobileMassCreateAccess = False, returnMobileMassCreateAccessCode = False, returnMobileMassDeleteAccess = False, returnMobileMassDeleteAccessCode = False, returnMobileMassUpdateAccess = False, returnMobileMassUpdateAccessCode = False, returnMobileReadAccess = False, returnMobileReadAccessCode = False, returnMobileUpdateAccess = False, returnMobileUpdateAccessCode = False, returnModifiedTime = False, returnModule = False, returnModuleController = False, returnNonReadOnlyImpersonationBlacklist = False, returnPageLoadCount = False, returnPortal = False, returnPortalCode = False, returnProfile_Module = False, returnProfile_Object = False, returnProfileID = False, returnReadAccess = False, returnReadAccessCode = False, returnReadOnlyImpersonationWhitelist = False, returnScreen = False, returnScreenLayoutChanges = False, returnScreenXML = False, returnShowReportType = False, returnShowReportTypeCode = False, returnSkipAntiForgeryTokenCheck = False, returnSkipLicense = False, returnSkywardHash = False, returnSkywardID = False, returnUpdateAccess = False, returnUpdateAccessCode = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidateSessionForFullPageLoad = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(ModulePathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createModulePath(EntityID = 1, setModulePathID = None, setAliasAction = None, setAliasIsWorkflow = None, setAliasModule = None, setAliasObject = None, setAverageLoadTimeMilliseconds = None, setController = None, setControllerDataObjectTypeIdentifier = None, setControllerScreen = None, setControllerSkywardID = None, setCreateAccess = None, setCreateAccessCode = None, setCreatedTime = None, setDataObjectTypeIdentifier = None, setDataObjectTypeName = None, setDataObjectTypeNameObjectID = None, setDeleteAccess = None, setDeleteAccessCode = None, setFullAlias = None, setIsAnonymous = None, setIsFullPageLoad = None, setIsListScreen = None, setIsProfileScreen = None, setIsSession = None, setIsSkywardDefined = None, setMassCreateAccess = None, setMassCreateAccessCode = None, setMassDeleteAccess = None, setMassDeleteAccessCode = None, setMassUpdateAccess = None, setMassUpdateAccessCode = None, setMaximumLoadTimeMilliseconds = None, setMinimumLoadTimeMilliseconds = None, setMobileCreateAccess = None, setMobileCreateAccessCode = None, setMobileDeleteAccess = None, setMobileDeleteAccessCode = None, setMobileMassCreateAccess = None, setMobileMassCreateAccessCode = None, setMobileMassDeleteAccess = None, setMobileMassDeleteAccessCode = None, setMobileMassUpdateAccess = None, setMobileMassUpdateAccessCode = None, setMobileReadAccess = None, setMobileReadAccessCode = None, setMobileUpdateAccess = None, setMobileUpdateAccessCode = None, setModifiedTime = None, setModule = None, setModuleController = None, setNonReadOnlyImpersonationBlacklist = None, setPageLoadCount = None, setPortal = None, setPortalCode = None, setProfile_Module = None, setProfile_Object = None, setProfileID = None, setReadAccess = None, setReadAccessCode = None, setReadOnlyImpersonationWhitelist = None, setScreen = None, setScreenLayoutChanges = None, setScreenXML = None, setShowReportType = None, setShowReportTypeCode = None, setSkipAntiForgeryTokenCheck = None, setSkipLicense = None, setSkywardHash = None, setSkywardID = None, setUpdateAccess = None, setUpdateAccessCode = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidateSessionForFullPageLoad = None, returnModulePathID = False, returnAliasAction = False, returnAliasIsWorkflow = False, returnAliasModule = False, returnAliasObject = False, returnAverageLoadTimeMilliseconds = False, returnController = False, returnControllerDataObjectTypeIdentifier = False, returnControllerScreen = False, returnControllerSkywardID = False, returnCreateAccess = False, returnCreateAccessCode = False, returnCreatedTime = False, returnDataObjectTypeIdentifier = False, returnDataObjectTypeName = False, returnDataObjectTypeNameObjectID = False, returnDeleteAccess = False, returnDeleteAccessCode = False, returnFullAlias = False, returnIsAnonymous = False, returnIsFullPageLoad = False, returnIsListScreen = False, returnIsProfileScreen = False, returnIsSession = False, returnIsSkywardDefined = False, returnMassCreateAccess = False, returnMassCreateAccessCode = False, returnMassDeleteAccess = False, returnMassDeleteAccessCode = False, returnMassUpdateAccess = False, returnMassUpdateAccessCode = False, returnMaximumLoadTimeMilliseconds = False, returnMinimumLoadTimeMilliseconds = False, returnMobileCreateAccess = False, returnMobileCreateAccessCode = False, returnMobileDeleteAccess = False, returnMobileDeleteAccessCode = False, returnMobileMassCreateAccess = False, returnMobileMassCreateAccessCode = False, returnMobileMassDeleteAccess = False, returnMobileMassDeleteAccessCode = False, returnMobileMassUpdateAccess = False, returnMobileMassUpdateAccessCode = False, returnMobileReadAccess = False, returnMobileReadAccessCode = False, returnMobileUpdateAccess = False, returnMobileUpdateAccessCode = False, returnModifiedTime = False, returnModule = False, returnModuleController = False, returnNonReadOnlyImpersonationBlacklist = False, returnPageLoadCount = False, returnPortal = False, returnPortalCode = False, returnProfile_Module = False, returnProfile_Object = False, returnProfileID = False, returnReadAccess = False, returnReadAccessCode = False, returnReadOnlyImpersonationWhitelist = False, returnScreen = False, returnScreenLayoutChanges = False, returnScreenXML = False, returnShowReportType = False, returnShowReportTypeCode = False, returnSkipAntiForgeryTokenCheck = False, returnSkipLicense = False, returnSkywardHash = False, returnSkywardID = False, returnUpdateAccess = False, returnUpdateAccessCode = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidateSessionForFullPageLoad = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteModulePath(ModulePathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ModulePath/" + str(ModulePathID), verb = "delete")


def getEveryObject(searchConditions = [], EntityID = 1, returnObjectID = False, returnAllowAttachments = False, returnChangeType = False, returnCodeGuidFieldPath = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCustomizationID = False, returnDescriptionGuidFieldPath = False, returnEffectiveDisplayName = False, returnEffectiveName = False, returnFormattedObjectPath = False, returnHasChangedFields = False, returnHasChangedRelationships = False, returnHasDefaultSortGroup = False, returnIsInDB = False, returnIsSkywardObject = False, returnIsTempDataObject = False, returnIsView = False, returnModifiedTime = False, returnModuleID = False, returnNotForDisplayInImporting = False, returnNotForDisplayInReporting = False, returnPendingDisplayName = False, returnPendingFormattedObjectPath = False, returnPendingName = False, returnScope = False, returnScopeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewSQL = False, returnViewSQLText = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Object in the district.

    This function returns a dataframe of every Object in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getObject(ObjectID, EntityID = 1, returnObjectID = False, returnAllowAttachments = False, returnChangeType = False, returnCodeGuidFieldPath = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCustomizationID = False, returnDescriptionGuidFieldPath = False, returnEffectiveDisplayName = False, returnEffectiveName = False, returnFormattedObjectPath = False, returnHasChangedFields = False, returnHasChangedRelationships = False, returnHasDefaultSortGroup = False, returnIsInDB = False, returnIsSkywardObject = False, returnIsTempDataObject = False, returnIsView = False, returnModifiedTime = False, returnModuleID = False, returnNotForDisplayInImporting = False, returnNotForDisplayInReporting = False, returnPendingDisplayName = False, returnPendingFormattedObjectPath = False, returnPendingName = False, returnScope = False, returnScopeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewSQL = False, returnViewSQLText = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(ObjectID), verb = "get", return_params_list = return_params)

def modifyObject(ObjectID, EntityID = 1, setObjectID = None, setAllowAttachments = None, setChangeType = None, setCodeGuidFieldPath = None, setCreatedTime = None, setCurrentDisplayName = None, setCurrentName = None, setCustomizationID = None, setDescriptionGuidFieldPath = None, setEffectiveDisplayName = None, setEffectiveName = None, setFormattedObjectPath = None, setHasChangedFields = None, setHasChangedRelationships = None, setHasDefaultSortGroup = None, setIsInDB = None, setIsSkywardObject = None, setIsTempDataObject = None, setIsView = None, setModifiedTime = None, setModuleID = None, setNotForDisplayInImporting = None, setNotForDisplayInReporting = None, setPendingDisplayName = None, setPendingFormattedObjectPath = None, setPendingName = None, setScope = None, setScopeCode = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setViewSQL = None, setViewSQLText = None, returnObjectID = False, returnAllowAttachments = False, returnChangeType = False, returnCodeGuidFieldPath = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCustomizationID = False, returnDescriptionGuidFieldPath = False, returnEffectiveDisplayName = False, returnEffectiveName = False, returnFormattedObjectPath = False, returnHasChangedFields = False, returnHasChangedRelationships = False, returnHasDefaultSortGroup = False, returnIsInDB = False, returnIsSkywardObject = False, returnIsTempDataObject = False, returnIsView = False, returnModifiedTime = False, returnModuleID = False, returnNotForDisplayInImporting = False, returnNotForDisplayInReporting = False, returnPendingDisplayName = False, returnPendingFormattedObjectPath = False, returnPendingName = False, returnScope = False, returnScopeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewSQL = False, returnViewSQLText = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(ObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createObject(EntityID = 1, setObjectID = None, setAllowAttachments = None, setChangeType = None, setCodeGuidFieldPath = None, setCreatedTime = None, setCurrentDisplayName = None, setCurrentName = None, setCustomizationID = None, setDescriptionGuidFieldPath = None, setEffectiveDisplayName = None, setEffectiveName = None, setFormattedObjectPath = None, setHasChangedFields = None, setHasChangedRelationships = None, setHasDefaultSortGroup = None, setIsInDB = None, setIsSkywardObject = None, setIsTempDataObject = None, setIsView = None, setModifiedTime = None, setModuleID = None, setNotForDisplayInImporting = None, setNotForDisplayInReporting = None, setPendingDisplayName = None, setPendingFormattedObjectPath = None, setPendingName = None, setScope = None, setScopeCode = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setViewSQL = None, setViewSQLText = None, returnObjectID = False, returnAllowAttachments = False, returnChangeType = False, returnCodeGuidFieldPath = False, returnCreatedTime = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCustomizationID = False, returnDescriptionGuidFieldPath = False, returnEffectiveDisplayName = False, returnEffectiveName = False, returnFormattedObjectPath = False, returnHasChangedFields = False, returnHasChangedRelationships = False, returnHasDefaultSortGroup = False, returnIsInDB = False, returnIsSkywardObject = False, returnIsTempDataObject = False, returnIsView = False, returnModifiedTime = False, returnModuleID = False, returnNotForDisplayInImporting = False, returnNotForDisplayInReporting = False, returnPendingDisplayName = False, returnPendingFormattedObjectPath = False, returnPendingName = False, returnScope = False, returnScopeCode = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnViewSQL = False, returnViewSQLText = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteObject(ObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Object/" + str(ObjectID), verb = "delete")


def getEveryOnlinePaymentLog(searchConditions = [], EntityID = 1, returnOnlinePaymentLogID = False, returnCreatedTime = False, returnEndpoint = False, returnEndpointCode = False, returnModifiedTime = False, returnRequestXML = False, returnResponseXML = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OnlinePaymentLog in the district.

    This function returns a dataframe of every OnlinePaymentLog in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOnlinePaymentLog(OnlinePaymentLogID, EntityID = 1, returnOnlinePaymentLogID = False, returnCreatedTime = False, returnEndpoint = False, returnEndpointCode = False, returnModifiedTime = False, returnRequestXML = False, returnResponseXML = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(OnlinePaymentLogID), verb = "get", return_params_list = return_params)

def modifyOnlinePaymentLog(OnlinePaymentLogID, EntityID = 1, setOnlinePaymentLogID = None, setCreatedTime = None, setEndpoint = None, setEndpointCode = None, setModifiedTime = None, setRequestXML = None, setResponseXML = None, setUserAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentLogID = False, returnCreatedTime = False, returnEndpoint = False, returnEndpointCode = False, returnModifiedTime = False, returnRequestXML = False, returnResponseXML = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(OnlinePaymentLogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlinePaymentLog(EntityID = 1, setOnlinePaymentLogID = None, setCreatedTime = None, setEndpoint = None, setEndpointCode = None, setModifiedTime = None, setRequestXML = None, setResponseXML = None, setUserAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentLogID = False, returnCreatedTime = False, returnEndpoint = False, returnEndpointCode = False, returnModifiedTime = False, returnRequestXML = False, returnResponseXML = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlinePaymentLog(OnlinePaymentLogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentLog/" + str(OnlinePaymentLogID), verb = "delete")


def getEveryOnlinePaymentVendor(searchConditions = [], EntityID = 1, returnOnlinePaymentVendorID = False, returnCreatedTime = False, returnEntitySummary = False, returnFeeManagementOnlinePaymentCodeDefault = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnName = False, returnURL = False, returnURLDisplayText = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OnlinePaymentVendor in the district.

    This function returns a dataframe of every OnlinePaymentVendor in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOnlinePaymentVendor(OnlinePaymentVendorID, EntityID = 1, returnOnlinePaymentVendorID = False, returnCreatedTime = False, returnEntitySummary = False, returnFeeManagementOnlinePaymentCodeDefault = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnName = False, returnURL = False, returnURLDisplayText = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(OnlinePaymentVendorID), verb = "get", return_params_list = return_params)

def modifyOnlinePaymentVendor(OnlinePaymentVendorID, EntityID = 1, setOnlinePaymentVendorID = None, setCreatedTime = None, setEntitySummary = None, setFeeManagementOnlinePaymentCodeDefault = None, setModifiedTime = None, setModule = None, setModuleCode = None, setName = None, setURL = None, setURLDisplayText = None, setUserAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentVendorID = False, returnCreatedTime = False, returnEntitySummary = False, returnFeeManagementOnlinePaymentCodeDefault = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnName = False, returnURL = False, returnURLDisplayText = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(OnlinePaymentVendorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlinePaymentVendor(EntityID = 1, setOnlinePaymentVendorID = None, setCreatedTime = None, setEntitySummary = None, setFeeManagementOnlinePaymentCodeDefault = None, setModifiedTime = None, setModule = None, setModuleCode = None, setName = None, setURL = None, setURLDisplayText = None, setUserAccessID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentVendorID = False, returnCreatedTime = False, returnEntitySummary = False, returnFeeManagementOnlinePaymentCodeDefault = False, returnModifiedTime = False, returnModule = False, returnModuleCode = False, returnName = False, returnURL = False, returnURLDisplayText = False, returnUserAccessID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlinePaymentVendor(OnlinePaymentVendorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendor/" + str(OnlinePaymentVendorID), verb = "delete")


def getEveryOnlinePaymentVendorEntity(searchConditions = [], EntityID = 1, returnOnlinePaymentVendorEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlinePaymentVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every OnlinePaymentVendorEntity in the district.

    This function returns a dataframe of every OnlinePaymentVendorEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOnlinePaymentVendorEntity(OnlinePaymentVendorEntityID, EntityID = 1, returnOnlinePaymentVendorEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlinePaymentVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(OnlinePaymentVendorEntityID), verb = "get", return_params_list = return_params)

def modifyOnlinePaymentVendorEntity(OnlinePaymentVendorEntityID, EntityID = 1, setOnlinePaymentVendorEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setOnlinePaymentVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentVendorEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlinePaymentVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(OnlinePaymentVendorEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlinePaymentVendorEntity(EntityID = 1, setOnlinePaymentVendorEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setOnlinePaymentVendorID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlinePaymentVendorEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlinePaymentVendorID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlinePaymentVendorEntity(OnlinePaymentVendorEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/OnlinePaymentVendorEntity/" + str(OnlinePaymentVendorEntityID), verb = "delete")


def getEveryPaymentNoticeLog(searchConditions = [], EntityID = 1, returnPaymentNoticeLogID = False, returnComponentConfirmationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnOnlinePaymentLogID = False, returnPaymentDetailIDFeeManagement = False, returnPaymentDetailIDFoodService = False, returnSuccess = False, returnTransactionConfirmationNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPaidBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PaymentNoticeLog in the district.

    This function returns a dataframe of every PaymentNoticeLog in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPaymentNoticeLog(PaymentNoticeLogID, EntityID = 1, returnPaymentNoticeLogID = False, returnComponentConfirmationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnOnlinePaymentLogID = False, returnPaymentDetailIDFeeManagement = False, returnPaymentDetailIDFoodService = False, returnSuccess = False, returnTransactionConfirmationNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPaidBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(PaymentNoticeLogID), verb = "get", return_params_list = return_params)

def modifyPaymentNoticeLog(PaymentNoticeLogID, EntityID = 1, setPaymentNoticeLogID = None, setComponentConfirmationNumber = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setOnlinePaymentLogID = None, setPaymentDetailIDFeeManagement = None, setPaymentDetailIDFoodService = None, setSuccess = None, setTransactionConfirmationNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDPaidBy = None, returnPaymentNoticeLogID = False, returnComponentConfirmationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnOnlinePaymentLogID = False, returnPaymentDetailIDFeeManagement = False, returnPaymentDetailIDFoodService = False, returnSuccess = False, returnTransactionConfirmationNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPaidBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(PaymentNoticeLogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPaymentNoticeLog(EntityID = 1, setPaymentNoticeLogID = None, setComponentConfirmationNumber = None, setCreatedTime = None, setFailureReason = None, setModifiedTime = None, setOnlinePaymentLogID = None, setPaymentDetailIDFeeManagement = None, setPaymentDetailIDFoodService = None, setSuccess = None, setTransactionConfirmationNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDPaidBy = None, returnPaymentNoticeLogID = False, returnComponentConfirmationNumber = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnOnlinePaymentLogID = False, returnPaymentDetailIDFeeManagement = False, returnPaymentDetailIDFoodService = False, returnSuccess = False, returnTransactionConfirmationNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDPaidBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePaymentNoticeLog(PaymentNoticeLogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/PaymentNoticeLog/" + str(PaymentNoticeLogID), verb = "delete")


def getEveryProfile(searchConditions = [], EntityID = 1, returnProfileID = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Profile in the district.

    This function returns a dataframe of every Profile in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProfile(ProfileID, EntityID = 1, returnProfileID = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(ProfileID), verb = "get", return_params_list = return_params)

def modifyProfile(ProfileID, EntityID = 1, setProfileID = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileID = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(ProfileID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProfile(EntityID = 1, setProfileID = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileID = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProfile(ProfileID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Profile/" + str(ProfileID), verb = "delete")


def getEveryProfileModule(searchConditions = [], EntityID = 1, returnProfileModuleID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnProfileID = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ProfileModule in the district.

    This function returns a dataframe of every ProfileModule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProfileModule(ProfileModuleID, EntityID = 1, returnProfileModuleID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnProfileID = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(ProfileModuleID), verb = "get", return_params_list = return_params)

def modifyProfileModule(ProfileModuleID, EntityID = 1, setProfileModuleID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setIsEnabled = None, setIsSkywardDefined = None, setModifiedTime = None, setProfileID = None, setSkywardDisplayName = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileModuleID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnProfileID = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(ProfileModuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProfileModule(EntityID = 1, setProfileModuleID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setIsEnabled = None, setIsSkywardDefined = None, setModifiedTime = None, setProfileID = None, setSkywardDisplayName = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileModuleID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnProfileID = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProfileModule(ProfileModuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileModule/" + str(ProfileModuleID), verb = "delete")


def getEveryProfileScreen(searchConditions = [], EntityID = 1, returnProfileScreenID = False, returnAttachmentTypeGUID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnProfileModuleID = False, returnRender = False, returnScreen = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ProfileScreen in the district.

    This function returns a dataframe of every ProfileScreen in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getProfileScreen(ProfileScreenID, EntityID = 1, returnProfileScreenID = False, returnAttachmentTypeGUID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnProfileModuleID = False, returnRender = False, returnScreen = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(ProfileScreenID), verb = "get", return_params_list = return_params)

def modifyProfileScreen(ProfileScreenID, EntityID = 1, setProfileScreenID = None, setAttachmentTypeGUID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setIsEnabled = None, setIsSkywardDefined = None, setModifiedTime = None, setModule = None, setObject = None, setProfileModuleID = None, setRender = None, setScreen = None, setSkywardDisplayName = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileScreenID = False, returnAttachmentTypeGUID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnProfileModuleID = False, returnRender = False, returnScreen = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(ProfileScreenID), verb = "post", return_params_list = return_params, payload = payload_params)

def createProfileScreen(EntityID = 1, setProfileScreenID = None, setAttachmentTypeGUID = None, setCreatedTime = None, setDisplayName = None, setDisplayOrder = None, setEffectiveDisplayName = None, setEffectiveDisplayOrder = None, setIsEnabled = None, setIsSkywardDefined = None, setModifiedTime = None, setModule = None, setObject = None, setProfileModuleID = None, setRender = None, setScreen = None, setSkywardDisplayName = None, setSkywardDisplayOrder = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnProfileScreenID = False, returnAttachmentTypeGUID = False, returnCreatedTime = False, returnDisplayName = False, returnDisplayOrder = False, returnEffectiveDisplayName = False, returnEffectiveDisplayOrder = False, returnIsEnabled = False, returnIsSkywardDefined = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnProfileModuleID = False, returnRender = False, returnScreen = False, returnSkywardDisplayName = False, returnSkywardDisplayOrder = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteProfileScreen(ProfileScreenID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ProfileScreen/" + str(ProfileScreenID), verb = "delete")


def getEveryPrompt(searchConditions = [], EntityID = 1, returnPromptID = False, returnColumns = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnDisplayOrder = False, returnFieldPath = False, returnFilter = False, returnFilterCondition = False, returnInputType = False, returnIsSkywardPrompt = False, returnLabel = False, returnLinkedPromptGuid = False, returnModifiedTime = False, returnPresenceType = False, returnPresenceTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Prompt in the district.

    This function returns a dataframe of every Prompt in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPrompt(PromptID, EntityID = 1, returnPromptID = False, returnColumns = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnDisplayOrder = False, returnFieldPath = False, returnFilter = False, returnFilterCondition = False, returnInputType = False, returnIsSkywardPrompt = False, returnLabel = False, returnLinkedPromptGuid = False, returnModifiedTime = False, returnPresenceType = False, returnPresenceTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(PromptID), verb = "get", return_params_list = return_params)

def modifyPrompt(PromptID, EntityID = 1, setPromptID = None, setColumns = None, setCreatedTime = None, setDataObjectFieldPathID = None, setDisplayOrder = None, setFieldPath = None, setFilter = None, setFilterCondition = None, setInputType = None, setIsSkywardPrompt = None, setLabel = None, setLinkedPromptGuid = None, setModifiedTime = None, setPresenceType = None, setPresenceTypeCode = None, setSkywardHash = None, setSkywardID = None, setSorts = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnPromptID = False, returnColumns = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnDisplayOrder = False, returnFieldPath = False, returnFilter = False, returnFilterCondition = False, returnInputType = False, returnIsSkywardPrompt = False, returnLabel = False, returnLinkedPromptGuid = False, returnModifiedTime = False, returnPresenceType = False, returnPresenceTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(PromptID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPrompt(EntityID = 1, setPromptID = None, setColumns = None, setCreatedTime = None, setDataObjectFieldPathID = None, setDisplayOrder = None, setFieldPath = None, setFilter = None, setFilterCondition = None, setInputType = None, setIsSkywardPrompt = None, setLabel = None, setLinkedPromptGuid = None, setModifiedTime = None, setPresenceType = None, setPresenceTypeCode = None, setSkywardHash = None, setSkywardID = None, setSorts = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnPromptID = False, returnColumns = False, returnCreatedTime = False, returnDataObjectFieldPathID = False, returnDisplayOrder = False, returnFieldPath = False, returnFilter = False, returnFilterCondition = False, returnInputType = False, returnIsSkywardPrompt = False, returnLabel = False, returnLinkedPromptGuid = False, returnModifiedTime = False, returnPresenceType = False, returnPresenceTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSorts = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePrompt(PromptID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Prompt/" + str(PromptID), verb = "delete")


def getEveryQuickEntryText(searchConditions = [], EntityID = 1, returnQuickEntryTextID = False, returnCreatedTime = False, returnEntry = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QuickEntryText in the district.

    This function returns a dataframe of every QuickEntryText in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQuickEntryText(QuickEntryTextID, EntityID = 1, returnQuickEntryTextID = False, returnCreatedTime = False, returnEntry = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(QuickEntryTextID), verb = "get", return_params_list = return_params)

def modifyQuickEntryText(QuickEntryTextID, EntityID = 1, setQuickEntryTextID = None, setCreatedTime = None, setEntry = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnQuickEntryTextID = False, returnCreatedTime = False, returnEntry = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(QuickEntryTextID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQuickEntryText(EntityID = 1, setQuickEntryTextID = None, setCreatedTime = None, setEntry = None, setModifiedTime = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDOwner = None, returnQuickEntryTextID = False, returnCreatedTime = False, returnEntry = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDOwner = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQuickEntryText(QuickEntryTextID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/QuickEntryText/" + str(QuickEntryTextID), verb = "delete")


def getEveryRelationship(searchConditions = [], EntityID = 1, returnRelationshipID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentCondition = False, returnCurrentConditionXML = False, returnCurrentDeleteBehavior = False, returnCurrentDeleteBehaviorCode = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFieldIDForeignKeyCurrent = False, returnFieldIDForeignKeyPending = False, returnIsInDB = False, returnIsSkywardRelationship = False, returnModifiedTime = False, returnObjectIDForeignCurrent = False, returnObjectIDForeignPending = False, returnObjectIDPrimary = False, returnPendingCondition = False, returnPendingConditionXML = False, returnPendingDeleteBehavior = False, returnPendingDeleteBehaviorCode = False, returnPendingDisplayName = False, returnPendingName = False, returnPendingType = False, returnPendingTypeCode = False, returnRelationshipIDRelated = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Relationship in the district.

    This function returns a dataframe of every Relationship in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRelationship(RelationshipID, EntityID = 1, returnRelationshipID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentCondition = False, returnCurrentConditionXML = False, returnCurrentDeleteBehavior = False, returnCurrentDeleteBehaviorCode = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFieldIDForeignKeyCurrent = False, returnFieldIDForeignKeyPending = False, returnIsInDB = False, returnIsSkywardRelationship = False, returnModifiedTime = False, returnObjectIDForeignCurrent = False, returnObjectIDForeignPending = False, returnObjectIDPrimary = False, returnPendingCondition = False, returnPendingConditionXML = False, returnPendingDeleteBehavior = False, returnPendingDeleteBehaviorCode = False, returnPendingDisplayName = False, returnPendingName = False, returnPendingType = False, returnPendingTypeCode = False, returnRelationshipIDRelated = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(RelationshipID), verb = "get", return_params_list = return_params)

def modifyRelationship(RelationshipID, EntityID = 1, setRelationshipID = None, setChangeType = None, setCreatedTime = None, setCurrentCondition = None, setCurrentConditionXML = None, setCurrentDeleteBehavior = None, setCurrentDeleteBehaviorCode = None, setCurrentDisplayName = None, setCurrentName = None, setCurrentType = None, setCurrentTypeCode = None, setCustomizationID = None, setFieldIDForeignKeyCurrent = None, setFieldIDForeignKeyPending = None, setIsInDB = None, setIsSkywardRelationship = None, setModifiedTime = None, setObjectIDForeignCurrent = None, setObjectIDForeignPending = None, setObjectIDPrimary = None, setPendingCondition = None, setPendingConditionXML = None, setPendingDeleteBehavior = None, setPendingDeleteBehaviorCode = None, setPendingDisplayName = None, setPendingName = None, setPendingType = None, setPendingTypeCode = None, setRelationshipIDRelated = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRelationshipID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentCondition = False, returnCurrentConditionXML = False, returnCurrentDeleteBehavior = False, returnCurrentDeleteBehaviorCode = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFieldIDForeignKeyCurrent = False, returnFieldIDForeignKeyPending = False, returnIsInDB = False, returnIsSkywardRelationship = False, returnModifiedTime = False, returnObjectIDForeignCurrent = False, returnObjectIDForeignPending = False, returnObjectIDPrimary = False, returnPendingCondition = False, returnPendingConditionXML = False, returnPendingDeleteBehavior = False, returnPendingDeleteBehaviorCode = False, returnPendingDisplayName = False, returnPendingName = False, returnPendingType = False, returnPendingTypeCode = False, returnRelationshipIDRelated = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(RelationshipID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRelationship(EntityID = 1, setRelationshipID = None, setChangeType = None, setCreatedTime = None, setCurrentCondition = None, setCurrentConditionXML = None, setCurrentDeleteBehavior = None, setCurrentDeleteBehaviorCode = None, setCurrentDisplayName = None, setCurrentName = None, setCurrentType = None, setCurrentTypeCode = None, setCustomizationID = None, setFieldIDForeignKeyCurrent = None, setFieldIDForeignKeyPending = None, setIsInDB = None, setIsSkywardRelationship = None, setModifiedTime = None, setObjectIDForeignCurrent = None, setObjectIDForeignPending = None, setObjectIDPrimary = None, setPendingCondition = None, setPendingConditionXML = None, setPendingDeleteBehavior = None, setPendingDeleteBehaviorCode = None, setPendingDisplayName = None, setPendingName = None, setPendingType = None, setPendingTypeCode = None, setRelationshipIDRelated = None, setSkywardHash = None, setSkywardID = None, setStatus = None, setStatusCode = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRelationshipID = False, returnChangeType = False, returnCreatedTime = False, returnCurrentCondition = False, returnCurrentConditionXML = False, returnCurrentDeleteBehavior = False, returnCurrentDeleteBehaviorCode = False, returnCurrentDisplayName = False, returnCurrentName = False, returnCurrentType = False, returnCurrentTypeCode = False, returnCustomizationID = False, returnFieldIDForeignKeyCurrent = False, returnFieldIDForeignKeyPending = False, returnIsInDB = False, returnIsSkywardRelationship = False, returnModifiedTime = False, returnObjectIDForeignCurrent = False, returnObjectIDForeignPending = False, returnObjectIDPrimary = False, returnPendingCondition = False, returnPendingConditionXML = False, returnPendingDeleteBehavior = False, returnPendingDeleteBehaviorCode = False, returnPendingDisplayName = False, returnPendingName = False, returnPendingType = False, returnPendingTypeCode = False, returnRelationshipIDRelated = False, returnSkywardHash = False, returnSkywardID = False, returnStatus = False, returnStatusCode = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRelationship(RelationshipID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Relationship/" + str(RelationshipID), verb = "delete")


def getEveryScheduledImport(searchConditions = [], EntityID = 1, returnScheduledImportID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnEntityID = False, returnEntityIDList = False, returnFileHasHeaderRow = False, returnFiscalYearID = False, returnImportID = False, returnModifiedTime = False, returnName = False, returnNetworkFilePath = False, returnPromptBoundValues = False, returnPromptBoundValuesXML = False, returnPromptsAreUpToDate = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduledImport in the district.

    This function returns a dataframe of every ScheduledImport in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduledImport(ScheduledImportID, EntityID = 1, returnScheduledImportID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnEntityID = False, returnEntityIDList = False, returnFileHasHeaderRow = False, returnFiscalYearID = False, returnImportID = False, returnModifiedTime = False, returnName = False, returnNetworkFilePath = False, returnPromptBoundValues = False, returnPromptBoundValuesXML = False, returnPromptsAreUpToDate = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(ScheduledImportID), verb = "get", return_params_list = return_params)

def modifyScheduledImport(ScheduledImportID, EntityID = 1, setScheduledImportID = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setEntityID = None, setEntityIDList = None, setFileHasHeaderRow = None, setFiscalYearID = None, setImportID = None, setModifiedTime = None, setName = None, setNetworkFilePath = None, setPromptBoundValues = None, setPromptBoundValuesXML = None, setPromptsAreUpToDate = None, setScheduledTaskID = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduledImportID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnEntityID = False, returnEntityIDList = False, returnFileHasHeaderRow = False, returnFiscalYearID = False, returnImportID = False, returnModifiedTime = False, returnName = False, returnNetworkFilePath = False, returnPromptBoundValues = False, returnPromptBoundValuesXML = False, returnPromptsAreUpToDate = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(ScheduledImportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduledImport(EntityID = 1, setScheduledImportID = None, setCachedEntity = None, setCachedFiscalYear = None, setCachedSchoolYear = None, setCreatedTime = None, setEntityID = None, setEntityIDList = None, setFileHasHeaderRow = None, setFiscalYearID = None, setImportID = None, setModifiedTime = None, setName = None, setNetworkFilePath = None, setPromptBoundValues = None, setPromptBoundValuesXML = None, setPromptsAreUpToDate = None, setScheduledTaskID = None, setSchoolYearID = None, setSchoolYearNumericYearOrCurrent = None, setSectionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnScheduledImportID = False, returnCachedEntity = False, returnCachedFiscalYear = False, returnCachedSchoolYear = False, returnCreatedTime = False, returnEntityID = False, returnEntityIDList = False, returnFileHasHeaderRow = False, returnFiscalYearID = False, returnImportID = False, returnModifiedTime = False, returnName = False, returnNetworkFilePath = False, returnPromptBoundValues = False, returnPromptBoundValuesXML = False, returnPromptsAreUpToDate = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnSchoolYearNumericYearOrCurrent = False, returnSectionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduledImport(ScheduledImportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledImport/" + str(ScheduledImportID), verb = "delete")


def getEveryScheduledTask(searchConditions = [], EntityID = 1, returnScheduledTaskID = False, returnCreatedTime = False, returnDayOfTheMonth = False, returnEffectiveStartTime = False, returnEndDate = False, returnFrequency = False, returnFrequencyCode = False, returnFriday = False, returnIsActive = False, returnIsMonthly = False, returnIsProductionOnly = False, returnIsSelfGeneratedFromWorkflow = False, returnIsWeekly = False, returnModifiedTime = False, returnMonday = False, returnName = False, returnParameters = False, returnParametersDictionary = False, returnRepeatInterval = False, returnRepeats = False, returnRepeatUntil = False, returnSaturday = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardStartTime = False, returnStartDate = False, returnStartTime = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWednesday = False, returnWeekOfTheMonth = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduledTask in the district.

    This function returns a dataframe of every ScheduledTask in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduledTask(ScheduledTaskID, EntityID = 1, returnScheduledTaskID = False, returnCreatedTime = False, returnDayOfTheMonth = False, returnEffectiveStartTime = False, returnEndDate = False, returnFrequency = False, returnFrequencyCode = False, returnFriday = False, returnIsActive = False, returnIsMonthly = False, returnIsProductionOnly = False, returnIsSelfGeneratedFromWorkflow = False, returnIsWeekly = False, returnModifiedTime = False, returnMonday = False, returnName = False, returnParameters = False, returnParametersDictionary = False, returnRepeatInterval = False, returnRepeats = False, returnRepeatUntil = False, returnSaturday = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardStartTime = False, returnStartDate = False, returnStartTime = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWednesday = False, returnWeekOfTheMonth = False, returnWorkflowID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(ScheduledTaskID), verb = "get", return_params_list = return_params)

def modifyScheduledTask(ScheduledTaskID, EntityID = 1, setScheduledTaskID = None, setCreatedTime = None, setDayOfTheMonth = None, setEffectiveStartTime = None, setEndDate = None, setFrequency = None, setFrequencyCode = None, setFriday = None, setIsActive = None, setIsMonthly = None, setIsProductionOnly = None, setIsSelfGeneratedFromWorkflow = None, setIsWeekly = None, setModifiedTime = None, setMonday = None, setName = None, setParameters = None, setParametersDictionary = None, setRepeatInterval = None, setRepeats = None, setRepeatUntil = None, setSaturday = None, setSkywardHash = None, setSkywardID = None, setSkywardStartTime = None, setStartDate = None, setStartTime = None, setSunday = None, setThursday = None, setTuesday = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWednesday = None, setWeekOfTheMonth = None, setWorkflowID = None, returnScheduledTaskID = False, returnCreatedTime = False, returnDayOfTheMonth = False, returnEffectiveStartTime = False, returnEndDate = False, returnFrequency = False, returnFrequencyCode = False, returnFriday = False, returnIsActive = False, returnIsMonthly = False, returnIsProductionOnly = False, returnIsSelfGeneratedFromWorkflow = False, returnIsWeekly = False, returnModifiedTime = False, returnMonday = False, returnName = False, returnParameters = False, returnParametersDictionary = False, returnRepeatInterval = False, returnRepeats = False, returnRepeatUntil = False, returnSaturday = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardStartTime = False, returnStartDate = False, returnStartTime = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWednesday = False, returnWeekOfTheMonth = False, returnWorkflowID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(ScheduledTaskID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduledTask(EntityID = 1, setScheduledTaskID = None, setCreatedTime = None, setDayOfTheMonth = None, setEffectiveStartTime = None, setEndDate = None, setFrequency = None, setFrequencyCode = None, setFriday = None, setIsActive = None, setIsMonthly = None, setIsProductionOnly = None, setIsSelfGeneratedFromWorkflow = None, setIsWeekly = None, setModifiedTime = None, setMonday = None, setName = None, setParameters = None, setParametersDictionary = None, setRepeatInterval = None, setRepeats = None, setRepeatUntil = None, setSaturday = None, setSkywardHash = None, setSkywardID = None, setSkywardStartTime = None, setStartDate = None, setStartTime = None, setSunday = None, setThursday = None, setTuesday = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWednesday = None, setWeekOfTheMonth = None, setWorkflowID = None, returnScheduledTaskID = False, returnCreatedTime = False, returnDayOfTheMonth = False, returnEffectiveStartTime = False, returnEndDate = False, returnFrequency = False, returnFrequencyCode = False, returnFriday = False, returnIsActive = False, returnIsMonthly = False, returnIsProductionOnly = False, returnIsSelfGeneratedFromWorkflow = False, returnIsWeekly = False, returnModifiedTime = False, returnMonday = False, returnName = False, returnParameters = False, returnParametersDictionary = False, returnRepeatInterval = False, returnRepeats = False, returnRepeatUntil = False, returnSaturday = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardStartTime = False, returnStartDate = False, returnStartTime = False, returnSunday = False, returnThursday = False, returnTuesday = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWednesday = False, returnWeekOfTheMonth = False, returnWorkflowID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduledTask(ScheduledTaskID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTask/" + str(ScheduledTaskID), verb = "delete")


def getEveryScheduledTaskInstance(searchConditions = [], EntityID = 1, returnScheduledTaskInstanceID = False, returnCreatedTime = False, returnExecutionTime = False, returnIsPaused = False, returnModifiedTime = False, returnName = False, returnScheduledTaskID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduledTaskInstance in the district.

    This function returns a dataframe of every ScheduledTaskInstance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduledTaskInstance(ScheduledTaskInstanceID, EntityID = 1, returnScheduledTaskInstanceID = False, returnCreatedTime = False, returnExecutionTime = False, returnIsPaused = False, returnModifiedTime = False, returnName = False, returnScheduledTaskID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(ScheduledTaskInstanceID), verb = "get", return_params_list = return_params)

def modifyScheduledTaskInstance(ScheduledTaskInstanceID, EntityID = 1, setScheduledTaskInstanceID = None, setCreatedTime = None, setExecutionTime = None, setIsPaused = None, setModifiedTime = None, setName = None, setScheduledTaskID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowID = None, returnScheduledTaskInstanceID = False, returnCreatedTime = False, returnExecutionTime = False, returnIsPaused = False, returnModifiedTime = False, returnName = False, returnScheduledTaskID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(ScheduledTaskInstanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduledTaskInstance(EntityID = 1, setScheduledTaskInstanceID = None, setCreatedTime = None, setExecutionTime = None, setIsPaused = None, setModifiedTime = None, setName = None, setScheduledTaskID = None, setStatus = None, setStatusCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowID = None, returnScheduledTaskInstanceID = False, returnCreatedTime = False, returnExecutionTime = False, returnIsPaused = False, returnModifiedTime = False, returnName = False, returnScheduledTaskID = False, returnStatus = False, returnStatusCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduledTaskInstance(ScheduledTaskInstanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskInstance/" + str(ScheduledTaskInstanceID), verb = "delete")


def getEveryScheduledTaskParameterData(searchConditions = [], EntityID = 1, returnScheduledTaskParameterDataID = False, returnCalendarYearID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityID = False, returnFiscalYearID = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowVersionIDAsOfScheduling = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ScheduledTaskParameterData in the district.

    This function returns a dataframe of every ScheduledTaskParameterData in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getScheduledTaskParameterData(ScheduledTaskParameterDataID, EntityID = 1, returnScheduledTaskParameterDataID = False, returnCalendarYearID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityID = False, returnFiscalYearID = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowVersionIDAsOfScheduling = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(ScheduledTaskParameterDataID), verb = "get", return_params_list = return_params)

def modifyScheduledTaskParameterData(ScheduledTaskParameterDataID, EntityID = 1, setScheduledTaskParameterDataID = None, setCalendarYearID = None, setCreatedTime = None, setDistrictID = None, setEntityID = None, setFiscalYearID = None, setModifiedTime = None, setScheduledTaskID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowVersionIDAsOfScheduling = None, returnScheduledTaskParameterDataID = False, returnCalendarYearID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityID = False, returnFiscalYearID = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowVersionIDAsOfScheduling = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(ScheduledTaskParameterDataID), verb = "post", return_params_list = return_params, payload = payload_params)

def createScheduledTaskParameterData(EntityID = 1, setScheduledTaskParameterDataID = None, setCalendarYearID = None, setCreatedTime = None, setDistrictID = None, setEntityID = None, setFiscalYearID = None, setModifiedTime = None, setScheduledTaskID = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowVersionIDAsOfScheduling = None, returnScheduledTaskParameterDataID = False, returnCalendarYearID = False, returnCreatedTime = False, returnDistrictID = False, returnEntityID = False, returnFiscalYearID = False, returnModifiedTime = False, returnScheduledTaskID = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowVersionIDAsOfScheduling = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteScheduledTaskParameterData(ScheduledTaskParameterDataID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ScheduledTaskParameterData/" + str(ScheduledTaskParameterDataID), verb = "delete")


def getEverySchemaHistory(searchConditions = [], EntityID = 1, returnSchemaHistoryID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnField = False, returnIndex = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPreviousField = False, returnPreviousIndex = False, returnPreviousModule = False, returnPreviousObject = False, returnReleaseVersion = False, returnScope = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchemaHistory in the district.

    This function returns a dataframe of every SchemaHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchemaHistory(SchemaHistoryID, EntityID = 1, returnSchemaHistoryID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnField = False, returnIndex = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPreviousField = False, returnPreviousIndex = False, returnPreviousModule = False, returnPreviousObject = False, returnReleaseVersion = False, returnScope = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(SchemaHistoryID), verb = "get", return_params_list = return_params)

def modifySchemaHistory(SchemaHistoryID, EntityID = 1, setSchemaHistoryID = None, setChangeType = None, setChangeTypeCode = None, setCreatedTime = None, setField = None, setIndex = None, setModifiedTime = None, setModule = None, setObject = None, setPreviousField = None, setPreviousIndex = None, setPreviousModule = None, setPreviousObject = None, setReleaseVersion = None, setScope = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchemaHistoryID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnField = False, returnIndex = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPreviousField = False, returnPreviousIndex = False, returnPreviousModule = False, returnPreviousObject = False, returnReleaseVersion = False, returnScope = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(SchemaHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchemaHistory(EntityID = 1, setSchemaHistoryID = None, setChangeType = None, setChangeTypeCode = None, setCreatedTime = None, setField = None, setIndex = None, setModifiedTime = None, setModule = None, setObject = None, setPreviousField = None, setPreviousIndex = None, setPreviousModule = None, setPreviousObject = None, setReleaseVersion = None, setScope = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchemaHistoryID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnField = False, returnIndex = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnPreviousField = False, returnPreviousIndex = False, returnPreviousModule = False, returnPreviousObject = False, returnReleaseVersion = False, returnScope = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchemaHistory(SchemaHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SchemaHistory/" + str(SchemaHistoryID), verb = "delete")


def getEverySkywardConfiguration(searchConditions = [], EntityID = 1, returnSkywardConfigurationID = False, returnAppPoolDecryptionKey = False, returnAppPoolValidationKey = False, returnCreatedTime = False, returnEncryptionKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SkywardConfiguration in the district.

    This function returns a dataframe of every SkywardConfiguration in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSkywardConfiguration(SkywardConfigurationID, EntityID = 1, returnSkywardConfigurationID = False, returnAppPoolDecryptionKey = False, returnAppPoolValidationKey = False, returnCreatedTime = False, returnEncryptionKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(SkywardConfigurationID), verb = "get", return_params_list = return_params)

def modifySkywardConfiguration(SkywardConfigurationID, EntityID = 1, setSkywardConfigurationID = None, setAppPoolDecryptionKey = None, setAppPoolValidationKey = None, setCreatedTime = None, setEncryptionKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardConfigurationID = False, returnAppPoolDecryptionKey = False, returnAppPoolValidationKey = False, returnCreatedTime = False, returnEncryptionKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(SkywardConfigurationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSkywardConfiguration(EntityID = 1, setSkywardConfigurationID = None, setAppPoolDecryptionKey = None, setAppPoolValidationKey = None, setCreatedTime = None, setEncryptionKey = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSkywardConfigurationID = False, returnAppPoolDecryptionKey = False, returnAppPoolValidationKey = False, returnCreatedTime = False, returnEncryptionKey = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSkywardConfiguration(SkywardConfigurationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SkywardConfiguration/" + str(SkywardConfigurationID), verb = "delete")


def getEveryStandardFilter(searchConditions = [], EntityID = 1, returnStandardFilterID = False, returnButtonText = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDisplayName = False, returnFilter = False, returnFilterCondition = False, returnIsSkywardFilter = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StandardFilter in the district.

    This function returns a dataframe of every StandardFilter in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStandardFilter(StandardFilterID, EntityID = 1, returnStandardFilterID = False, returnButtonText = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDisplayName = False, returnFilter = False, returnFilterCondition = False, returnIsSkywardFilter = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(StandardFilterID), verb = "get", return_params_list = return_params)

def modifyStandardFilter(StandardFilterID, EntityID = 1, setStandardFilterID = None, setButtonText = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setDisplayName = None, setFilter = None, setFilterCondition = None, setIsSkywardFilter = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardFilterID = False, returnButtonText = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDisplayName = False, returnFilter = False, returnFilterCondition = False, returnIsSkywardFilter = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(StandardFilterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStandardFilter(EntityID = 1, setStandardFilterID = None, setButtonText = None, setCreatedTime = None, setDataModule = None, setDataObject = None, setDisplayName = None, setFilter = None, setFilterCondition = None, setIsSkywardFilter = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardFilterID = False, returnButtonText = False, returnCreatedTime = False, returnDataModule = False, returnDataObject = False, returnDisplayName = False, returnFilter = False, returnFilterCondition = False, returnIsSkywardFilter = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStandardFilter(StandardFilterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilter/" + str(StandardFilterID), verb = "delete")


def getEveryStandardFilterPrompt(searchConditions = [], EntityID = 1, returnStandardFilterPromptID = False, returnCreatedTime = False, returnModifiedTime = False, returnPromptID = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StandardFilterPrompt in the district.

    This function returns a dataframe of every StandardFilterPrompt in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStandardFilterPrompt(StandardFilterPromptID, EntityID = 1, returnStandardFilterPromptID = False, returnCreatedTime = False, returnModifiedTime = False, returnPromptID = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(StandardFilterPromptID), verb = "get", return_params_list = return_params)

def modifyStandardFilterPrompt(StandardFilterPromptID, EntityID = 1, setStandardFilterPromptID = None, setCreatedTime = None, setModifiedTime = None, setPromptID = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardFilterPromptID = False, returnCreatedTime = False, returnModifiedTime = False, returnPromptID = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(StandardFilterPromptID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStandardFilterPrompt(EntityID = 1, setStandardFilterPromptID = None, setCreatedTime = None, setModifiedTime = None, setPromptID = None, setSkywardHash = None, setSkywardID = None, setStandardFilterID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardFilterPromptID = False, returnCreatedTime = False, returnModifiedTime = False, returnPromptID = False, returnSkywardHash = False, returnSkywardID = False, returnStandardFilterID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStandardFilterPrompt(StandardFilterPromptID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardFilterPrompt/" + str(StandardFilterPromptID), verb = "delete")


def getEveryStandardNormalDistribution(searchConditions = [], EntityID = 1, returnStandardNormalDistributionID = False, returnCreatedTime = False, returnModifiedTime = False, returnProbability = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZScore = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StandardNormalDistribution in the district.

    This function returns a dataframe of every StandardNormalDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStandardNormalDistribution(StandardNormalDistributionID, EntityID = 1, returnStandardNormalDistributionID = False, returnCreatedTime = False, returnModifiedTime = False, returnProbability = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZScore = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(StandardNormalDistributionID), verb = "get", return_params_list = return_params)

def modifyStandardNormalDistribution(StandardNormalDistributionID, EntityID = 1, setStandardNormalDistributionID = None, setCreatedTime = None, setModifiedTime = None, setProbability = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZScore = None, returnStandardNormalDistributionID = False, returnCreatedTime = False, returnModifiedTime = False, returnProbability = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZScore = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(StandardNormalDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStandardNormalDistribution(EntityID = 1, setStandardNormalDistributionID = None, setCreatedTime = None, setModifiedTime = None, setProbability = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZScore = None, returnStandardNormalDistributionID = False, returnCreatedTime = False, returnModifiedTime = False, returnProbability = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZScore = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStandardNormalDistribution(StandardNormalDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/StandardNormalDistribution/" + str(StandardNormalDistributionID), verb = "delete")


def getEveryState(searchConditions = [], EntityID = 1, returnStateID = False, returnCode = False, returnCountryCode = False, returnCreatedTime = False, returnDisplayName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every State in the district.

    This function returns a dataframe of every State in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getState(StateID, EntityID = 1, returnStateID = False, returnCode = False, returnCountryCode = False, returnCreatedTime = False, returnDisplayName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(StateID), verb = "get", return_params_list = return_params)

def modifyState(StateID, EntityID = 1, setStateID = None, setCode = None, setCountryCode = None, setCreatedTime = None, setDisplayName = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStateID = False, returnCode = False, returnCountryCode = False, returnCreatedTime = False, returnDisplayName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(StateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createState(EntityID = 1, setStateID = None, setCode = None, setCountryCode = None, setCreatedTime = None, setDisplayName = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStateID = False, returnCode = False, returnCountryCode = False, returnCreatedTime = False, returnDisplayName = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteState(StateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/State/" + str(StateID), verb = "delete")


def getEverySurvey(searchConditions = [], EntityID = 1, returnSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Survey in the district.

    This function returns a dataframe of every Survey in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSurvey(SurveyID, EntityID = 1, returnSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(SurveyID), verb = "get", return_params_list = return_params)

def modifySurvey(SurveyID, EntityID = 1, setSurveyID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(SurveyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSurvey(EntityID = 1, setSurveyID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSurvey(SurveyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Survey/" + str(SurveyID), verb = "delete")


def getEverySurveyAnswer(searchConditions = [], EntityID = 1, returnSurveyAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyInstanceID = False, returnSurveyQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SurveyAnswer in the district.

    This function returns a dataframe of every SurveyAnswer in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSurveyAnswer(SurveyAnswerID, EntityID = 1, returnSurveyAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyInstanceID = False, returnSurveyQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(SurveyAnswerID), verb = "get", return_params_list = return_params)

def modifySurveyAnswer(SurveyAnswerID, EntityID = 1, setSurveyAnswerID = None, setCreatedTime = None, setModifiedTime = None, setSurveyInstanceID = None, setSurveyQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSurveyAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyInstanceID = False, returnSurveyQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(SurveyAnswerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSurveyAnswer(EntityID = 1, setSurveyAnswerID = None, setCreatedTime = None, setModifiedTime = None, setSurveyInstanceID = None, setSurveyQuestionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSurveyAnswerID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyInstanceID = False, returnSurveyQuestionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSurveyAnswer(SurveyAnswerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyAnswer/" + str(SurveyAnswerID), verb = "delete")


def getEverySurveyInstance(searchConditions = [], EntityID = 1, returnSurveyInstanceID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyID = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SurveyInstance in the district.

    This function returns a dataframe of every SurveyInstance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSurveyInstance(SurveyInstanceID, EntityID = 1, returnSurveyInstanceID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyID = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(SurveyInstanceID), verb = "get", return_params_list = return_params)

def modifySurveyInstance(SurveyInstanceID, EntityID = 1, setSurveyInstanceID = None, setCreatedTime = None, setModifiedTime = None, setSurveyID = None, setSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyInstanceID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyID = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(SurveyInstanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSurveyInstance(EntityID = 1, setSurveyInstanceID = None, setCreatedTime = None, setModifiedTime = None, setSurveyID = None, setSystemVersion = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyInstanceID = False, returnCreatedTime = False, returnModifiedTime = False, returnSurveyID = False, returnSystemVersion = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSurveyInstance(SurveyInstanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyInstance/" + str(SurveyInstanceID), verb = "delete")


def getEverySurveyQuestion(searchConditions = [], EntityID = 1, returnSurveyQuestionID = False, returnCreatedTime = False, returnInverse = False, returnModifiedTime = False, returnQuestion = False, returnSkywardHash = False, returnSkywardID = False, returnSortNumber = False, returnSurveyID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SurveyQuestion in the district.

    This function returns a dataframe of every SurveyQuestion in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSurveyQuestion(SurveyQuestionID, EntityID = 1, returnSurveyQuestionID = False, returnCreatedTime = False, returnInverse = False, returnModifiedTime = False, returnQuestion = False, returnSkywardHash = False, returnSkywardID = False, returnSortNumber = False, returnSurveyID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(SurveyQuestionID), verb = "get", return_params_list = return_params)

def modifySurveyQuestion(SurveyQuestionID, EntityID = 1, setSurveyQuestionID = None, setCreatedTime = None, setInverse = None, setModifiedTime = None, setQuestion = None, setSkywardHash = None, setSkywardID = None, setSortNumber = None, setSurveyID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyQuestionID = False, returnCreatedTime = False, returnInverse = False, returnModifiedTime = False, returnQuestion = False, returnSkywardHash = False, returnSkywardID = False, returnSortNumber = False, returnSurveyID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(SurveyQuestionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSurveyQuestion(EntityID = 1, setSurveyQuestionID = None, setCreatedTime = None, setInverse = None, setModifiedTime = None, setQuestion = None, setSkywardHash = None, setSkywardID = None, setSortNumber = None, setSurveyID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSurveyQuestionID = False, returnCreatedTime = False, returnInverse = False, returnModifiedTime = False, returnQuestion = False, returnSkywardHash = False, returnSkywardID = False, returnSortNumber = False, returnSurveyID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSurveyQuestion(SurveyQuestionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SurveyQuestion/" + str(SurveyQuestionID), verb = "delete")


def getEverySystemVersion(searchConditions = [], EntityID = 1, returnSystemVersionID = False, returnBuild = False, returnCreatedTime = False, returnMajor = False, returnMinor = False, returnModifiedTime = False, returnRevision = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVersion = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SystemVersion in the district.

    This function returns a dataframe of every SystemVersion in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSystemVersion(SystemVersionID, EntityID = 1, returnSystemVersionID = False, returnBuild = False, returnCreatedTime = False, returnMajor = False, returnMinor = False, returnModifiedTime = False, returnRevision = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVersion = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(SystemVersionID), verb = "get", return_params_list = return_params)

def modifySystemVersion(SystemVersionID, EntityID = 1, setSystemVersionID = None, setBuild = None, setCreatedTime = None, setMajor = None, setMinor = None, setModifiedTime = None, setRevision = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVersion = None, returnSystemVersionID = False, returnBuild = False, returnCreatedTime = False, returnMajor = False, returnMinor = False, returnModifiedTime = False, returnRevision = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVersion = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(SystemVersionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSystemVersion(EntityID = 1, setSystemVersionID = None, setBuild = None, setCreatedTime = None, setMajor = None, setMinor = None, setModifiedTime = None, setRevision = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVersion = None, returnSystemVersionID = False, returnBuild = False, returnCreatedTime = False, returnMajor = False, returnMinor = False, returnModifiedTime = False, returnRevision = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVersion = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSystemVersion(SystemVersionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/SystemVersion/" + str(SystemVersionID), verb = "delete")


def getEveryTempAttachmentError(searchConditions = [], EntityID = 1, returnTempAttachmentErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAttachmentError in the district.

    This function returns a dataframe of every TempAttachmentError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAttachmentError(TempAttachmentErrorID, EntityID = 1, returnTempAttachmentErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(TempAttachmentErrorID), verb = "get", return_params_list = return_params)

def modifyTempAttachmentError(TempAttachmentErrorID, EntityID = 1, setTempAttachmentErrorID = None, setCreatedTime = None, setErrorMessage = None, setMediaID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAttachmentErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(TempAttachmentErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAttachmentError(EntityID = 1, setTempAttachmentErrorID = None, setCreatedTime = None, setErrorMessage = None, setMediaID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAttachmentErrorID = False, returnCreatedTime = False, returnErrorMessage = False, returnMediaID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAttachmentError(TempAttachmentErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempAttachmentError/" + str(TempAttachmentErrorID), verb = "delete")


def getEveryTempBrowseViewColumn(searchConditions = [], EntityID = 1, returnTempBrowseViewColumnID = False, returnColumnHeaderText = False, returnColumnIndex = False, returnCreatedTime = False, returnFieldName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempBrowseViewColumn in the district.

    This function returns a dataframe of every TempBrowseViewColumn in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempBrowseViewColumn(TempBrowseViewColumnID, EntityID = 1, returnTempBrowseViewColumnID = False, returnColumnHeaderText = False, returnColumnIndex = False, returnCreatedTime = False, returnFieldName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(TempBrowseViewColumnID), verb = "get", return_params_list = return_params)

def modifyTempBrowseViewColumn(TempBrowseViewColumnID, EntityID = 1, setTempBrowseViewColumnID = None, setColumnHeaderText = None, setColumnIndex = None, setCreatedTime = None, setFieldName = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempBrowseViewColumnID = False, returnColumnHeaderText = False, returnColumnIndex = False, returnCreatedTime = False, returnFieldName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(TempBrowseViewColumnID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempBrowseViewColumn(EntityID = 1, setTempBrowseViewColumnID = None, setColumnHeaderText = None, setColumnIndex = None, setCreatedTime = None, setFieldName = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempBrowseViewColumnID = False, returnColumnHeaderText = False, returnColumnIndex = False, returnCreatedTime = False, returnFieldName = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempBrowseViewColumn(TempBrowseViewColumnID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempBrowseViewColumn/" + str(TempBrowseViewColumnID), verb = "delete")


def getEveryTempDiagnostic(searchConditions = [], EntityID = 1, returnTempDiagnosticID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempDiagnostic in the district.

    This function returns a dataframe of every TempDiagnostic in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempDiagnostic(TempDiagnosticID, EntityID = 1, returnTempDiagnosticID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(TempDiagnosticID), verb = "get", return_params_list = return_params)

def modifyTempDiagnostic(TempDiagnosticID, EntityID = 1, setTempDiagnosticID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDiagnosticID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(TempDiagnosticID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDiagnostic(EntityID = 1, setTempDiagnosticID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDiagnosticID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDiagnostic(TempDiagnosticID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempDiagnostic/" + str(TempDiagnosticID), verb = "delete")


def getEveryTempFailedTileYearUpdate(searchConditions = [], EntityID = 1, returnTempFailedTileYearUpdateID = False, returnCreatedTime = False, returnFailedMessage = False, returnModifiedTime = False, returnTileID = False, returnTileName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFailedTileYearUpdate in the district.

    This function returns a dataframe of every TempFailedTileYearUpdate in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFailedTileYearUpdate(TempFailedTileYearUpdateID, EntityID = 1, returnTempFailedTileYearUpdateID = False, returnCreatedTime = False, returnFailedMessage = False, returnModifiedTime = False, returnTileID = False, returnTileName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(TempFailedTileYearUpdateID), verb = "get", return_params_list = return_params)

def modifyTempFailedTileYearUpdate(TempFailedTileYearUpdateID, EntityID = 1, setTempFailedTileYearUpdateID = None, setCreatedTime = None, setFailedMessage = None, setModifiedTime = None, setTileID = None, setTileName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFailedTileYearUpdateID = False, returnCreatedTime = False, returnFailedMessage = False, returnModifiedTime = False, returnTileID = False, returnTileName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(TempFailedTileYearUpdateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFailedTileYearUpdate(EntityID = 1, setTempFailedTileYearUpdateID = None, setCreatedTime = None, setFailedMessage = None, setModifiedTime = None, setTileID = None, setTileName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserName = None, returnTempFailedTileYearUpdateID = False, returnCreatedTime = False, returnFailedMessage = False, returnModifiedTime = False, returnTileID = False, returnTileName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserName = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFailedTileYearUpdate(TempFailedTileYearUpdateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFailedTileYearUpdate/" + str(TempFailedTileYearUpdateID), verb = "delete")


def getEveryTempFieldSelection(searchConditions = [], EntityID = 1, returnTempFieldSelectionID = False, returnCreatedTime = False, returnFieldID = False, returnFieldName = False, returnModifiedTime = False, returnModuleName = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFieldSelection in the district.

    This function returns a dataframe of every TempFieldSelection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFieldSelection(TempFieldSelectionID, EntityID = 1, returnTempFieldSelectionID = False, returnCreatedTime = False, returnFieldID = False, returnFieldName = False, returnModifiedTime = False, returnModuleName = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(TempFieldSelectionID), verb = "get", return_params_list = return_params)

def modifyTempFieldSelection(TempFieldSelectionID, EntityID = 1, setTempFieldSelectionID = None, setCreatedTime = None, setFieldID = None, setFieldName = None, setModifiedTime = None, setModuleName = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFieldSelectionID = False, returnCreatedTime = False, returnFieldID = False, returnFieldName = False, returnModifiedTime = False, returnModuleName = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(TempFieldSelectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFieldSelection(EntityID = 1, setTempFieldSelectionID = None, setCreatedTime = None, setFieldID = None, setFieldName = None, setModifiedTime = None, setModuleName = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFieldSelectionID = False, returnCreatedTime = False, returnFieldID = False, returnFieldName = False, returnModifiedTime = False, returnModuleName = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFieldSelection(TempFieldSelectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempFieldSelection/" + str(TempFieldSelectionID), verb = "delete")


def getEveryTempImportPreviewResultRow(searchConditions = [], EntityID = 1, returnTempImportPreviewResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnImportFileRowNumber = False, returnModifiedTime = False, returnPreviewData = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempImportPreviewResultRow in the district.

    This function returns a dataframe of every TempImportPreviewResultRow in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempImportPreviewResultRow(TempImportPreviewResultRowID, EntityID = 1, returnTempImportPreviewResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnImportFileRowNumber = False, returnModifiedTime = False, returnPreviewData = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(TempImportPreviewResultRowID), verb = "get", return_params_list = return_params)

def modifyTempImportPreviewResultRow(TempImportPreviewResultRowID, EntityID = 1, setTempImportPreviewResultRowID = None, setCreatedTime = None, setErrorMessage = None, setImportFileRowNumber = None, setModifiedTime = None, setPreviewData = None, setResultType = None, setResultTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempImportPreviewResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnImportFileRowNumber = False, returnModifiedTime = False, returnPreviewData = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(TempImportPreviewResultRowID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempImportPreviewResultRow(EntityID = 1, setTempImportPreviewResultRowID = None, setCreatedTime = None, setErrorMessage = None, setImportFileRowNumber = None, setModifiedTime = None, setPreviewData = None, setResultType = None, setResultTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempImportPreviewResultRowID = False, returnCreatedTime = False, returnErrorMessage = False, returnImportFileRowNumber = False, returnModifiedTime = False, returnPreviewData = False, returnResultType = False, returnResultTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempImportPreviewResultRow(TempImportPreviewResultRowID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempImportPreviewResultRow/" + str(TempImportPreviewResultRowID), verb = "delete")


def getEveryTempLoginHistory(searchConditions = [], EntityID = 1, returnTempLoginHistoryID = False, returnBrowserType = False, returnCreatedTime = False, returnDeviceType = False, returnModifiedTime = False, returnOperatingSystemType = False, returnSuccesfulNumberOfLogins = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempLoginHistory in the district.

    This function returns a dataframe of every TempLoginHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempLoginHistory(TempLoginHistoryID, EntityID = 1, returnTempLoginHistoryID = False, returnBrowserType = False, returnCreatedTime = False, returnDeviceType = False, returnModifiedTime = False, returnOperatingSystemType = False, returnSuccesfulNumberOfLogins = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(TempLoginHistoryID), verb = "get", return_params_list = return_params)

def modifyTempLoginHistory(TempLoginHistoryID, EntityID = 1, setTempLoginHistoryID = None, setBrowserType = None, setCreatedTime = None, setDeviceType = None, setModifiedTime = None, setOperatingSystemType = None, setSuccesfulNumberOfLogins = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLoginHistoryID = False, returnBrowserType = False, returnCreatedTime = False, returnDeviceType = False, returnModifiedTime = False, returnOperatingSystemType = False, returnSuccesfulNumberOfLogins = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(TempLoginHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempLoginHistory(EntityID = 1, setTempLoginHistoryID = None, setBrowserType = None, setCreatedTime = None, setDeviceType = None, setModifiedTime = None, setOperatingSystemType = None, setSuccesfulNumberOfLogins = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempLoginHistoryID = False, returnBrowserType = False, returnCreatedTime = False, returnDeviceType = False, returnModifiedTime = False, returnOperatingSystemType = False, returnSuccesfulNumberOfLogins = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempLoginHistory(TempLoginHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempLoginHistory/" + str(TempLoginHistoryID), verb = "delete")


def getEveryTempMassChangeResult(searchConditions = [], EntityID = 1, returnTempMassChangeResultID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnObjectIdentifier = False, returnResult = False, returnResultCode = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempMassChangeResult in the district.

    This function returns a dataframe of every TempMassChangeResult in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempMassChangeResult(TempMassChangeResultID, EntityID = 1, returnTempMassChangeResultID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnObjectIdentifier = False, returnResult = False, returnResultCode = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(TempMassChangeResultID), verb = "get", return_params_list = return_params)

def modifyTempMassChangeResult(TempMassChangeResultID, EntityID = 1, setTempMassChangeResultID = None, setCreatedTime = None, setMessage = None, setModifiedTime = None, setObjectIdentifier = None, setResult = None, setResultCode = None, setType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMassChangeResultID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnObjectIdentifier = False, returnResult = False, returnResultCode = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(TempMassChangeResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempMassChangeResult(EntityID = 1, setTempMassChangeResultID = None, setCreatedTime = None, setMessage = None, setModifiedTime = None, setObjectIdentifier = None, setResult = None, setResultCode = None, setType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMassChangeResultID = False, returnCreatedTime = False, returnMessage = False, returnModifiedTime = False, returnObjectIdentifier = False, returnResult = False, returnResultCode = False, returnType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempMassChangeResult(TempMassChangeResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMassChangeResult/" + str(TempMassChangeResultID), verb = "delete")


def getEveryTempMedia(searchConditions = [], EntityID = 1, returnTempMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnModuleID = False, returnObjectID = False, returnProcessID = False, returnProcessIndicator = False, returnProcessIndicatorCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempMedia in the district.

    This function returns a dataframe of every TempMedia in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempMedia(TempMediaID, EntityID = 1, returnTempMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnModuleID = False, returnObjectID = False, returnProcessID = False, returnProcessIndicator = False, returnProcessIndicatorCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(TempMediaID), verb = "get", return_params_list = return_params)

def modifyTempMedia(TempMediaID, EntityID = 1, setTempMediaID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setModuleID = None, setObjectID = None, setProcessID = None, setProcessIndicator = None, setProcessIndicatorCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnModuleID = False, returnObjectID = False, returnProcessID = False, returnProcessIndicator = False, returnProcessIndicatorCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(TempMediaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempMedia(EntityID = 1, setTempMediaID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setModuleID = None, setObjectID = None, setProcessID = None, setProcessIndicator = None, setProcessIndicatorCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMediaID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnModuleID = False, returnObjectID = False, returnProcessID = False, returnProcessIndicator = False, returnProcessIndicatorCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempMedia(TempMediaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempMedia/" + str(TempMediaID), verb = "delete")


def getEveryTempUploadImportLog(searchConditions = [], EntityID = 1, returnTempUploadImportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempUploadImportLog in the district.

    This function returns a dataframe of every TempUploadImportLog in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempUploadImportLog(TempUploadImportLogID, EntityID = 1, returnTempUploadImportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(TempUploadImportLogID), verb = "get", return_params_list = return_params)

def modifyTempUploadImportLog(TempUploadImportLogID, EntityID = 1, setTempUploadImportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setResult = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUploadImportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(TempUploadImportLogID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempUploadImportLog(EntityID = 1, setTempUploadImportLogID = None, setCreatedTime = None, setFileName = None, setLogID = None, setMessage = None, setModifiedTime = None, setResult = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUploadImportLogID = False, returnCreatedTime = False, returnFileName = False, returnLogID = False, returnMessage = False, returnModifiedTime = False, returnResult = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempUploadImportLog(TempUploadImportLogID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUploadImportLog/" + str(TempUploadImportLogID), verb = "delete")


def getEveryTempUsageHistory(searchConditions = [], EntityID = 1, returnTempUsageHistoryID = False, returnAverageServerResponseTime = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUsageHistoryRecordTotal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempUsageHistory in the district.

    This function returns a dataframe of every TempUsageHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempUsageHistory(TempUsageHistoryID, EntityID = 1, returnTempUsageHistoryID = False, returnAverageServerResponseTime = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUsageHistoryRecordTotal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(TempUsageHistoryID), verb = "get", return_params_list = return_params)

def modifyTempUsageHistory(TempUsageHistoryID, EntityID = 1, setTempUsageHistoryID = None, setAverageServerResponseTime = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUsageHistoryRecordTotal = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUsageHistoryID = False, returnAverageServerResponseTime = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUsageHistoryRecordTotal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(TempUsageHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempUsageHistory(EntityID = 1, setTempUsageHistoryID = None, setAverageServerResponseTime = None, setCreatedTime = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUsageHistoryRecordTotal = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempUsageHistoryID = False, returnAverageServerResponseTime = False, returnCreatedTime = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUsageHistoryRecordTotal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempUsageHistory(TempUsageHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempUsageHistory/" + str(TempUsageHistoryID), verb = "delete")


def getEveryTempValidateBusinessObject(searchConditions = [], EntityID = 1, returnTempValidateBusinessObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempValidateBusinessObject in the district.

    This function returns a dataframe of every TempValidateBusinessObject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempValidateBusinessObject(TempValidateBusinessObjectID, EntityID = 1, returnTempValidateBusinessObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(TempValidateBusinessObjectID), verb = "get", return_params_list = return_params)

def modifyTempValidateBusinessObject(TempValidateBusinessObjectID, EntityID = 1, setTempValidateBusinessObjectID = None, setCreatedTime = None, setModifiedTime = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempValidateBusinessObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(TempValidateBusinessObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempValidateBusinessObject(EntityID = 1, setTempValidateBusinessObjectID = None, setCreatedTime = None, setModifiedTime = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempValidateBusinessObjectID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempValidateBusinessObject(TempValidateBusinessObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/TempValidateBusinessObject/" + str(TempValidateBusinessObjectID), verb = "delete")


def getEveryTheme(searchConditions = [], EntityID = 1, returnThemeID = False, returnCreatedTime = False, returnImageName = False, returnIsDefault = False, returnIsSkywardTheme = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnThemeColors = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Theme in the district.

    This function returns a dataframe of every Theme in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTheme(ThemeID, EntityID = 1, returnThemeID = False, returnCreatedTime = False, returnImageName = False, returnIsDefault = False, returnIsSkywardTheme = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnThemeColors = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(ThemeID), verb = "get", return_params_list = return_params)

def modifyTheme(ThemeID, EntityID = 1, setThemeID = None, setCreatedTime = None, setImageName = None, setIsDefault = None, setIsSkywardTheme = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setThemeColors = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThemeID = False, returnCreatedTime = False, returnImageName = False, returnIsDefault = False, returnIsSkywardTheme = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnThemeColors = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(ThemeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTheme(EntityID = 1, setThemeID = None, setCreatedTime = None, setImageName = None, setIsDefault = None, setIsSkywardTheme = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setThemeColors = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThemeID = False, returnCreatedTime = False, returnImageName = False, returnIsDefault = False, returnIsSkywardTheme = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnThemeColors = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTheme(ThemeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Theme/" + str(ThemeID), verb = "delete")


def getEveryThreadActivity(searchConditions = [], EntityID = 1, returnThreadActivityID = False, returnCreatedTime = False, returnLastSuccess = False, returnLastSuccessTime = False, returnModifiedTime = False, returnServerName = False, returnServiceName = False, returnStartTime = False, returnThreadName = False, returnThreadQueue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ThreadActivity in the district.

    This function returns a dataframe of every ThreadActivity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getThreadActivity(ThreadActivityID, EntityID = 1, returnThreadActivityID = False, returnCreatedTime = False, returnLastSuccess = False, returnLastSuccessTime = False, returnModifiedTime = False, returnServerName = False, returnServiceName = False, returnStartTime = False, returnThreadName = False, returnThreadQueue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(ThreadActivityID), verb = "get", return_params_list = return_params)

def modifyThreadActivity(ThreadActivityID, EntityID = 1, setThreadActivityID = None, setCreatedTime = None, setLastSuccess = None, setLastSuccessTime = None, setModifiedTime = None, setServerName = None, setServiceName = None, setStartTime = None, setThreadName = None, setThreadQueue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThreadActivityID = False, returnCreatedTime = False, returnLastSuccess = False, returnLastSuccessTime = False, returnModifiedTime = False, returnServerName = False, returnServiceName = False, returnStartTime = False, returnThreadName = False, returnThreadQueue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(ThreadActivityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createThreadActivity(EntityID = 1, setThreadActivityID = None, setCreatedTime = None, setLastSuccess = None, setLastSuccessTime = None, setModifiedTime = None, setServerName = None, setServiceName = None, setStartTime = None, setThreadName = None, setThreadQueue = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnThreadActivityID = False, returnCreatedTime = False, returnLastSuccess = False, returnLastSuccessTime = False, returnModifiedTime = False, returnServerName = False, returnServiceName = False, returnStartTime = False, returnThreadName = False, returnThreadQueue = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteThreadActivity(ThreadActivityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ThreadActivity/" + str(ThreadActivityID), verb = "delete")


def getEveryTile(searchConditions = [], EntityID = 1, returnTileID = False, returnAggregationType = False, returnAggregationTypeCode = False, returnAnimate = False, returnAnimateClockwise = False, returnAxisLabelColor = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnChartTileOptions = False, returnChartTitle = False, returnChartType = False, returnChartTypeCode = False, returnCreatedTime = False, returnDashboardID = False, returnDisplayOrder = False, returnDisplayText = False, returnHeight = False, returnIconColor = False, returnIconColorHex = False, returnIconColorRgba = False, returnIsMulticolor = False, returnLabelDisplayType = False, returnLabelDisplayTypeCode = False, returnModifiedTime = False, returnNumberPrefix = False, returnNumberSuffix = False, returnParameters = False, returnPlotHoverEffect = False, returnRotateValues = False, returnShowAlternateHGridColor = False, returnShowAlternateVGridColor = False, returnShowPercentValues = False, returnShowValues = False, returnSizeType = False, returnSizeTypeCode = False, returnTextColor = False, returnTextColorHex = False, returnTextColorRgba = False, returnTileColorType = False, returnTileColorTypeCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseRoundEdges = False, returnWidth = False, returnXAxisLabel = False, returnXAxisVariable = False, returnYAxisLabel = False, returnYAxisVariable = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Tile in the district.

    This function returns a dataframe of every Tile in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTile(TileID, EntityID = 1, returnTileID = False, returnAggregationType = False, returnAggregationTypeCode = False, returnAnimate = False, returnAnimateClockwise = False, returnAxisLabelColor = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnChartTileOptions = False, returnChartTitle = False, returnChartType = False, returnChartTypeCode = False, returnCreatedTime = False, returnDashboardID = False, returnDisplayOrder = False, returnDisplayText = False, returnHeight = False, returnIconColor = False, returnIconColorHex = False, returnIconColorRgba = False, returnIsMulticolor = False, returnLabelDisplayType = False, returnLabelDisplayTypeCode = False, returnModifiedTime = False, returnNumberPrefix = False, returnNumberSuffix = False, returnParameters = False, returnPlotHoverEffect = False, returnRotateValues = False, returnShowAlternateHGridColor = False, returnShowAlternateVGridColor = False, returnShowPercentValues = False, returnShowValues = False, returnSizeType = False, returnSizeTypeCode = False, returnTextColor = False, returnTextColorHex = False, returnTextColorRgba = False, returnTileColorType = False, returnTileColorTypeCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseRoundEdges = False, returnWidth = False, returnXAxisLabel = False, returnXAxisVariable = False, returnYAxisLabel = False, returnYAxisVariable = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(TileID), verb = "get", return_params_list = return_params)

def modifyTile(TileID, EntityID = 1, setTileID = None, setAggregationType = None, setAggregationTypeCode = None, setAnimate = None, setAnimateClockwise = None, setAxisLabelColor = None, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setChartTileOptions = None, setChartTitle = None, setChartType = None, setChartTypeCode = None, setCreatedTime = None, setDashboardID = None, setDisplayOrder = None, setDisplayText = None, setHeight = None, setIconColor = None, setIconColorHex = None, setIconColorRgba = None, setIsMulticolor = None, setLabelDisplayType = None, setLabelDisplayTypeCode = None, setModifiedTime = None, setNumberPrefix = None, setNumberSuffix = None, setParameters = None, setPlotHoverEffect = None, setRotateValues = None, setShowAlternateHGridColor = None, setShowAlternateVGridColor = None, setShowPercentValues = None, setShowValues = None, setSizeType = None, setSizeTypeCode = None, setTextColor = None, setTextColorHex = None, setTextColorRgba = None, setTileColorType = None, setTileColorTypeCode = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseRoundEdges = None, setWidth = None, setXAxisLabel = None, setXAxisVariable = None, setYAxisLabel = None, setYAxisVariable = None, returnTileID = False, returnAggregationType = False, returnAggregationTypeCode = False, returnAnimate = False, returnAnimateClockwise = False, returnAxisLabelColor = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnChartTileOptions = False, returnChartTitle = False, returnChartType = False, returnChartTypeCode = False, returnCreatedTime = False, returnDashboardID = False, returnDisplayOrder = False, returnDisplayText = False, returnHeight = False, returnIconColor = False, returnIconColorHex = False, returnIconColorRgba = False, returnIsMulticolor = False, returnLabelDisplayType = False, returnLabelDisplayTypeCode = False, returnModifiedTime = False, returnNumberPrefix = False, returnNumberSuffix = False, returnParameters = False, returnPlotHoverEffect = False, returnRotateValues = False, returnShowAlternateHGridColor = False, returnShowAlternateVGridColor = False, returnShowPercentValues = False, returnShowValues = False, returnSizeType = False, returnSizeTypeCode = False, returnTextColor = False, returnTextColorHex = False, returnTextColorRgba = False, returnTileColorType = False, returnTileColorTypeCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseRoundEdges = False, returnWidth = False, returnXAxisLabel = False, returnXAxisVariable = False, returnYAxisLabel = False, returnYAxisVariable = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(TileID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTile(EntityID = 1, setTileID = None, setAggregationType = None, setAggregationTypeCode = None, setAnimate = None, setAnimateClockwise = None, setAxisLabelColor = None, setBackgroundColor = None, setBackgroundColorHex = None, setBackgroundColorRgba = None, setChartTileOptions = None, setChartTitle = None, setChartType = None, setChartTypeCode = None, setCreatedTime = None, setDashboardID = None, setDisplayOrder = None, setDisplayText = None, setHeight = None, setIconColor = None, setIconColorHex = None, setIconColorRgba = None, setIsMulticolor = None, setLabelDisplayType = None, setLabelDisplayTypeCode = None, setModifiedTime = None, setNumberPrefix = None, setNumberSuffix = None, setParameters = None, setPlotHoverEffect = None, setRotateValues = None, setShowAlternateHGridColor = None, setShowAlternateVGridColor = None, setShowPercentValues = None, setShowValues = None, setSizeType = None, setSizeTypeCode = None, setTextColor = None, setTextColorHex = None, setTextColorRgba = None, setTileColorType = None, setTileColorTypeCode = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseRoundEdges = None, setWidth = None, setXAxisLabel = None, setXAxisVariable = None, setYAxisLabel = None, setYAxisVariable = None, returnTileID = False, returnAggregationType = False, returnAggregationTypeCode = False, returnAnimate = False, returnAnimateClockwise = False, returnAxisLabelColor = False, returnBackgroundColor = False, returnBackgroundColorHex = False, returnBackgroundColorRgba = False, returnChartTileOptions = False, returnChartTitle = False, returnChartType = False, returnChartTypeCode = False, returnCreatedTime = False, returnDashboardID = False, returnDisplayOrder = False, returnDisplayText = False, returnHeight = False, returnIconColor = False, returnIconColorHex = False, returnIconColorRgba = False, returnIsMulticolor = False, returnLabelDisplayType = False, returnLabelDisplayTypeCode = False, returnModifiedTime = False, returnNumberPrefix = False, returnNumberSuffix = False, returnParameters = False, returnPlotHoverEffect = False, returnRotateValues = False, returnShowAlternateHGridColor = False, returnShowAlternateVGridColor = False, returnShowPercentValues = False, returnShowValues = False, returnSizeType = False, returnSizeTypeCode = False, returnTextColor = False, returnTextColorHex = False, returnTextColorRgba = False, returnTileColorType = False, returnTileColorTypeCode = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseRoundEdges = False, returnWidth = False, returnXAxisLabel = False, returnXAxisVariable = False, returnYAxisLabel = False, returnYAxisVariable = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTile(TileID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/Tile/" + str(TileID), verb = "delete")


def getEveryUNCPath(searchConditions = [], EntityID = 1, returnUNCPathID = False, returnCreatedTime = False, returnDomain = False, returnLocation = False, returnModifiedTime = False, returnPassword = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UNCPath in the district.

    This function returns a dataframe of every UNCPath in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUNCPath(UNCPathID, EntityID = 1, returnUNCPathID = False, returnCreatedTime = False, returnDomain = False, returnLocation = False, returnModifiedTime = False, returnPassword = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(UNCPathID), verb = "get", return_params_list = return_params)

def modifyUNCPath(UNCPathID, EntityID = 1, setUNCPathID = None, setCreatedTime = None, setDomain = None, setLocation = None, setModifiedTime = None, setPassword = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, returnUNCPathID = False, returnCreatedTime = False, returnDomain = False, returnLocation = False, returnModifiedTime = False, returnPassword = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(UNCPathID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUNCPath(EntityID = 1, setUNCPathID = None, setCreatedTime = None, setDomain = None, setLocation = None, setModifiedTime = None, setPassword = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUsername = None, returnUNCPathID = False, returnCreatedTime = False, returnDomain = False, returnLocation = False, returnModifiedTime = False, returnPassword = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUsername = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUNCPath(UNCPathID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UNCPath/" + str(UNCPathID), verb = "delete")


def getEveryUpdateTracker(searchConditions = [], EntityID = 1, returnUpdateTrackerID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnUpdateType = False, returnUpdateTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UpdateTracker in the district.

    This function returns a dataframe of every UpdateTracker in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUpdateTracker(UpdateTrackerID, EntityID = 1, returnUpdateTrackerID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnUpdateType = False, returnUpdateTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(UpdateTrackerID), verb = "get", return_params_list = return_params)

def modifyUpdateTracker(UpdateTrackerID, EntityID = 1, setUpdateTrackerID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setHasBeenProcessed = None, setModifiedTime = None, setUpdateType = None, setUpdateTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUpdateTrackerID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnUpdateType = False, returnUpdateTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(UpdateTrackerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUpdateTracker(EntityID = 1, setUpdateTrackerID = None, setApplySchemaChangeRunID = None, setCreatedTime = None, setHasBeenProcessed = None, setModifiedTime = None, setUpdateType = None, setUpdateTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUpdateTrackerID = False, returnApplySchemaChangeRunID = False, returnCreatedTime = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnUpdateType = False, returnUpdateTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUpdateTracker(UpdateTrackerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UpdateTracker/" + str(UpdateTrackerID), verb = "delete")


def getEveryUsageHistory(searchConditions = [], EntityID = 1, returnUsageHistoryID = False, returnBrowseFilterID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDataObjectID = False, returnEntityID = False, returnFiscalYearID = False, returnFriendlyName = False, returnHostAddress = False, returnHostname = False, returnImpersonationID = False, returnIsFullPageLoad = False, returnModifiedTime = False, returnModule = False, returnModulePath = False, returnNetworkTimeMilliseconds = False, returnObject = False, returnPageGUID = False, returnResponseSize = False, returnSchoolYearID = False, returnScreen = False, returnServerResponseTimeMilliseconds = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWindowGUID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UsageHistory in the district.

    This function returns a dataframe of every UsageHistory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUsageHistory(UsageHistoryID, EntityID = 1, returnUsageHistoryID = False, returnBrowseFilterID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDataObjectID = False, returnEntityID = False, returnFiscalYearID = False, returnFriendlyName = False, returnHostAddress = False, returnHostname = False, returnImpersonationID = False, returnIsFullPageLoad = False, returnModifiedTime = False, returnModule = False, returnModulePath = False, returnNetworkTimeMilliseconds = False, returnObject = False, returnPageGUID = False, returnResponseSize = False, returnSchoolYearID = False, returnScreen = False, returnServerResponseTimeMilliseconds = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWindowGUID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(UsageHistoryID), verb = "get", return_params_list = return_params)

def modifyUsageHistory(UsageHistoryID, EntityID = 1, setUsageHistoryID = None, setBrowseFilterID = None, setBrowseViewID = None, setCreatedTime = None, setDataObjectID = None, setEntityID = None, setFiscalYearID = None, setFriendlyName = None, setHostAddress = None, setHostname = None, setImpersonationID = None, setIsFullPageLoad = None, setModifiedTime = None, setModule = None, setModulePath = None, setNetworkTimeMilliseconds = None, setObject = None, setPageGUID = None, setResponseSize = None, setSchoolYearID = None, setScreen = None, setServerResponseTimeMilliseconds = None, setSessionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWindowGUID = None, returnUsageHistoryID = False, returnBrowseFilterID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDataObjectID = False, returnEntityID = False, returnFiscalYearID = False, returnFriendlyName = False, returnHostAddress = False, returnHostname = False, returnImpersonationID = False, returnIsFullPageLoad = False, returnModifiedTime = False, returnModule = False, returnModulePath = False, returnNetworkTimeMilliseconds = False, returnObject = False, returnPageGUID = False, returnResponseSize = False, returnSchoolYearID = False, returnScreen = False, returnServerResponseTimeMilliseconds = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWindowGUID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(UsageHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUsageHistory(EntityID = 1, setUsageHistoryID = None, setBrowseFilterID = None, setBrowseViewID = None, setCreatedTime = None, setDataObjectID = None, setEntityID = None, setFiscalYearID = None, setFriendlyName = None, setHostAddress = None, setHostname = None, setImpersonationID = None, setIsFullPageLoad = None, setModifiedTime = None, setModule = None, setModulePath = None, setNetworkTimeMilliseconds = None, setObject = None, setPageGUID = None, setResponseSize = None, setSchoolYearID = None, setScreen = None, setServerResponseTimeMilliseconds = None, setSessionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWindowGUID = None, returnUsageHistoryID = False, returnBrowseFilterID = False, returnBrowseViewID = False, returnCreatedTime = False, returnDataObjectID = False, returnEntityID = False, returnFiscalYearID = False, returnFriendlyName = False, returnHostAddress = False, returnHostname = False, returnImpersonationID = False, returnIsFullPageLoad = False, returnModifiedTime = False, returnModule = False, returnModulePath = False, returnNetworkTimeMilliseconds = False, returnObject = False, returnPageGUID = False, returnResponseSize = False, returnSchoolYearID = False, returnScreen = False, returnServerResponseTimeMilliseconds = False, returnSessionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWindowGUID = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUsageHistory(UsageHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsageHistory/" + str(UsageHistoryID), verb = "delete")


def getEveryUserDock(searchConditions = [], EntityID = 1, returnUserDockID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserDock in the district.

    This function returns a dataframe of every UserDock in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserDock(UserDockID, EntityID = 1, returnUserDockID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(UserDockID), verb = "get", return_params_list = return_params)

def modifyUserDock(UserDockID, EntityID = 1, setUserDockID = None, setCreatedTime = None, setDescription = None, setDisplayOrder = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserDockID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(UserDockID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserDock(EntityID = 1, setUserDockID = None, setCreatedTime = None, setDescription = None, setDisplayOrder = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserDockID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserDock(UserDockID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserDock/" + str(UserDockID), verb = "delete")


def getEveryUserFavorite(searchConditions = [], EntityID = 1, returnUserFavoriteID = False, returnCreatedTime = False, returnDisplayOrder = False, returnFriendlyName = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserFavorite in the district.

    This function returns a dataframe of every UserFavorite in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserFavorite(UserFavoriteID, EntityID = 1, returnUserFavoriteID = False, returnCreatedTime = False, returnDisplayOrder = False, returnFriendlyName = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(UserFavoriteID), verb = "get", return_params_list = return_params)

def modifyUserFavorite(UserFavoriteID, EntityID = 1, setUserFavoriteID = None, setCreatedTime = None, setDisplayOrder = None, setFriendlyName = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserFavoriteID = False, returnCreatedTime = False, returnDisplayOrder = False, returnFriendlyName = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(UserFavoriteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserFavorite(EntityID = 1, setUserFavoriteID = None, setCreatedTime = None, setDisplayOrder = None, setFriendlyName = None, setModifiedTime = None, setModule = None, setObject = None, setScreen = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserFavoriteID = False, returnCreatedTime = False, returnDisplayOrder = False, returnFriendlyName = False, returnModifiedTime = False, returnModule = False, returnObject = False, returnScreen = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserFavorite(UserFavoriteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserFavorite/" + str(UserFavoriteID), verb = "delete")


def getEveryUserImportApproval(searchConditions = [], EntityID = 1, returnUserImportApprovalID = False, returnApprovalDate = False, returnCreatedTime = False, returnIsExpired = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserImportApproval in the district.

    This function returns a dataframe of every UserImportApproval in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserImportApproval(UserImportApprovalID, EntityID = 1, returnUserImportApprovalID = False, returnApprovalDate = False, returnCreatedTime = False, returnIsExpired = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(UserImportApprovalID), verb = "get", return_params_list = return_params)

def modifyUserImportApproval(UserImportApprovalID, EntityID = 1, setUserImportApprovalID = None, setApprovalDate = None, setCreatedTime = None, setIsExpired = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserImportApprovalID = False, returnApprovalDate = False, returnCreatedTime = False, returnIsExpired = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(UserImportApprovalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserImportApproval(EntityID = 1, setUserImportApprovalID = None, setApprovalDate = None, setCreatedTime = None, setIsExpired = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserImportApprovalID = False, returnApprovalDate = False, returnCreatedTime = False, returnIsExpired = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserImportApproval(UserImportApprovalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserImportApproval/" + str(UserImportApprovalID), verb = "delete")


def getEveryUserMenuModule(searchConditions = [], EntityID = 1, returnUserMenuModuleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnMenuModuleID = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UserMenuModule in the district.

    This function returns a dataframe of every UserMenuModule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUserMenuModule(UserMenuModuleID, EntityID = 1, returnUserMenuModuleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnMenuModuleID = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(UserMenuModuleID), verb = "get", return_params_list = return_params)

def modifyUserMenuModule(UserMenuModuleID, EntityID = 1, setUserMenuModuleID = None, setCreatedTime = None, setDisplayOrder = None, setMenuModuleID = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserMenuModuleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnMenuModuleID = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(UserMenuModuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUserMenuModule(EntityID = 1, setUserMenuModuleID = None, setCreatedTime = None, setDisplayOrder = None, setMenuModuleID = None, setModifiedTime = None, setUserID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUserMenuModuleID = False, returnCreatedTime = False, returnDisplayOrder = False, returnMenuModuleID = False, returnModifiedTime = False, returnUserID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUserMenuModule(UserMenuModuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UserMenuModule/" + str(UserMenuModuleID), verb = "delete")


def getEveryUsernameStructure(searchConditions = [], EntityID = 1, returnUsernameStructureID = False, returnCharacterLimitGroupID = False, returnCreatedTime = False, returnGroupTruncationOrder = False, returnIsEmployeeEmail = False, returnIsEmployeeUser = False, returnIsGuardianUser = False, returnIsStaffUser = False, returnIsStudentEmail = False, returnIsStudentUser = False, returnLimitCharacterNumber = False, returnLimitCharacterType = False, returnLimitCharacterTypeCode = False, returnMinimumLength = False, returnMinimumTiebreakerLength = False, returnModifiedTime = False, returnPartType = False, returnPartTypeCode = False, returnRank = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every UsernameStructure in the district.

    This function returns a dataframe of every UsernameStructure in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getUsernameStructure(UsernameStructureID, EntityID = 1, returnUsernameStructureID = False, returnCharacterLimitGroupID = False, returnCreatedTime = False, returnGroupTruncationOrder = False, returnIsEmployeeEmail = False, returnIsEmployeeUser = False, returnIsGuardianUser = False, returnIsStaffUser = False, returnIsStudentEmail = False, returnIsStudentUser = False, returnLimitCharacterNumber = False, returnLimitCharacterType = False, returnLimitCharacterTypeCode = False, returnMinimumLength = False, returnMinimumTiebreakerLength = False, returnModifiedTime = False, returnPartType = False, returnPartTypeCode = False, returnRank = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(UsernameStructureID), verb = "get", return_params_list = return_params)

def modifyUsernameStructure(UsernameStructureID, EntityID = 1, setUsernameStructureID = None, setCharacterLimitGroupID = None, setCreatedTime = None, setGroupTruncationOrder = None, setIsEmployeeEmail = None, setIsEmployeeUser = None, setIsGuardianUser = None, setIsStaffUser = None, setIsStudentEmail = None, setIsStudentUser = None, setLimitCharacterNumber = None, setLimitCharacterType = None, setLimitCharacterTypeCode = None, setMinimumLength = None, setMinimumTiebreakerLength = None, setModifiedTime = None, setPartType = None, setPartTypeCode = None, setRank = None, setText = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUsernameStructureID = False, returnCharacterLimitGroupID = False, returnCreatedTime = False, returnGroupTruncationOrder = False, returnIsEmployeeEmail = False, returnIsEmployeeUser = False, returnIsGuardianUser = False, returnIsStaffUser = False, returnIsStudentEmail = False, returnIsStudentUser = False, returnLimitCharacterNumber = False, returnLimitCharacterType = False, returnLimitCharacterTypeCode = False, returnMinimumLength = False, returnMinimumTiebreakerLength = False, returnModifiedTime = False, returnPartType = False, returnPartTypeCode = False, returnRank = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(UsernameStructureID), verb = "post", return_params_list = return_params, payload = payload_params)

def createUsernameStructure(EntityID = 1, setUsernameStructureID = None, setCharacterLimitGroupID = None, setCreatedTime = None, setGroupTruncationOrder = None, setIsEmployeeEmail = None, setIsEmployeeUser = None, setIsGuardianUser = None, setIsStaffUser = None, setIsStudentEmail = None, setIsStudentUser = None, setLimitCharacterNumber = None, setLimitCharacterType = None, setLimitCharacterTypeCode = None, setMinimumLength = None, setMinimumTiebreakerLength = None, setModifiedTime = None, setPartType = None, setPartTypeCode = None, setRank = None, setText = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnUsernameStructureID = False, returnCharacterLimitGroupID = False, returnCreatedTime = False, returnGroupTruncationOrder = False, returnIsEmployeeEmail = False, returnIsEmployeeUser = False, returnIsGuardianUser = False, returnIsStaffUser = False, returnIsStudentEmail = False, returnIsStudentUser = False, returnLimitCharacterNumber = False, returnLimitCharacterType = False, returnLimitCharacterTypeCode = False, returnMinimumLength = False, returnMinimumTiebreakerLength = False, returnModifiedTime = False, returnPartType = False, returnPartTypeCode = False, returnRank = False, returnText = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteUsernameStructure(UsernameStructureID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/UsernameStructure/" + str(UsernameStructureID), verb = "delete")


def getEveryValidationRule(searchConditions = [], EntityID = 1, returnValidationRuleID = False, returnApplyOnDelete = False, returnApplyOnInsert = False, returnApplyOnUpdate = False, returnCondition = False, returnConditionData = False, returnCreatedTime = False, returnField = False, returnIgnoreOnAutoDeleteRelationship = False, returnIsActive = False, returnIsRequiredField = False, returnIsSkywardValidationRule = False, returnMessage = False, returnModifiedTime = False, returnModule = False, returnNullRelationshipBehavior = False, returnNullRelationshipBehaviorCode = False, returnObject = False, returnScreen = False, returnSeverityType = False, returnSeverityTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ValidationRule in the district.

    This function returns a dataframe of every ValidationRule in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getValidationRule(ValidationRuleID, EntityID = 1, returnValidationRuleID = False, returnApplyOnDelete = False, returnApplyOnInsert = False, returnApplyOnUpdate = False, returnCondition = False, returnConditionData = False, returnCreatedTime = False, returnField = False, returnIgnoreOnAutoDeleteRelationship = False, returnIsActive = False, returnIsRequiredField = False, returnIsSkywardValidationRule = False, returnMessage = False, returnModifiedTime = False, returnModule = False, returnNullRelationshipBehavior = False, returnNullRelationshipBehaviorCode = False, returnObject = False, returnScreen = False, returnSeverityType = False, returnSeverityTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(ValidationRuleID), verb = "get", return_params_list = return_params)

def modifyValidationRule(ValidationRuleID, EntityID = 1, setValidationRuleID = None, setApplyOnDelete = None, setApplyOnInsert = None, setApplyOnUpdate = None, setCondition = None, setConditionData = None, setCreatedTime = None, setField = None, setIgnoreOnAutoDeleteRelationship = None, setIsActive = None, setIsRequiredField = None, setIsSkywardValidationRule = None, setMessage = None, setModifiedTime = None, setModule = None, setNullRelationshipBehavior = None, setNullRelationshipBehaviorCode = None, setObject = None, setScreen = None, setSeverityType = None, setSeverityTypeCode = None, setSkywardHash = None, setSkywardID = None, setTask = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnValidationRuleID = False, returnApplyOnDelete = False, returnApplyOnInsert = False, returnApplyOnUpdate = False, returnCondition = False, returnConditionData = False, returnCreatedTime = False, returnField = False, returnIgnoreOnAutoDeleteRelationship = False, returnIsActive = False, returnIsRequiredField = False, returnIsSkywardValidationRule = False, returnMessage = False, returnModifiedTime = False, returnModule = False, returnNullRelationshipBehavior = False, returnNullRelationshipBehaviorCode = False, returnObject = False, returnScreen = False, returnSeverityType = False, returnSeverityTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(ValidationRuleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createValidationRule(EntityID = 1, setValidationRuleID = None, setApplyOnDelete = None, setApplyOnInsert = None, setApplyOnUpdate = None, setCondition = None, setConditionData = None, setCreatedTime = None, setField = None, setIgnoreOnAutoDeleteRelationship = None, setIsActive = None, setIsRequiredField = None, setIsSkywardValidationRule = None, setMessage = None, setModifiedTime = None, setModule = None, setNullRelationshipBehavior = None, setNullRelationshipBehaviorCode = None, setObject = None, setScreen = None, setSeverityType = None, setSeverityTypeCode = None, setSkywardHash = None, setSkywardID = None, setTask = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnValidationRuleID = False, returnApplyOnDelete = False, returnApplyOnInsert = False, returnApplyOnUpdate = False, returnCondition = False, returnConditionData = False, returnCreatedTime = False, returnField = False, returnIgnoreOnAutoDeleteRelationship = False, returnIsActive = False, returnIsRequiredField = False, returnIsSkywardValidationRule = False, returnMessage = False, returnModifiedTime = False, returnModule = False, returnNullRelationshipBehavior = False, returnNullRelationshipBehaviorCode = False, returnObject = False, returnScreen = False, returnSeverityType = False, returnSeverityTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnTask = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteValidationRule(ValidationRuleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValidationRule/" + str(ValidationRuleID), verb = "delete")


def getEveryValueSource(searchConditions = [], EntityID = 1, returnValueSourceID = False, returnBooleanValue = False, returnColumn = False, returnColumnIndex = False, returnCreatedTime = False, returnDataObjectFieldPathIDDisplay = False, returnDataType = False, returnDataTypeCode = False, returnDateTimeDateValue = False, returnDateTimeTimeValue = False, returnDecimalValue = False, returnFieldIDKey = False, returnFilterSearchCondition = False, returnFilterXML = False, returnImportID = False, returnMissingCrossReferenceAction = False, returnModifiedTime = False, returnName = False, returnNumberValue = False, returnPositionStart = False, returnPromptType = False, returnPromptTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSourceType = False, returnSourceTypeCode = False, returnSourceTypeInstance = False, returnTextValue = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnWidth = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ValueSource in the district.

    This function returns a dataframe of every ValueSource in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getValueSource(ValueSourceID, EntityID = 1, returnValueSourceID = False, returnBooleanValue = False, returnColumn = False, returnColumnIndex = False, returnCreatedTime = False, returnDataObjectFieldPathIDDisplay = False, returnDataType = False, returnDataTypeCode = False, returnDateTimeDateValue = False, returnDateTimeTimeValue = False, returnDecimalValue = False, returnFieldIDKey = False, returnFilterSearchCondition = False, returnFilterXML = False, returnImportID = False, returnMissingCrossReferenceAction = False, returnModifiedTime = False, returnName = False, returnNumberValue = False, returnPositionStart = False, returnPromptType = False, returnPromptTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSourceType = False, returnSourceTypeCode = False, returnSourceTypeInstance = False, returnTextValue = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnWidth = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(ValueSourceID), verb = "get", return_params_list = return_params)

def modifyValueSource(ValueSourceID, EntityID = 1, setValueSourceID = None, setBooleanValue = None, setColumn = None, setColumnIndex = None, setCreatedTime = None, setDataObjectFieldPathIDDisplay = None, setDataType = None, setDataTypeCode = None, setDateTimeDateValue = None, setDateTimeTimeValue = None, setDecimalValue = None, setFieldIDKey = None, setFilterSearchCondition = None, setFilterXML = None, setImportID = None, setMissingCrossReferenceAction = None, setModifiedTime = None, setName = None, setNumberValue = None, setPositionStart = None, setPromptType = None, setPromptTypeCode = None, setSkywardHash = None, setSkywardID = None, setSourceType = None, setSourceTypeCode = None, setSourceTypeInstance = None, setTextValue = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setWidth = None, returnValueSourceID = False, returnBooleanValue = False, returnColumn = False, returnColumnIndex = False, returnCreatedTime = False, returnDataObjectFieldPathIDDisplay = False, returnDataType = False, returnDataTypeCode = False, returnDateTimeDateValue = False, returnDateTimeTimeValue = False, returnDecimalValue = False, returnFieldIDKey = False, returnFilterSearchCondition = False, returnFilterXML = False, returnImportID = False, returnMissingCrossReferenceAction = False, returnModifiedTime = False, returnName = False, returnNumberValue = False, returnPositionStart = False, returnPromptType = False, returnPromptTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSourceType = False, returnSourceTypeCode = False, returnSourceTypeInstance = False, returnTextValue = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnWidth = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(ValueSourceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createValueSource(EntityID = 1, setValueSourceID = None, setBooleanValue = None, setColumn = None, setColumnIndex = None, setCreatedTime = None, setDataObjectFieldPathIDDisplay = None, setDataType = None, setDataTypeCode = None, setDateTimeDateValue = None, setDateTimeTimeValue = None, setDecimalValue = None, setFieldIDKey = None, setFilterSearchCondition = None, setFilterXML = None, setImportID = None, setMissingCrossReferenceAction = None, setModifiedTime = None, setName = None, setNumberValue = None, setPositionStart = None, setPromptType = None, setPromptTypeCode = None, setSkywardHash = None, setSkywardID = None, setSourceType = None, setSourceTypeCode = None, setSourceTypeInstance = None, setTextValue = None, setUniqueID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, setWidth = None, returnValueSourceID = False, returnBooleanValue = False, returnColumn = False, returnColumnIndex = False, returnCreatedTime = False, returnDataObjectFieldPathIDDisplay = False, returnDataType = False, returnDataTypeCode = False, returnDateTimeDateValue = False, returnDateTimeTimeValue = False, returnDecimalValue = False, returnFieldIDKey = False, returnFilterSearchCondition = False, returnFilterXML = False, returnImportID = False, returnMissingCrossReferenceAction = False, returnModifiedTime = False, returnName = False, returnNumberValue = False, returnPositionStart = False, returnPromptType = False, returnPromptTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnSourceType = False, returnSourceTypeCode = False, returnSourceTypeInstance = False, returnTextValue = False, returnUniqueID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnWidth = False):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteValueSource(ValueSourceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/SkySys/ValueSource/" + str(ValueSourceID), verb = "delete")