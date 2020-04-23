# This module contains StaffPlanning functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryAssignmentTypePlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AssignmentTypePlanPositionDistributionSummary in the district.

    This function returns a dataframe of every AssignmentTypePlanPositionDistributionSummary in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params)

def modifyAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setAssignmentTypeID = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params, payload = payload_params)

def createAssignmentTypePlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setAssignmentTypeID = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnAssignmentTypeID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "delete")


def getEveryBuildingPlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every BuildingPlanPositionDistributionSummary in the district.

    This function returns a dataframe of every BuildingPlanPositionDistributionSummary in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params)

def modifyBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setBuildingID = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params, payload = payload_params)

def createBuildingPlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setBuildingID = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnBuildingID = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "delete")


def getEveryPlan(searchConditions = [], EntityID = 1, returnPlanID = False, returnBudgetVersionAmount = False, returnBudgetVersionDifference = False, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnIsBudgeted = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Plan in the district.

    This function returns a dataframe of every Plan in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlan(PlanID, EntityID = 1, returnPlanID = False, returnBudgetVersionAmount = False, returnBudgetVersionDifference = False, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnIsBudgeted = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(PlanID), verb = "get", return_params_list = return_params)

def modifyPlan(PlanID, EntityID = 1, setPlanID = None, setBudgetVersionAmount = None, setBudgetVersionDifference = None, setCalculationStatus = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setDistrictID = None, setFiscalYearID = None, setIsBudgeted = None, setModifiedTime = None, setNumberOfOccupiedPositions = None, setNumberOfVacantPositions = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanID = False, returnBudgetVersionAmount = False, returnBudgetVersionDifference = False, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnIsBudgeted = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(PlanID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlan(EntityID = 1, setPlanID = None, setBudgetVersionAmount = None, setBudgetVersionDifference = None, setCalculationStatus = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setDistrictID = None, setFiscalYearID = None, setIsBudgeted = None, setModifiedTime = None, setNumberOfOccupiedPositions = None, setNumberOfVacantPositions = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanID = False, returnBudgetVersionAmount = False, returnBudgetVersionDifference = False, returnCalculationStatus = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnDistrictID = False, returnFiscalYearID = False, returnIsBudgeted = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlan(PlanID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/Plan/" + str(PlanID), verb = "delete")


def getEveryPlanEmployee(searchConditions = [], EntityID = 1, returnPlanEmployeeID = False, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanEmployee in the district.

    This function returns a dataframe of every PlanEmployee in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanEmployee(PlanEmployeeID, EntityID = 1, returnPlanEmployeeID = False, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(PlanEmployeeID), verb = "get", return_params_list = return_params)

def modifyPlanEmployee(PlanEmployeeID, EntityID = 1, setPlanEmployeeID = None, setAssignedFTE = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setEmployeeID = None, setModifiedTime = None, setPlanID = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanEmployeeID = False, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(PlanEmployeeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanEmployee(EntityID = 1, setPlanEmployeeID = None, setAssignedFTE = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setEmployeeID = None, setModifiedTime = None, setPlanID = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanEmployeeID = False, returnAssignedFTE = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnEmployeeID = False, returnModifiedTime = False, returnPlanID = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanEmployee(PlanEmployeeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanEmployee/" + str(PlanEmployeeID), verb = "delete")


def getEveryPlanGroup(searchConditions = [], EntityID = 1, returnPlanGroupID = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanGroup in the district.

    This function returns a dataframe of every PlanGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanGroup(PlanGroupID, EntityID = 1, returnPlanGroupID = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(PlanGroupID), verb = "get", return_params_list = return_params)

def modifyPlanGroup(PlanGroupID, EntityID = 1, setPlanGroupID = None, setAssignedFTE = None, setAvailableFTE = None, setBudgetedFTE = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setIsUnassigned = None, setModifiedTime = None, setNumberOfOccupiedPositions = None, setNumberOfVacantPositions = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupID = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(PlanGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanGroup(EntityID = 1, setPlanGroupID = None, setAssignedFTE = None, setAvailableFTE = None, setBudgetedFTE = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setIsUnassigned = None, setModifiedTime = None, setNumberOfOccupiedPositions = None, setNumberOfVacantPositions = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupID = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnIsUnassigned = False, returnModifiedTime = False, returnNumberOfOccupiedPositions = False, returnNumberOfVacantPositions = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanGroup(PlanGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroup/" + str(PlanGroupID), verb = "delete")


def getEveryPlanGroupAssignmentType(searchConditions = [], EntityID = 1, returnPlanGroupAssignmentTypeID = False, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanGroupAssignmentType in the district.

    This function returns a dataframe of every PlanGroupAssignmentType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1, returnPlanGroupAssignmentTypeID = False, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(PlanGroupAssignmentTypeID), verb = "get", return_params_list = return_params)

def modifyPlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1, setPlanGroupAssignmentTypeID = None, setAssignmentTypeID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupAssignmentTypeID = False, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(PlanGroupAssignmentTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanGroupAssignmentType(EntityID = 1, setPlanGroupAssignmentTypeID = None, setAssignmentTypeID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupAssignmentTypeID = False, returnAssignmentTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanGroupAssignmentType(PlanGroupAssignmentTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupAssignmentType/" + str(PlanGroupAssignmentTypeID), verb = "delete")


def getEveryPlanGroupBuilding(searchConditions = [], EntityID = 1, returnPlanGroupBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanGroupBuilding in the district.

    This function returns a dataframe of every PlanGroupBuilding in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanGroupBuilding(PlanGroupBuildingID, EntityID = 1, returnPlanGroupBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(PlanGroupBuildingID), verb = "get", return_params_list = return_params)

def modifyPlanGroupBuilding(PlanGroupBuildingID, EntityID = 1, setPlanGroupBuildingID = None, setBuildingID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(PlanGroupBuildingID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanGroupBuilding(EntityID = 1, setPlanGroupBuildingID = None, setBuildingID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupBuildingID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanGroupBuilding(PlanGroupBuildingID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupBuilding/" + str(PlanGroupBuildingID), verb = "delete")


def getEveryPlanGroupClearance(searchConditions = [], EntityID = 1, returnPlanGroupClearanceID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanGroupClearance in the district.

    This function returns a dataframe of every PlanGroupClearance in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanGroupClearance(PlanGroupClearanceID, EntityID = 1, returnPlanGroupClearanceID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(PlanGroupClearanceID), verb = "get", return_params_list = return_params)

def modifyPlanGroupClearance(PlanGroupClearanceID, EntityID = 1, setPlanGroupClearanceID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setSecurityGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupClearanceID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(PlanGroupClearanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanGroupClearance(EntityID = 1, setPlanGroupClearanceID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setSecurityGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupClearanceID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnSecurityGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanGroupClearance(PlanGroupClearanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupClearance/" + str(PlanGroupClearanceID), verb = "delete")


def getEveryPlanGroupPositionType(searchConditions = [], EntityID = 1, returnPlanGroupPositionTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanGroupPositionType in the district.

    This function returns a dataframe of every PlanGroupPositionType in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1, returnPlanGroupPositionTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(PlanGroupPositionTypeID), verb = "get", return_params_list = return_params)

def modifyPlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1, setPlanGroupPositionTypeID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setPositionTypeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupPositionTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(PlanGroupPositionTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanGroupPositionType(EntityID = 1, setPlanGroupPositionTypeID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setModifiedTime = None, setPlanGroupID = None, setPositionTypeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanGroupPositionTypeID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnModifiedTime = False, returnPlanGroupID = False, returnPositionTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanGroupPositionType(PlanGroupPositionTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanGroupPositionType/" + str(PlanGroupPositionTypeID), verb = "delete")


def getEveryPlanPosition(searchConditions = [], EntityID = 1, returnPlanPositionID = False, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPosition in the district.

    This function returns a dataframe of every PlanPosition in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPosition(PlanPositionID, EntityID = 1, returnPlanPositionID = False, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(PlanPositionID), verb = "get", return_params_list = return_params)

def modifyPlanPosition(PlanPositionID, EntityID = 1, setPlanPositionID = None, setAnnualPay = None, setAssignedFTE = None, setAvailableFTE = None, setBudgetedFTE = None, setCalculationStatus = None, setCalculationStatusCode = None, setCalendarID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setFormattedFullPaySecondsPerDay = None, setFormattedFullPaySecondsPerDayDecimal = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setJobTypeID = None, setLaneID = None, setMatrixID = None, setModifiedTime = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanEmployeeID = None, setPlanID = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsAssignmentTypeDescriptions = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionDistributionsBuildingDescriptions = None, setPlanPositionDistributionsDepartmentCodes = None, setPlanPositionDistributionsDepartmentDescriptions = None, setPlanPositionDistributionsFTEGroupCodes = None, setPlanPositionDistributionsFTEGroupDescriptions = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberID = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionID = False, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(PlanPositionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPosition(EntityID = 1, setPlanPositionID = None, setAnnualPay = None, setAssignedFTE = None, setAvailableFTE = None, setBudgetedFTE = None, setCalculationStatus = None, setCalculationStatusCode = None, setCalendarID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDescription = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setFormattedFullPaySecondsPerDay = None, setFormattedFullPaySecondsPerDayDecimal = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setJobTypeID = None, setLaneID = None, setMatrixID = None, setModifiedTime = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanEmployeeID = None, setPlanID = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsAssignmentTypeDescriptions = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionDistributionsBuildingDescriptions = None, setPlanPositionDistributionsDepartmentCodes = None, setPlanPositionDistributionsDepartmentDescriptions = None, setPlanPositionDistributionsFTEGroupCodes = None, setPlanPositionDistributionsFTEGroupDescriptions = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberID = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTotalBenefitAmount = None, setTotalCompensationAmount = None, setTotalPayAmount = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionID = False, returnAnnualPay = False, returnAssignedFTE = False, returnAvailableFTE = False, returnBudgetedFTE = False, returnCalculationStatus = False, returnCalculationStatusCode = False, returnCalendarID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDescription = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnFormattedFullPaySecondsPerDay = False, returnFormattedFullPaySecondsPerDayDecimal = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnJobTypeID = False, returnLaneID = False, returnMatrixID = False, returnModifiedTime = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanEmployeeID = False, returnPlanID = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsAssignmentTypeDescriptions = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionDistributionsBuildingDescriptions = False, returnPlanPositionDistributionsDepartmentCodes = False, returnPlanPositionDistributionsDepartmentDescriptions = False, returnPlanPositionDistributionsFTEGroupCodes = False, returnPlanPositionDistributionsFTEGroupDescriptions = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberID = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTotalBenefitAmount = False, returnTotalCompensationAmount = False, returnTotalPayAmount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPosition(PlanPositionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPosition/" + str(PlanPositionID), verb = "delete")


def getEveryPlanPositionBenefit(searchConditions = [], EntityID = 1, returnPlanPositionBenefitID = False, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionBenefit in the district.

    This function returns a dataframe of every PlanPositionBenefit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionBenefit(PlanPositionBenefitID, EntityID = 1, returnPlanPositionBenefitID = False, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(PlanPositionBenefitID), verb = "get", return_params_list = return_params)

def modifyPlanPositionBenefit(PlanPositionBenefitID, EntityID = 1, setPlanPositionBenefitID = None, setBenefitID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionID = None, setTotalAnnualAmountCalculated = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnPlanPositionBenefitID = False, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(PlanPositionBenefitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionBenefit(EntityID = 1, setPlanPositionBenefitID = None, setBenefitID = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionID = None, setTotalAnnualAmountCalculated = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnPlanPositionBenefitID = False, returnBenefitID = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnTotalAnnualAmountCalculated = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionBenefit(PlanPositionBenefitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionBenefit/" + str(PlanPositionBenefitID), verb = "delete")


def getEveryPlanPositionDistribution(searchConditions = [], EntityID = 1, returnPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionDistribution in the district.

    This function returns a dataframe of every PlanPositionDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionDistribution(PlanPositionDistributionID, EntityID = 1, returnPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(PlanPositionDistributionID), verb = "get", return_params_list = return_params)

def modifyPlanPositionDistribution(PlanPositionDistributionID, EntityID = 1, setPlanPositionDistributionID = None, setAssignmentTypeID = None, setBuildingID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setModifiedTime = None, setPlanGroupID = None, setPlanPositionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(PlanPositionDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionDistribution(EntityID = 1, setPlanPositionDistributionID = None, setAssignmentTypeID = None, setBuildingID = None, setCreatedTime = None, setCurrentUserHasPlanGroupAccess = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setModifiedTime = None, setPlanGroupID = None, setPlanPositionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnCurrentUserHasPlanGroupAccess = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnPlanGroupID = False, returnPlanPositionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionDistribution(PlanPositionDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistribution/" + str(PlanPositionDistributionID), verb = "delete")


def getEveryPlanPositionDistributionAccountDistribution(searchConditions = [], EntityID = 1, returnPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionDistributionID = False, returnProratedDistributionPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionDistributionAccountDistribution in the district.

    This function returns a dataframe of every PlanPositionDistributionAccountDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionDistributionAccountDistribution(PlanPositionDistributionAccountDistributionID, EntityID = 1, returnPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionDistributionID = False, returnProratedDistributionPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(PlanPositionDistributionAccountDistributionID), verb = "get", return_params_list = return_params)

def modifyPlanPositionDistributionAccountDistribution(PlanPositionDistributionAccountDistributionID, EntityID = 1, setPlanPositionDistributionAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionDistributionID = None, setProratedDistributionPercent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionDistributionID = False, returnProratedDistributionPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(PlanPositionDistributionAccountDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionDistributionAccountDistribution(EntityID = 1, setPlanPositionDistributionAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionDistributionID = None, setProratedDistributionPercent = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionDistributionID = False, returnProratedDistributionPercent = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionDistributionAccountDistribution(PlanPositionDistributionAccountDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionDistributionAccountDistribution/" + str(PlanPositionDistributionAccountDistributionID), verb = "delete")


def getEveryPlanPositionPay(searchConditions = [], EntityID = 1, returnPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionPay in the district.

    This function returns a dataframe of every PlanPositionPay in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionPay(PlanPositionPayID, EntityID = 1, returnPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(PlanPositionPayID), verb = "get", return_params_list = return_params)

def modifyPlanPositionPay(PlanPositionPayID, EntityID = 1, setPlanPositionPayID = None, setAccountDistributionString = None, setAssignmentPayTypeIDOriginal = None, setCreatedTime = None, setModifiedTime = None, setPayScheduleID = None, setPayTypeID = None, setPlanPositionID = None, setStipendAmount = None, setTotalAmount = None, setTotalAnnualAmountCalculated = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(PlanPositionPayID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionPay(EntityID = 1, setPlanPositionPayID = None, setAccountDistributionString = None, setAssignmentPayTypeIDOriginal = None, setCreatedTime = None, setModifiedTime = None, setPayScheduleID = None, setPayTypeID = None, setPlanPositionID = None, setStipendAmount = None, setTotalAmount = None, setTotalAnnualAmountCalculated = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnCreatedTime = False, returnModifiedTime = False, returnPayScheduleID = False, returnPayTypeID = False, returnPlanPositionID = False, returnStipendAmount = False, returnTotalAmount = False, returnTotalAnnualAmountCalculated = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionPay(PlanPositionPayID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPay/" + str(PlanPositionPayID), verb = "delete")


def getEveryPlanPositionPayAccountCalculation(searchConditions = [], EntityID = 1, returnPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionPayAccountCalculation in the district.

    This function returns a dataframe of every PlanPositionPayAccountCalculation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1, returnPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(PlanPositionPayAccountCalculationID), verb = "get", return_params_list = return_params)

def modifyPlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1, setPlanPositionPayAccountCalculationID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(PlanPositionPayAccountCalculationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionPayAccountCalculation(EntityID = 1, setPlanPositionPayAccountCalculationID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountCalculation/" + str(PlanPositionPayAccountCalculationID), verb = "delete")


def getEveryPlanPositionPayAccountDistribution(searchConditions = [], EntityID = 1, returnPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionPayAccountDistribution in the district.

    This function returns a dataframe of every PlanPositionPayAccountDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1, returnPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(PlanPositionPayAccountDistributionID), verb = "get", return_params_list = return_params)

def modifyPlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1, setPlanPositionPayAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(PlanPositionPayAccountDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionPayAccountDistribution(EntityID = 1, setPlanPositionPayAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayAccountDistribution/" + str(PlanPositionPayAccountDistributionID), verb = "delete")


def getEveryPlanPositionPayBenefit(searchConditions = [], EntityID = 1, returnPlanPositionPayBenefitID = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionPayBenefit in the district.

    This function returns a dataframe of every PlanPositionPayBenefit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1, returnPlanPositionPayBenefitID = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(PlanPositionPayBenefitID), verb = "get", return_params_list = return_params)

def modifyPlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1, setPlanPositionPayBenefitID = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionBenefitID = None, setPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayBenefitID = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(PlanPositionPayBenefitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionPayBenefit(EntityID = 1, setPlanPositionPayBenefitID = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionBenefitID = None, setPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayBenefitID = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionBenefitID = False, returnPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionPayBenefit(PlanPositionPayBenefitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefit/" + str(PlanPositionPayBenefitID), verb = "delete")


def getEveryPlanPositionPayBenefitAccount(searchConditions = [], EntityID = 1, returnPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionPayBenefitAccount in the district.

    This function returns a dataframe of every PlanPositionPayBenefitAccount in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1, returnPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(PlanPositionPayBenefitAccountID), verb = "get", return_params_list = return_params)

def modifyPlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1, setPlanPositionPayBenefitAccountID = None, setAccountID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(PlanPositionPayBenefitAccountID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionPayBenefitAccount(EntityID = 1, setPlanPositionPayBenefitAccountID = None, setAccountID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionPayBenefitAccount/" + str(PlanPositionPayBenefitAccountID), verb = "delete")


def getEveryPlanPositionSupplement(searchConditions = [], EntityID = 1, returnPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanPositionSupplement in the district.

    This function returns a dataframe of every PlanPositionSupplement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanPositionSupplement(PlanPositionSupplementID, EntityID = 1, returnPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(PlanPositionSupplementID), verb = "get", return_params_list = return_params)

def modifyPlanPositionSupplement(PlanPositionSupplementID, EntityID = 1, setPlanPositionSupplementID = None, setAnnualPay = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionID = None, setRate = None, setSupplementTypeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(PlanPositionSupplementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanPositionSupplement(EntityID = 1, setPlanPositionSupplementID = None, setAnnualPay = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionID = None, setRate = None, setSupplementTypeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionID = False, returnRate = False, returnSupplementTypeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanPositionSupplement(PlanPositionSupplementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PlanPositionSupplement/" + str(PlanPositionSupplementID), verb = "delete")


def getEveryPositionTypePlanPositionDistributionSummary(searchConditions = [], EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PositionTypePlanPositionDistributionSummary in the district.

    This function returns a dataframe of every PositionTypePlanPositionDistributionSummary in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, returnPlanPositionDistributionIDFirst = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "get", return_params_list = return_params)

def modifyPositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1, setPlanPositionDistributionIDFirst = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "post", return_params_list = return_params, payload = payload_params)

def createPositionTypePlanPositionDistributionSummary(EntityID = 1, setPlanPositionDistributionIDFirst = None, setFTE = None, setPlanGroupID = None, setPositionTypeID = None, returnPlanPositionDistributionIDFirst = False, returnFTE = False, returnPlanGroupID = False, returnPositionTypeID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + str(PlanPositionDistributionIDFirst), verb = "delete")


def getEveryTempException(searchConditions = [], EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempException in the district.

    This function returns a dataframe of every TempException in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempException(TempExceptionID, EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(TempExceptionID), verb = "get", return_params_list = return_params)

def modifyTempException(TempExceptionID, EntityID = 1, setTempExceptionID = None, setCreatedTime = None, setError = None, setErroredObjectID = None, setErrorField = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempExceptionID = False, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(TempExceptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempException(EntityID = 1, setTempExceptionID = None, setCreatedTime = None, setError = None, setErroredObjectID = None, setErrorField = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempExceptionID = False, returnCreatedTime = False, returnError = False, returnErroredObjectID = False, returnErrorField = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempException(TempExceptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempException/" + str(TempExceptionID), verb = "delete")


def getEveryTempPlanPositionBenefit(searchConditions = [], EntityID = 1, returnTempPlanPositionBenefitID = False, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionBenefit in the district.

    This function returns a dataframe of every TempPlanPositionBenefit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1, returnTempPlanPositionBenefitID = False, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(TempPlanPositionBenefitID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1, setTempPlanPositionBenefitID = None, setBenefitCodeDescription = None, setBenefitID = None, setBenefitTypeTX = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setErrorCount = None, setModifiedTime = None, setNewValue = None, setPlanPositionBenefitID = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPositionNumber = None, setPositionTypeDescription = None, setStateBenefitTXID = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnTempPlanPositionBenefitID = False, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(TempPlanPositionBenefitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionBenefit(EntityID = 1, setTempPlanPositionBenefitID = None, setBenefitCodeDescription = None, setBenefitID = None, setBenefitTypeTX = None, setCalculationType = None, setCalculationTypeCode = None, setCreatedTime = None, setErrorCount = None, setModifiedTime = None, setNewValue = None, setPlanPositionBenefitID = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPositionNumber = None, setPositionTypeDescription = None, setStateBenefitTXID = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnTempPlanPositionBenefitID = False, returnBenefitCodeDescription = False, returnBenefitID = False, returnBenefitTypeTX = False, returnCalculationType = False, returnCalculationTypeCode = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnNewValue = False, returnPlanPositionBenefitID = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPositionNumber = False, returnPositionTypeDescription = False, returnStateBenefitTXID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionBenefit(TempPlanPositionBenefitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionBenefit/" + str(TempPlanPositionBenefitID), verb = "delete")


def getEveryTempPlanPositionDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionDistribution in the district.

    This function returns a dataframe of every TempPlanPositionDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1, returnTempPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(TempPlanPositionDistributionID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1, setTempPlanPositionDistributionID = None, setAssignmentTypeID = None, setBuildingID = None, setCreatedTime = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setModifiedTime = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(TempPlanPositionDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionDistribution(EntityID = 1, setTempPlanPositionDistributionID = None, setAssignmentTypeID = None, setBuildingID = None, setCreatedTime = None, setDepartmentID = None, setFTE = None, setFTEGroupID = None, setModifiedTime = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionDistributionID = False, returnAssignmentTypeID = False, returnBuildingID = False, returnCreatedTime = False, returnDepartmentID = False, returnFTE = False, returnFTEGroupID = False, returnModifiedTime = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionDistribution(TempPlanPositionDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistribution/" + str(TempPlanPositionDistributionID), verb = "delete")


def getEveryTempPlanPositionDistributionAccountDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionDistributionAccountDistribution in the district.

    This function returns a dataframe of every TempPlanPositionDistributionAccountDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionDistributionAccountDistribution(TempPlanPositionDistributionAccountDistributionID, EntityID = 1, returnTempPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(TempPlanPositionDistributionAccountDistributionID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionDistributionAccountDistribution(TempPlanPositionDistributionAccountDistributionID, EntityID = 1, setTempPlanPositionDistributionAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setStateConcordDepartmentTNID = None, setTempPlanPositionDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(TempPlanPositionDistributionAccountDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionDistributionAccountDistribution(EntityID = 1, setTempPlanPositionDistributionAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDistributionPercent = None, setModifiedTime = None, setStateConcordDepartmentTNID = None, setTempPlanPositionDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionDistributionAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDistributionPercent = False, returnModifiedTime = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionDistributionAccountDistribution(TempPlanPositionDistributionAccountDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionDistributionAccountDistribution/" + str(TempPlanPositionDistributionAccountDistributionID), verb = "delete")


def getEveryTempPlanPositionEmployee(searchConditions = [], EntityID = 1, returnTempPlanPositionEmployeeID = False, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorCount = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCode = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionEmployee in the district.

    This function returns a dataframe of every TempPlanPositionEmployee in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1, returnTempPlanPositionEmployeeID = False, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorCount = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCode = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(TempPlanPositionEmployeeID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1, setTempPlanPositionEmployeeID = None, setAmountType = None, setAmountTypeCode = None, setAnnualPay = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBudgetedFTE = None, setBuildingCodes = None, setBuildingDescriptions = None, setCalendarCode = None, setCalendarID = None, setCappedAtMaximumRate = None, setConfigFiscalYearTRSStateBaseStepID = None, setConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = None, setCreatedTime = None, setDescription = None, setEmployeeFullNameLFM = None, setEmployeeID = None, setEmployeeNumber = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setErrorCount = None, setErrorMessage = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setHasFatalException = None, setJobTypeID = None, setLaneCode = None, setLaneID = None, setMatrixCode = None, setMatrixID = None, setMidpointGroup = None, setMidpointGroupCodeDescription = None, setMidpointGroupID = None, setModifiedTime = None, setOldAnnualPay = None, setOldBudgetedFTE = None, setOldCalendarCode = None, setOldEmployeePlacementDescription = None, setOldFormattedFullPaySecondsPerDay = None, setOldFullPaySecondsPerDay = None, setOldLaneCode = None, setOldMatrixCode = None, setOldMidpointGroup = None, setOldPlacementCode = None, setOldPlacementType = None, setOldPlacementTypeCode = None, setOldRate = None, setOldRequiredCredits = None, setOldSalaryCalculationMethodCode = None, setOldStepNumber = None, setOldTRSStateBaseStep = None, setOldTRSStateBaseStepAmount = None, setPlacementCode = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanPositionID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberCode = None, setPositionNumberID = None, setPositionTypeCode = None, setPositionTypeCodeDescription = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodCode = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTRSStateBaseStep = None, setTRSStateBaseStepAmount = None, setTRSStateBaseStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionEmployeeID = False, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorCount = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCode = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(TempPlanPositionEmployeeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionEmployee(EntityID = 1, setTempPlanPositionEmployeeID = None, setAmountType = None, setAmountTypeCode = None, setAnnualPay = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBudgetedFTE = None, setBuildingCodes = None, setBuildingDescriptions = None, setCalendarCode = None, setCalendarID = None, setCappedAtMaximumRate = None, setConfigFiscalYearTRSStateBaseStepID = None, setConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = None, setCreatedTime = None, setDescription = None, setEmployeeFullNameLFM = None, setEmployeeID = None, setEmployeeNumber = None, setEmployeePlacementDescription = None, setEmployeePlacementID = None, setErrorCount = None, setErrorMessage = None, setFormattedFullPaySecondsPerDay = None, setFullPaidDays = None, setFullPaySecondsPerDay = None, setHasFatalException = None, setJobTypeID = None, setLaneCode = None, setLaneID = None, setMatrixCode = None, setMatrixID = None, setMidpointGroup = None, setMidpointGroupCodeDescription = None, setMidpointGroupID = None, setModifiedTime = None, setOldAnnualPay = None, setOldBudgetedFTE = None, setOldCalendarCode = None, setOldEmployeePlacementDescription = None, setOldFormattedFullPaySecondsPerDay = None, setOldFullPaySecondsPerDay = None, setOldLaneCode = None, setOldMatrixCode = None, setOldMidpointGroup = None, setOldPlacementCode = None, setOldPlacementType = None, setOldPlacementTypeCode = None, setOldRate = None, setOldRequiredCredits = None, setOldSalaryCalculationMethodCode = None, setOldStepNumber = None, setOldTRSStateBaseStep = None, setOldTRSStateBaseStepAmount = None, setPlacementCode = None, setPlacementID = None, setPlacementType = None, setPlacementTypeCode = None, setPlanPositionID = None, setPositionGroupID = None, setPositionIDClonedFrom = None, setPositionIdentifier = None, setPositionNumberCode = None, setPositionNumberID = None, setPositionTypeCode = None, setPositionTypeCodeDescription = None, setPositionTypeID = None, setRate = None, setRequiredCredits = None, setSalaryCalculationMethodCode = None, setSalaryCalculationMethodID = None, setStepNumber = None, setTRSStateBaseStep = None, setTRSStateBaseStepAmount = None, setTRSStateBaseStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionEmployeeID = False, returnAmountType = False, returnAmountTypeCode = False, returnAnnualPay = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBudgetedFTE = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCalendarCode = False, returnCalendarID = False, returnCappedAtMaximumRate = False, returnConfigFiscalYearTRSStateBaseStepID = False, returnConfigFiscalYearTRSStateBaseStepLaneCodeStepNumber = False, returnCreatedTime = False, returnDescription = False, returnEmployeeFullNameLFM = False, returnEmployeeID = False, returnEmployeeNumber = False, returnEmployeePlacementDescription = False, returnEmployeePlacementID = False, returnErrorCount = False, returnErrorMessage = False, returnFormattedFullPaySecondsPerDay = False, returnFullPaidDays = False, returnFullPaySecondsPerDay = False, returnHasFatalException = False, returnJobTypeID = False, returnLaneCode = False, returnLaneID = False, returnMatrixCode = False, returnMatrixID = False, returnMidpointGroup = False, returnMidpointGroupCodeDescription = False, returnMidpointGroupID = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldBudgetedFTE = False, returnOldCalendarCode = False, returnOldEmployeePlacementDescription = False, returnOldFormattedFullPaySecondsPerDay = False, returnOldFullPaySecondsPerDay = False, returnOldLaneCode = False, returnOldMatrixCode = False, returnOldMidpointGroup = False, returnOldPlacementCode = False, returnOldPlacementType = False, returnOldPlacementTypeCode = False, returnOldRate = False, returnOldRequiredCredits = False, returnOldSalaryCalculationMethodCode = False, returnOldStepNumber = False, returnOldTRSStateBaseStep = False, returnOldTRSStateBaseStepAmount = False, returnPlacementCode = False, returnPlacementID = False, returnPlacementType = False, returnPlacementTypeCode = False, returnPlanPositionID = False, returnPositionGroupID = False, returnPositionIDClonedFrom = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnPositionNumberID = False, returnPositionTypeCode = False, returnPositionTypeCodeDescription = False, returnPositionTypeID = False, returnRate = False, returnRequiredCredits = False, returnSalaryCalculationMethodCode = False, returnSalaryCalculationMethodID = False, returnStepNumber = False, returnTRSStateBaseStep = False, returnTRSStateBaseStepAmount = False, returnTRSStateBaseStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionEmployee(TempPlanPositionEmployeeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionEmployee/" + str(TempPlanPositionEmployeeID), verb = "delete")


def getEveryTempPlanPositionException(searchConditions = [], EntityID = 1, returnTempPlanPositionExceptionID = False, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionException in the district.

    This function returns a dataframe of every TempPlanPositionException in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1, returnTempPlanPositionExceptionID = False, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(TempPlanPositionExceptionID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1, setTempPlanPositionExceptionID = None, setCreatedTime = None, setDescription = None, setError = None, setErrorType = None, setErrorTypeCode = None, setModifiedTime = None, setPositionIdentifier = None, setPositionNumberCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionExceptionID = False, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(TempPlanPositionExceptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionException(EntityID = 1, setTempPlanPositionExceptionID = None, setCreatedTime = None, setDescription = None, setError = None, setErrorType = None, setErrorTypeCode = None, setModifiedTime = None, setPositionIdentifier = None, setPositionNumberCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionExceptionID = False, returnCreatedTime = False, returnDescription = False, returnError = False, returnErrorType = False, returnErrorTypeCode = False, returnModifiedTime = False, returnPositionIdentifier = False, returnPositionNumberCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionException(TempPlanPositionExceptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionException/" + str(TempPlanPositionExceptionID), verb = "delete")


def getEveryTempPlanPositionPay(searchConditions = [], EntityID = 1, returnTempPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionPay in the district.

    This function returns a dataframe of every TempPlanPositionPay in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1, returnTempPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(TempPlanPositionPayID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1, setTempPlanPositionPayID = None, setAccountDistributionString = None, setAssignmentPayTypeIDOriginal = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBuildingCodes = None, setBuildingDescriptions = None, setCreatedTime = None, setEmployeeFullNameLFM = None, setEmployeeNumber = None, setErrorCount = None, setMatchingExpenditureEligibility = None, setMatchingExpenditureEligibilityCode = None, setModifiedTime = None, setNewDisplayAccount = None, setNewMatchingExpenditureEligibility = None, setNewMatchingExpenditureEligibilityCode = None, setOldDisplayAccount = None, setPayScheduleCodeDescription = None, setPayScheduleID = None, setPayTypeCodeDescription = None, setPayTypeID = None, setPlanPositionPayID = None, setPositionTypeCodeDescription = None, setStipendAmount = None, setTempPlanPositionEmployeeID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(TempPlanPositionPayID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionPay(EntityID = 1, setTempPlanPositionPayID = None, setAccountDistributionString = None, setAssignmentPayTypeIDOriginal = None, setAssignmentTypeCodes = None, setAssignmentTypeDescriptions = None, setBuildingCodes = None, setBuildingDescriptions = None, setCreatedTime = None, setEmployeeFullNameLFM = None, setEmployeeNumber = None, setErrorCount = None, setMatchingExpenditureEligibility = None, setMatchingExpenditureEligibilityCode = None, setModifiedTime = None, setNewDisplayAccount = None, setNewMatchingExpenditureEligibility = None, setNewMatchingExpenditureEligibilityCode = None, setOldDisplayAccount = None, setPayScheduleCodeDescription = None, setPayScheduleID = None, setPayTypeCodeDescription = None, setPayTypeID = None, setPlanPositionPayID = None, setPositionTypeCodeDescription = None, setStipendAmount = None, setTempPlanPositionEmployeeID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayID = False, returnAccountDistributionString = False, returnAssignmentPayTypeIDOriginal = False, returnAssignmentTypeCodes = False, returnAssignmentTypeDescriptions = False, returnBuildingCodes = False, returnBuildingDescriptions = False, returnCreatedTime = False, returnEmployeeFullNameLFM = False, returnEmployeeNumber = False, returnErrorCount = False, returnMatchingExpenditureEligibility = False, returnMatchingExpenditureEligibilityCode = False, returnModifiedTime = False, returnNewDisplayAccount = False, returnNewMatchingExpenditureEligibility = False, returnNewMatchingExpenditureEligibilityCode = False, returnOldDisplayAccount = False, returnPayScheduleCodeDescription = False, returnPayScheduleID = False, returnPayTypeCodeDescription = False, returnPayTypeID = False, returnPlanPositionPayID = False, returnPositionTypeCodeDescription = False, returnStipendAmount = False, returnTempPlanPositionEmployeeID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionPay(TempPlanPositionPayID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPay/" + str(TempPlanPositionPayID), verb = "delete")


def getEveryTempPlanPositionPayAccountCalculation(searchConditions = [], EntityID = 1, returnTempPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionPayAccountCalculation in the district.

    This function returns a dataframe of every TempPlanPositionPayAccountCalculation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1, returnTempPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(TempPlanPositionPayAccountCalculationID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1, setTempPlanPositionPayAccountCalculationID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(TempPlanPositionPayAccountCalculationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionPayAccountCalculation(EntityID = 1, setTempPlanPositionPayAccountCalculationID = None, setAnnualAmount = None, setCreatedTime = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayAccountCalculationID = False, returnAnnualAmount = False, returnCreatedTime = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + str(TempPlanPositionPayAccountCalculationID), verb = "delete")


def getEveryTempPlanPositionPayAccountDistribution(searchConditions = [], EntityID = 1, returnTempPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionPayAccountDistribution in the district.

    This function returns a dataframe of every TempPlanPositionPayAccountDistribution in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1, returnTempPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(TempPlanPositionPayAccountDistributionID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1, setTempPlanPositionPayAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDisplayAccount = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionPayID = None, setStateConcordDepartmentTNID = None, setTempPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(TempPlanPositionPayAccountDistributionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionPayAccountDistribution(EntityID = 1, setTempPlanPositionPayAccountDistributionID = None, setAccountID = None, setCreatedTime = None, setDisplayAccount = None, setDistributionPercent = None, setModifiedTime = None, setPlanPositionPayID = None, setStateConcordDepartmentTNID = None, setTempPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayAccountDistributionID = False, returnAccountID = False, returnCreatedTime = False, returnDisplayAccount = False, returnDistributionPercent = False, returnModifiedTime = False, returnPlanPositionPayID = False, returnStateConcordDepartmentTNID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + str(TempPlanPositionPayAccountDistributionID), verb = "delete")


def getEveryTempPlanPositionPayBenefit(searchConditions = [], EntityID = 1, returnTempPlanPositionPayBenefitID = False, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionPayBenefit in the district.

    This function returns a dataframe of every TempPlanPositionPayBenefit in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1, returnTempPlanPositionPayBenefitID = False, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(TempPlanPositionPayBenefitID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1, setTempPlanPositionPayBenefitID = None, setBenefitCodeDescription = None, setCreatedTime = None, setEmployeeNumber = None, setErrorCount = None, setModifiedTime = None, setPayScheduleCodeDescription = None, setPayTypeCodeDescription = None, setPlanPositionEmployeeName = None, setPlanPositionPayBenefitID = None, setPlanPositionPayID = None, setPositionTypeDescription = None, setTempPlanPositionBenefitID = None, setTempPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayBenefitID = False, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(TempPlanPositionPayBenefitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionPayBenefit(EntityID = 1, setTempPlanPositionPayBenefitID = None, setBenefitCodeDescription = None, setCreatedTime = None, setEmployeeNumber = None, setErrorCount = None, setModifiedTime = None, setPayScheduleCodeDescription = None, setPayTypeCodeDescription = None, setPlanPositionEmployeeName = None, setPlanPositionPayBenefitID = None, setPlanPositionPayID = None, setPositionTypeDescription = None, setTempPlanPositionBenefitID = None, setTempPlanPositionPayID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayBenefitID = False, returnBenefitCodeDescription = False, returnCreatedTime = False, returnEmployeeNumber = False, returnErrorCount = False, returnModifiedTime = False, returnPayScheduleCodeDescription = False, returnPayTypeCodeDescription = False, returnPlanPositionEmployeeName = False, returnPlanPositionPayBenefitID = False, returnPlanPositionPayID = False, returnPositionTypeDescription = False, returnTempPlanPositionBenefitID = False, returnTempPlanPositionPayID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefit/" + str(TempPlanPositionPayBenefitID), verb = "delete")


def getEveryTempPlanPositionPayBenefitAccount(searchConditions = [], EntityID = 1, returnTempPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionPayBenefitAccount in the district.

    This function returns a dataframe of every TempPlanPositionPayBenefitAccount in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1, returnTempPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(TempPlanPositionPayBenefitAccountID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1, setTempPlanPositionPayBenefitAccountID = None, setAccountID = None, setAnnualAmount = None, setCreatedTime = None, setDisplayAccount = None, setIsAccountPreviouslyCreated = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setTempPlanPositionPayBenefitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(TempPlanPositionPayBenefitAccountID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionPayBenefitAccount(EntityID = 1, setTempPlanPositionPayBenefitAccountID = None, setAccountID = None, setAnnualAmount = None, setCreatedTime = None, setDisplayAccount = None, setIsAccountPreviouslyCreated = None, setModifiedTime = None, setPlanPositionPayAccountDistributionID = None, setPlanPositionPayBenefitID = None, setTempPlanPositionPayBenefitID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionPayBenefitAccountID = False, returnAccountID = False, returnAnnualAmount = False, returnCreatedTime = False, returnDisplayAccount = False, returnIsAccountPreviouslyCreated = False, returnModifiedTime = False, returnPlanPositionPayAccountDistributionID = False, returnPlanPositionPayBenefitID = False, returnTempPlanPositionPayBenefitID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + str(TempPlanPositionPayBenefitAccountID), verb = "delete")


def getEveryTempPlanPositionSupplement(searchConditions = [], EntityID = 1, returnTempPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempPlanPositionSupplement in the district.

    This function returns a dataframe of every TempPlanPositionSupplement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1, returnTempPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(TempPlanPositionSupplementID), verb = "get", return_params_list = return_params)

def modifyTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1, setTempPlanPositionSupplementID = None, setAnnualPay = None, setCreatedTime = None, setErrorCount = None, setModifiedTime = None, setOldAnnualPay = None, setOldRate = None, setOldSupplementTypeAmountType = None, setOldSupplementTypeCodeDescription = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPlanPositionNewAnnualPay = None, setPlanPositionOldAnnualPay = None, setPlanPositionPositionTypeCodeDescription = None, setPlanPositionSupplementID = None, setRate = None, setSupplementTypeAmountType = None, setSupplementTypeCodeDescription = None, setSupplementTypeID = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(TempPlanPositionSupplementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempPlanPositionSupplement(EntityID = 1, setTempPlanPositionSupplementID = None, setAnnualPay = None, setCreatedTime = None, setErrorCount = None, setModifiedTime = None, setOldAnnualPay = None, setOldRate = None, setOldSupplementTypeAmountType = None, setOldSupplementTypeCodeDescription = None, setPlanPositionDistributionsAssignmentTypeCodes = None, setPlanPositionDistributionsBuildingCodes = None, setPlanPositionEmployeeName = None, setPlanPositionEmployeeNumber = None, setPlanPositionID = None, setPlanPositionNewAnnualPay = None, setPlanPositionOldAnnualPay = None, setPlanPositionPositionTypeCodeDescription = None, setPlanPositionSupplementID = None, setRate = None, setSupplementTypeAmountType = None, setSupplementTypeCodeDescription = None, setSupplementTypeID = None, setTempPlanPositionEmployeeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempPlanPositionSupplementID = False, returnAnnualPay = False, returnCreatedTime = False, returnErrorCount = False, returnModifiedTime = False, returnOldAnnualPay = False, returnOldRate = False, returnOldSupplementTypeAmountType = False, returnOldSupplementTypeCodeDescription = False, returnPlanPositionDistributionsAssignmentTypeCodes = False, returnPlanPositionDistributionsBuildingCodes = False, returnPlanPositionEmployeeName = False, returnPlanPositionEmployeeNumber = False, returnPlanPositionID = False, returnPlanPositionNewAnnualPay = False, returnPlanPositionOldAnnualPay = False, returnPlanPositionPositionTypeCodeDescription = False, returnPlanPositionSupplementID = False, returnRate = False, returnSupplementTypeAmountType = False, returnSupplementTypeCodeDescription = False, returnSupplementTypeID = False, returnTempPlanPositionEmployeeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempPlanPositionSupplement(TempPlanPositionSupplementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/StaffPlanning/TempPlanPositionSupplement/" + str(TempPlanPositionSupplementID), verb = "delete")