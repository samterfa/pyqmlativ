# This module contains District functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBuilding(searchConditions = [], EntityID = 1, returnBuildingID = False, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Building in the district.

    This function returns a dataframe of every Building in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBuilding(BuildingID, EntityID = 1, returnBuildingID = False, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "get", return_params_list = return_params)

def modifyBuilding(BuildingID, EntityID = 1, setBuildingID = None, setAccountDistributionString = None, setAddressID = None, setBuildingMNID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setFederalNCESSchoolID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setModifiedTime = None, setOptimumStudentCount = None, setParcelNumber = None, setSTARSchoolNumber = None, setUnemploymentInsuranceUnitLocation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBuildingID = False, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBuilding(EntityID = 1, setBuildingID = None, setAccountDistributionString = None, setAddressID = None, setBuildingMNID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setFederalNCESSchoolID = None, setMaximumStudentCount = None, setMinimumStudentCount = None, setModifiedTime = None, setOptimumStudentCount = None, setParcelNumber = None, setSTARSchoolNumber = None, setUnemploymentInsuranceUnitLocation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBuildingID = False, returnAccountDistributionString = False, returnAddressID = False, returnBuildingMNID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnFederalNCESSchoolID = False, returnMaximumStudentCount = False, returnMinimumStudentCount = False, returnModifiedTime = False, returnOptimumStudentCount = False, returnParcelNumber = False, returnSTARSchoolNumber = False, returnUnemploymentInsuranceUnitLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBuilding(BuildingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Building/" + str(BuildingID), verb = "delete")


def getEveryCalendarYear(searchConditions = [], EntityID = 1, returnCalendarYearID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CalendarYear in the district.

    This function returns a dataframe of every CalendarYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCalendarYear(CalendarYearID, EntityID = 1, returnCalendarYearID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "get", return_params_list = return_params)

def modifyCalendarYear(CalendarYearID, EntityID = 1, setCalendarYearID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setNumericYear = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarYearID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCalendarYear(EntityID = 1, setCalendarYearID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setNumericYear = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCalendarYearID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnNumericYear = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCalendarYear(CalendarYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/CalendarYear/" + str(CalendarYearID), verb = "delete")


def getEveryConfigEntityYear(searchConditions = [], EntityID = 1, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigEntityYear in the district.

    This function returns a dataframe of every ConfigEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigEntityYear(ConfigEntityYearID, EntityID = 1, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "get", return_params_list = return_params)

def modifyConfigEntityYear(ConfigEntityYearID, EntityID = 1, setConfigEntityYearID = None, setConfigEntityYearIDClonedFrom = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigEntityYear(EntityID = 1, setConfigEntityYearID = None, setConfigEntityYearIDClonedFrom = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigEntityYearID = False, returnConfigEntityYearIDClonedFrom = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigEntityYear(ConfigEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/ConfigEntityYear/" + str(ConfigEntityYearID), verb = "delete")


def getEveryDistrictGroup(searchConditions = [], EntityID = 1, returnDistrictGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DistrictGroup in the district.

    This function returns a dataframe of every DistrictGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDistrictGroup(DistrictGroupID, EntityID = 1, returnDistrictGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "get", return_params_list = return_params)

def modifyDistrictGroup(DistrictGroupID, EntityID = 1, setDistrictGroupID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDistrictGroup(EntityID = 1, setDistrictGroupID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDistrictGroup(DistrictGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictGroup/" + str(DistrictGroupID), verb = "delete")


def getEveryDistrict(searchConditions = [], EntityID = 1, returnDistrictID = False, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnIsCurrentlySelected = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every District in the district.

    This function returns a dataframe of every District in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDistrict(DistrictID, EntityID = 1, returnDistrictID = False, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnIsCurrentlySelected = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "get", return_params_list = return_params)

def modifyDistrict(DistrictID, EntityID = 1, setDistrictID = None, setBuildingID = None, setCodeName = None, setCreatedTime = None, setDistrictCodeBySchoolYear = None, setDistrictGroupID = None, setDistrictMNID = None, setDistrictNumber = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFormattedPhoneNumber = None, setIsCurrentlySelected = None, setModifiedTime = None, setName = None, setNCESIDCode = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRCDTCodeBySchoolYear = None, setStaffIDSuperintendent = None, setStateDistrictCode = None, setStateDistrictMNID = None, setStateDistrictTypeCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictID = False, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnIsCurrentlySelected = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDistrict(EntityID = 1, setDistrictID = None, setBuildingID = None, setCodeName = None, setCreatedTime = None, setDistrictCodeBySchoolYear = None, setDistrictGroupID = None, setDistrictMNID = None, setDistrictNumber = None, setFaxNumber = None, setFaxNumberIsInternational = None, setFormattedPhoneNumber = None, setIsCurrentlySelected = None, setModifiedTime = None, setName = None, setNCESIDCode = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRCDTCodeBySchoolYear = None, setStaffIDSuperintendent = None, setStateDistrictCode = None, setStateDistrictMNID = None, setStateDistrictTypeCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictID = False, returnBuildingID = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeBySchoolYear = False, returnDistrictGroupID = False, returnDistrictMNID = False, returnDistrictNumber = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFormattedPhoneNumber = False, returnIsCurrentlySelected = False, returnModifiedTime = False, returnName = False, returnNCESIDCode = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRCDTCodeBySchoolYear = False, returnStaffIDSuperintendent = False, returnStateDistrictCode = False, returnStateDistrictMNID = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDistrict(DistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/District/" + str(DistrictID), verb = "delete")


def getEveryDistrictSchoolYear(searchConditions = [], EntityID = 1, returnDistrictSchoolYearID = False, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every DistrictSchoolYear in the district.

    This function returns a dataframe of every DistrictSchoolYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, returnDistrictSchoolYearID = False, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "get", return_params_list = return_params)

def modifyDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1, setDistrictSchoolYearID = None, setCreatedTime = None, setDistrictID = None, setDistrictSchoolYearIDClonedFrom = None, setEdFiDistrictID = None, setHarassmentPolicyWebLink = None, setHasDesegregationPlan = None, setHasDistanceEducation = None, setHasEarlyChildhood = None, setHasEarlyChildhoodNonIDEA = None, setHasGEDPreparationProgram = None, setHasHarassmentPolicy = None, setHasKindergarten = None, setHasKindergartenFullDayCost = None, setHasKindergartenFullDayFree = None, setHasKindergartenPartDayCost = None, setHasKindergartenPartDayFree = None, setHasPreschool = None, setHasPreschoolAllChildren = None, setHasPreschoolFullDayCost = None, setHasPreschoolFullDayFree = None, setHasPreschoolIDEA = None, setHasPreschoolLowIncome = None, setHasPreschoolPartDayCost = None, setHasPreschoolPartDayFree = None, setHasPreschoolTitleI = None, setIsCRDCCollectedForSchoolYear = None, setModifiedTime = None, setNameIDDisability = None, setNameIDRace = None, setNameIDSex = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictSchoolYearID = False, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDistrictSchoolYear(EntityID = 1, setDistrictSchoolYearID = None, setCreatedTime = None, setDistrictID = None, setDistrictSchoolYearIDClonedFrom = None, setEdFiDistrictID = None, setHarassmentPolicyWebLink = None, setHasDesegregationPlan = None, setHasDistanceEducation = None, setHasEarlyChildhood = None, setHasEarlyChildhoodNonIDEA = None, setHasGEDPreparationProgram = None, setHasHarassmentPolicy = None, setHasKindergarten = None, setHasKindergartenFullDayCost = None, setHasKindergartenFullDayFree = None, setHasKindergartenPartDayCost = None, setHasKindergartenPartDayFree = None, setHasPreschool = None, setHasPreschoolAllChildren = None, setHasPreschoolFullDayCost = None, setHasPreschoolFullDayFree = None, setHasPreschoolIDEA = None, setHasPreschoolLowIncome = None, setHasPreschoolPartDayCost = None, setHasPreschoolPartDayFree = None, setHasPreschoolTitleI = None, setIsCRDCCollectedForSchoolYear = None, setModifiedTime = None, setNameIDDisability = None, setNameIDRace = None, setNameIDSex = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDistrictSchoolYearID = False, returnCreatedTime = False, returnDistrictID = False, returnDistrictSchoolYearIDClonedFrom = False, returnEdFiDistrictID = False, returnHarassmentPolicyWebLink = False, returnHasDesegregationPlan = False, returnHasDistanceEducation = False, returnHasEarlyChildhood = False, returnHasEarlyChildhoodNonIDEA = False, returnHasGEDPreparationProgram = False, returnHasHarassmentPolicy = False, returnHasKindergarten = False, returnHasKindergartenFullDayCost = False, returnHasKindergartenFullDayFree = False, returnHasKindergartenPartDayCost = False, returnHasKindergartenPartDayFree = False, returnHasPreschool = False, returnHasPreschoolAllChildren = False, returnHasPreschoolFullDayCost = False, returnHasPreschoolFullDayFree = False, returnHasPreschoolIDEA = False, returnHasPreschoolLowIncome = False, returnHasPreschoolPartDayCost = False, returnHasPreschoolPartDayFree = False, returnHasPreschoolTitleI = False, returnIsCRDCCollectedForSchoolYear = False, returnModifiedTime = False, returnNameIDDisability = False, returnNameIDRace = False, returnNameIDSex = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDistrictSchoolYear(DistrictSchoolYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/DistrictSchoolYear/" + str(DistrictSchoolYearID), verb = "delete")


def getEveryEntityCloneDestination(searchConditions = [], EntityID = 1, returnEntityCloneDestinationID = False, returnCreatedTime = False, returnEntityCloneRunID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityCloneDestination in the district.

    This function returns a dataframe of every EntityCloneDestination in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityCloneDestination(EntityCloneDestinationID, EntityID = 1, returnEntityCloneDestinationID = False, returnCreatedTime = False, returnEntityCloneRunID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(EntityCloneDestinationID), verb = "get", return_params_list = return_params)

def modifyEntityCloneDestination(EntityCloneDestinationID, EntityID = 1, setEntityCloneDestinationID = None, setCreatedTime = None, setEntityCloneRunID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneDestinationID = False, returnCreatedTime = False, returnEntityCloneRunID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(EntityCloneDestinationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityCloneDestination(EntityID = 1, setEntityCloneDestinationID = None, setCreatedTime = None, setEntityCloneRunID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneDestinationID = False, returnCreatedTime = False, returnEntityCloneRunID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityCloneDestination(EntityCloneDestinationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneDestination/" + str(EntityCloneDestinationID), verb = "delete")


def getEveryEntityCloneError(searchConditions = [], EntityID = 1, returnEntityCloneErrorID = False, returnAttemptedOperation = False, returnAttemptedOperationCode = False, returnCreatedTime = False, returnEntityCloneSelectedObjectID = False, returnEntityIDTarget = False, returnMessage = False, returnModifiedTime = False, returnObjectJSON = False, returnSchoolYearIDTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityCloneError in the district.

    This function returns a dataframe of every EntityCloneError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityCloneError(EntityCloneErrorID, EntityID = 1, returnEntityCloneErrorID = False, returnAttemptedOperation = False, returnAttemptedOperationCode = False, returnCreatedTime = False, returnEntityCloneSelectedObjectID = False, returnEntityIDTarget = False, returnMessage = False, returnModifiedTime = False, returnObjectJSON = False, returnSchoolYearIDTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(EntityCloneErrorID), verb = "get", return_params_list = return_params)

def modifyEntityCloneError(EntityCloneErrorID, EntityID = 1, setEntityCloneErrorID = None, setAttemptedOperation = None, setAttemptedOperationCode = None, setCreatedTime = None, setEntityCloneSelectedObjectID = None, setEntityIDTarget = None, setMessage = None, setModifiedTime = None, setObjectJSON = None, setSchoolYearIDTarget = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneErrorID = False, returnAttemptedOperation = False, returnAttemptedOperationCode = False, returnCreatedTime = False, returnEntityCloneSelectedObjectID = False, returnEntityIDTarget = False, returnMessage = False, returnModifiedTime = False, returnObjectJSON = False, returnSchoolYearIDTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(EntityCloneErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityCloneError(EntityID = 1, setEntityCloneErrorID = None, setAttemptedOperation = None, setAttemptedOperationCode = None, setCreatedTime = None, setEntityCloneSelectedObjectID = None, setEntityIDTarget = None, setMessage = None, setModifiedTime = None, setObjectJSON = None, setSchoolYearIDTarget = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneErrorID = False, returnAttemptedOperation = False, returnAttemptedOperationCode = False, returnCreatedTime = False, returnEntityCloneSelectedObjectID = False, returnEntityIDTarget = False, returnMessage = False, returnModifiedTime = False, returnObjectJSON = False, returnSchoolYearIDTarget = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityCloneError(EntityCloneErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneError/" + str(EntityCloneErrorID), verb = "delete")


def getEveryEntityCloneRun(searchConditions = [], EntityID = 1, returnEntityCloneRunID = False, returnCreatedTime = False, returnEntityIDSource = False, returnMediaID = False, returnModifiedTime = False, returnSchoolYearIDSource = False, returnStatus = False, returnStatusCode = False, returnTargetEntities = False, returnTargetYears = False, returnTotalRecordsAdded = False, returnTotalRecordsDeleted = False, returnTotalRecordsErrored = False, returnTotalRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityCloneRun in the district.

    This function returns a dataframe of every EntityCloneRun in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityCloneRun(EntityCloneRunID, EntityID = 1, returnEntityCloneRunID = False, returnCreatedTime = False, returnEntityIDSource = False, returnMediaID = False, returnModifiedTime = False, returnSchoolYearIDSource = False, returnStatus = False, returnStatusCode = False, returnTargetEntities = False, returnTargetYears = False, returnTotalRecordsAdded = False, returnTotalRecordsDeleted = False, returnTotalRecordsErrored = False, returnTotalRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(EntityCloneRunID), verb = "get", return_params_list = return_params)

def modifyEntityCloneRun(EntityCloneRunID, EntityID = 1, setEntityCloneRunID = None, setCreatedTime = None, setEntityIDSource = None, setMediaID = None, setModifiedTime = None, setSchoolYearIDSource = None, setStatus = None, setStatusCode = None, setTargetEntities = None, setTargetYears = None, setTotalRecordsAdded = None, setTotalRecordsDeleted = None, setTotalRecordsErrored = None, setTotalRecordsUpdated = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneRunID = False, returnCreatedTime = False, returnEntityIDSource = False, returnMediaID = False, returnModifiedTime = False, returnSchoolYearIDSource = False, returnStatus = False, returnStatusCode = False, returnTargetEntities = False, returnTargetYears = False, returnTotalRecordsAdded = False, returnTotalRecordsDeleted = False, returnTotalRecordsErrored = False, returnTotalRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(EntityCloneRunID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityCloneRun(EntityID = 1, setEntityCloneRunID = None, setCreatedTime = None, setEntityIDSource = None, setMediaID = None, setModifiedTime = None, setSchoolYearIDSource = None, setStatus = None, setStatusCode = None, setTargetEntities = None, setTargetYears = None, setTotalRecordsAdded = None, setTotalRecordsDeleted = None, setTotalRecordsErrored = None, setTotalRecordsUpdated = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneRunID = False, returnCreatedTime = False, returnEntityIDSource = False, returnMediaID = False, returnModifiedTime = False, returnSchoolYearIDSource = False, returnStatus = False, returnStatusCode = False, returnTargetEntities = False, returnTargetYears = False, returnTotalRecordsAdded = False, returnTotalRecordsDeleted = False, returnTotalRecordsErrored = False, returnTotalRecordsUpdated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityCloneRun(EntityCloneRunID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneRun/" + str(EntityCloneRunID), verb = "delete")


def getEveryEntityCloneSelectedObject(searchConditions = [], EntityID = 1, returnEntityCloneSelectedObjectID = False, returnCloneOrder = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnNumberOfRecordsAdded = False, returnNumberOfRecordsDeleted = False, returnNumberOfRecordsErrored = False, returnNumberOfRecordsExported = False, returnNumberOfRecordsUpdated = False, returnObjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityCloneSelectedObject in the district.

    This function returns a dataframe of every EntityCloneSelectedObject in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityCloneSelectedObject(EntityCloneSelectedObjectID, EntityID = 1, returnEntityCloneSelectedObjectID = False, returnCloneOrder = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnNumberOfRecordsAdded = False, returnNumberOfRecordsDeleted = False, returnNumberOfRecordsErrored = False, returnNumberOfRecordsExported = False, returnNumberOfRecordsUpdated = False, returnObjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(EntityCloneSelectedObjectID), verb = "get", return_params_list = return_params)

def modifyEntityCloneSelectedObject(EntityCloneSelectedObjectID, EntityID = 1, setEntityCloneSelectedObjectID = None, setCloneOrder = None, setCreatedTime = None, setDependencies = None, setEntityCloneRunID = None, setIsAdding = None, setIsDeleting = None, setIsUpdating = None, setModifiedTime = None, setNumberOfRecordsAdded = None, setNumberOfRecordsDeleted = None, setNumberOfRecordsErrored = None, setNumberOfRecordsExported = None, setNumberOfRecordsUpdated = None, setObjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneSelectedObjectID = False, returnCloneOrder = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnNumberOfRecordsAdded = False, returnNumberOfRecordsDeleted = False, returnNumberOfRecordsErrored = False, returnNumberOfRecordsExported = False, returnNumberOfRecordsUpdated = False, returnObjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(EntityCloneSelectedObjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityCloneSelectedObject(EntityID = 1, setEntityCloneSelectedObjectID = None, setCloneOrder = None, setCreatedTime = None, setDependencies = None, setEntityCloneRunID = None, setIsAdding = None, setIsDeleting = None, setIsUpdating = None, setModifiedTime = None, setNumberOfRecordsAdded = None, setNumberOfRecordsDeleted = None, setNumberOfRecordsErrored = None, setNumberOfRecordsExported = None, setNumberOfRecordsUpdated = None, setObjectID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneSelectedObjectID = False, returnCloneOrder = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnNumberOfRecordsAdded = False, returnNumberOfRecordsDeleted = False, returnNumberOfRecordsErrored = False, returnNumberOfRecordsExported = False, returnNumberOfRecordsUpdated = False, returnObjectID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityCloneSelectedObject(EntityCloneSelectedObjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelectedObject/" + str(EntityCloneSelectedObjectID), verb = "delete")


def getEveryEntityCloneSelection(searchConditions = [], EntityID = 1, returnEntityCloneSelectionID = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnModuleID = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityCloneSelection in the district.

    This function returns a dataframe of every EntityCloneSelection in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityCloneSelection(EntityCloneSelectionID, EntityID = 1, returnEntityCloneSelectionID = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnModuleID = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(EntityCloneSelectionID), verb = "get", return_params_list = return_params)

def modifyEntityCloneSelection(EntityCloneSelectionID, EntityID = 1, setEntityCloneSelectionID = None, setCreatedTime = None, setDependencies = None, setEntityCloneRunID = None, setIsAdding = None, setIsDeleting = None, setIsUpdating = None, setModifiedTime = None, setModuleID = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneSelectionID = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnModuleID = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(EntityCloneSelectionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityCloneSelection(EntityID = 1, setEntityCloneSelectionID = None, setCreatedTime = None, setDependencies = None, setEntityCloneRunID = None, setIsAdding = None, setIsDeleting = None, setIsUpdating = None, setModifiedTime = None, setModuleID = None, setObjectName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityCloneSelectionID = False, returnCreatedTime = False, returnDependencies = False, returnEntityCloneRunID = False, returnIsAdding = False, returnIsDeleting = False, returnIsUpdating = False, returnModifiedTime = False, returnModuleID = False, returnObjectName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityCloneSelection(EntityCloneSelectionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityCloneSelection/" + str(EntityCloneSelectionID), verb = "delete")


def getEveryEntityGroup(searchConditions = [], EntityID = 1, returnEntityGroupID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroup in the district.

    This function returns a dataframe of every EntityGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroup(EntityGroupID, EntityID = 1, returnEntityGroupID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "get", return_params_list = return_params)

def modifyEntityGroup(EntityGroupID, EntityID = 1, setEntityGroupID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroup(EntityID = 1, setEntityGroupID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroup(EntityGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroup/" + str(EntityGroupID), verb = "delete")


def getEveryEntityGroupEntity(searchConditions = [], EntityID = 1, returnEntityGroupEntityID = False, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroupEntity in the district.

    This function returns a dataframe of every EntityGroupEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroupEntity(EntityGroupEntityID, EntityID = 1, returnEntityGroupEntityID = False, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "get", return_params_list = return_params)

def modifyEntityGroupEntity(EntityGroupEntityID, EntityID = 1, setEntityGroupEntityID = None, setCreatedTime = None, setEntityGroupID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupEntityID = False, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroupEntity(EntityID = 1, setEntityGroupEntityID = None, setCreatedTime = None, setEntityGroupID = None, setEntityID = None, setModifiedTime = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupEntityID = False, returnCreatedTime = False, returnEntityGroupID = False, returnEntityID = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroupEntity(EntityGroupEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupEntity/" + str(EntityGroupEntityID), verb = "delete")


def getEveryEntityGroupSetup(searchConditions = [], EntityID = 1, returnEntityGroupSetupID = False, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroupSetup in the district.

    This function returns a dataframe of every EntityGroupSetup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroupSetup(EntityGroupSetupID, EntityID = 1, returnEntityGroupSetupID = False, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "get", return_params_list = return_params)

def modifyEntityGroupSetup(EntityGroupSetupID, EntityID = 1, setEntityGroupSetupID = None, setCreatedTime = None, setEffectiveGroupName = None, setEntityGroupID = None, setEntityIDPrimary = None, setHasBeenProcessed = None, setModifiedTime = None, setNewGroupName = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupID = False, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroupSetup(EntityID = 1, setEntityGroupSetupID = None, setCreatedTime = None, setEffectiveGroupName = None, setEntityGroupID = None, setEntityIDPrimary = None, setHasBeenProcessed = None, setModifiedTime = None, setNewGroupName = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupID = False, returnCreatedTime = False, returnEffectiveGroupName = False, returnEntityGroupID = False, returnEntityIDPrimary = False, returnHasBeenProcessed = False, returnModifiedTime = False, returnNewGroupName = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroupSetup(EntityGroupSetupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetup/" + str(EntityGroupSetupID), verb = "delete")


def getEveryEntityGroupSetupEntity(searchConditions = [], EntityID = 1, returnEntityGroupSetupEntityID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroupSetupEntity in the district.

    This function returns a dataframe of every EntityGroupSetupEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, returnEntityGroupSetupEntityID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "get", return_params_list = return_params)

def modifyEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1, setEntityGroupSetupEntityID = None, setCreatedTime = None, setEntityGroupSetupID = None, setEntityID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupEntityID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroupSetupEntity(EntityID = 1, setEntityGroupSetupEntityID = None, setCreatedTime = None, setEntityGroupSetupID = None, setEntityID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupEntityID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnEntityID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroupSetupEntity(EntityGroupSetupEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupEntity/" + str(EntityGroupSetupEntityID), verb = "delete")


def getEveryEntityGroupSetupRun(searchConditions = [], EntityID = 1, returnEntityGroupSetupRunID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroupSetupRun in the district.

    This function returns a dataframe of every EntityGroupSetupRun in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, returnEntityGroupSetupRunID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "get", return_params_list = return_params)

def modifyEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1, setEntityGroupSetupRunID = None, setCreatedTime = None, setEntityGroupSetupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupRunID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroupSetupRun(EntityID = 1, setEntityGroupSetupRunID = None, setCreatedTime = None, setEntityGroupSetupID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupRunID = False, returnCreatedTime = False, returnEntityGroupSetupID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroupSetupRun(EntityGroupSetupRunID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRun/" + str(EntityGroupSetupRunID), verb = "delete")


def getEveryEntityGroupSetupRunDetail(searchConditions = [], EntityID = 1, returnEntityGroupSetupRunDetailID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EntityGroupSetupRunDetail in the district.

    This function returns a dataframe of every EntityGroupSetupRunDetail in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, returnEntityGroupSetupRunDetailID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "get", return_params_list = return_params)

def modifyEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1, setEntityGroupSetupRunDetailID = None, setChangeType = None, setChangeTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setEntityGroupSetupRunID = None, setEntityID = None, setError = None, setIdentifyingFields = None, setIsProcessed = None, setIsUpdated = None, setModifiedTime = None, setModule = None, setNewFieldValues = None, setNewValues = None, setObject = None, setObjectPrimaryKey = None, setOriginalValues = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupRunDetailID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntityGroupSetupRunDetail(EntityID = 1, setEntityGroupSetupRunDetailID = None, setChangeType = None, setChangeTypeCode = None, setCreatedTime = None, setEntityGroupKey = None, setEntityGroupSetupRunID = None, setEntityID = None, setError = None, setIdentifyingFields = None, setIsProcessed = None, setIsUpdated = None, setModifiedTime = None, setModule = None, setNewFieldValues = None, setNewValues = None, setObject = None, setObjectPrimaryKey = None, setOriginalValues = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityGroupSetupRunDetailID = False, returnChangeType = False, returnChangeTypeCode = False, returnCreatedTime = False, returnEntityGroupKey = False, returnEntityGroupSetupRunID = False, returnEntityID = False, returnError = False, returnIdentifyingFields = False, returnIsProcessed = False, returnIsUpdated = False, returnModifiedTime = False, returnModule = False, returnNewFieldValues = False, returnNewValues = False, returnObject = False, returnObjectPrimaryKey = False, returnOriginalValues = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntityGroupSetupRunDetail(EntityGroupSetupRunDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/EntityGroupSetupRunDetail/" + str(EntityGroupSetupRunDetailID), verb = "delete")


def getEveryEntity(searchConditions = [], EntityID = 1, returnEntityID = False, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIlluminateEndGradeLevel = False, returnIlluminateSiteType = False, returnIlluminateSiteTypeCalculated = False, returnIlluminateSiteTypeOverride = False, returnIlluminateStartGradeLevel = False, returnIsCurrentlySelected = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Entity in the district.

    This function returns a dataframe of every Entity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEntity(EntityID, returnEntityID = False, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIlluminateEndGradeLevel = False, returnIlluminateSiteType = False, returnIlluminateSiteTypeCalculated = False, returnIlluminateSiteTypeOverride = False, returnIlluminateStartGradeLevel = False, returnIsCurrentlySelected = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "get", return_params_list = return_params)

def modifyEntity(EntityID, setEntityID = None, setAllowDualEnrollment = None, setCampusID = None, setCode = None, setCodeName = None, setCreatedTime = None, setDistrictCodeEntityCode = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setEntityCodeOrCombinedCodesFollettExport = None, setEntityGroupCount = None, setEntityIDHash = None, setEntityMNID = None, setExternalLinkEntityCount = None, setIlluminateEndGradeLevel = None, setIlluminateSiteType = None, setIlluminateSiteTypeCalculated = None, setIlluminateSiteTypeOverride = None, setIlluminateStartGradeLevel = None, setIsCurrentlySelected = None, setIsDistrictWide = None, setIsSystemWide = None, setModifiedTime = None, setName = None, setReportToState = None, setSchoolYearIDCurrent = None, setTotalPlanEntityYears = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityID = False, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIlluminateEndGradeLevel = False, returnIlluminateSiteType = False, returnIlluminateSiteTypeCalculated = False, returnIlluminateSiteTypeOverride = False, returnIlluminateStartGradeLevel = False, returnIsCurrentlySelected = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEntity(EntityID = 1, setEntityID = None, setAllowDualEnrollment = None, setCampusID = None, setCode = None, setCodeName = None, setCreatedTime = None, setDistrictCodeEntityCode = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setEntityCodeOrCombinedCodesFollettExport = None, setEntityGroupCount = None, setEntityIDHash = None, setEntityMNID = None, setExternalLinkEntityCount = None, setIlluminateEndGradeLevel = None, setIlluminateSiteType = None, setIlluminateSiteTypeCalculated = None, setIlluminateSiteTypeOverride = None, setIlluminateStartGradeLevel = None, setIsCurrentlySelected = None, setIsDistrictWide = None, setIsSystemWide = None, setModifiedTime = None, setName = None, setReportToState = None, setSchoolYearIDCurrent = None, setTotalPlanEntityYears = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEntityID = False, returnAllowDualEnrollment = False, returnCampusID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDistrictCodeEntityCode = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnEntityCodeOrCombinedCodesFollettExport = False, returnEntityGroupCount = False, returnEntityIDHash = False, returnEntityMNID = False, returnExternalLinkEntityCount = False, returnIlluminateEndGradeLevel = False, returnIlluminateSiteType = False, returnIlluminateSiteTypeCalculated = False, returnIlluminateSiteTypeOverride = False, returnIlluminateStartGradeLevel = False, returnIsCurrentlySelected = False, returnIsDistrictWide = False, returnIsSystemWide = False, returnModifiedTime = False, returnName = False, returnReportToState = False, returnSchoolYearIDCurrent = False, returnTotalPlanEntityYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEntity(EntityID):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Entity/" + str(EntityID), verb = "delete")


def getEveryFiscalYear(searchConditions = [], EntityID = 1, returnFiscalYearID = False, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDynamicRelationshipID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every FiscalYear in the district.

    This function returns a dataframe of every FiscalYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getFiscalYear(FiscalYearID, EntityID = 1, returnFiscalYearID = False, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDynamicRelationshipID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "get", return_params_list = return_params)

def modifyFiscalYear(FiscalYearID, EntityID = 1, setFiscalYearID = None, setConflictAccountingUpdates = None, setConflictAccountsPayableRuns = None, setConflictAdditionDisposals = None, setConflictBudgetAmendments = None, setConflictCashReceiptDeposits = None, setConflictDepreciations = None, setConflictInvoices = None, setConflictJournalEntries = None, setConflictPayrollRuns = None, setConflictPurchaseOrders = None, setConflictWarehouseRequests = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setDynamicRelationshipID = None, setEndDate = None, setIsClosed = None, setIsLockedByHR = None, setModifiedTime = None, setNumericYear = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFiscalYearID = False, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDynamicRelationshipID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createFiscalYear(EntityID = 1, setFiscalYearID = None, setConflictAccountingUpdates = None, setConflictAccountsPayableRuns = None, setConflictAdditionDisposals = None, setConflictBudgetAmendments = None, setConflictCashReceiptDeposits = None, setConflictDepreciations = None, setConflictInvoices = None, setConflictJournalEntries = None, setConflictPayrollRuns = None, setConflictPurchaseOrders = None, setConflictWarehouseRequests = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setDynamicRelationshipID = None, setEndDate = None, setIsClosed = None, setIsLockedByHR = None, setModifiedTime = None, setNumericYear = None, setStartDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnFiscalYearID = False, returnConflictAccountingUpdates = False, returnConflictAccountsPayableRuns = False, returnConflictAdditionDisposals = False, returnConflictBudgetAmendments = False, returnConflictCashReceiptDeposits = False, returnConflictDepreciations = False, returnConflictInvoices = False, returnConflictJournalEntries = False, returnConflictPayrollRuns = False, returnConflictPurchaseOrders = False, returnConflictWarehouseRequests = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnDynamicRelationshipID = False, returnEndDate = False, returnIsClosed = False, returnIsLockedByHR = False, returnModifiedTime = False, returnNumericYear = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteFiscalYear(FiscalYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/FiscalYear/" + str(FiscalYearID), verb = "delete")


def getEveryRoom(searchConditions = [], EntityID = 1, returnRoomID = False, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSeatsAvailableForDateRangeAndDisplayPeriods = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Room in the district.

    This function returns a dataframe of every Room in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoom(RoomID, EntityID = 1, returnRoomID = False, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSeatsAvailableForDateRangeAndDisplayPeriods = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "get", return_params_list = return_params)

def modifyRoom(RoomID, EntityID = 1, setRoomID = None, setBuildingCodeRoomNumber = None, setBuildingID = None, setCreatedTime = None, setDescription = None, setFormattedPhoneNumber = None, setMaxConcurrentSections = None, setMaxSeats = None, setModifiedTime = None, setPhoneExtension = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRoomNumber = None, setRoomNumberDescription = None, setRoomTypeID = None, setSeatsAvailableForDateRangeAndDisplayPeriods = None, setSquareFootage = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomID = False, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSeatsAvailableForDateRangeAndDisplayPeriods = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoom(EntityID = 1, setRoomID = None, setBuildingCodeRoomNumber = None, setBuildingID = None, setCreatedTime = None, setDescription = None, setFormattedPhoneNumber = None, setMaxConcurrentSections = None, setMaxSeats = None, setModifiedTime = None, setPhoneExtension = None, setPhoneNumber = None, setPhoneNumberIsInternational = None, setRoomNumber = None, setRoomNumberDescription = None, setRoomTypeID = None, setSeatsAvailableForDateRangeAndDisplayPeriods = None, setSquareFootage = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomID = False, returnBuildingCodeRoomNumber = False, returnBuildingID = False, returnCreatedTime = False, returnDescription = False, returnFormattedPhoneNumber = False, returnMaxConcurrentSections = False, returnMaxSeats = False, returnModifiedTime = False, returnPhoneExtension = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnRoomNumber = False, returnRoomNumberDescription = False, returnRoomTypeID = False, returnSeatsAvailableForDateRangeAndDisplayPeriods = False, returnSquareFootage = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoom(RoomID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/Room/" + str(RoomID), verb = "delete")


def getEveryRoomType(searchConditions = [], EntityID = 1, returnRoomTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RoomType in the district.

    This function returns a dataframe of every RoomType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRoomType(RoomTypeID, EntityID = 1, returnRoomTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "get", return_params_list = return_params)

def modifyRoomType(RoomTypeID, EntityID = 1, setRoomTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRoomType(EntityID = 1, setRoomTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRoomTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRoomType(RoomTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/RoomType/" + str(RoomTypeID), verb = "delete")


def getEverySchoolYear(searchConditions = [], EntityID = 1, returnSchoolYearID = False, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnStudentAwardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SchoolYear in the district.

    This function returns a dataframe of every SchoolYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSchoolYear(SchoolYearID, EntityID = 1, returnSchoolYearID = False, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnStudentAwardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "get", return_params_list = return_params)

def modifySchoolYear(SchoolYearID, EntityID = 1, setSchoolYearID = None, setCreatedTime = None, setDescription = None, setIsCurrentYearForProvidedEntity = None, setIsUpcomingYearForProvidedEntity = None, setModifiedTime = None, setNextNumericYear = None, setNumericYear = None, setStudentAwardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolYearID = False, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnStudentAwardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSchoolYear(EntityID = 1, setSchoolYearID = None, setCreatedTime = None, setDescription = None, setIsCurrentYearForProvidedEntity = None, setIsUpcomingYearForProvidedEntity = None, setModifiedTime = None, setNextNumericYear = None, setNumericYear = None, setStudentAwardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSchoolYearID = False, returnCreatedTime = False, returnDescription = False, returnIsCurrentYearForProvidedEntity = False, returnIsUpcomingYearForProvidedEntity = False, returnModifiedTime = False, returnNextNumericYear = False, returnNumericYear = False, returnStudentAwardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSchoolYear(SchoolYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/SchoolYear/" + str(SchoolYearID), verb = "delete")


def getEveryStateDistrictMN(searchConditions = [], EntityID = 1, returnStateDistrictMNID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StateDistrictMN in the district.

    This function returns a dataframe of every StateDistrictMN in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStateDistrictMN(StateDistrictMNID, EntityID = 1, returnStateDistrictMNID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "get", return_params_list = return_params)

def modifyStateDistrictMN(StateDistrictMNID, EntityID = 1, setStateDistrictMNID = None, setCode = None, setCodeName = None, setCreatedTime = None, setModifiedTime = None, setName = None, setStateDistrictTypeCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStateDistrictMNID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStateDistrictMN(EntityID = 1, setStateDistrictMNID = None, setCode = None, setCodeName = None, setCreatedTime = None, setModifiedTime = None, setName = None, setStateDistrictTypeCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStateDistrictMNID = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateDistrictTypeCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStateDistrictMN(StateDistrictMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/District/StateDistrictMN/" + str(StateDistrictMNID), verb = "delete")