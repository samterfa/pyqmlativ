# This module contains GraduationRequirements functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryArea(searchConditions = [], EntityID = 1, returnAreaID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Area in the district.

    This function returns a dataframe of every Area in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getArea(AreaID, EntityID = 1, returnAreaID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "get", return_params_list = return_params)

def modifyArea(AreaID, EntityID = 1, setAreaID = None, setCreatedTime = None, setDescription = None, setDisplayOrder = None, setElectiveSubAreaID = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setIsNotElective = None, setIsNotSystemArea = None, setIsSystemArea = None, setModifiedTime = None, setNonElectiveCreditTotal = None, setPlanID = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setUseGradReqSubjectType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAreaID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createArea(EntityID = 1, setAreaID = None, setCreatedTime = None, setDescription = None, setDisplayOrder = None, setElectiveSubAreaID = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setIsElective = None, setIsNotElective = None, setIsNotSystemArea = None, setIsSystemArea = None, setModifiedTime = None, setNonElectiveCreditTotal = None, setPlanID = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setUseGradReqSubjectType = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAreaID = False, returnCreatedTime = False, returnDescription = False, returnDisplayOrder = False, returnElectiveSubAreaID = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnIsElective = False, returnIsNotElective = False, returnIsNotSystemArea = False, returnIsSystemArea = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnPlanID = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnUseGradReqSubjectType = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteArea(AreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Area/" + str(AreaID), verb = "delete")


def getEveryCareerPlanDeclarationTimePeriod(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CareerPlanDeclarationTimePeriod in the district.

    This function returns a dataframe of every CareerPlanDeclarationTimePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "get", return_params_list = return_params)

def modifyCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setModifiedTime = None, setSchoolYearID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCareerPlanDeclarationTimePeriod(EntityID = 1, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setModifiedTime = None, setSchoolYearID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriod(CareerPlanDeclarationTimePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriod/" + str(CareerPlanDeclarationTimePeriodID), verb = "delete")


def getEveryCareerPlanDeclarationTimePeriodGradeReference(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CareerPlanDeclarationTimePeriodGradeReference in the district.

    This function returns a dataframe of every CareerPlanDeclarationTimePeriodGradeReference in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "get", return_params_list = return_params)

def modifyCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1, setCareerPlanDeclarationTimePeriodGradeReferenceID = None, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setGradeReferenceID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCareerPlanDeclarationTimePeriodGradeReference(EntityID = 1, setCareerPlanDeclarationTimePeriodGradeReferenceID = None, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setGradeReferenceID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodGradeReferenceID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriodGradeReference(CareerPlanDeclarationTimePeriodGradeReferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodGradeReference/" + str(CareerPlanDeclarationTimePeriodGradeReferenceID), verb = "delete")


def getEveryCareerPlanDeclarationTimePeriodStudentEntityYear(searchConditions = [], EntityID = 1, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CareerPlanDeclarationTimePeriodStudentEntityYear in the district.

    This function returns a dataframe of every CareerPlanDeclarationTimePeriodStudentEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "get", return_params_list = return_params)

def modifyCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1, setCareerPlanDeclarationTimePeriodStudentEntityYearID = None, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setModifiedTime = None, setStudentEntityYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCareerPlanDeclarationTimePeriodStudentEntityYear(EntityID = 1, setCareerPlanDeclarationTimePeriodStudentEntityYearID = None, setCareerPlanDeclarationTimePeriodID = None, setCreatedTime = None, setModifiedTime = None, setStudentEntityYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanDeclarationTimePeriodStudentEntityYearID = False, returnCareerPlanDeclarationTimePeriodID = False, returnCreatedTime = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCareerPlanDeclarationTimePeriodStudentEntityYear(CareerPlanDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanDeclarationTimePeriodStudentEntityYear/" + str(CareerPlanDeclarationTimePeriodStudentEntityYearID), verb = "delete")


def getEveryCareerPlanGradeLevel(searchConditions = [], EntityID = 1, returnCareerPlanGradeLevelID = False, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CareerPlanGradeLevel in the district.

    This function returns a dataframe of every CareerPlanGradeLevel in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, returnCareerPlanGradeLevelID = False, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "get", return_params_list = return_params)

def modifyCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1, setCareerPlanGradeLevelID = None, setConfigDistrictID = None, setCreatedTime = None, setDisplayName = None, setGradeLevelID = None, setIsPriorLevel = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanGradeLevelID = False, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCareerPlanGradeLevel(EntityID = 1, setCareerPlanGradeLevelID = None, setConfigDistrictID = None, setCreatedTime = None, setDisplayName = None, setGradeLevelID = None, setIsPriorLevel = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCareerPlanGradeLevelID = False, returnConfigDistrictID = False, returnCreatedTime = False, returnDisplayName = False, returnGradeLevelID = False, returnIsPriorLevel = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCareerPlanGradeLevel(CareerPlanGradeLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CareerPlanGradeLevel/" + str(CareerPlanGradeLevelID), verb = "delete")


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setCourseWorkAppliedByType = None, setCourseWorkAppliedByTypeCode = None, setCreatedTime = None, setDistrictID = None, setGradingPeriodEndDateLastCheckedDate = None, setIncludeFutureCredit = None, setIncludeInProgressCredit = None, setModifiedTime = None, setTurnOffAutomaticCalculation = None, setTurnOffAutomaticEndorsementCalculation = None, setUsePriorToLastGradeLevel = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setCourseWorkAppliedByType = None, setCourseWorkAppliedByTypeCode = None, setCreatedTime = None, setDistrictID = None, setGradingPeriodEndDateLastCheckedDate = None, setIncludeFutureCredit = None, setIncludeInProgressCredit = None, setModifiedTime = None, setTurnOffAutomaticCalculation = None, setTurnOffAutomaticEndorsementCalculation = None, setUsePriorToLastGradeLevel = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCourseWorkAppliedByType = False, returnCourseWorkAppliedByTypeCode = False, returnCreatedTime = False, returnDistrictID = False, returnGradingPeriodEndDateLastCheckedDate = False, returnIncludeFutureCredit = False, returnIncludeInProgressCredit = False, returnModifiedTime = False, returnTurnOffAutomaticCalculation = False, returnTurnOffAutomaticEndorsementCalculation = False, returnUsePriorToLastGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


def getEveryCurriculumCluster(searchConditions = [], EntityID = 1, returnCurriculumClusterID = False, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumCluster in the district.

    This function returns a dataframe of every CurriculumCluster in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumCluster(CurriculumClusterID, EntityID = 1, returnCurriculumClusterID = False, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "get", return_params_list = return_params)

def modifyCurriculumCluster(CurriculumClusterID, EntityID = 1, setCurriculumClusterID = None, setCreatedTime = None, setCurriculumClusterDefaultID = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterID = False, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumCluster(EntityID = 1, setCurriculumClusterID = None, setCreatedTime = None, setCurriculumClusterDefaultID = None, setDescription = None, setDistrictID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterID = False, returnCreatedTime = False, returnCurriculumClusterDefaultID = False, returnDescription = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumCluster(CurriculumClusterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumCluster/" + str(CurriculumClusterID), verb = "delete")


def getEveryCurriculumClusterCurriculum(searchConditions = [], EntityID = 1, returnCurriculumClusterCurriculumID = False, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumClusterCurriculum in the district.

    This function returns a dataframe of every CurriculumClusterCurriculum in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, returnCurriculumClusterCurriculumID = False, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "get", return_params_list = return_params)

def modifyCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1, setCurriculumClusterCurriculumID = None, setCreatedTime = None, setCurriculumClusterID = None, setCurriculumID = None, setGradYearHigh = None, setGradYearLow = None, setIsAdvancedCredit = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterCurriculumID = False, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumClusterCurriculum(EntityID = 1, setCurriculumClusterCurriculumID = None, setCreatedTime = None, setCurriculumClusterID = None, setCurriculumID = None, setGradYearHigh = None, setGradYearLow = None, setIsAdvancedCredit = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterCurriculumID = False, returnCreatedTime = False, returnCurriculumClusterID = False, returnCurriculumID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsAdvancedCredit = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumClusterCurriculum(CurriculumClusterCurriculumID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterCurriculum/" + str(CurriculumClusterCurriculumID), verb = "delete")


def getEveryCurriculumClusterDefault(searchConditions = [], EntityID = 1, returnCurriculumClusterDefaultID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumClusterDefault in the district.

    This function returns a dataframe of every CurriculumClusterDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, returnCurriculumClusterDefaultID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "get", return_params_list = return_params)

def modifyCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1, setCurriculumClusterDefaultID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterDefaultID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumClusterDefault(EntityID = 1, setCurriculumClusterDefaultID = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumClusterDefaultID = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumClusterDefault(CurriculumClusterDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumClusterDefault/" + str(CurriculumClusterDefaultID), verb = "delete")


def getEveryCurriculumSubArea(searchConditions = [], EntityID = 1, returnCurriculumSubAreaID = False, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CurriculumSubArea in the district.

    This function returns a dataframe of every CurriculumSubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, returnCurriculumSubAreaID = False, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "get", return_params_list = return_params)

def modifyCurriculumSubArea(CurriculumSubAreaID, EntityID = 1, setCurriculumSubAreaID = None, setAllowReuseOfPreviouslyAppliedCredits = None, setApplicationOrder = None, setCreatedTime = None, setCurriculumID = None, setIsCustomCurriculumSubAreaWithStudentID = None, setIsGradReqRankGPAWaiver = None, setMaximumPercentOfCourseCredit = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setStudentID = None, setSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubAreaID = False, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCurriculumSubArea(EntityID = 1, setCurriculumSubAreaID = None, setAllowReuseOfPreviouslyAppliedCredits = None, setApplicationOrder = None, setCreatedTime = None, setCurriculumID = None, setIsCustomCurriculumSubAreaWithStudentID = None, setIsGradReqRankGPAWaiver = None, setMaximumPercentOfCourseCredit = None, setModifiedTime = None, setSchoolYearHigh = None, setSchoolYearLow = None, setStudentID = None, setSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCurriculumSubAreaID = False, returnAllowReuseOfPreviouslyAppliedCredits = False, returnApplicationOrder = False, returnCreatedTime = False, returnCurriculumID = False, returnIsCustomCurriculumSubAreaWithStudentID = False, returnIsGradReqRankGPAWaiver = False, returnMaximumPercentOfCourseCredit = False, returnModifiedTime = False, returnSchoolYearHigh = False, returnSchoolYearLow = False, returnStudentID = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCurriculumSubArea(CurriculumSubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/CurriculumSubArea/" + str(CurriculumSubAreaID), verb = "delete")


def getEveryEndorsement(searchConditions = [], EntityID = 1, returnEndorsementID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsDistrictDefined = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Endorsement in the district.

    This function returns a dataframe of every Endorsement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsement(EndorsementID, EntityID = 1, returnEndorsementID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsDistrictDefined = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "get", return_params_list = return_params)

def modifyEndorsement(EndorsementID, EntityID = 1, setEndorsementID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEndorsementDefaultID = None, setHasEndorsementOptions = None, setIsActive = None, setIsDeclarable = None, setIsDistrictDefined = None, setIsPreviouslyLoaded = None, setModifiedTime = None, setPrintOnTranscript = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsDistrictDefined = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsement(EntityID = 1, setEndorsementID = None, setCode = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEndorsementDefaultID = None, setHasEndorsementOptions = None, setIsActive = None, setIsDeclarable = None, setIsDistrictDefined = None, setIsPreviouslyLoaded = None, setModifiedTime = None, setPrintOnTranscript = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndorsementDefaultID = False, returnHasEndorsementOptions = False, returnIsActive = False, returnIsDeclarable = False, returnIsDistrictDefined = False, returnIsPreviouslyLoaded = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsement(EndorsementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Endorsement/" + str(EndorsementID), verb = "delete")


def getEveryEndorsementDeclarationTimePeriod(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementDeclarationTimePeriod in the district.

    This function returns a dataframe of every EndorsementDeclarationTimePeriod in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, returnEndorsementDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "get", return_params_list = return_params)

def modifyEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setCreatedTime = None, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setModifiedTime = None, setSchoolYearID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementDeclarationTimePeriod(EntityID = 1, setEndorsementDeclarationTimePeriodID = None, setCreatedTime = None, setEndTime = None, setEntityID = None, setFilterOption = None, setFilterOptionCode = None, setModifiedTime = None, setSchoolYearID = None, setStartTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodID = False, returnCreatedTime = False, returnEndTime = False, returnEntityID = False, returnFilterOption = False, returnFilterOptionCode = False, returnModifiedTime = False, returnSchoolYearID = False, returnStartTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementDeclarationTimePeriod(EndorsementDeclarationTimePeriodID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriod/" + str(EndorsementDeclarationTimePeriodID), verb = "delete")


def getEveryEndorsementDeclarationTimePeriodGradeReference(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementDeclarationTimePeriodGradeReference in the district.

    This function returns a dataframe of every EndorsementDeclarationTimePeriodGradeReference in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, returnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "get", return_params_list = return_params)

def modifyEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1, setEndorsementDeclarationTimePeriodGradeReferenceID = None, setCreatedTime = None, setEndorsementDeclarationTimePeriodID = None, setGradeReferenceID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementDeclarationTimePeriodGradeReference(EntityID = 1, setEndorsementDeclarationTimePeriodGradeReferenceID = None, setCreatedTime = None, setEndorsementDeclarationTimePeriodID = None, setGradeReferenceID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodGradeReferenceID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnGradeReferenceID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementDeclarationTimePeriodGradeReference(EndorsementDeclarationTimePeriodGradeReferenceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodGradeReference/" + str(EndorsementDeclarationTimePeriodGradeReferenceID), verb = "delete")


def getEveryEndorsementDeclarationTimePeriodStudentEntityYear(searchConditions = [], EntityID = 1, returnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementDeclarationTimePeriodStudentEntityYear in the district.

    This function returns a dataframe of every EndorsementDeclarationTimePeriodStudentEntityYear in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, returnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "get", return_params_list = return_params)

def modifyEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1, setEndorsementDeclarationTimePeriodStudentEntityYearID = None, setCreatedTime = None, setEndorsementDeclarationTimePeriodID = None, setModifiedTime = None, setStudentEntityYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementDeclarationTimePeriodStudentEntityYear(EntityID = 1, setEndorsementDeclarationTimePeriodStudentEntityYearID = None, setCreatedTime = None, setEndorsementDeclarationTimePeriodID = None, setModifiedTime = None, setStudentEntityYearID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDeclarationTimePeriodStudentEntityYearID = False, returnCreatedTime = False, returnEndorsementDeclarationTimePeriodID = False, returnModifiedTime = False, returnStudentEntityYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementDeclarationTimePeriodStudentEntityYear(EndorsementDeclarationTimePeriodStudentEntityYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDeclarationTimePeriodStudentEntityYear/" + str(EndorsementDeclarationTimePeriodStudentEntityYearID), verb = "delete")


def getEveryEndorsementDefault(searchConditions = [], EntityID = 1, returnEndorsementDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementDefault in the district.

    This function returns a dataframe of every EndorsementDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementDefault(EndorsementDefaultID, EntityID = 1, returnEndorsementDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementDefault(EndorsementDefaultID, EntityID = 1, setEndorsementDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setIsActive = None, setIsDeclarable = None, setModifiedTime = None, setPrintOnTranscript = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementDefault(EntityID = 1, setEndorsementDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setIsActive = None, setIsDeclarable = None, setModifiedTime = None, setPrintOnTranscript = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnIsActive = False, returnIsDeclarable = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementDefault(EndorsementDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementDefault/" + str(EndorsementDefaultID), verb = "delete")


def getEveryEndorsementOption(searchConditions = [], EntityID = 1, returnEndorsementOptionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementOption in the district.

    This function returns a dataframe of every EndorsementOption in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementOption(EndorsementOptionID, EntityID = 1, returnEndorsementOptionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "get", return_params_list = return_params)

def modifyEndorsementOption(EndorsementOptionID, EntityID = 1, setEndorsementOptionID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEndorsementID = None, setEndorsementOptionDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setMustCompleteGradPlan = None, setOrderNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementOptionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementOption(EntityID = 1, setEndorsementOptionID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEndorsementID = None, setEndorsementOptionDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setMustCompleteGradPlan = None, setOrderNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementOptionID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEndorsementID = False, returnEndorsementOptionDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementOption(EndorsementOptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOption/" + str(EndorsementOptionID), verb = "delete")


def getEveryEndorsementOptionDefault(searchConditions = [], EntityID = 1, returnEndorsementOptionDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementOptionDefault in the district.

    This function returns a dataframe of every EndorsementOptionDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, returnEndorsementOptionDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1, setEndorsementOptionDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setEndorsementDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setMustCompleteGradPlan = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementOptionDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementOptionDefault(EntityID = 1, setEndorsementOptionDefaultID = None, setCode = None, setCreatedTime = None, setDescription = None, setEndorsementDefaultID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setMustCompleteGradPlan = None, setOrderNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementOptionDefaultID = False, returnCode = False, returnCreatedTime = False, returnDescription = False, returnEndorsementDefaultID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnMustCompleteGradPlan = False, returnOrderNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementOptionDefault(EndorsementOptionDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementOptionDefault/" + str(EndorsementOptionDefaultID), verb = "delete")


def getEveryEndorsementRequirement(searchConditions = [], EntityID = 1, returnEndorsementRequirementID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirement in the district.

    This function returns a dataframe of every EndorsementRequirement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirement(EndorsementRequirementID, EntityID = 1, returnEndorsementRequirementID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirement(EndorsementRequirementID, EntityID = 1, setEndorsementRequirementID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setDescription = None, setEndorsementOptionID = None, setEndorsementRequirementDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setModifiedTime = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setUseMaximumClusterLimit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirement(EntityID = 1, setEndorsementRequirementID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setDescription = None, setEndorsementOptionID = None, setEndorsementRequirementDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setModifiedTime = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setUseMaximumClusterLimit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionID = False, returnEndorsementRequirementDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirement(EndorsementRequirementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirement/" + str(EndorsementRequirementID), verb = "delete")


def getEveryEndorsementRequirementAssessment(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessment in the district.

    This function returns a dataframe of every EndorsementRequirementAssessment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, returnEndorsementRequirementAssessmentID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1, setEndorsementRequirementAssessmentID = None, setClusterType = None, setClusterTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentDefaultID = None, setEndorsementRequirementID = None, setModifiedTime = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessment(EntityID = 1, setEndorsementRequirementAssessmentID = None, setClusterType = None, setClusterTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentDefaultID = None, setEndorsementRequirementID = None, setModifiedTime = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessment(EndorsementRequirementAssessmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessment/" + str(EndorsementRequirementAssessmentID), verb = "delete")


def getEveryEndorsementRequirementAssessmentCluster(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentClusterID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessmentCluster in the district.

    This function returns a dataframe of every EndorsementRequirementAssessmentCluster in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, returnEndorsementRequirementAssessmentClusterID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1, setEndorsementRequirementAssessmentClusterID = None, setClusterScoreType = None, setClusterScoreTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setEndorsementRequirementAssessmentID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentClusterID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessmentCluster(EntityID = 1, setEndorsementRequirementAssessmentClusterID = None, setClusterScoreType = None, setClusterScoreTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setEndorsementRequirementAssessmentID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentClusterID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnEndorsementRequirementAssessmentID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessmentCluster(EndorsementRequirementAssessmentClusterID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentCluster/" + str(EndorsementRequirementAssessmentClusterID), verb = "delete")


def getEveryEndorsementRequirementAssessmentClusterDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessmentClusterDefault in the district.

    This function returns a dataframe of every EndorsementRequirementAssessmentClusterDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1, setEndorsementRequirementAssessmentClusterDefaultID = None, setClusterScoreType = None, setClusterScoreTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessmentClusterDefault(EntityID = 1, setEndorsementRequirementAssessmentClusterDefaultID = None, setClusterScoreType = None, setClusterScoreTypeCode = None, setCreatedTime = None, setEndorsementRequirementAssessmentDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnClusterScoreType = False, returnClusterScoreTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessmentClusterDefault(EndorsementRequirementAssessmentClusterDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentClusterDefault/" + str(EndorsementRequirementAssessmentClusterDefaultID), verb = "delete")


def getEveryEndorsementRequirementAssessmentDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentDefaultID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessmentDefault in the district.

    This function returns a dataframe of every EndorsementRequirementAssessmentDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentDefaultID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1, setEndorsementRequirementAssessmentDefaultID = None, setClusterType = None, setClusterTypeCode = None, setCreatedTime = None, setEndorsementRequirementDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentDefaultID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessmentDefault(EntityID = 1, setEndorsementRequirementAssessmentDefaultID = None, setClusterType = None, setClusterTypeCode = None, setCreatedTime = None, setEndorsementRequirementDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setTestType = None, setTestTypeCode = None, setTestVersion = None, setTestVersionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentDefaultID = False, returnClusterType = False, returnClusterTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnTestType = False, returnTestTypeCode = False, returnTestVersion = False, returnTestVersionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessmentDefault(EndorsementRequirementAssessmentDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentDefault/" + str(EndorsementRequirementAssessmentDefaultID), verb = "delete")


def getEveryEndorsementRequirementAssessmentScore(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentScoreID = False, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessmentScore in the district.

    This function returns a dataframe of every EndorsementRequirementAssessmentScore in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, returnEndorsementRequirementAssessmentScoreID = False, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1, setEndorsementRequirementAssessmentScoreID = None, setAssessmentScoreColumn = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterID = None, setEndorsementRequirementAssessmentScoreDefaultID = None, setModifiedTime = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentScoreID = False, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessmentScore(EntityID = 1, setEndorsementRequirementAssessmentScoreID = None, setAssessmentScoreColumn = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterID = None, setEndorsementRequirementAssessmentScoreDefaultID = None, setModifiedTime = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentScoreID = False, returnAssessmentScoreColumn = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterID = False, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessmentScore(EndorsementRequirementAssessmentScoreID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScore/" + str(EndorsementRequirementAssessmentScoreID), verb = "delete")


def getEveryEndorsementRequirementAssessmentScoreDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementAssessmentScoreDefault in the district.

    This function returns a dataframe of every EndorsementRequirementAssessmentScoreDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1, setEndorsementRequirementAssessmentScoreDefaultID = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setModifiedTime = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementAssessmentScoreDefault(EntityID = 1, setEndorsementRequirementAssessmentScoreDefaultID = None, setCreatedTime = None, setEndorsementRequirementAssessmentClusterDefaultID = None, setModifiedTime = None, setPassingScore = None, setPassingScoreHigh = None, setPassingScoreLow = None, setScoreLocation = None, setScoreType = None, setScoreTypeCode = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementAssessmentScoreDefaultID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentClusterDefaultID = False, returnModifiedTime = False, returnPassingScore = False, returnPassingScoreHigh = False, returnPassingScoreLow = False, returnScoreLocation = False, returnScoreType = False, returnScoreTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementAssessmentScoreDefault(EndorsementRequirementAssessmentScoreDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementAssessmentScoreDefault/" + str(EndorsementRequirementAssessmentScoreDefaultID), verb = "delete")


def getEveryEndorsementRequirementCurriculum(searchConditions = [], EntityID = 1, returnEndorsementRequirementCurriculumID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementCurriculum in the district.

    This function returns a dataframe of every EndorsementRequirementCurriculum in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, returnEndorsementRequirementCurriculumID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1, setEndorsementRequirementCurriculumID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setCreditsRequired = None, setCurriculumClusterID = None, setEndorsementRequirementCurriculumDefaultID = None, setEndorsementRequirementID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementCurriculumID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementCurriculum(EntityID = 1, setEndorsementRequirementCurriculumID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setCreditsRequired = None, setCurriculumClusterID = None, setEndorsementRequirementCurriculumDefaultID = None, setEndorsementRequirementID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementCurriculumID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterID = False, returnEndorsementRequirementCurriculumDefaultID = False, returnEndorsementRequirementID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementCurriculum(EndorsementRequirementCurriculumID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculum/" + str(EndorsementRequirementCurriculumID), verb = "delete")


def getEveryEndorsementRequirementCurriculumDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementCurriculumDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementCurriculumDefault in the district.

    This function returns a dataframe of every EndorsementRequirementCurriculumDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, returnEndorsementRequirementCurriculumDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1, setEndorsementRequirementCurriculumDefaultID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setCreditsRequired = None, setCurriculumClusterDefaultID = None, setEndorsementRequirementDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementCurriculumDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementCurriculumDefault(EntityID = 1, setEndorsementRequirementCurriculumDefaultID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setCreditsRequired = None, setCurriculumClusterDefaultID = None, setEndorsementRequirementDefaultID = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementCurriculumDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnCreditsRequired = False, returnCurriculumClusterDefaultID = False, returnEndorsementRequirementDefaultID = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementCurriculumDefault(EndorsementRequirementCurriculumDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementCurriculumDefault/" + str(EndorsementRequirementCurriculumDefaultID), verb = "delete")


def getEveryEndorsementRequirementDefault(searchConditions = [], EntityID = 1, returnEndorsementRequirementDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EndorsementRequirementDefault in the district.

    This function returns a dataframe of every EndorsementRequirementDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, returnEndorsementRequirementDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "get", return_params_list = return_params)

def modifyEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1, setEndorsementRequirementDefaultID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setDescription = None, setEndorsementOptionDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setModifiedTime = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setSkywardHash = None, setSkywardID = None, setUseMaximumClusterLimit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEndorsementRequirementDefault(EntityID = 1, setEndorsementRequirementDefaultID = None, setAdvancedCreditsRequired = None, setCreatedTime = None, setDescription = None, setEndorsementOptionDefaultID = None, setMaximumClusterLimit = None, setMinimumClusterLimit = None, setModifiedTime = None, setMustFulfillAllCurriculumClusters = None, setOrderNumber = None, setOverallCreditsRequired = None, setRequirementAssessmentType = None, setRequirementAssessmentTypeCode = None, setRequirementType = None, setRequirementTypeCode = None, setSkywardHash = None, setSkywardID = None, setUseMaximumClusterLimit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEndorsementRequirementDefaultID = False, returnAdvancedCreditsRequired = False, returnCreatedTime = False, returnDescription = False, returnEndorsementOptionDefaultID = False, returnMaximumClusterLimit = False, returnMinimumClusterLimit = False, returnModifiedTime = False, returnMustFulfillAllCurriculumClusters = False, returnOrderNumber = False, returnOverallCreditsRequired = False, returnRequirementAssessmentType = False, returnRequirementAssessmentTypeCode = False, returnRequirementType = False, returnRequirementTypeCode = False, returnSkywardHash = False, returnSkywardID = False, returnUseMaximumClusterLimit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEndorsementRequirementDefault(EndorsementRequirementDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/EndorsementRequirementDefault/" + str(EndorsementRequirementDefaultID), verb = "delete")


def getEveryPlan(searchConditions = [], EntityID = 1, returnPlanID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlan(PlanID, EntityID = 1, returnPlanID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "get", return_params_list = return_params)

def modifyPlan(PlanID, EntityID = 1, setPlanID = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEarnedCreditsMethodIDDefaultOverride = None, setEdFiGraduationPlanID = None, setGeneralElectiveSubAreaID = None, setGradYearHigh = None, setGradYearLow = None, setIsNotSystemPlan = None, setIsSystemPlan = None, setModifiedTime = None, setNonElectiveCreditTotal = None, setNumberOfSubAreasForCurriculum = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setTotalYears = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlan(EntityID = 1, setPlanID = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setEarnedCreditsMethodIDDefaultOverride = None, setEdFiGraduationPlanID = None, setGeneralElectiveSubAreaID = None, setGradYearHigh = None, setGradYearLow = None, setIsNotSystemPlan = None, setIsSystemPlan = None, setModifiedTime = None, setNonElectiveCreditTotal = None, setNumberOfSubAreasForCurriculum = None, setSkywardHash = None, setSkywardID = None, setTotalCredits = None, setTotalYears = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanID = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEarnedCreditsMethodIDDefaultOverride = False, returnEdFiGraduationPlanID = False, returnGeneralElectiveSubAreaID = False, returnGradYearHigh = False, returnGradYearLow = False, returnIsNotSystemPlan = False, returnIsSystemPlan = False, returnModifiedTime = False, returnNonElectiveCreditTotal = False, returnNumberOfSubAreasForCurriculum = False, returnSkywardHash = False, returnSkywardID = False, returnTotalCredits = False, returnTotalYears = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlan(PlanID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/Plan/" + str(PlanID), verb = "delete")


def getEveryPlanDefault(searchConditions = [], EntityID = 1, returnPlanDefaultID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanDefault in the district.

    This function returns a dataframe of every PlanDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanDefault(PlanDefaultID, EntityID = 1, returnPlanDefaultID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "get", return_params_list = return_params)

def modifyPlanDefault(PlanDefaultID, EntityID = 1, setPlanDefaultID = None, setCreatedTime = None, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanDefaultID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanDefault(EntityID = 1, setPlanDefaultID = None, setCreatedTime = None, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setModifiedTime = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanDefaultID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanDefault(PlanDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanDefault/" + str(PlanDefaultID), verb = "delete")


def getEveryPlanEntity(searchConditions = [], EntityID = 1, returnPlanEntityID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PlanEntity in the district.

    This function returns a dataframe of every PlanEntity in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPlanEntity(PlanEntityID, EntityID = 1, returnPlanEntityID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "get", return_params_list = return_params)

def modifyPlanEntity(PlanEntityID, EntityID = 1, setPlanEntityID = None, setCreatedTime = None, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setGradYearRange = None, setModifiedTime = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanEntityID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPlanEntity(EntityID = 1, setPlanEntityID = None, setCreatedTime = None, setEntityID = None, setGradYearHigh = None, setGradYearLow = None, setGradYearRange = None, setModifiedTime = None, setPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPlanEntityID = False, returnCreatedTime = False, returnEntityID = False, returnGradYearHigh = False, returnGradYearLow = False, returnGradYearRange = False, returnModifiedTime = False, returnPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePlanEntity(PlanEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/PlanEntity/" + str(PlanEntityID), verb = "delete")


def getEveryQueuedGraduationPlanRecalcTrigger(searchConditions = [], EntityID = 1, returnQueuedGraduationPlanRecalcTriggerID = False, returnCreatedTime = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QueuedGraduationPlanRecalcTrigger in the district.

    This function returns a dataframe of every QueuedGraduationPlanRecalcTrigger in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, returnQueuedGraduationPlanRecalcTriggerID = False, returnCreatedTime = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "get", return_params_list = return_params)

def modifyQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1, setQueuedGraduationPlanRecalcTriggerID = None, setCreatedTime = None, setEndTime = None, setHostName = None, setModifiedTime = None, setProcessID = None, setSourceID = None, setSourceObject = None, setSourceObjectCode = None, setStartTime = None, setStatus = None, setStatusCode = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnQueuedGraduationPlanRecalcTriggerID = False, returnCreatedTime = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQueuedGraduationPlanRecalcTrigger(EntityID = 1, setQueuedGraduationPlanRecalcTriggerID = None, setCreatedTime = None, setEndTime = None, setHostName = None, setModifiedTime = None, setProcessID = None, setSourceID = None, setSourceObject = None, setSourceObjectCode = None, setStartTime = None, setStatus = None, setStatusCode = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnQueuedGraduationPlanRecalcTriggerID = False, returnCreatedTime = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnSourceID = False, returnSourceObject = False, returnSourceObjectCode = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQueuedGraduationPlanRecalcTrigger(QueuedGraduationPlanRecalcTriggerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedGraduationPlanRecalcTrigger/" + str(QueuedGraduationPlanRecalcTriggerID), verb = "delete")


def getEveryQueuedStudentEndorsementCalculation(searchConditions = [], EntityID = 1, returnQueuedStudentEndorsementCalculationID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QueuedStudentEndorsementCalculation in the district.

    This function returns a dataframe of every QueuedStudentEndorsementCalculation in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQueuedStudentEndorsementCalculation(QueuedStudentEndorsementCalculationID, EntityID = 1, returnQueuedStudentEndorsementCalculationID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(QueuedStudentEndorsementCalculationID), verb = "get", return_params_list = return_params)

def modifyQueuedStudentEndorsementCalculation(QueuedStudentEndorsementCalculationID, EntityID = 1, setQueuedStudentEndorsementCalculationID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedStudentEndorsementCalculationID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(QueuedStudentEndorsementCalculationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQueuedStudentEndorsementCalculation(EntityID = 1, setQueuedStudentEndorsementCalculationID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setStatus = None, setStatusCode = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnQueuedStudentEndorsementCalculationID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStatus = False, returnStatusCode = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQueuedStudentEndorsementCalculation(QueuedStudentEndorsementCalculationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentEndorsementCalculation/" + str(QueuedStudentEndorsementCalculationID), verb = "delete")


def getEveryQueuedStudentPlanCourseworkApplication(searchConditions = [], EntityID = 1, returnQueuedStudentPlanCourseworkApplicationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every QueuedStudentPlanCourseworkApplication in the district.

    This function returns a dataframe of every QueuedStudentPlanCourseworkApplication in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, returnQueuedStudentPlanCourseworkApplicationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "get", return_params_list = return_params)

def modifyQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1, setQueuedStudentPlanCourseworkApplicationID = None, setCreatedTime = None, setDistrictID = None, setEndTime = None, setHostName = None, setModifiedTime = None, setProcessID = None, setRecalculationStatusDetails = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentPlanID = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnQueuedStudentPlanCourseworkApplicationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createQueuedStudentPlanCourseworkApplication(EntityID = 1, setQueuedStudentPlanCourseworkApplicationID = None, setCreatedTime = None, setDistrictID = None, setEndTime = None, setHostName = None, setModifiedTime = None, setProcessID = None, setRecalculationStatusDetails = None, setStartTime = None, setStatus = None, setStatusCode = None, setStudentPlanID = None, setThreadName = None, setUserIDCreatedBy = None, setUserIDImpersonator = None, setUserIDModifiedBy = None, returnQueuedStudentPlanCourseworkApplicationID = False, returnCreatedTime = False, returnDistrictID = False, returnEndTime = False, returnHostName = False, returnModifiedTime = False, returnProcessID = False, returnRecalculationStatusDetails = False, returnStartTime = False, returnStatus = False, returnStatusCode = False, returnStudentPlanID = False, returnThreadName = False, returnUserIDCreatedBy = False, returnUserIDImpersonator = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteQueuedStudentPlanCourseworkApplication(QueuedStudentPlanCourseworkApplicationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/QueuedStudentPlanCourseworkApplication/" + str(QueuedStudentPlanCourseworkApplicationID), verb = "delete")


def getEveryStudentArea(searchConditions = [], EntityID = 1, returnStudentAreaID = False, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentArea in the district.

    This function returns a dataframe of every StudentArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentArea(StudentAreaID, EntityID = 1, returnStudentAreaID = False, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "get", return_params_list = return_params)

def modifyStudentArea(StudentAreaID, EntityID = 1, setStudentAreaID = None, setAreaID = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsFulfilledInPlan = None, setModifiedTime = None, setPlannedCredits = None, setRemainingCredits = None, setStudentPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentAreaID = False, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentArea(EntityID = 1, setStudentAreaID = None, setAreaID = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsFulfilledInPlan = None, setModifiedTime = None, setPlannedCredits = None, setRemainingCredits = None, setStudentPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentAreaID = False, returnAreaID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentArea(StudentAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentArea/" + str(StudentAreaID), verb = "delete")


def getEveryStudentCareerPlan(searchConditions = [], EntityID = 1, returnStudentCareerPlanID = False, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentCareerPlan in the district.

    This function returns a dataframe of every StudentCareerPlan in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentCareerPlan(StudentCareerPlanID, EntityID = 1, returnStudentCareerPlanID = False, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "get", return_params_list = return_params)

def modifyStudentCareerPlan(StudentCareerPlanID, EntityID = 1, setStudentCareerPlanID = None, setCareerPlanGradeLevelID = None, setCreatedTime = None, setCredits = None, setCurriculumID = None, setGradeListDisplay = None, setIsStudentPermittedToChangeGradeLevel = None, setIsStudentPermittedToDelete = None, setModifiedTime = None, setStudentCourseRequestID = None, setStudentID = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentCareerPlanID = False, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentCareerPlan(EntityID = 1, setStudentCareerPlanID = None, setCareerPlanGradeLevelID = None, setCreatedTime = None, setCredits = None, setCurriculumID = None, setGradeListDisplay = None, setIsStudentPermittedToChangeGradeLevel = None, setIsStudentPermittedToDelete = None, setModifiedTime = None, setStudentCourseRequestID = None, setStudentID = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentCareerPlanID = False, returnCareerPlanGradeLevelID = False, returnCreatedTime = False, returnCredits = False, returnCurriculumID = False, returnGradeListDisplay = False, returnIsStudentPermittedToChangeGradeLevel = False, returnIsStudentPermittedToDelete = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentCareerPlan(StudentCareerPlanID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentCareerPlan/" + str(StudentCareerPlanID), verb = "delete")


def getEveryStudentEndorsement(searchConditions = [], EntityID = 1, returnStudentEndorsementID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsement in the district.

    This function returns a dataframe of every StudentEndorsement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsement(StudentEndorsementID, EntityID = 1, returnStudentEndorsementID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsement(StudentEndorsementID, EntityID = 1, setStudentEndorsementID = None, setAttachmentComments = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCompletionMethod = None, setCreatedTime = None, setDistrictID = None, setEndorsementID = None, setGuardianSignedTime = None, setHasDeclaredEndorsementOptions = None, setHasEndorsementOptions = None, setHasEndorsementOptionsToAddOrDeclare = None, setIsAdminAdded = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setIsSignedByGuardian = None, setIsSignedByStudent = None, setModifiedTime = None, setNameIDGuardianSignedBy = None, setStudentID = None, setStudentSignedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsement(EntityID = 1, setStudentEndorsementID = None, setAttachmentComments = None, setAttachmentCount = None, setAttachmentIndicatorColumn = None, setCompletionMethod = None, setCreatedTime = None, setDistrictID = None, setEndorsementID = None, setGuardianSignedTime = None, setHasDeclaredEndorsementOptions = None, setHasEndorsementOptions = None, setHasEndorsementOptionsToAddOrDeclare = None, setIsAdminAdded = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setIsSignedByGuardian = None, setIsSignedByStudent = None, setModifiedTime = None, setNameIDGuardianSignedBy = None, setStudentID = None, setStudentSignedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementID = False, returnAttachmentComments = False, returnAttachmentCount = False, returnAttachmentIndicatorColumn = False, returnCompletionMethod = False, returnCreatedTime = False, returnDistrictID = False, returnEndorsementID = False, returnGuardianSignedTime = False, returnHasDeclaredEndorsementOptions = False, returnHasEndorsementOptions = False, returnHasEndorsementOptionsToAddOrDeclare = False, returnIsAdminAdded = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnIsSignedByGuardian = False, returnIsSignedByStudent = False, returnModifiedTime = False, returnNameIDGuardianSignedBy = False, returnStudentID = False, returnStudentSignedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsement(StudentEndorsementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsement/" + str(StudentEndorsementID), verb = "delete")


def getEveryStudentEndorsementOption(searchConditions = [], EntityID = 1, returnStudentEndorsementOptionID = False, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementOption in the district.

    This function returns a dataframe of every StudentEndorsementOption in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, returnStudentEndorsementOptionID = False, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1, setStudentEndorsementOptionID = None, setAdminAdded = None, setCreatedTime = None, setEndorsementOptionID = None, setGradPlanInProgress = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setModifiedTime = None, setOverallCreditsRequired = None, setStudentEndorsementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementOptionID = False, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementOption(EntityID = 1, setStudentEndorsementOptionID = None, setAdminAdded = None, setCreatedTime = None, setEndorsementOptionID = None, setGradPlanInProgress = None, setIsComplete = None, setIsDeclared = None, setIsReceived = None, setModifiedTime = None, setOverallCreditsRequired = None, setStudentEndorsementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementOptionID = False, returnAdminAdded = False, returnCreatedTime = False, returnEndorsementOptionID = False, returnGradPlanInProgress = False, returnIsComplete = False, returnIsDeclared = False, returnIsReceived = False, returnModifiedTime = False, returnOverallCreditsRequired = False, returnStudentEndorsementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementOption(StudentEndorsementOptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementOption/" + str(StudentEndorsementOptionID), verb = "delete")


def getEveryStudentEndorsementRequirement(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementRequirement in the district.

    This function returns a dataframe of every StudentEndorsementRequirement in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, returnStudentEndorsementRequirementID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1, setStudentEndorsementRequirementID = None, setAdvancedCreditsApplied = None, setCreatedTime = None, setEndorsementRequirementID = None, setIsComplete = None, setModifiedTime = None, setOverallCreditsApplied = None, setStudentEndorsementOptionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementRequirement(EntityID = 1, setStudentEndorsementRequirementID = None, setAdvancedCreditsApplied = None, setCreatedTime = None, setEndorsementRequirementID = None, setIsComplete = None, setModifiedTime = None, setOverallCreditsApplied = None, setStudentEndorsementOptionID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementOptionID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementRequirement(StudentEndorsementRequirementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirement/" + str(StudentEndorsementRequirementID), verb = "delete")


def getEveryStudentEndorsementRequirementAssessment(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementAssessmentID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementRequirementAssessment in the district.

    This function returns a dataframe of every StudentEndorsementRequirementAssessment in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, returnStudentEndorsementRequirementAssessmentID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1, setStudentEndorsementRequirementAssessmentID = None, setCreatedTime = None, setEndorsementRequirementAssessmentID = None, setIsComplete = None, setModifiedTime = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementAssessmentID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementRequirementAssessment(EntityID = 1, setStudentEndorsementRequirementAssessmentID = None, setCreatedTime = None, setEndorsementRequirementAssessmentID = None, setIsComplete = None, setModifiedTime = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementAssessmentID = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentID = False, returnIsComplete = False, returnModifiedTime = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementRequirementAssessment(StudentEndorsementRequirementAssessmentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessment/" + str(StudentEndorsementRequirementAssessmentID), verb = "delete")


def getEveryStudentEndorsementRequirementAssessmentScore(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementAssessmentScoreID = False, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementRequirementAssessmentScore in the district.

    This function returns a dataframe of every StudentEndorsementRequirementAssessmentScore in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, returnStudentEndorsementRequirementAssessmentScoreID = False, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1, setStudentEndorsementRequirementAssessmentScoreID = None, setAssessmentScore = None, setCreatedTime = None, setEndorsementRequirementAssessmentScoreID = None, setIsPassingScore = None, setModifiedTime = None, setStudentEndorsementRequirementAssessmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementAssessmentScoreID = False, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementRequirementAssessmentScore(EntityID = 1, setStudentEndorsementRequirementAssessmentScoreID = None, setAssessmentScore = None, setCreatedTime = None, setEndorsementRequirementAssessmentScoreID = None, setIsPassingScore = None, setModifiedTime = None, setStudentEndorsementRequirementAssessmentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementAssessmentScoreID = False, returnAssessmentScore = False, returnCreatedTime = False, returnEndorsementRequirementAssessmentScoreID = False, returnIsPassingScore = False, returnModifiedTime = False, returnStudentEndorsementRequirementAssessmentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementRequirementAssessmentScore(StudentEndorsementRequirementAssessmentScoreID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementAssessmentScore/" + str(StudentEndorsementRequirementAssessmentScoreID), verb = "delete")


def getEveryStudentEndorsementRequirementCourseRequest(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementCourseRequestID = False, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementRequirementCourseRequest in the district.

    This function returns a dataframe of every StudentEndorsementRequirementCourseRequest in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, returnStudentEndorsementRequirementCourseRequestID = False, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1, setStudentEndorsementRequirementCourseRequestID = None, setAppliedAdvancedCredits = None, setAppliedOverallCredits = None, setApplyToType = None, setApplyToTypeCode = None, setCreatedTime = None, setEndorsementRequirementCurriculumID = None, setModifiedTime = None, setStudentCourseRequestID = None, setStudentEndorsementRequirementCurriculumID = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementCourseRequestID = False, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementRequirementCourseRequest(EntityID = 1, setStudentEndorsementRequirementCourseRequestID = None, setAppliedAdvancedCredits = None, setAppliedOverallCredits = None, setApplyToType = None, setApplyToTypeCode = None, setCreatedTime = None, setEndorsementRequirementCurriculumID = None, setModifiedTime = None, setStudentCourseRequestID = None, setStudentEndorsementRequirementCurriculumID = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementCourseRequestID = False, returnAppliedAdvancedCredits = False, returnAppliedOverallCredits = False, returnApplyToType = False, returnApplyToTypeCode = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnModifiedTime = False, returnStudentCourseRequestID = False, returnStudentEndorsementRequirementCurriculumID = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementRequirementCourseRequest(StudentEndorsementRequirementCourseRequestID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCourseRequest/" + str(StudentEndorsementRequirementCourseRequestID), verb = "delete")


def getEveryStudentEndorsementRequirementCurriculum(searchConditions = [], EntityID = 1, returnStudentEndorsementRequirementCurriculumID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentEndorsementRequirementCurriculum in the district.

    This function returns a dataframe of every StudentEndorsementRequirementCurriculum in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, returnStudentEndorsementRequirementCurriculumID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "get", return_params_list = return_params)

def modifyStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1, setStudentEndorsementRequirementCurriculumID = None, setAdvancedCreditsApplied = None, setCreatedTime = None, setEndorsementRequirementCurriculumID = None, setIsComplete = None, setModifiedTime = None, setOverallCreditsApplied = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementCurriculumID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentEndorsementRequirementCurriculum(EntityID = 1, setStudentEndorsementRequirementCurriculumID = None, setAdvancedCreditsApplied = None, setCreatedTime = None, setEndorsementRequirementCurriculumID = None, setIsComplete = None, setModifiedTime = None, setOverallCreditsApplied = None, setStudentEndorsementRequirementID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentEndorsementRequirementCurriculumID = False, returnAdvancedCreditsApplied = False, returnCreatedTime = False, returnEndorsementRequirementCurriculumID = False, returnIsComplete = False, returnModifiedTime = False, returnOverallCreditsApplied = False, returnStudentEndorsementRequirementID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentEndorsementRequirementCurriculum(StudentEndorsementRequirementCurriculumID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentEndorsementRequirementCurriculum/" + str(StudentEndorsementRequirementCurriculumID), verb = "delete")


def getEveryStudentPlan(searchConditions = [], EntityID = 1, returnStudentPlanID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentPlan in the district.

    This function returns a dataframe of every StudentPlan in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentPlan(StudentPlanID, EntityID = 1, returnStudentPlanID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "get", return_params_list = return_params)

def modifyStudentPlan(StudentPlanID, EntityID = 1, setStudentPlanID = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsCurrent = None, setModifiedTime = None, setPlanID = None, setPlannedCredits = None, setRemainingCredits = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentPlanID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentPlan(EntityID = 1, setStudentPlanID = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsCurrent = None, setModifiedTime = None, setPlanID = None, setPlannedCredits = None, setRemainingCredits = None, setStudentID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentPlanID = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsCurrent = False, returnModifiedTime = False, returnPlanID = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentPlan(StudentPlanID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlan/" + str(StudentPlanID), verb = "delete")


def getEveryStudentPlanThreadLock(searchConditions = [], EntityID = 1, returnStudentPlanThreadLockID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentPlanThreadLock in the district.

    This function returns a dataframe of every StudentPlanThreadLock in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, returnStudentPlanThreadLockID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "get", return_params_list = return_params)

def modifyStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1, setStudentPlanThreadLockID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setStudentPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentPlanThreadLockID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentPlanThreadLock(EntityID = 1, setStudentPlanThreadLockID = None, setCreatedTime = None, setDistrictID = None, setModifiedTime = None, setStudentPlanID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentPlanThreadLockID = False, returnCreatedTime = False, returnDistrictID = False, returnModifiedTime = False, returnStudentPlanID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentPlanThreadLock(StudentPlanThreadLockID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentPlanThreadLock/" + str(StudentPlanThreadLockID), verb = "delete")


def getEveryStudentSubArea(searchConditions = [], EntityID = 1, returnStudentSubAreaID = False, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentSubArea in the district.

    This function returns a dataframe of every StudentSubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentSubArea(StudentSubAreaID, EntityID = 1, returnStudentSubAreaID = False, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "get", return_params_list = return_params)

def modifyStudentSubArea(StudentSubAreaID, EntityID = 1, setStudentSubAreaID = None, setAttemptedCredits = None, setCanAddManualStudentSubAreaCurriculumSubArea = None, setCanAddWaiver = None, setCanHaveWaiver = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsFulfilledInPlan = None, setModifiedTime = None, setPlannedCredits = None, setRemainingCredits = None, setStudentAreaID = None, setStudentPlanID = None, setSubAreaID = None, setTotalManualCredits = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentSubAreaID = False, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentSubArea(EntityID = 1, setStudentSubAreaID = None, setAttemptedCredits = None, setCanAddManualStudentSubAreaCurriculumSubArea = None, setCanAddWaiver = None, setCanHaveWaiver = None, setCompletedCredits = None, setCreatedTime = None, setFutureCredits = None, setInProgressCredits = None, setIsFulfilledInPlan = None, setModifiedTime = None, setPlannedCredits = None, setRemainingCredits = None, setStudentAreaID = None, setStudentPlanID = None, setSubAreaID = None, setTotalManualCredits = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivedCredits = None, returnStudentSubAreaID = False, returnAttemptedCredits = False, returnCanAddManualStudentSubAreaCurriculumSubArea = False, returnCanAddWaiver = False, returnCanHaveWaiver = False, returnCompletedCredits = False, returnCreatedTime = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsFulfilledInPlan = False, returnModifiedTime = False, returnPlannedCredits = False, returnRemainingCredits = False, returnStudentAreaID = False, returnStudentPlanID = False, returnSubAreaID = False, returnTotalManualCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivedCredits = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentSubArea(StudentSubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubArea/" + str(StudentSubAreaID), verb = "delete")


def getEveryStudentSubAreaCurriculumSubArea(searchConditions = [], EntityID = 1, returnStudentSubAreaCurriculumSubAreaID = False, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentSubAreaCurriculumSubArea in the district.

    This function returns a dataframe of every StudentSubAreaCurriculumSubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, returnStudentSubAreaCurriculumSubAreaID = False, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "get", return_params_list = return_params)

def modifyStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1, setStudentSubAreaCurriculumSubAreaID = None, setAppliedOrder = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setCurriculumSubAreaID = None, setEntryMethod = None, setEntryMethodCode = None, setFutureCredits = None, setInProgressCredits = None, setIsAutomatic = None, setModifiedTime = None, setPlannedCredits = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setTotalCredits = None, setTotalNonAttemptedCredits = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSubAreaCurriculumSubAreaID = False, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentSubAreaCurriculumSubArea(EntityID = 1, setStudentSubAreaCurriculumSubAreaID = None, setAppliedOrder = None, setAttemptedCredits = None, setCompletedCredits = None, setCreatedTime = None, setCurriculumSubAreaID = None, setEntryMethod = None, setEntryMethodCode = None, setFutureCredits = None, setInProgressCredits = None, setIsAutomatic = None, setModifiedTime = None, setPlannedCredits = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setTotalCredits = None, setTotalNonAttemptedCredits = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSubAreaCurriculumSubAreaID = False, returnAppliedOrder = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntryMethod = False, returnEntryMethodCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnIsAutomatic = False, returnModifiedTime = False, returnPlannedCredits = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnTotalCredits = False, returnTotalNonAttemptedCredits = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentSubAreaCurriculumSubArea(StudentSubAreaCurriculumSubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaCurriculumSubArea/" + str(StudentSubAreaCurriculumSubAreaID), verb = "delete")


def getEveryStudentSubAreaWaiver(searchConditions = [], EntityID = 1, returnStudentSubAreaWaiverID = False, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every StudentSubAreaWaiver in the district.

    This function returns a dataframe of every StudentSubAreaWaiver in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, returnStudentSubAreaWaiverID = False, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "get", return_params_list = return_params)

def modifyStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1, setStudentSubAreaWaiverID = None, setComment = None, setCreatedTime = None, setCredits = None, setModifiedTime = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSubAreaWaiverID = False, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStudentSubAreaWaiver(EntityID = 1, setStudentSubAreaWaiverID = None, setComment = None, setCreatedTime = None, setCredits = None, setModifiedTime = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStudentSubAreaWaiverID = False, returnComment = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStudentSubAreaWaiver(StudentSubAreaWaiverID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/StudentSubAreaWaiver/" + str(StudentSubAreaWaiverID), verb = "delete")


def getEverySubArea(searchConditions = [], EntityID = 1, returnSubAreaID = False, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubArea in the district.

    This function returns a dataframe of every SubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubArea(SubAreaID, EntityID = 1, returnSubAreaID = False, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "get", return_params_list = return_params)

def modifySubArea(SubAreaID, EntityID = 1, setSubAreaID = None, setAreaID = None, setAreaSubAreaDescription = None, setCreatedTime = None, setCredits = None, setCurriculumSubAreaExistsForNonStudentCurriculum = None, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setHasSkywardID = None, setIsElective = None, setIsSystemSubArea = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaID = False, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubArea(EntityID = 1, setSubAreaID = None, setAreaID = None, setAreaSubAreaDescription = None, setCreatedTime = None, setCredits = None, setCurriculumSubAreaExistsForNonStudentCurriculum = None, setDescription = None, setDisplayOrder = None, setGradReqRankGPARequiredCourseRuleOverride = None, setGradReqRankGPARequiredCourseRuleOverrideCode = None, setHasSkywardID = None, setIsElective = None, setIsSystemSubArea = None, setModifiedTime = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaID = False, returnAreaID = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnCurriculumSubAreaExistsForNonStudentCurriculum = False, returnDescription = False, returnDisplayOrder = False, returnGradReqRankGPARequiredCourseRuleOverride = False, returnGradReqRankGPARequiredCourseRuleOverrideCode = False, returnHasSkywardID = False, returnIsElective = False, returnIsSystemSubArea = False, returnModifiedTime = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubArea(SubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubArea/" + str(SubAreaID), verb = "delete")


def getEverySubAreaLimitGroup(searchConditions = [], EntityID = 1, returnSubAreaLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubAreaLimitGroup in the district.

    This function returns a dataframe of every SubAreaLimitGroup in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, returnSubAreaLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "get", return_params_list = return_params)

def modifySubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1, setSubAreaLimitGroupID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCreditLimit = None, setDescription = None, setModifiedTime = None, setSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubAreaLimitGroup(EntityID = 1, setSubAreaLimitGroupID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCreditLimit = None, setDescription = None, setModifiedTime = None, setSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaLimitGroupID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCreditLimit = False, returnDescription = False, returnModifiedTime = False, returnSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubAreaLimitGroup(SubAreaLimitGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroup/" + str(SubAreaLimitGroupID), verb = "delete")


def getEverySubAreaLimitGroupCurriculumSubArea(searchConditions = [], EntityID = 1, returnSubAreaLimitGroupCurriculumSubAreaID = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every SubAreaLimitGroupCurriculumSubArea in the district.

    This function returns a dataframe of every SubAreaLimitGroupCurriculumSubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, returnSubAreaLimitGroupCurriculumSubAreaID = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "get", return_params_list = return_params)

def modifySubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1, setSubAreaLimitGroupCurriculumSubAreaID = None, setCreatedTime = None, setCurriculumSubAreaID = None, setModifiedTime = None, setSubAreaLimitGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaLimitGroupCurriculumSubAreaID = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSubAreaLimitGroupCurriculumSubArea(EntityID = 1, setSubAreaLimitGroupCurriculumSubAreaID = None, setCreatedTime = None, setCurriculumSubAreaID = None, setModifiedTime = None, setSubAreaLimitGroupID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnSubAreaLimitGroupCurriculumSubAreaID = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnModifiedTime = False, returnSubAreaLimitGroupID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSubAreaLimitGroupCurriculumSubArea(SubAreaLimitGroupCurriculumSubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/SubAreaLimitGroupCurriculumSubArea/" + str(SubAreaLimitGroupCurriculumSubAreaID), verb = "delete")


def getEveryTempEndorsementDefault(searchConditions = [], EntityID = 1, returnTempEndorsementDefaultID = False, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempEndorsementDefault in the district.

    This function returns a dataframe of every TempEndorsementDefault in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, returnTempEndorsementDefaultID = False, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "get", return_params_list = return_params)

def modifyTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1, setTempEndorsementDefaultID = None, setActionType = None, setActionTypeCode = None, setCodeDescription = None, setCreatedTime = None, setEndorsementDefaultID = None, setEndorsementID = None, setModifiedTime = None, setPrintOnTranscript = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivable = None, returnTempEndorsementDefaultID = False, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEndorsementDefault(EntityID = 1, setTempEndorsementDefaultID = None, setActionType = None, setActionTypeCode = None, setCodeDescription = None, setCreatedTime = None, setEndorsementDefaultID = None, setEndorsementID = None, setModifiedTime = None, setPrintOnTranscript = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWaivable = None, returnTempEndorsementDefaultID = False, returnActionType = False, returnActionTypeCode = False, returnCodeDescription = False, returnCreatedTime = False, returnEndorsementDefaultID = False, returnEndorsementID = False, returnModifiedTime = False, returnPrintOnTranscript = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWaivable = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEndorsementDefault(TempEndorsementDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementDefault/" + str(TempEndorsementDefaultID), verb = "delete")


def getEveryTempEndorsementImportError(searchConditions = [], EntityID = 1, returnTempEndorsementImportErrorID = False, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempEndorsementImportError in the district.

    This function returns a dataframe of every TempEndorsementImportError in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, returnTempEndorsementImportErrorID = False, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "get", return_params_list = return_params)

def modifyTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1, setTempEndorsementImportErrorID = None, setCodeDescription = None, setCreatedTime = None, setErrorString = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEndorsementImportErrorID = False, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEndorsementImportError(EntityID = 1, setTempEndorsementImportErrorID = None, setCodeDescription = None, setCreatedTime = None, setErrorString = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEndorsementImportErrorID = False, returnCodeDescription = False, returnCreatedTime = False, returnErrorString = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEndorsementImportError(TempEndorsementImportErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempEndorsementImportError/" + str(TempEndorsementImportErrorID), verb = "delete")


def getEveryTempFailedStudentSubAreaCurriculumSubArea(searchConditions = [], EntityID = 1, returnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFailedStudentSubAreaCurriculumSubArea in the district.

    This function returns a dataframe of every TempFailedStudentSubAreaCurriculumSubArea in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, returnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "get", return_params_list = return_params)

def modifyTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1, setTempFailedStudentSubAreaCurriculumSubAreaID = None, setActionType = None, setAppliedOrder = None, setAreaSubAreaDescription = None, setAttemptedCredits = None, setCompletedCredits = None, setCourseCode = None, setCourseDescription = None, setCreatedTime = None, setCurriculumSubAreaID = None, setEntityCode = None, setFutureCredits = None, setInProgressCredits = None, setModifiedTime = None, setNote = None, setSchoolYearDescription = None, setSectionCode = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFailedStudentSubAreaCurriculumSubArea(EntityID = 1, setTempFailedStudentSubAreaCurriculumSubAreaID = None, setActionType = None, setAppliedOrder = None, setAreaSubAreaDescription = None, setAttemptedCredits = None, setCompletedCredits = None, setCourseCode = None, setCourseDescription = None, setCreatedTime = None, setCurriculumSubAreaID = None, setEntityCode = None, setFutureCredits = None, setInProgressCredits = None, setModifiedTime = None, setNote = None, setSchoolYearDescription = None, setSectionCode = None, setStudentCourseRequestID = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFailedStudentSubAreaCurriculumSubAreaID = False, returnActionType = False, returnAppliedOrder = False, returnAreaSubAreaDescription = False, returnAttemptedCredits = False, returnCompletedCredits = False, returnCourseCode = False, returnCourseDescription = False, returnCreatedTime = False, returnCurriculumSubAreaID = False, returnEntityCode = False, returnFutureCredits = False, returnInProgressCredits = False, returnModifiedTime = False, returnNote = False, returnSchoolYearDescription = False, returnSectionCode = False, returnStudentCourseRequestID = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFailedStudentSubAreaCurriculumSubArea(TempFailedStudentSubAreaCurriculumSubAreaID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaCurriculumSubArea/" + str(TempFailedStudentSubAreaCurriculumSubAreaID), verb = "delete")


def getEveryTempFailedStudentSubAreaWaiver(searchConditions = [], EntityID = 1, returnTempFailedStudentSubAreaWaiverID = False, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempFailedStudentSubAreaWaiver in the district.

    This function returns a dataframe of every TempFailedStudentSubAreaWaiver in the district filtered by search conditions.

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, returnTempFailedStudentSubAreaWaiverID = False, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "get", return_params_list = return_params)

def modifyTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1, setTempFailedStudentSubAreaWaiverID = None, setActionType = None, setAreaSubAreaDescription = None, setCreatedTime = None, setCredits = None, setModifiedTime = None, setNote = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFailedStudentSubAreaWaiverID = False, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempFailedStudentSubAreaWaiver(EntityID = 1, setTempFailedStudentSubAreaWaiverID = None, setActionType = None, setAreaSubAreaDescription = None, setCreatedTime = None, setCredits = None, setModifiedTime = None, setNote = None, setStudentSubAreaID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempFailedStudentSubAreaWaiverID = False, returnActionType = False, returnAreaSubAreaDescription = False, returnCreatedTime = False, returnCredits = False, returnModifiedTime = False, returnNote = False, returnStudentSubAreaID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempFailedStudentSubAreaWaiver(TempFailedStudentSubAreaWaiverID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/GraduationRequirements/TempFailedStudentSubAreaWaiver/" + str(TempFailedStudentSubAreaWaiverID), verb = "delete")