# This module contains Transportation functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryBus(searchConditions = [], EntityID = 1, returnBusID = False, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHasHistoricBusRoutes = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Bus in the district.

    This function returns a dataframe of every Bus in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBus(BusID, EntityID = 1, returnBusID = False, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHasHistoricBusRoutes = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(BusID), verb = "get", return_params_list = return_params)

def modifyBus(BusID, EntityID = 1, setBusID = None, setCapacity = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setHasHistoricBusRoutes = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusID = False, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHasHistoricBusRoutes = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(BusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBus(EntityID = 1, setBusID = None, setCapacity = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setHasHistoricBusRoutes = None, setIsActive = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusID = False, returnCapacity = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnHasHistoricBusRoutes = False, returnIsActive = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBus(BusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/Bus/" + str(BusID), verb = "delete")


def getEveryBusRoute(searchConditions = [], EntityID = 1, returnBusRouteID = False, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BusRoute in the district.

    This function returns a dataframe of every BusRoute in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBusRoute(BusRouteID, EntityID = 1, returnBusRouteID = False, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(BusRouteID), verb = "get", return_params_list = return_params)

def modifyBusRoute(BusRouteID, EntityID = 1, setBusRouteID = None, setArrivalTime = None, setBusID = None, setBusRouteIDClonedFrom = None, setCreatedTime = None, setDepartureTime = None, setDescription = None, setHasBusStops = None, setMileage = None, setModifiedTime = None, setNameIDDriver = None, setRouteType = None, setRouteTypeCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusRouteID = False, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(BusRouteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBusRoute(EntityID = 1, setBusRouteID = None, setArrivalTime = None, setBusID = None, setBusRouteIDClonedFrom = None, setCreatedTime = None, setDepartureTime = None, setDescription = None, setHasBusStops = None, setMileage = None, setModifiedTime = None, setNameIDDriver = None, setRouteType = None, setRouteTypeCode = None, setSchoolYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusRouteID = False, returnArrivalTime = False, returnBusID = False, returnBusRouteIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnHasBusStops = False, returnMileage = False, returnModifiedTime = False, returnNameIDDriver = False, returnRouteType = False, returnRouteTypeCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBusRoute(BusRouteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusRoute/" + str(BusRouteID), verb = "delete")


def getEveryBusStop(searchConditions = [], EntityID = 1, returnBusStopID = False, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BusStop in the district.

    This function returns a dataframe of every BusStop in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBusStop(BusStopID, EntityID = 1, returnBusStopID = False, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(BusStopID), verb = "get", return_params_list = return_params)

def modifyBusStop(BusStopID, EntityID = 1, setBusStopID = None, setAddressID = None, setArrivalTime = None, setArrivalTimeFormatted = None, setBusRouteID = None, setBusStopIDClonedFrom = None, setCreatedTime = None, setDepartureTime = None, setDescription = None, setModifiedTime = None, setStopNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusStopID = False, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(BusStopID), verb = "post", return_params_list = return_params, payload = payload_params)

def createBusStop(EntityID = 1, setBusStopID = None, setAddressID = None, setArrivalTime = None, setArrivalTimeFormatted = None, setBusRouteID = None, setBusStopIDClonedFrom = None, setCreatedTime = None, setDepartureTime = None, setDescription = None, setModifiedTime = None, setStopNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnBusStopID = False, returnAddressID = False, returnArrivalTime = False, returnArrivalTimeFormatted = False, returnBusRouteID = False, returnBusStopIDClonedFrom = False, returnCreatedTime = False, returnDepartureTime = False, returnDescription = False, returnModifiedTime = False, returnStopNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBusStop(BusStopID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/BusStop/" + str(BusStopID), verb = "delete")


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnTransportationImportFileLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ConfigDistrict in the district.

    This function returns a dataframe of every ConfigDistrict in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnTransportationImportFileLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setTransportationImportFileLocation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnTransportationImportFileLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setTransportationImportFileLocation = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnTransportationImportFileLocation = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


def getEveryStudentBusStop(searchConditions = [], EntityID = 1, returnStudentBusStopID = False, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentBusStop in the district.

    This function returns a dataframe of every StudentBusStop in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentBusStop(StudentBusStopID, EntityID = 1, returnStudentBusStopID = False, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(StudentBusStopID), verb = "get", return_params_list = return_params)

def modifyStudentBusStop(StudentBusStopID, EntityID = 1, setStudentBusStopID = None, setBusStopID = None, setCreatedTime = None, setIsFriday = None, setIsMonday = None, setIsSaturday = None, setIsSunday = None, setIsThursday = None, setIsTuesday = None, setIsWednesday = None, setModifiedTime = None, setStopType = None, setStopTypeCode = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentBusStopID = False, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(StudentBusStopID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentBusStop(EntityID = 1, setStudentBusStopID = None, setBusStopID = None, setCreatedTime = None, setIsFriday = None, setIsMonday = None, setIsSaturday = None, setIsSunday = None, setIsThursday = None, setIsTuesday = None, setIsWednesday = None, setModifiedTime = None, setStopType = None, setStopTypeCode = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentBusStopID = False, returnBusStopID = False, returnCreatedTime = False, returnIsFriday = False, returnIsMonday = False, returnIsSaturday = False, returnIsSunday = False, returnIsThursday = False, returnIsTuesday = False, returnIsWednesday = False, returnModifiedTime = False, returnStopType = False, returnStopTypeCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentBusStop(StudentBusStopID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentBusStop/" + str(StudentBusStopID), verb = "delete")


def getEveryStudentTransportation(searchConditions = [], EntityID = 1, returnStudentTransportationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStateDistrictMNID = False, returnStudentID = False, returnStudentTransportationMNID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentTransportation in the district.

    This function returns a dataframe of every StudentTransportation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentTransportation(StudentTransportationID, EntityID = 1, returnStudentTransportationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStateDistrictMNID = False, returnStudentID = False, returnStudentTransportationMNID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(StudentTransportationID), verb = "get", return_params_list = return_params)

def modifyStudentTransportation(StudentTransportationID, EntityID = 1, setStudentTransportationID = None, setCreatedTime = None, setDistrictID = None, setEndDate = None, setMiles = None, setModifiedTime = None, setSchoolYearID = None, setStartDate = None, setStateDistrictMNID = None, setStudentID = None, setStudentTransportationMNID = None, setTransportationCategoryID = None, setTransported = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentTransportationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStateDistrictMNID = False, returnStudentID = False, returnStudentTransportationMNID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(StudentTransportationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentTransportation(EntityID = 1, setStudentTransportationID = None, setCreatedTime = None, setDistrictID = None, setEndDate = None, setMiles = None, setModifiedTime = None, setSchoolYearID = None, setStartDate = None, setStateDistrictMNID = None, setStudentID = None, setStudentTransportationMNID = None, setTransportationCategoryID = None, setTransported = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentTransportationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndDate = False, returnMiles = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartDate = False, returnStateDistrictMNID = False, returnStudentID = False, returnStudentTransportationMNID = False, returnTransportationCategoryID = False, returnTransported = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentTransportation(StudentTransportationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/StudentTransportation/" + str(StudentTransportationID), verb = "delete")


def getEveryTempStudentBusStop(searchConditions = [], EntityID = 1, returnTempStudentBusStopID = False, returnBusStopArrivalTime = False, returnBusStopDescription = False, returnBusStopFullAddress = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStudentBusStopID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentBusStop in the district.

    This function returns a dataframe of every TempStudentBusStop in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentBusStop(TempStudentBusStopID, EntityID = 1, returnTempStudentBusStopID = False, returnBusStopArrivalTime = False, returnBusStopDescription = False, returnBusStopFullAddress = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStudentBusStopID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(TempStudentBusStopID), verb = "get", return_params_list = return_params)

def modifyTempStudentBusStop(TempStudentBusStopID, EntityID = 1, setTempStudentBusStopID = None, setBusStopArrivalTime = None, setBusStopDescription = None, setBusStopFullAddress = None, setCreatedTime = None, setExceptions = None, setHasExceptions = None, setModifiedTime = None, setStudentBusStopID = None, setStudentNameLFM = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentBusStopID = False, returnBusStopArrivalTime = False, returnBusStopDescription = False, returnBusStopFullAddress = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStudentBusStopID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(TempStudentBusStopID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentBusStop(EntityID = 1, setTempStudentBusStopID = None, setBusStopArrivalTime = None, setBusStopDescription = None, setBusStopFullAddress = None, setCreatedTime = None, setExceptions = None, setHasExceptions = None, setModifiedTime = None, setStudentBusStopID = None, setStudentNameLFM = None, setStudentNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentBusStopID = False, returnBusStopArrivalTime = False, returnBusStopDescription = False, returnBusStopFullAddress = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStudentBusStopID = False, returnStudentNameLFM = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentBusStop(TempStudentBusStopID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentBusStop/" + str(TempStudentBusStopID), verb = "delete")


def getEveryTempStudentTransportation(searchConditions = [], EntityID = 1, returnTempStudentTransportationID = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStartDate = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentTransportationID = False, returnTransportationCategoryDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempStudentTransportation in the district.

    This function returns a dataframe of every TempStudentTransportation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempStudentTransportation(TempStudentTransportationID, EntityID = 1, returnTempStudentTransportationID = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStartDate = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentTransportationID = False, returnTransportationCategoryDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(TempStudentTransportationID), verb = "get", return_params_list = return_params)

def modifyTempStudentTransportation(TempStudentTransportationID, EntityID = 1, setTempStudentTransportationID = None, setCreatedTime = None, setExceptions = None, setHasExceptions = None, setModifiedTime = None, setStartDate = None, setStudentNameLFM = None, setStudentNumber = None, setStudentTransportationID = None, setTransportationCategoryDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentTransportationID = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStartDate = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentTransportationID = False, returnTransportationCategoryDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(TempStudentTransportationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentTransportation(EntityID = 1, setTempStudentTransportationID = None, setCreatedTime = None, setExceptions = None, setHasExceptions = None, setModifiedTime = None, setStartDate = None, setStudentNameLFM = None, setStudentNumber = None, setStudentTransportationID = None, setTransportationCategoryDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentTransportationID = False, returnCreatedTime = False, returnExceptions = False, returnHasExceptions = False, returnModifiedTime = False, returnStartDate = False, returnStudentNameLFM = False, returnStudentNumber = False, returnStudentTransportationID = False, returnTransportationCategoryDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentTransportation(TempStudentTransportationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempStudentTransportation/" + str(TempStudentTransportationID), verb = "delete")


def getEveryTempTransportation(searchConditions = [], EntityID = 1, returnTempTransportationID = False, returnArrivalTime = False, returnBus = False, returnBusRoute = False, returnBusStop = False, returnBusStopAddress = False, returnCreatedTime = False, returnDays = False, returnDriver = False, returnExceptions = False, returnFirstName = False, returnGradeLevel = False, returnHasExceptions = False, returnLastName = False, returnModifiedTime = False, returnSchool = False, returnStopType = False, returnStudentAddress = False, returnStudentNumber = False, returnTransportationCategory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempTransportation in the district.

    This function returns a dataframe of every TempTransportation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempTransportation(TempTransportationID, EntityID = 1, returnTempTransportationID = False, returnArrivalTime = False, returnBus = False, returnBusRoute = False, returnBusStop = False, returnBusStopAddress = False, returnCreatedTime = False, returnDays = False, returnDriver = False, returnExceptions = False, returnFirstName = False, returnGradeLevel = False, returnHasExceptions = False, returnLastName = False, returnModifiedTime = False, returnSchool = False, returnStopType = False, returnStudentAddress = False, returnStudentNumber = False, returnTransportationCategory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(TempTransportationID), verb = "get", return_params_list = return_params)

def modifyTempTransportation(TempTransportationID, EntityID = 1, setTempTransportationID = None, setArrivalTime = None, setBus = None, setBusRoute = None, setBusStop = None, setBusStopAddress = None, setCreatedTime = None, setDays = None, setDriver = None, setExceptions = None, setFirstName = None, setGradeLevel = None, setHasExceptions = None, setLastName = None, setModifiedTime = None, setSchool = None, setStopType = None, setStudentAddress = None, setStudentNumber = None, setTransportationCategory = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempTransportationID = False, returnArrivalTime = False, returnBus = False, returnBusRoute = False, returnBusStop = False, returnBusStopAddress = False, returnCreatedTime = False, returnDays = False, returnDriver = False, returnExceptions = False, returnFirstName = False, returnGradeLevel = False, returnHasExceptions = False, returnLastName = False, returnModifiedTime = False, returnSchool = False, returnStopType = False, returnStudentAddress = False, returnStudentNumber = False, returnTransportationCategory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(TempTransportationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempTransportation(EntityID = 1, setTempTransportationID = None, setArrivalTime = None, setBus = None, setBusRoute = None, setBusStop = None, setBusStopAddress = None, setCreatedTime = None, setDays = None, setDriver = None, setExceptions = None, setFirstName = None, setGradeLevel = None, setHasExceptions = None, setLastName = None, setModifiedTime = None, setSchool = None, setStopType = None, setStudentAddress = None, setStudentNumber = None, setTransportationCategory = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempTransportationID = False, returnArrivalTime = False, returnBus = False, returnBusRoute = False, returnBusStop = False, returnBusStopAddress = False, returnCreatedTime = False, returnDays = False, returnDriver = False, returnExceptions = False, returnFirstName = False, returnGradeLevel = False, returnHasExceptions = False, returnLastName = False, returnModifiedTime = False, returnSchool = False, returnStopType = False, returnStudentAddress = False, returnStudentNumber = False, returnTransportationCategory = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempTransportation(TempTransportationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TempTransportation/" + str(TempTransportationID), verb = "delete")


def getEveryTransportationCategory(searchConditions = [], EntityID = 1, returnTransportationCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateTransportationCategoryCodeMNID = False, returnTransportationCategoryIDClonedFrom = False, returnTransportationCategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TransportationCategory in the district.

    This function returns a dataframe of every TransportationCategory in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTransportationCategory(TransportationCategoryID, EntityID = 1, returnTransportationCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateTransportationCategoryCodeMNID = False, returnTransportationCategoryIDClonedFrom = False, returnTransportationCategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(TransportationCategoryID), verb = "get", return_params_list = return_params)

def modifyTransportationCategory(TransportationCategoryID, EntityID = 1, setTransportationCategoryID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setStateTransportationCategoryCodeMNID = None, setTransportationCategoryIDClonedFrom = None, setTransportationCategoryMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTransportationCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateTransportationCategoryCodeMNID = False, returnTransportationCategoryIDClonedFrom = False, returnTransportationCategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(TransportationCategoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTransportationCategory(EntityID = 1, setTransportationCategoryID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setSchoolYearID = None, setStateTransportationCategoryCodeMNID = None, setTransportationCategoryIDClonedFrom = None, setTransportationCategoryMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTransportationCategoryID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateTransportationCategoryCodeMNID = False, returnTransportationCategoryIDClonedFrom = False, returnTransportationCategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTransportationCategory(TransportationCategoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Transportation/TransportationCategory/" + str(TransportationCategoryID), verb = "delete")