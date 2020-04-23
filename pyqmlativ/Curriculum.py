# This module contains Curriculum functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAcademicStandard(searchConditions = [], EntityID = 1, returnAcademicStandardID = False, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnBackgroundColor = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandard in the district.

    This function returns a dataframe of every AcademicStandard in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandard(AcademicStandardID, EntityID = 1, returnAcademicStandardID = False, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnBackgroundColor = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "get", return_params_list = return_params)

def modifyAcademicStandard(AcademicStandardID, EntityID = 1, setAcademicStandardID = None, setAcademicStandardDefaultID = None, setAcademicStandardGradeRangeID = None, setAcademicStandardIDParent = None, setBackgroundColor = None, setChildAcademicStandardCount = None, setCreatedTime = None, setDescription = None, setDescriptionToUse = None, setDisplayAs = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setExtendedDescription = None, setFullKey = None, setFullKeyPrefix = None, setGrandChildLevelHierarchyDepthDescription = None, setGuid = None, setHierarchyDepthDescription = None, setIsAttachedToASubject = None, setIsHighFrequencyWord = None, setIsLettersAndSounds = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setModifiedTime = None, setNextLevelHierarchyDepthDescription = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTextColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardID = False, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnBackgroundColor = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandard(EntityID = 1, setAcademicStandardID = None, setAcademicStandardDefaultID = None, setAcademicStandardGradeRangeID = None, setAcademicStandardIDParent = None, setBackgroundColor = None, setChildAcademicStandardCount = None, setCreatedTime = None, setDescription = None, setDescriptionToUse = None, setDisplayAs = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setExtendedDescription = None, setFullKey = None, setFullKeyPrefix = None, setGrandChildLevelHierarchyDepthDescription = None, setGuid = None, setHierarchyDepthDescription = None, setIsAttachedToASubject = None, setIsHighFrequencyWord = None, setIsLettersAndSounds = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setModifiedTime = None, setNextLevelHierarchyDepthDescription = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTextColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardID = False, returnAcademicStandardDefaultID = False, returnAcademicStandardGradeRangeID = False, returnAcademicStandardIDParent = False, returnBackgroundColor = False, returnChildAcademicStandardCount = False, returnCreatedTime = False, returnDescription = False, returnDescriptionToUse = False, returnDisplayAs = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnFullKey = False, returnFullKeyPrefix = False, returnGrandChildLevelHierarchyDepthDescription = False, returnGuid = False, returnHierarchyDepthDescription = False, returnIsAttachedToASubject = False, returnIsHighFrequencyWord = False, returnIsLettersAndSounds = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnNextLevelHierarchyDepthDescription = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandard(AcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandard/" + str(AcademicStandardID), verb = "delete")


def getEveryAcademicStandardDefault(searchConditions = [], EntityID = 1, returnAcademicStandardDefaultID = False, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardDefault in the district.

    This function returns a dataframe of every AcademicStandardDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, returnAcademicStandardDefaultID = False, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1, setAcademicStandardDefaultID = None, setAcademicStandardDefaultIDParent = None, setAcademicStandardGradeRangeDefaultID = None, setCreatedTime = None, setDescription = None, setIsHighFrequencyWord = None, setKey = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setModifiedTime = None, setParentGuid = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardDefaultID = False, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardDefault(EntityID = 1, setAcademicStandardDefaultID = None, setAcademicStandardDefaultIDParent = None, setAcademicStandardGradeRangeDefaultID = None, setCreatedTime = None, setDescription = None, setIsHighFrequencyWord = None, setKey = None, setLetterAndSoundType = None, setLetterAndSoundTypeCode = None, setLetterType = None, setLetterTypeCode = None, setLevel = None, setModifiedTime = None, setParentGuid = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardDefaultID = False, returnAcademicStandardDefaultIDParent = False, returnAcademicStandardGradeRangeDefaultID = False, returnCreatedTime = False, returnDescription = False, returnIsHighFrequencyWord = False, returnKey = False, returnLetterAndSoundType = False, returnLetterAndSoundTypeCode = False, returnLetterType = False, returnLetterTypeCode = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardDefault/" + str(AcademicStandardDefaultID), verb = "delete")


def getEveryAcademicStandardGradeRange(searchConditions = [], EntityID = 1, returnAcademicStandardGradeRangeID = False, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardGradeRange in the district.

    This function returns a dataframe of every AcademicStandardGradeRange in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, returnAcademicStandardGradeRangeID = False, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1, setAcademicStandardGradeRangeID = None, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setFullKey = None, setFullKeyPrefix = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setKey = None, setModifiedTime = None, setSequence = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradeRangeID = False, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardGradeRange(EntityID = 1, setAcademicStandardGradeRangeID = None, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setFullKey = None, setFullKeyPrefix = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setKey = None, setModifiedTime = None, setSequence = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradeRangeID = False, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRange/" + str(AcademicStandardGradeRangeID), verb = "delete")


def getEveryAcademicStandardGradeRangeDefault(searchConditions = [], EntityID = 1, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardGradeRangeDefault in the district.

    This function returns a dataframe of every AcademicStandardGradeRangeDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardGradeRangeDefault(EntityID = 1, setAcademicStandardGradeRangeDefaultID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardGradeRangeDefaultID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardGradeRangeDefault/" + str(AcademicStandardGradeRangeDefaultID), verb = "delete")


def getEveryAcademicStandardHierarchyDepth(searchConditions = [], EntityID = 1, returnAcademicStandardHierarchyDepthID = False, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardHierarchyDepth in the district.

    This function returns a dataframe of every AcademicStandardHierarchyDepth in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, returnAcademicStandardHierarchyDepthID = False, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1, setAcademicStandardHierarchyDepthID = None, setAcademicStandardID = None, setAcademicStandardIDAtLevel = None, setCreatedTime = None, setDistrictGroupKey = None, setHierarchyDepthID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardHierarchyDepthID = False, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardHierarchyDepth(EntityID = 1, setAcademicStandardHierarchyDepthID = None, setAcademicStandardID = None, setAcademicStandardIDAtLevel = None, setCreatedTime = None, setDistrictGroupKey = None, setHierarchyDepthID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardHierarchyDepthID = False, returnAcademicStandardID = False, returnAcademicStandardIDAtLevel = False, returnCreatedTime = False, returnDistrictGroupKey = False, returnHierarchyDepthID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardHierarchyDepth/" + str(AcademicStandardHierarchyDepthID), verb = "delete")


def getEveryAcademicStandardSet(searchConditions = [], EntityID = 1, returnAcademicStandardSetID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardSet in the district.

    This function returns a dataframe of every AcademicStandardSet in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardSet(AcademicStandardSetID, EntityID = 1, returnAcademicStandardSetID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardSet(AcademicStandardSetID, EntityID = 1, setAcademicStandardSetID = None, setAcademicStandardSetDefaultID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEnteredByDistrict = None, setIsActive = None, setKey = None, setModifiedTime = None, setStateCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSetID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardSet(EntityID = 1, setAcademicStandardSetID = None, setAcademicStandardSetDefaultID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEnteredByDistrict = None, setIsActive = None, setKey = None, setModifiedTime = None, setStateCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSetID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEnteredByDistrict = False, returnIsActive = False, returnKey = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardSet(AcademicStandardSetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSet/" + str(AcademicStandardSetID), verb = "delete")


def getEveryAcademicStandardSetDefault(searchConditions = [], EntityID = 1, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardSetDefault in the district.

    This function returns a dataframe of every AcademicStandardSetDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardSetDefault(EntityID = 1, setAcademicStandardSetDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSetDefault/" + str(AcademicStandardSetDefaultID), verb = "delete")


def getEveryAcademicStandardSubject(searchConditions = [], EntityID = 1, returnAcademicStandardSubjectID = False, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardSubject in the district.

    This function returns a dataframe of every AcademicStandardSubject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, returnAcademicStandardSubjectID = False, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1, setAcademicStandardSubjectID = None, setAcademicStandardSetID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setFullKey = None, setFullKeyPrefix = None, setKey = None, setModifiedTime = None, setSequence = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setYear = None, returnAcademicStandardSubjectID = False, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardSubject(EntityID = 1, setAcademicStandardSubjectID = None, setAcademicStandardSetID = None, setAcademicStandardSubjectDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setEnteredByDistrict = None, setFullKey = None, setFullKeyPrefix = None, setKey = None, setModifiedTime = None, setSequence = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setYear = None, returnAcademicStandardSubjectID = False, returnAcademicStandardSetID = False, returnAcademicStandardSubjectDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnEnteredByDistrict = False, returnFullKey = False, returnFullKeyPrefix = False, returnKey = False, returnModifiedTime = False, returnSequence = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubject/" + str(AcademicStandardSubjectID), verb = "delete")


def getEveryAcademicStandardSubjectDefault(searchConditions = [], EntityID = 1, returnAcademicStandardSubjectDefaultID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AcademicStandardSubjectDefault in the district.

    This function returns a dataframe of every AcademicStandardSubjectDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, returnAcademicStandardSubjectDefaultID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "get", return_params_list = return_params)

def modifyAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1, setAcademicStandardSubjectDefaultID = None, setAcademicStandardSetDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSubjectDefaultID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAcademicStandardSubjectDefault(EntityID = 1, setAcademicStandardSubjectDefaultID = None, setAcademicStandardSetDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setKey = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAcademicStandardSubjectDefaultID = False, returnAcademicStandardSetDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnKey = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AcademicStandardSubjectDefault/" + str(AcademicStandardSubjectDefaultID), verb = "delete")


def getEveryAssessmentToolMN(searchConditions = [], EntityID = 1, returnAssessmentToolMNID = False, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AssessmentToolMN in the district.

    This function returns a dataframe of every AssessmentToolMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAssessmentToolMN(AssessmentToolMNID, EntityID = 1, returnAssessmentToolMNID = False, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "get", return_params_list = return_params)

def modifyAssessmentToolMN(AssessmentToolMNID, EntityID = 1, setAssessmentToolMNID = None, setAssessmentToolMNIDClonedFrom = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setStateAssessmentToolMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssessmentToolMNID = False, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssessmentToolMN(EntityID = 1, setAssessmentToolMNID = None, setAssessmentToolMNIDClonedFrom = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setStateAssessmentToolMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAssessmentToolMNID = False, returnAssessmentToolMNIDClonedFrom = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateAssessmentToolMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssessmentToolMN(AssessmentToolMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/AssessmentToolMN/" + str(AssessmentToolMNID), verb = "delete")


def getEveryCurriculum(searchConditions = [], EntityID = 1, returnCurriculumID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Curriculum in the district.

    This function returns a dataframe of every Curriculum in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculum(CurriculumID, EntityID = 1, returnCurriculumID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "get", return_params_list = return_params)

def modifyCurriculum(CurriculumID, EntityID = 1, setCurriculumID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurriculumSubAreaExistsForStudentAndSubArea = None, setCurriculumSubAreaExistsForSubAreaWithoutStudent = None, setCurriculumSubjectSummary = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEarnedCredits = None, setGradeLevelSummary = None, setGradReqRankGPAIgnoreDuplicateCheck = None, setGradReqSubjectTypeID = None, setHasPrerequisiteCurriculums = None, setHasPrerequisites = None, setIsActive = None, setIsAllowedToBeSelectedInCareerPlan = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setModifiedTime = None, setNumberOfActiveCurrentOrFutureCourses = None, setNumberOfAttachedSubjects = None, setPrerequisiteCurriculumExistsForPrerequisite = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculum(EntityID = 1, setCurriculumID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurriculumSubAreaExistsForStudentAndSubArea = None, setCurriculumSubAreaExistsForSubAreaWithoutStudent = None, setCurriculumSubjectSummary = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setEarnedCredits = None, setGradeLevelSummary = None, setGradReqRankGPAIgnoreDuplicateCheck = None, setGradReqSubjectTypeID = None, setHasPrerequisiteCurriculums = None, setHasPrerequisites = None, setIsActive = None, setIsAllowedToBeSelectedInCareerPlan = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setModifiedTime = None, setNumberOfActiveCurrentOrFutureCourses = None, setNumberOfAttachedSubjects = None, setPrerequisiteCurriculumExistsForPrerequisite = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumSubAreaExistsForStudentAndSubArea = False, returnCurriculumSubAreaExistsForSubAreaWithoutStudent = False, returnCurriculumSubjectSummary = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEarnedCredits = False, returnGradeLevelSummary = False, returnGradReqRankGPAIgnoreDuplicateCheck = False, returnGradReqSubjectTypeID = False, returnHasPrerequisiteCurriculums = False, returnHasPrerequisites = False, returnIsActive = False, returnIsAllowedToBeSelectedInCareerPlan = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnModifiedTime = False, returnNumberOfActiveCurrentOrFutureCourses = False, returnNumberOfAttachedSubjects = False, returnPrerequisiteCurriculumExistsForPrerequisite = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculum(CurriculumID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Curriculum/" + str(CurriculumID), verb = "delete")


def getEveryCurriculumAcademicStandard(searchConditions = [], EntityID = 1, returnCurriculumAcademicStandardID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumAcademicStandard in the district.

    This function returns a dataframe of every CurriculumAcademicStandard in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, returnCurriculumAcademicStandardID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1, setCurriculumAcademicStandardID = None, setAcademicStandardID = None, setCreatedTime = None, setCurriculumID = None, setDistrictGroupKey = None, setIsGraded = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumAcademicStandardID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumAcademicStandard(EntityID = 1, setCurriculumAcademicStandardID = None, setAcademicStandardID = None, setCreatedTime = None, setCurriculumID = None, setDistrictGroupKey = None, setIsGraded = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumAcademicStandardID = False, returnAcademicStandardID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnIsGraded = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumAcademicStandard/" + str(CurriculumAcademicStandardID), verb = "delete")


def getEveryCurriculumCustomRequirement(searchConditions = [], EntityID = 1, returnCurriculumCustomRequirementID = False, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumCustomRequirement in the district.

    This function returns a dataframe of every CurriculumCustomRequirement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, returnCurriculumCustomRequirementID = False, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "get", return_params_list = return_params)

def modifyCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1, setCurriculumCustomRequirementID = None, setCreatedTime = None, setCurriculumID = None, setCustomRequirementID = None, setDistrictGroupKey = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumCustomRequirementID = False, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumCustomRequirement(EntityID = 1, setCurriculumCustomRequirementID = None, setCreatedTime = None, setCurriculumID = None, setCustomRequirementID = None, setDistrictGroupKey = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumCustomRequirementID = False, returnCreatedTime = False, returnCurriculumID = False, returnCustomRequirementID = False, returnDistrictGroupKey = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumCustomRequirement/" + str(CurriculumCustomRequirementID), verb = "delete")


def getEveryCurriculumGradeLevel(searchConditions = [], EntityID = 1, returnCurriculumGradeLevelID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumGradeLevel in the district.

    This function returns a dataframe of every CurriculumGradeLevel in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, returnCurriculumGradeLevelID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "get", return_params_list = return_params)

def modifyCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1, setCurriculumGradeLevelID = None, setCreatedTime = None, setCurriculumID = None, setDistrictGroupKey = None, setGradeLevelID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumGradeLevelID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumGradeLevel(EntityID = 1, setCurriculumGradeLevelID = None, setCreatedTime = None, setCurriculumID = None, setDistrictGroupKey = None, setGradeLevelID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumGradeLevelID = False, returnCreatedTime = False, returnCurriculumID = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumGradeLevel/" + str(CurriculumGradeLevelID), verb = "delete")


def getEveryCurriculumProgramMN(searchConditions = [], EntityID = 1, returnCurriculumProgramMNID = False, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumProgramMN in the district.

    This function returns a dataframe of every CurriculumProgramMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, returnCurriculumProgramMNID = False, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "get", return_params_list = return_params)

def modifyCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1, setCurriculumProgramMNID = None, setCreatedTime = None, setCurriculumProgramMNIDClonedFrom = None, setCurriculumYearID = None, setModifiedTime = None, setStateCurriculumProgramMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumProgramMNID = False, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumProgramMN(EntityID = 1, setCurriculumProgramMNID = None, setCreatedTime = None, setCurriculumProgramMNIDClonedFrom = None, setCurriculumYearID = None, setModifiedTime = None, setStateCurriculumProgramMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumProgramMNID = False, returnCreatedTime = False, returnCurriculumProgramMNIDClonedFrom = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateCurriculumProgramMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumProgramMN/" + str(CurriculumProgramMNID), verb = "delete")


def getEveryCurriculumSubject(searchConditions = [], EntityID = 1, returnCurriculumSubjectID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumSubject in the district.

    This function returns a dataframe of every CurriculumSubject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumSubject(CurriculumSubjectID, EntityID = 1, returnCurriculumSubjectID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "get", return_params_list = return_params)

def modifyCurriculumSubject(CurriculumSubjectID, EntityID = 1, setCurriculumSubjectID = None, setCreatedTime = None, setCurriculumID = None, setCurriculumSubjectIDClonedFrom = None, setCurriculumSubjectIDClonedTo = None, setDistrictGroupKey = None, setIsDefault = None, setModifiedTime = None, setNumberOfAttachedCurriculumAcademicStandards = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubjectID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumSubject(EntityID = 1, setCurriculumSubjectID = None, setCreatedTime = None, setCurriculumID = None, setCurriculumSubjectIDClonedFrom = None, setCurriculumSubjectIDClonedTo = None, setDistrictGroupKey = None, setIsDefault = None, setModifiedTime = None, setNumberOfAttachedCurriculumAcademicStandards = None, setSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubjectID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumSubjectIDClonedFrom = False, returnCurriculumSubjectIDClonedTo = False, returnDistrictGroupKey = False, returnIsDefault = False, returnModifiedTime = False, returnNumberOfAttachedCurriculumAcademicStandards = False, returnSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumSubject(CurriculumSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubject/" + str(CurriculumSubjectID), verb = "delete")


def getEveryCurriculumSubjectAcademicStandard(searchConditions = [], EntityID = 1, returnCurriculumSubjectAcademicStandardID = False, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumSubjectAcademicStandard in the district.

    This function returns a dataframe of every CurriculumSubjectAcademicStandard in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, returnCurriculumSubjectAcademicStandardID = False, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1, setCurriculumSubjectAcademicStandardID = None, setCreatedTime = None, setCurriculumAcademicStandardID = None, setCurriculumSubjectID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubjectAcademicStandardID = False, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumSubjectAcademicStandard(EntityID = 1, setCurriculumSubjectAcademicStandardID = None, setCreatedTime = None, setCurriculumAcademicStandardID = None, setCurriculumSubjectID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubjectAcademicStandardID = False, returnCreatedTime = False, returnCurriculumAcademicStandardID = False, returnCurriculumSubjectID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumSubjectAcademicStandard/" + str(CurriculumSubjectAcademicStandardID), verb = "delete")


def getEveryCurriculumYear(searchConditions = [], EntityID = 1, returnCurriculumYearID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumYear in the district.

    This function returns a dataframe of every CurriculumYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumYear(CurriculumYearID, EntityID = 1, returnCurriculumYearID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "get", return_params_list = return_params)

def modifyCurriculumYear(CurriculumYearID, EntityID = 1, setCurriculumYearID = None, setCreatedTime = None, setCurriculumID = None, setCurriculumYearIDClonedFrom = None, setCurriculumYearIDClonedTo = None, setCurriculumYearMNID = None, setDescription = None, setDistrictGroupKey = None, setFederalAdvancedPlacementCourseTypeID = None, setFederalSubjectTypeID = None, setHasCourseLevels = None, setIsAdultBasicEducation = None, setIsEndOfCourse = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsFederalProgram = None, setIsGraduationRequirement = None, setIsStateProgram = None, setModifiedTime = None, setReportToFitnessGram = None, setSchoolYearID = None, setStateCourseCodeMNID = None, setStateEarlyEducationLocationMNID = None, setStateStandardAddressedCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSubjectAreaCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumYearID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumYear(EntityID = 1, setCurriculumYearID = None, setCreatedTime = None, setCurriculumID = None, setCurriculumYearIDClonedFrom = None, setCurriculumYearIDClonedTo = None, setCurriculumYearMNID = None, setDescription = None, setDistrictGroupKey = None, setFederalAdvancedPlacementCourseTypeID = None, setFederalSubjectTypeID = None, setHasCourseLevels = None, setIsAdultBasicEducation = None, setIsEndOfCourse = None, setIsFederalDistanceEducation = None, setIsFederalDualEnrollment = None, setIsFederalProgram = None, setIsGraduationRequirement = None, setIsStateProgram = None, setModifiedTime = None, setReportToFitnessGram = None, setSchoolYearID = None, setStateCourseCodeMNID = None, setStateEarlyEducationLocationMNID = None, setStateStandardAddressedCodeMNID = None, setStateSTARAssignmentCodeMNID = None, setStateSubjectAreaCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumYearID = False, returnCreatedTime = False, returnCurriculumID = False, returnCurriculumYearIDClonedFrom = False, returnCurriculumYearIDClonedTo = False, returnCurriculumYearMNID = False, returnDescription = False, returnDistrictGroupKey = False, returnFederalAdvancedPlacementCourseTypeID = False, returnFederalSubjectTypeID = False, returnHasCourseLevels = False, returnIsAdultBasicEducation = False, returnIsEndOfCourse = False, returnIsFederalDistanceEducation = False, returnIsFederalDualEnrollment = False, returnIsFederalProgram = False, returnIsGraduationRequirement = False, returnIsStateProgram = False, returnModifiedTime = False, returnReportToFitnessGram = False, returnSchoolYearID = False, returnStateCourseCodeMNID = False, returnStateEarlyEducationLocationMNID = False, returnStateStandardAddressedCodeMNID = False, returnStateSTARAssignmentCodeMNID = False, returnStateSubjectAreaCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumYear(CurriculumYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/CurriculumYear/" + str(CurriculumYearID), verb = "delete")


def getEveryEarlyEducationInstructionalApproachMN(searchConditions = [], EntityID = 1, returnEarlyEducationInstructionalApproachMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EarlyEducationInstructionalApproachMN in the district.

    This function returns a dataframe of every EarlyEducationInstructionalApproachMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, returnEarlyEducationInstructionalApproachMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "get", return_params_list = return_params)

def modifyEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1, setEarlyEducationInstructionalApproachMNID = None, setCreatedTime = None, setCurriculumYearID = None, setEarlyEducationInstructionalApproachMNIDClonedFrom = None, setModifiedTime = None, setStateEarlyEducationInstructionalApproachMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEarlyEducationInstructionalApproachMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEarlyEducationInstructionalApproachMN(EntityID = 1, setEarlyEducationInstructionalApproachMNID = None, setCreatedTime = None, setCurriculumYearID = None, setEarlyEducationInstructionalApproachMNIDClonedFrom = None, setModifiedTime = None, setStateEarlyEducationInstructionalApproachMNID = None, setStateImplementationStatusMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEarlyEducationInstructionalApproachMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationInstructionalApproachMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationInstructionalApproachMNID = False, returnStateImplementationStatusMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationInstructionalApproachMN/" + str(EarlyEducationInstructionalApproachMNID), verb = "delete")


def getEveryEarlyEducationProgramMN(searchConditions = [], EntityID = 1, returnEarlyEducationProgramMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EarlyEducationProgramMN in the district.

    This function returns a dataframe of every EarlyEducationProgramMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, returnEarlyEducationProgramMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "get", return_params_list = return_params)

def modifyEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1, setEarlyEducationProgramMNID = None, setCreatedTime = None, setCurriculumYearID = None, setEarlyEducationProgramMNIDClonedFrom = None, setModifiedTime = None, setStateEarlyEducationProgramMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEarlyEducationProgramMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEarlyEducationProgramMN(EntityID = 1, setEarlyEducationProgramMNID = None, setCreatedTime = None, setCurriculumYearID = None, setEarlyEducationProgramMNIDClonedFrom = None, setModifiedTime = None, setStateEarlyEducationProgramMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEarlyEducationProgramMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnEarlyEducationProgramMNIDClonedFrom = False, returnModifiedTime = False, returnStateEarlyEducationProgramMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/EarlyEducationProgramMN/" + str(EarlyEducationProgramMNID), verb = "delete")


def getEveryHierarchyDepth(searchConditions = [], EntityID = 1, returnHierarchyDepthID = False, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnDynamicRelationshipID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every HierarchyDepth in the district.

    This function returns a dataframe of every HierarchyDepth in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getHierarchyDepth(HierarchyDepthID, EntityID = 1, returnHierarchyDepthID = False, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnDynamicRelationshipID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "get", return_params_list = return_params)

def modifyHierarchyDepth(HierarchyDepthID, EntityID = 1, setHierarchyDepthID = None, setAcademicStandardSetID = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setDistrictGroupKey = None, setDynamicRelationshipID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnHierarchyDepthID = False, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnDynamicRelationshipID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createHierarchyDepth(EntityID = 1, setHierarchyDepthID = None, setAcademicStandardSetID = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setDistrictGroupKey = None, setDynamicRelationshipID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnHierarchyDepthID = False, returnAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnDistrictGroupKey = False, returnDynamicRelationshipID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteHierarchyDepth(HierarchyDepthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/HierarchyDepth/" + str(HierarchyDepthID), verb = "delete")


def getEveryPrerequisite(searchConditions = [], EntityID = 1, returnPrerequisiteID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Prerequisite in the district.

    This function returns a dataframe of every Prerequisite in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPrerequisite(PrerequisiteID, EntityID = 1, returnPrerequisiteID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "get", return_params_list = return_params)

def modifyPrerequisite(PrerequisiteID, EntityID = 1, setPrerequisiteID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurriculumID = None, setDescription = None, setDistrictGroupKey = None, setEarnedCredits = None, setHasPrerequisiteCurriculums = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPrerequisiteID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPrerequisite(EntityID = 1, setPrerequisiteID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurriculumID = None, setDescription = None, setDistrictGroupKey = None, setEarnedCredits = None, setHasPrerequisiteCurriculums = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPrerequisiteID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurriculumID = False, returnDescription = False, returnDistrictGroupKey = False, returnEarnedCredits = False, returnHasPrerequisiteCurriculums = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePrerequisite(PrerequisiteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Prerequisite/" + str(PrerequisiteID), verb = "delete")


def getEveryPrerequisiteCurriculum(searchConditions = [], EntityID = 1, returnPrerequisiteCurriculumID = False, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PrerequisiteCurriculum in the district.

    This function returns a dataframe of every PrerequisiteCurriculum in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, returnPrerequisiteCurriculumID = False, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "get", return_params_list = return_params)

def modifyPrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1, setPrerequisiteCurriculumID = None, setCreatedTime = None, setCurriculumIDRequired = None, setModifiedTime = None, setPrerequisiteID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPrerequisiteCurriculumID = False, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPrerequisiteCurriculum(EntityID = 1, setPrerequisiteCurriculumID = None, setCreatedTime = None, setCurriculumIDRequired = None, setModifiedTime = None, setPrerequisiteID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPrerequisiteCurriculumID = False, returnCreatedTime = False, returnCurriculumIDRequired = False, returnModifiedTime = False, returnPrerequisiteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/PrerequisiteCurriculum/" + str(PrerequisiteCurriculumID), verb = "delete")


def getEverySiteBasedInitiativeMN(searchConditions = [], EntityID = 1, returnSiteBasedInitiativeMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SiteBasedInitiativeMN in the district.

    This function returns a dataframe of every SiteBasedInitiativeMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, returnSiteBasedInitiativeMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "get", return_params_list = return_params)

def modifySiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1, setSiteBasedInitiativeMNID = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setSiteBasedInitiativeMNIDClonedFrom = None, setStateImplementationStatusMNID = None, setStateSiteBasedInitiativeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSiteBasedInitiativeMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSiteBasedInitiativeMN(EntityID = 1, setSiteBasedInitiativeMNID = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setSiteBasedInitiativeMNIDClonedFrom = None, setStateImplementationStatusMNID = None, setStateSiteBasedInitiativeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSiteBasedInitiativeMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnSiteBasedInitiativeMNIDClonedFrom = False, returnStateImplementationStatusMNID = False, returnStateSiteBasedInitiativeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/SiteBasedInitiativeMN/" + str(SiteBasedInitiativeMNID), verb = "delete")


def getEveryStandardPlacementMN(searchConditions = [], EntityID = 1, returnStandardPlacementMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StandardPlacementMN in the district.

    This function returns a dataframe of every StandardPlacementMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStandardPlacementMN(StandardPlacementMNID, EntityID = 1, returnStandardPlacementMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "get", return_params_list = return_params)

def modifyStandardPlacementMN(StandardPlacementMNID, EntityID = 1, setStandardPlacementMNID = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setStateStandardCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardPlacementMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStandardPlacementMN(EntityID = 1, setStandardPlacementMNID = None, setCreatedTime = None, setCurriculumYearID = None, setModifiedTime = None, setStateStandardCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStandardPlacementMNID = False, returnCreatedTime = False, returnCurriculumYearID = False, returnModifiedTime = False, returnStateStandardCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStandardPlacementMN(StandardPlacementMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/StandardPlacementMN/" + str(StandardPlacementMNID), verb = "delete")


def getEverySubject(searchConditions = [], EntityID = 1, returnSubjectID = False, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubject(SubjectID, EntityID = 1, returnSubjectID = False, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "get", return_params_list = return_params)

def modifySubject(SubjectID, EntityID = 1, setSubjectID = None, setBackgroundColor = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsPrimaryForSelectedCurriculum = None, setModifiedTime = None, setNumberOfAttachedCurriculums = None, setSchoolYearID = None, setSubjectIDClonedFrom = None, setSubjectIDClonedTo = None, setTextColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectID = False, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubject(EntityID = 1, setSubjectID = None, setBackgroundColor = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictGroupKey = None, setDistrictID = None, setIsPrimaryForSelectedCurriculum = None, setModifiedTime = None, setNumberOfAttachedCurriculums = None, setSchoolYearID = None, setSubjectIDClonedFrom = None, setSubjectIDClonedTo = None, setTextColor = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubjectID = False, returnBackgroundColor = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnIsPrimaryForSelectedCurriculum = False, returnModifiedTime = False, returnNumberOfAttachedCurriculums = False, returnSchoolYearID = False, returnSubjectIDClonedFrom = False, returnSubjectIDClonedTo = False, returnTextColor = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubject(SubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/Subject/" + str(SubjectID), verb = "delete")


def getEveryTempAcademicStandard(searchConditions = [], EntityID = 1, returnTempAcademicStandardID = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAcademicStandard in the district.

    This function returns a dataframe of every TempAcademicStandard in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAcademicStandard(TempAcademicStandardID, EntityID = 1, returnTempAcademicStandardID = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "get", return_params_list = return_params)

def modifyTempAcademicStandard(TempAcademicStandardID, EntityID = 1, setTempAcademicStandardID = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setImportedFrom = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLevel = None, setModifiedTime = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTempAcademicStandardGradeRangeID = None, setTempAcademicStandardIDParent = None, setTempAcademicStandardSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardID = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAcademicStandard(EntityID = 1, setTempAcademicStandardID = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setExtendedDescription = None, setGuid = None, setImportedFrom = None, setIsPlaceHolder = None, setKey = None, setLabel = None, setLevel = None, setModifiedTime = None, setParentGuid = None, setSequence = None, setStateNumber = None, setTempAcademicStandardGradeRangeID = None, setTempAcademicStandardIDParent = None, setTempAcademicStandardSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardID = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnExtendedDescription = False, returnGuid = False, returnImportedFrom = False, returnIsPlaceHolder = False, returnKey = False, returnLabel = False, returnLevel = False, returnModifiedTime = False, returnParentGuid = False, returnSequence = False, returnStateNumber = False, returnTempAcademicStandardGradeRangeID = False, returnTempAcademicStandardIDParent = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAcademicStandard(TempAcademicStandardID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandard/" + str(TempAcademicStandardID), verb = "delete")


def getEveryTempAcademicStandardGradeRange(searchConditions = [], EntityID = 1, returnTempAcademicStandardGradeRangeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAcademicStandardGradeRange in the district.

    This function returns a dataframe of every TempAcademicStandardGradeRange in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, returnTempAcademicStandardGradeRangeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "get", return_params_list = return_params)

def modifyTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1, setTempAcademicStandardGradeRangeID = None, setCode = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setImportedFrom = None, setModifiedTime = None, setSequence = None, setTempAcademicStandardSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardGradeRangeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAcademicStandardGradeRange(EntityID = 1, setTempAcademicStandardGradeRangeID = None, setCode = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setGradeRangeHigh = None, setGradeRangeLow = None, setGuid = None, setImportedFrom = None, setModifiedTime = None, setSequence = None, setTempAcademicStandardSubjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardGradeRangeID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnGradeRangeHigh = False, returnGradeRangeLow = False, returnGuid = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSubjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardGradeRange/" + str(TempAcademicStandardGradeRangeID), verb = "delete")


def getEveryTempAcademicStandardSet(searchConditions = [], EntityID = 1, returnTempAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAcademicStandardSet in the district.

    This function returns a dataframe of every TempAcademicStandardSet in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, returnTempAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "get", return_params_list = return_params)

def modifyTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1, setTempAcademicStandardSetID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEnteredByDistrict = None, setImportedFrom = None, setIsActive = None, setModifiedTime = None, setStateCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAcademicStandardSet(EntityID = 1, setTempAcademicStandardSetID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEnteredByDistrict = None, setImportedFrom = None, setIsActive = None, setModifiedTime = None, setStateCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempAcademicStandardSetID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnIsActive = False, returnModifiedTime = False, returnStateCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSet/" + str(TempAcademicStandardSetID), verb = "delete")


def getEveryTempAcademicStandardSubject(searchConditions = [], EntityID = 1, returnTempAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAcademicStandardSubject in the district.

    This function returns a dataframe of every TempAcademicStandardSubject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, returnTempAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "get", return_params_list = return_params)

def modifyTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1, setTempAcademicStandardSubjectID = None, setCode = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setImportedFrom = None, setModifiedTime = None, setSequence = None, setTempAcademicStandardSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setYear = None, returnTempAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAcademicStandardSubject(EntityID = 1, setTempAcademicStandardSubjectID = None, setCode = None, setCreatedTime = None, setDescription = None, setEnteredByDistrict = None, setImportedFrom = None, setModifiedTime = None, setSequence = None, setTempAcademicStandardSetID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setYear = None, returnTempAcademicStandardSubjectID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEnteredByDistrict = False, returnImportedFrom = False, returnModifiedTime = False, returnSequence = False, returnTempAcademicStandardSetID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempAcademicStandardSubject/" + str(TempAcademicStandardSubjectID), verb = "delete")


def getEveryTempGradeRangeCopyResult(searchConditions = [], EntityID = 1, returnTempGradeRangeCopyResultID = False, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempGradeRangeCopyResult in the district.

    This function returns a dataframe of every TempGradeRangeCopyResult in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, returnTempGradeRangeCopyResultID = False, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "get", return_params_list = return_params)

def modifyTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1, setTempGradeRangeCopyResultID = None, setAcademicStandardSubjectCode = None, setCreatedTime = None, setErrorText = None, setGradeRangeCode = None, setIsError = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradeRangeCopyResultID = False, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempGradeRangeCopyResult(EntityID = 1, setTempGradeRangeCopyResultID = None, setAcademicStandardSubjectCode = None, setCreatedTime = None, setErrorText = None, setGradeRangeCode = None, setIsError = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempGradeRangeCopyResultID = False, returnAcademicStandardSubjectCode = False, returnCreatedTime = False, returnErrorText = False, returnGradeRangeCode = False, returnIsError = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempGradeRangeCopyResult/" + str(TempGradeRangeCopyResultID), verb = "delete")


def getEveryTempHierarchyDepth(searchConditions = [], EntityID = 1, returnTempHierarchyDepthID = False, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempHierarchyDepth in the district.

    This function returns a dataframe of every TempHierarchyDepth in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, returnTempHierarchyDepthID = False, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "get", return_params_list = return_params)

def modifyTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1, setTempHierarchyDepthID = None, setAcademicStandardSetCode = None, setAcademicStandardSetDescription = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHierarchyDepthID = False, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempHierarchyDepth(EntityID = 1, setTempHierarchyDepthID = None, setAcademicStandardSetCode = None, setAcademicStandardSetDescription = None, setCode = None, setCreatedTime = None, setDepthLevel = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempHierarchyDepthID = False, returnAcademicStandardSetCode = False, returnAcademicStandardSetDescription = False, returnCode = False, returnCreatedTime = False, returnDepthLevel = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Curriculum/TempHierarchyDepth/" + str(TempHierarchyDepthID), verb = "delete")