# This module contains Demographics functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryACHAccount(searchConditions = [], EntityID = 1, returnACHAccountID = False, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every ACHAccount in the district.

    This function returns a dataframe of every ACHAccount in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getACHAccount(ACHAccountID, EntityID = 1, returnACHAccountID = False, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "get", return_params_list = return_params)

def modifyACHAccount(ACHAccountID, EntityID = 1, setACHAccountID = None, setAccountType = None, setAccountTypeCode = None, setACHAccountNumber = None, setClass = None, setClassCode = None, setCompanyEntryDescription = None, setCreatedTime = None, setIsActive = None, setIsEmployeeChildSupportACH = None, setIsEmployeeNetPayrollACH = None, setIsStateDisbursementUnit = None, setIsVendorAccountsPayableACH = None, setModifiedTime = None, setNameID = None, setPrenoteDate = None, setReceivingCompany = None, setRoutingNumber = None, setStateIDSDU = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnACHAccountID = False, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "post", return_params_list = return_params, payload = payload_params)

def createACHAccount(EntityID = 1, setACHAccountID = None, setAccountType = None, setAccountTypeCode = None, setACHAccountNumber = None, setClass = None, setClassCode = None, setCompanyEntryDescription = None, setCreatedTime = None, setIsActive = None, setIsEmployeeChildSupportACH = None, setIsEmployeeNetPayrollACH = None, setIsStateDisbursementUnit = None, setIsVendorAccountsPayableACH = None, setModifiedTime = None, setNameID = None, setPrenoteDate = None, setReceivingCompany = None, setRoutingNumber = None, setStateIDSDU = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnACHAccountID = False, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteACHAccount(ACHAccountID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "delete")


def getEveryAddress(searchConditions = [], EntityID = 1, returnAddressID = False, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnGeoID = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnIsLoadedLatitudeLongitude = False, returnLatitude = False, returnLatitudeLongitudeConfidence = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Address in the district.

    This function returns a dataframe of every Address in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAddress(AddressID, EntityID = 1, returnAddressID = False, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnGeoID = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnIsLoadedLatitudeLongitude = False, returnLatitude = False, returnLatitudeLongitudeConfidence = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "get", return_params_list = return_params)

def modifyAddress(AddressID, EntityID = 1, setAddressID = None, setAddressLine2 = None, setAddressRangeNumericStreetNumber = None, setAddressRangeNumericStreetNumberIsOdd = None, setAddressSecondaryUnitID = None, setAddressType = None, setAddressTypeCode = None, setCountyID = None, setCreatedTime = None, setFormattedFullAddress = None, setFreeformAddress = None, setFullAddress = None, setGeoID = None, setInternationalAddress1 = None, setInternationalAddress2 = None, setInternationalAddress3 = None, setInternationalAddress4 = None, setIsLoadedLatitudeLongitude = None, setLatitude = None, setLatitudeLongitudeConfidence = None, setLongitude = None, setModifiedTime = None, setPOBox = None, setPrintableHTMLAddress = None, setSecondaryUnitNumber = None, setStreetID = None, setStreetNumber = None, setStreetNumberAndName = None, setStreetNumberAndNameIncludeSecondaryUnit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCodeAddOn = None, setZipCodeWithAddon = None, setZipCodeWithAddonNoHyphen = None, setZipID = None, returnAddressID = False, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnGeoID = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnIsLoadedLatitudeLongitude = False, returnLatitude = False, returnLatitudeLongitudeConfidence = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAddress(EntityID = 1, setAddressID = None, setAddressLine2 = None, setAddressRangeNumericStreetNumber = None, setAddressRangeNumericStreetNumberIsOdd = None, setAddressSecondaryUnitID = None, setAddressType = None, setAddressTypeCode = None, setCountyID = None, setCreatedTime = None, setFormattedFullAddress = None, setFreeformAddress = None, setFullAddress = None, setGeoID = None, setInternationalAddress1 = None, setInternationalAddress2 = None, setInternationalAddress3 = None, setInternationalAddress4 = None, setIsLoadedLatitudeLongitude = None, setLatitude = None, setLatitudeLongitudeConfidence = None, setLongitude = None, setModifiedTime = None, setPOBox = None, setPrintableHTMLAddress = None, setSecondaryUnitNumber = None, setStreetID = None, setStreetNumber = None, setStreetNumberAndName = None, setStreetNumberAndNameIncludeSecondaryUnit = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCodeAddOn = None, setZipCodeWithAddon = None, setZipCodeWithAddonNoHyphen = None, setZipID = None, returnAddressID = False, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnGeoID = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnIsLoadedLatitudeLongitude = False, returnLatitude = False, returnLatitudeLongitudeConfidence = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAddress(AddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "delete")


def getEveryAddressRangeDefault(searchConditions = [], EntityID = 1, returnAddressRangeDefaultID = False, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AddressRangeDefault in the district.

    This function returns a dataframe of every AddressRangeDefault in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, returnAddressRangeDefaultID = False, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "get", return_params_list = return_params)

def modifyAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, setAddressRangeDefaultID = None, setAddressRangeDefaultIDClonedFrom = None, setAddressRangeDefaultIDClonedTo = None, setCity = None, setCreatedTime = None, setDefaultSchools = None, setDistrictID = None, setFullAddressRange = None, setIsManual = None, setModifiedTime = None, setSchoolPathID = None, setSchoolYearID = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSide = None, setStreetSideCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, setZipCodeAddOn = None, returnAddressRangeDefaultID = False, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAddressRangeDefault(EntityID = 1, setAddressRangeDefaultID = None, setAddressRangeDefaultIDClonedFrom = None, setAddressRangeDefaultIDClonedTo = None, setCity = None, setCreatedTime = None, setDefaultSchools = None, setDistrictID = None, setFullAddressRange = None, setIsManual = None, setModifiedTime = None, setSchoolPathID = None, setSchoolYearID = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSide = None, setStreetSideCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, setZipCodeAddOn = None, returnAddressRangeDefaultID = False, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolPathID = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAddressRangeDefault(AddressRangeDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "delete")


def getEveryAddressRangeDefaultAddress(searchConditions = [], EntityID = 1, returnAddressRangeDefaultAddressID = False, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AddressRangeDefaultAddress in the district.

    This function returns a dataframe of every AddressRangeDefaultAddress in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, returnAddressRangeDefaultAddressID = False, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "get", return_params_list = return_params)

def modifyAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, setAddressRangeDefaultAddressID = None, setAddressID = None, setAddressRangeDefaultID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressRangeDefaultAddressID = False, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAddressRangeDefaultAddress(EntityID = 1, setAddressRangeDefaultAddressID = None, setAddressID = None, setAddressRangeDefaultID = None, setCreatedTime = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressRangeDefaultAddressID = False, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "delete")


def getEveryAddressRangeImportSchool(searchConditions = [], EntityID = 1, returnAddressRangeImportSchoolID = False, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AddressRangeImportSchool in the district.

    This function returns a dataframe of every AddressRangeImportSchool in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, returnAddressRangeImportSchoolID = False, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "get", return_params_list = return_params)

def modifyAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, setAddressRangeImportSchoolID = None, setAddressRangeImportSchoolIDClonedFrom = None, setAddressRangeImportSchoolIDClonedTo = None, setCreatedTime = None, setDescription = None, setImportSchoolCode = None, setModifiedTime = None, setSchoolID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressRangeImportSchoolID = False, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAddressRangeImportSchool(EntityID = 1, setAddressRangeImportSchoolID = None, setAddressRangeImportSchoolIDClonedFrom = None, setAddressRangeImportSchoolIDClonedTo = None, setCreatedTime = None, setDescription = None, setImportSchoolCode = None, setModifiedTime = None, setSchoolID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressRangeImportSchoolID = False, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "delete")


def getEveryAddressSecondaryUnit(searchConditions = [], EntityID = 1, returnAddressSecondaryUnitID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every AddressSecondaryUnit in the district.

    This function returns a dataframe of every AddressSecondaryUnit in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, returnAddressSecondaryUnitID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "get", return_params_list = return_params)

def modifyAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, setAddressSecondaryUnitID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRequiresNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressSecondaryUnitID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "post", return_params_list = return_params, payload = payload_params)

def createAddressSecondaryUnit(EntityID = 1, setAddressSecondaryUnitID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setRequiresNumber = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnAddressSecondaryUnitID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "delete")


def getEveryCertification(searchConditions = [], EntityID = 1, returnCertificationID = False, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Certification in the district.

    This function returns a dataframe of every Certification in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertification(CertificationID, EntityID = 1, returnCertificationID = False, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "get", return_params_list = return_params)

def modifyCertification(CertificationID, EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationThirdPartyImportID = None, setCertificationTypeID = None, setComment = None, setCreatedTime = None, setExpirationDate = None, setInstitutionID = None, setIssueDate = None, setModifiedTime = None, setNameID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationID = False, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertification(EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationThirdPartyImportID = None, setCertificationTypeID = None, setComment = None, setCreatedTime = None, setExpirationDate = None, setInstitutionID = None, setIssueDate = None, setModifiedTime = None, setNameID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationID = False, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertification(CertificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "delete")


def getEveryCertificationCompetency(searchConditions = [], EntityID = 1, returnCertificationCompetencyID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationCompetency in the district.

    This function returns a dataframe of every CertificationCompetency in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationCompetency(CertificationCompetencyID, EntityID = 1, returnCertificationCompetencyID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "get", return_params_list = return_params)

def modifyCertificationCompetency(CertificationCompetencyID, EntityID = 1, setCertificationCompetencyID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationCompetencyID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationCompetency(EntityID = 1, setCertificationCompetencyID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationCompetencyID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationCompetency(CertificationCompetencyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "delete")


def getEveryCertificationDelimitedFileFormat(searchConditions = [], EntityID = 1, returnCertificationDelimitedFileFormatID = False, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationDelimitedFileFormat in the district.

    This function returns a dataframe of every CertificationDelimitedFileFormat in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, returnCertificationDelimitedFileFormatID = False, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "get", return_params_list = return_params)

def modifyCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, setCertificationDelimitedFileFormatID = None, setCertificationCompetencyColumnNumber = None, setCertificationDetailExpirationDateColumnNumber = None, setCertificationDetailIssueDateColumnNumber = None, setCertificationLevelColumnNumber = None, setCertificationNumberColumnNumber = None, setCertificationSubjectColumnNumber = None, setCertificationThirdPartyFormatID = None, setCertificationTypeColumnNumber = None, setCommentColumnNumber = None, setCreatedTime = None, setDelimiterCharacter = None, setDelimiterType = None, setDelimiterTypeCode = None, setEmployeeColumnNumber = None, setExpirationDateColumnNumber = None, setHighCertificationGradeColumnNumber = None, setHighlyQualifiedColumnNumber = None, setInstitutionNameColumnNumber = None, setIssueDateColumnNumber = None, setLowCertificationGradeColumnNumber = None, setModifiedTime = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateColumnNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationDelimitedFileFormatID = False, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationDelimitedFileFormat(EntityID = 1, setCertificationDelimitedFileFormatID = None, setCertificationCompetencyColumnNumber = None, setCertificationDetailExpirationDateColumnNumber = None, setCertificationDetailIssueDateColumnNumber = None, setCertificationLevelColumnNumber = None, setCertificationNumberColumnNumber = None, setCertificationSubjectColumnNumber = None, setCertificationThirdPartyFormatID = None, setCertificationTypeColumnNumber = None, setCommentColumnNumber = None, setCreatedTime = None, setDelimiterCharacter = None, setDelimiterType = None, setDelimiterTypeCode = None, setEmployeeColumnNumber = None, setExpirationDateColumnNumber = None, setHighCertificationGradeColumnNumber = None, setHighlyQualifiedColumnNumber = None, setInstitutionNameColumnNumber = None, setIssueDateColumnNumber = None, setLowCertificationGradeColumnNumber = None, setModifiedTime = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateColumnNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationDelimitedFileFormatID = False, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "delete")


def getEveryCertificationDetail(searchConditions = [], EntityID = 1, returnCertificationDetailID = False, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationDetail in the district.

    This function returns a dataframe of every CertificationDetail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationDetail(CertificationDetailID, EntityID = 1, returnCertificationDetailID = False, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "get", return_params_list = return_params)

def modifyCertificationDetail(CertificationDetailID, EntityID = 1, setCertificationDetailID = None, setCertificationCompetencyID = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationID = None, setCertificationLevelID = None, setCertificationSubjectID = None, setCertificationThirdPartyImportID = None, setCreatedTime = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationDetailID = False, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationDetail(EntityID = 1, setCertificationDetailID = None, setCertificationCompetencyID = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationID = None, setCertificationLevelID = None, setCertificationSubjectID = None, setCertificationThirdPartyImportID = None, setCreatedTime = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationDetailID = False, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationDetail(CertificationDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "delete")


def getEveryCertificationFixedLengthFileFormat(searchConditions = [], EntityID = 1, returnCertificationFixedLengthFileFormatID = False, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationFixedLengthFileFormat in the district.

    This function returns a dataframe of every CertificationFixedLengthFileFormat in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, returnCertificationFixedLengthFileFormatID = False, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "get", return_params_list = return_params)

def modifyCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, setCertificationFixedLengthFileFormatID = None, setCertificationCompetencyLength = None, setCertificationCompetencyStartPosition = None, setCertificationDetailExpirationDateLength = None, setCertificationDetailExpirationDateStartPosition = None, setCertificationDetailIssueDateLength = None, setCertificationDetailIssueDateStartPosition = None, setCertificationLevelLength = None, setCertificationLevelStartPosition = None, setCertificationNumberLength = None, setCertificationNumberStartPosition = None, setCertificationSubjectLength = None, setCertificationSubjectStartPosition = None, setCertificationThirdPartyFormatID = None, setCertificationTypeLength = None, setCertificationTypeStartPosition = None, setCommentLength = None, setCommentStartPosition = None, setCreatedTime = None, setEmployeeLength = None, setEmployeeStartPosition = None, setExpirationDateLength = None, setExpirationDateStartPosition = None, setHighCertificationGradeLength = None, setHighCertificationGradeStartPosition = None, setHighlyQualifiedLength = None, setHighlyQualifiedStartPosition = None, setInstitutionNameLength = None, setInstitutionNameStartPosition = None, setIssueDateLength = None, setIssueDateStartPosition = None, setLowCertificationGradeLength = None, setLowCertificationGradeStartPosition = None, setModifiedTime = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateLength = None, setStateStartPosition = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationFixedLengthFileFormatID = False, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationFixedLengthFileFormat(EntityID = 1, setCertificationFixedLengthFileFormatID = None, setCertificationCompetencyLength = None, setCertificationCompetencyStartPosition = None, setCertificationDetailExpirationDateLength = None, setCertificationDetailExpirationDateStartPosition = None, setCertificationDetailIssueDateLength = None, setCertificationDetailIssueDateStartPosition = None, setCertificationLevelLength = None, setCertificationLevelStartPosition = None, setCertificationNumberLength = None, setCertificationNumberStartPosition = None, setCertificationSubjectLength = None, setCertificationSubjectStartPosition = None, setCertificationThirdPartyFormatID = None, setCertificationTypeLength = None, setCertificationTypeStartPosition = None, setCommentLength = None, setCommentStartPosition = None, setCreatedTime = None, setEmployeeLength = None, setEmployeeStartPosition = None, setExpirationDateLength = None, setExpirationDateStartPosition = None, setHighCertificationGradeLength = None, setHighCertificationGradeStartPosition = None, setHighlyQualifiedLength = None, setHighlyQualifiedStartPosition = None, setInstitutionNameLength = None, setInstitutionNameStartPosition = None, setIssueDateLength = None, setIssueDateStartPosition = None, setLowCertificationGradeLength = None, setLowCertificationGradeStartPosition = None, setModifiedTime = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateLength = None, setStateStartPosition = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationFixedLengthFileFormatID = False, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "delete")


def getEveryCertificationGrade(searchConditions = [], EntityID = 1, returnCertificationGradeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationGrade in the district.

    This function returns a dataframe of every CertificationGrade in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationGrade(CertificationGradeID, EntityID = 1, returnCertificationGradeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "get", return_params_list = return_params)

def modifyCertificationGrade(CertificationGradeID, EntityID = 1, setCertificationGradeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationGradeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationGrade(EntityID = 1, setCertificationGradeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationGradeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationGrade(CertificationGradeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "delete")


def getEveryCertificationLevel(searchConditions = [], EntityID = 1, returnCertificationLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationLevel in the district.

    This function returns a dataframe of every CertificationLevel in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationLevel(CertificationLevelID, EntityID = 1, returnCertificationLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "get", return_params_list = return_params)

def modifyCertificationLevel(CertificationLevelID, EntityID = 1, setCertificationLevelID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationLevel(EntityID = 1, setCertificationLevelID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationLevelID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationLevel(CertificationLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "delete")


def getEveryCertificationSubject(searchConditions = [], EntityID = 1, returnCertificationSubjectID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationSubject in the district.

    This function returns a dataframe of every CertificationSubject in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationSubject(CertificationSubjectID, EntityID = 1, returnCertificationSubjectID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "get", return_params_list = return_params)

def modifyCertificationSubject(CertificationSubjectID, EntityID = 1, setCertificationSubjectID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationSubjectID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationSubject(EntityID = 1, setCertificationSubjectID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationSubjectID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationSubject(CertificationSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "delete")


def getEveryCertificationThirdPartyFormat(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormat in the district.

    This function returns a dataframe of every CertificationThirdPartyFormat in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, returnCertificationThirdPartyFormatID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, setCertificationThirdPartyFormatID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDateFormat = None, setDateFormatCode = None, setDescription = None, setDistrictID = None, setImportType = None, setImportTypeCode = None, setIsSystemLoaded = None, setModifiedTime = None, setNameIdentification = None, setNameIdentificationCode = None, setSkywardHash = None, setSkywardID = None, setSkywardIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormat(EntityID = 1, setCertificationThirdPartyFormatID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDateFormat = None, setDateFormatCode = None, setDescription = None, setDistrictID = None, setImportType = None, setImportTypeCode = None, setIsSystemLoaded = None, setModifiedTime = None, setNameIdentification = None, setNameIdentificationCode = None, setSkywardHash = None, setSkywardID = None, setSkywardIDClonedFrom = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "delete")


def getEveryCertificationThirdPartyFormatCertificationCompetency(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatCertificationCompetencyID = False, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatCertificationCompetency in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatCertificationCompetency in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, returnCertificationThirdPartyFormatCertificationCompetencyID = False, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, setCertificationThirdPartyFormatCertificationCompetencyID = None, setCertificationCompetencyID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationCompetencyID = False, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatCertificationCompetency(EntityID = 1, setCertificationThirdPartyFormatCertificationCompetencyID = None, setCertificationCompetencyID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationCompetencyID = False, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "delete")


def getEveryCertificationThirdPartyFormatCertificationGrade(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatCertificationGradeID = False, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatCertificationGrade in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatCertificationGrade in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, returnCertificationThirdPartyFormatCertificationGradeID = False, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, setCertificationThirdPartyFormatCertificationGradeID = None, setCertificationGradeID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationGradeID = False, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatCertificationGrade(EntityID = 1, setCertificationThirdPartyFormatCertificationGradeID = None, setCertificationGradeID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationGradeID = False, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "delete")


def getEveryCertificationThirdPartyFormatCertificationLevel(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatCertificationLevelID = False, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatCertificationLevel in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatCertificationLevel in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, returnCertificationThirdPartyFormatCertificationLevelID = False, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, setCertificationThirdPartyFormatCertificationLevelID = None, setCertificationLevelID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationLevelID = False, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatCertificationLevel(EntityID = 1, setCertificationThirdPartyFormatCertificationLevelID = None, setCertificationLevelID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationLevelID = False, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "delete")


def getEveryCertificationThirdPartyFormatCertificationSubject(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatCertificationSubjectID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatCertificationSubject in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatCertificationSubject in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, returnCertificationThirdPartyFormatCertificationSubjectID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, setCertificationThirdPartyFormatCertificationSubjectID = None, setCertificationSubjectID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationSubjectID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatCertificationSubject(EntityID = 1, setCertificationThirdPartyFormatCertificationSubjectID = None, setCertificationSubjectID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationSubjectID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "delete")


def getEveryCertificationThirdPartyFormatCertificationType(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatCertificationTypeID = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatCertificationType in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatCertificationType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, returnCertificationThirdPartyFormatCertificationTypeID = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, setCertificationThirdPartyFormatCertificationTypeID = None, setCertificationThirdPartyFormatID = None, setCertificationTypeID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationTypeID = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatCertificationType(EntityID = 1, setCertificationThirdPartyFormatCertificationTypeID = None, setCertificationThirdPartyFormatID = None, setCertificationTypeID = None, setCreatedTime = None, setImportValue = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatCertificationTypeID = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "delete")


def getEveryCertificationThirdPartyFormatInstitution(searchConditions = [], EntityID = 1, returnCertificationThirdPartyFormatInstitutionID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyFormatInstitution in the district.

    This function returns a dataframe of every CertificationThirdPartyFormatInstitution in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, returnCertificationThirdPartyFormatInstitutionID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, setCertificationThirdPartyFormatInstitutionID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setInstitutionID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatInstitutionID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyFormatInstitution(EntityID = 1, setCertificationThirdPartyFormatInstitutionID = None, setCertificationThirdPartyFormatID = None, setCreatedTime = None, setImportValue = None, setInstitutionID = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyFormatInstitutionID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "delete")


def getEveryCertificationThirdPartyImport(searchConditions = [], EntityID = 1, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationThirdPartyImport in the district.

    This function returns a dataframe of every CertificationThirdPartyImport in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "get", return_params_list = return_params)

def modifyCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, setCertificationThirdPartyImportID = None, setCreatedTime = None, setImportTime = None, setMediaID = None, setMediaIDFailedResult = None, setModifiedTime = None, setThirdPartyFormatID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationThirdPartyImport(EntityID = 1, setCertificationThirdPartyImportID = None, setCreatedTime = None, setImportTime = None, setMediaID = None, setMediaIDFailedResult = None, setModifiedTime = None, setThirdPartyFormatID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "delete")


def getEveryCertificationType(searchConditions = [], EntityID = 1, returnCertificationTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every CertificationType in the district.

    This function returns a dataframe of every CertificationType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCertificationType(CertificationTypeID, EntityID = 1, returnCertificationTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "get", return_params_list = return_params)

def modifyCertificationType(CertificationTypeID, EntityID = 1, setCertificationTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setIsCRDCCertified = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCertificationType(EntityID = 1, setCertificationTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setIsCRDCCertified = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCertificationTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCertificationType(CertificationTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "delete")


def getEveryConfigDistrict(searchConditions = [], EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigDistrict(EntityID = 1, setConfigDistrictID = None, setCreatedTime = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnConfigDistrictID = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")


def getEveryConfigSystem(searchConditions = [], EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setConfigSystemID = None, setCreatedTime = None, setDefaultCaseAddressType = None, setDefaultCaseAddressTypeCode = None, setDefaultCaseNameType = None, setDefaultCaseNameTypeCode = None, setModifiedTime = None, setNameNumberLength = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseSyncedNameNumber = None, returnConfigSystemID = False, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params, payload = payload_params)

def createConfigSystem(EntityID = 1, setConfigSystemID = None, setCreatedTime = None, setDefaultCaseAddressType = None, setDefaultCaseAddressTypeCode = None, setDefaultCaseNameType = None, setDefaultCaseNameTypeCode = None, setModifiedTime = None, setNameNumberLength = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseSyncedNameNumber = None, returnConfigSystemID = False, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "delete")


def getEveryCounty(searchConditions = [], EntityID = 1, returnCountyID = False, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every County in the district.

    This function returns a dataframe of every County in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getCounty(CountyID, EntityID = 1, returnCountyID = False, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "get", return_params_list = return_params)

def modifyCounty(CountyID, EntityID = 1, setCountyID = None, setCountyMNID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setStateCountyMNID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCountyID = False, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "post", return_params_list = return_params, payload = payload_params)

def createCounty(EntityID = 1, setCountyID = None, setCountyMNID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setStateCountyMNID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnCountyID = False, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteCounty(CountyID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "delete")


def getEveryDependent(searchConditions = [], EntityID = 1, returnDependentID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Dependent in the district.

    This function returns a dataframe of every Dependent in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDependent(DependentID, EntityID = 1, returnDependentID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "get", return_params_list = return_params)

def modifyDependent(DependentID, EntityID = 1, setDependentID = None, setCreatedTime = None, setModifiedTime = None, setNameIDDependent = None, setNameIDOwner = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDependentID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDependent(EntityID = 1, setDependentID = None, setCreatedTime = None, setModifiedTime = None, setNameIDDependent = None, setNameIDOwner = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDependentID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDependent(DependentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "delete")


def getEveryDirectional(searchConditions = [], EntityID = 1, returnDirectionalID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Directional in the district.

    This function returns a dataframe of every Directional in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getDirectional(DirectionalID, EntityID = 1, returnDirectionalID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "get", return_params_list = return_params)

def modifyDirectional(DirectionalID, EntityID = 1, setDirectionalID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDirectionalID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "post", return_params_list = return_params, payload = payload_params)

def createDirectional(EntityID = 1, setDirectionalID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnDirectionalID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteDirectional(DirectionalID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "delete")


def getEveryEmailType(searchConditions = [], EntityID = 1, returnEmailTypeID = False, returnARConfigDistrictEmailTypeRank = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EmailType in the district.

    This function returns a dataframe of every EmailType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEmailType(EmailTypeID, EntityID = 1, returnEmailTypeID = False, returnARConfigDistrictEmailTypeRank = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "get", return_params_list = return_params)

def modifyEmailType(EmailTypeID, EntityID = 1, setEmailTypeID = None, setARConfigDistrictEmailTypeRank = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setPreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmailTypeID = False, returnARConfigDistrictEmailTypeRank = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEmailType(EntityID = 1, setEmailTypeID = None, setARConfigDistrictEmailTypeRank = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setPreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmailTypeID = False, returnARConfigDistrictEmailTypeRank = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEmailType(EmailTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "delete")


def getEveryEmergencyContact(searchConditions = [], EntityID = 1, returnEmergencyContactID = False, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every EmergencyContact in the district.

    This function returns a dataframe of every EmergencyContact in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEmergencyContact(EmergencyContactID, EntityID = 1, returnEmergencyContactID = False, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "get", return_params_list = return_params)

def modifyEmergencyContact(EmergencyContactID, EntityID = 1, setEmergencyContactID = None, setAllowPickUp = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmergencyContactID = False, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEmergencyContact(EntityID = 1, setEmergencyContactID = None, setAllowPickUp = None, setComment = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmergencyContactID = False, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEmergencyContact(EmergencyContactID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "delete")


def getEveryEmployer(searchConditions = [], EntityID = 1, returnEmployerID = False, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Employer in the district.

    This function returns a dataframe of every Employer in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getEmployer(EmployerID, EntityID = 1, returnEmployerID = False, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "get", return_params_list = return_params)

def modifyEmployer(EmployerID, EntityID = 1, setEmployerID = None, setACATransmitterControlCode = None, setCreatedTime = None, setDistrictID = None, setEEO4ControlNumber = None, setEEO4JurisdictionName = None, setEEO5NameOfCertifyingOfficial = None, setEEO5OfficeOfSchoolNumber = None, setEEO5SchoolDistrictName = None, setEEOCTitleOfCertifyingOfficial = None, setEmployerMNID = None, setFederalEEO4FunctionID = None, setModifiedTime = None, setNameID = None, setPERAEmployerNumber = None, setTRACountyGroupNumber = None, setTRADistrictUnitNumber = None, setUnemploymentInsuranceAccountNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmployerID = False, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createEmployer(EntityID = 1, setEmployerID = None, setACATransmitterControlCode = None, setCreatedTime = None, setDistrictID = None, setEEO4ControlNumber = None, setEEO4JurisdictionName = None, setEEO5NameOfCertifyingOfficial = None, setEEO5OfficeOfSchoolNumber = None, setEEO5SchoolDistrictName = None, setEEOCTitleOfCertifyingOfficial = None, setEmployerMNID = None, setFederalEEO4FunctionID = None, setModifiedTime = None, setNameID = None, setPERAEmployerNumber = None, setTRACountyGroupNumber = None, setTRADistrictUnitNumber = None, setUnemploymentInsuranceAccountNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnEmployerID = False, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteEmployer(EmployerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "delete")


def getEveryInstitutionDefault(searchConditions = [], EntityID = 1, returnInstitutionDefaultID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every InstitutionDefault in the district.

    This function returns a dataframe of every InstitutionDefault in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getInstitutionDefault(InstitutionDefaultID, EntityID = 1, returnInstitutionDefaultID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "get", return_params_list = return_params)

def modifyInstitutionDefault(InstitutionDefaultID, EntityID = 1, setInstitutionDefaultID = None, setCEEBCode = None, setCreatedTime = None, setInstitutionDefaultMNID = None, setMCCCCollegeCode = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnInstitutionDefaultID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createInstitutionDefault(EntityID = 1, setInstitutionDefaultID = None, setCEEBCode = None, setCreatedTime = None, setInstitutionDefaultMNID = None, setMCCCCollegeCode = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnInstitutionDefaultID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteInstitutionDefault(InstitutionDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "delete")


def getEveryInstitution(searchConditions = [], EntityID = 1, returnInstitutionID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Institution in the district.

    This function returns a dataframe of every Institution in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getInstitution(InstitutionID, EntityID = 1, returnInstitutionID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "get", return_params_list = return_params)

def modifyInstitution(InstitutionID, EntityID = 1, setInstitutionID = None, setCEEBCode = None, setCreatedTime = None, setInstitutionDefaultID = None, setInstitutionMNID = None, setMCCCCollegeCode = None, setModifiedTime = None, setNameID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnInstitutionID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createInstitution(EntityID = 1, setInstitutionID = None, setCEEBCode = None, setCreatedTime = None, setInstitutionDefaultID = None, setInstitutionMNID = None, setMCCCCollegeCode = None, setModifiedTime = None, setNameID = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnInstitutionID = False, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteInstitution(InstitutionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "delete")


def getEveryLanguage(searchConditions = [], EntityID = 1, returnLanguageID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Language in the district.

    This function returns a dataframe of every Language in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLanguage(LanguageID, EntityID = 1, returnLanguageID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "get", return_params_list = return_params)

def modifyLanguage(LanguageID, EntityID = 1, setLanguageID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentStateLanguage = None, setCurrentStateLanguageCode = None, setCurrentStateLanguageID = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLanguageID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLanguage(EntityID = 1, setLanguageID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setCurrentStateLanguage = None, setCurrentStateLanguageCode = None, setCurrentStateLanguageID = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLanguageID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLanguage(LanguageID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "delete")


def getEveryLanguageSchoolYear(searchConditions = [], EntityID = 1, returnLanguageSchoolYearID = False, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LanguageSchoolYear in the district.

    This function returns a dataframe of every LanguageSchoolYear in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, returnLanguageSchoolYearID = False, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "get", return_params_list = return_params)

def modifyLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, setLanguageSchoolYearID = None, setCreatedTime = None, setEdFiLanguageID = None, setLanguageID = None, setLanguageSchoolYearIDClonedFrom = None, setLanguageSchoolYearMNID = None, setModifiedTime = None, setSchoolYearID = None, setStateHeadStartLanguageMNID = None, setStateLanguageCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLanguageSchoolYearID = False, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLanguageSchoolYear(EntityID = 1, setLanguageSchoolYearID = None, setCreatedTime = None, setEdFiLanguageID = None, setLanguageID = None, setLanguageSchoolYearIDClonedFrom = None, setLanguageSchoolYearMNID = None, setModifiedTime = None, setSchoolYearID = None, setStateHeadStartLanguageMNID = None, setStateLanguageCodeMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLanguageSchoolYearID = False, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "delete")


def getEveryLastNameNumber(searchConditions = [], EntityID = 1, returnLastNameNumberID = False, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every LastNameNumber in the district.

    This function returns a dataframe of every LastNameNumber in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getLastNameNumber(LastNameNumberID, EntityID = 1, returnLastNameNumberID = False, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "get", return_params_list = return_params)

def modifyLastNameNumber(LastNameNumberID, EntityID = 1, setLastNameNumberID = None, setConfigSystemID = None, setCreatedTime = None, setModifiedTime = None, setNameNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLastNameNumberID = False, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "post", return_params_list = return_params, payload = payload_params)

def createLastNameNumber(EntityID = 1, setLastNameNumberID = None, setConfigSystemID = None, setCreatedTime = None, setModifiedTime = None, setNameNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnLastNameNumberID = False, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteLastNameNumber(LastNameNumberID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "delete")


def getEveryName(searchConditions = [], EntityID = 1, returnNameID = False, returnAge = False, returnBirthDate = False, returnBirthMonth = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFamilyStudentAccessStaffNameToUse = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnGrandPeopleMAID = False, returnGrandPersonMAID = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Name in the district.

    This function returns a dataframe of every Name in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getName(NameID, EntityID = 1, returnNameID = False, returnAge = False, returnBirthDate = False, returnBirthMonth = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFamilyStudentAccessStaffNameToUse = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnGrandPeopleMAID = False, returnGrandPersonMAID = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "get", return_params_list = return_params)

def modifyName(NameID, EntityID = 1, setNameID = None, setAge = None, setBirthDate = None, setBirthMonth = None, setBirthMonthDay = None, setBirthYear = None, setBypassStudentRaceValidation = None, setCalculatedPrimaryFormattedPhoneNumber = None, setContactPerson = None, setConversionKey = None, setCreatedTime = None, setDatePhysicalAddressLastChanged = None, setDriversLicenseNumber = None, setEthnicity = None, setEthnicityAndRace = None, setExternalUniqueIdentifier = None, setFamilyStudentAccessStaffNameToUse = None, setFederalEIN = None, setFirstInitial = None, setFirstInitialLastName = None, setFirstInitialLastNameLegal = None, setFirstInitialLegal = None, setFirstName = None, setFirstNameLegal = None, setFullNameFL = None, setFullNameFMIL = None, setFullNameFML = None, setFullNameLegalFL = None, setFullNameLegalFML = None, setFullNameLegalLFM = None, setFullNameLF = None, setFullNameLFM = None, setGender = None, setGenderCode = None, setGetNameUse = None, setGrandPeopleMAID = None, setGrandPersonMAID = None, setHasMailingOrPhysicalAddress = None, setInitials = None, setInitialsLegal = None, setIsAlaskan = None, setIsAsian = None, setIsBlack = None, setIsBusiness = None, setIsCurrentStudent = None, setIsEmergencyContactName = None, setIsEmployeeName = None, setIsEmployeeNameForDistrict = None, setIsEmployeeNameOrInEmployeeFamily = None, setIsFeeManagementCustomerName = None, setIsFeeManagementPayorName = None, setIsFoodServiceCustomerName = None, setIsFoodServicePayorName = None, setIsGuardianName = None, setIsHawaiian = None, setIsHealthProfessionalName = None, setIsHispanic = None, setIsInstitution = None, setIsPayorName = None, setIsPayorNameForDistrict = None, setIsPlaceOfEmployment = None, setIsSingleLegalName = None, setIsSkyward = None, setIsStaffName = None, setIsStudentInDistrict = None, setIsStudentName = None, setIsUserName = None, setIsVendorName = None, setIsVendorNameForDistrict = None, setIsWhite = None, setLastInitial = None, setLastInitialLegal = None, setLastName = None, setLastNameFirstInitial = None, setLastNameLegal = None, setMaritalStatus = None, setMaritalStatusCode = None, setMaskedSocialSecurityNumber = None, setMediaIDPhoto = None, setMiddleInitial = None, setMiddleInitialLegal = None, setMiddleName = None, setMiddleNameLegal = None, setModifiedTime = None, setNameAddressMailingID = None, setNameIDPlaceOfEmployment = None, setNameKey = None, setNameNumber = None, setNameSuffixID = None, setNameSuffixIDLegal = None, setNameTitleID = None, setNameTitleIDLegal = None, setOccupationID = None, setRace = None, setRaceEduphoriaCode = None, setRaceVerifiedBy = None, setRaceVerifiedByCode = None, setRaceVerifiedDate = None, setSkywardHash = None, setSkywardID = None, setSocialSecurityNumber = None, setSpecifySeparateLegalName = None, setTitledName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameID = False, returnAge = False, returnBirthDate = False, returnBirthMonth = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFamilyStudentAccessStaffNameToUse = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnGrandPeopleMAID = False, returnGrandPersonMAID = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "post", return_params_list = return_params, payload = payload_params)

def createName(EntityID = 1, setNameID = None, setAge = None, setBirthDate = None, setBirthMonth = None, setBirthMonthDay = None, setBirthYear = None, setBypassStudentRaceValidation = None, setCalculatedPrimaryFormattedPhoneNumber = None, setContactPerson = None, setConversionKey = None, setCreatedTime = None, setDatePhysicalAddressLastChanged = None, setDriversLicenseNumber = None, setEthnicity = None, setEthnicityAndRace = None, setExternalUniqueIdentifier = None, setFamilyStudentAccessStaffNameToUse = None, setFederalEIN = None, setFirstInitial = None, setFirstInitialLastName = None, setFirstInitialLastNameLegal = None, setFirstInitialLegal = None, setFirstName = None, setFirstNameLegal = None, setFullNameFL = None, setFullNameFMIL = None, setFullNameFML = None, setFullNameLegalFL = None, setFullNameLegalFML = None, setFullNameLegalLFM = None, setFullNameLF = None, setFullNameLFM = None, setGender = None, setGenderCode = None, setGetNameUse = None, setGrandPeopleMAID = None, setGrandPersonMAID = None, setHasMailingOrPhysicalAddress = None, setInitials = None, setInitialsLegal = None, setIsAlaskan = None, setIsAsian = None, setIsBlack = None, setIsBusiness = None, setIsCurrentStudent = None, setIsEmergencyContactName = None, setIsEmployeeName = None, setIsEmployeeNameForDistrict = None, setIsEmployeeNameOrInEmployeeFamily = None, setIsFeeManagementCustomerName = None, setIsFeeManagementPayorName = None, setIsFoodServiceCustomerName = None, setIsFoodServicePayorName = None, setIsGuardianName = None, setIsHawaiian = None, setIsHealthProfessionalName = None, setIsHispanic = None, setIsInstitution = None, setIsPayorName = None, setIsPayorNameForDistrict = None, setIsPlaceOfEmployment = None, setIsSingleLegalName = None, setIsSkyward = None, setIsStaffName = None, setIsStudentInDistrict = None, setIsStudentName = None, setIsUserName = None, setIsVendorName = None, setIsVendorNameForDistrict = None, setIsWhite = None, setLastInitial = None, setLastInitialLegal = None, setLastName = None, setLastNameFirstInitial = None, setLastNameLegal = None, setMaritalStatus = None, setMaritalStatusCode = None, setMaskedSocialSecurityNumber = None, setMediaIDPhoto = None, setMiddleInitial = None, setMiddleInitialLegal = None, setMiddleName = None, setMiddleNameLegal = None, setModifiedTime = None, setNameAddressMailingID = None, setNameIDPlaceOfEmployment = None, setNameKey = None, setNameNumber = None, setNameSuffixID = None, setNameSuffixIDLegal = None, setNameTitleID = None, setNameTitleIDLegal = None, setOccupationID = None, setRace = None, setRaceEduphoriaCode = None, setRaceVerifiedBy = None, setRaceVerifiedByCode = None, setRaceVerifiedDate = None, setSkywardHash = None, setSkywardID = None, setSocialSecurityNumber = None, setSpecifySeparateLegalName = None, setTitledName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameID = False, returnAge = False, returnBirthDate = False, returnBirthMonth = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFamilyStudentAccessStaffNameToUse = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnGrandPeopleMAID = False, returnGrandPersonMAID = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteName(NameID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "delete")


def getEveryNameAddress(searchConditions = [], EntityID = 1, returnNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnHideFromDirectoryMA = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameAddress in the district.

    This function returns a dataframe of every NameAddress in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameAddress(NameAddressID, EntityID = 1, returnNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnHideFromDirectoryMA = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "get", return_params_list = return_params)

def modifyNameAddress(NameAddressID, EntityID = 1, setNameAddressID = None, setAddressID = None, setCreatedTime = None, setGetAddressType = None, setHideFromDirectoryMA = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsPrimaryGuardian = None, setIsRemitTo = None, setIsW2 = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnHideFromDirectoryMA = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameAddress(EntityID = 1, setNameAddressID = None, setAddressID = None, setCreatedTime = None, setGetAddressType = None, setHideFromDirectoryMA = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsPrimaryGuardian = None, setIsRemitTo = None, setIsW2 = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnHideFromDirectoryMA = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameAddress(NameAddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "delete")


def getEveryNameAlias(searchConditions = [], EntityID = 1, returnNameAliasID = False, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameAlias in the district.

    This function returns a dataframe of every NameAlias in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameAlias(NameAliasID, EntityID = 1, returnNameAliasID = False, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "get", return_params_list = return_params)

def modifyNameAlias(NameAliasID, EntityID = 1, setNameAliasID = None, setCreatedTime = None, setEffectiveDate = None, setFirstName = None, setFullNameFL = None, setFullNameLF = None, setIsBusiness = None, setIsLegalName = None, setIsMaidenName = None, setIsSingleLegalName = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNameSuffixID = None, setNameTitleID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameAliasID = False, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameAlias(EntityID = 1, setNameAliasID = None, setCreatedTime = None, setEffectiveDate = None, setFirstName = None, setFullNameFL = None, setFullNameLF = None, setIsBusiness = None, setIsLegalName = None, setIsMaidenName = None, setIsSingleLegalName = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNameSuffixID = None, setNameTitleID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameAliasID = False, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameAlias(NameAliasID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "delete")


def getEveryNameEmail(searchConditions = [], EntityID = 1, returnNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameEmail in the district.

    This function returns a dataframe of every NameEmail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameEmail(NameEmailID, EntityID = 1, returnNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "get", return_params_list = return_params)

def modifyNameEmail(NameEmailID, EntityID = 1, setNameEmailID = None, setCreatedTime = None, setEmailAddress = None, setEmailTypeID = None, setIsAccountsPayableDirectDepositNotificationEmail = None, setModifiedTime = None, setNameID = None, setNote = None, setRank = None, setUsedByHealthProfessional = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameEmail(EntityID = 1, setNameEmailID = None, setCreatedTime = None, setEmailAddress = None, setEmailTypeID = None, setIsAccountsPayableDirectDepositNotificationEmail = None, setModifiedTime = None, setNameID = None, setNote = None, setRank = None, setUsedByHealthProfessional = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameEmail(NameEmailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "delete")


def getEveryNameEthnicityRaceSubcategoryMN(searchConditions = [], EntityID = 1, returnNameEthnicityRaceSubcategoryMNID = False, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameEthnicityRaceSubcategoryMN in the district.

    This function returns a dataframe of every NameEthnicityRaceSubcategoryMN in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, returnNameEthnicityRaceSubcategoryMNID = False, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "get", return_params_list = return_params)

def modifyNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, setNameEthnicityRaceSubcategoryMNID = None, setCreatedTime = None, setEthnicityRaceType = None, setEthnicityRaceTypeCode = None, setModifiedTime = None, setNameID = None, setStateEthnicityRaceSubcategoryMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameEthnicityRaceSubcategoryMNID = False, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameEthnicityRaceSubcategoryMN(EntityID = 1, setNameEthnicityRaceSubcategoryMNID = None, setCreatedTime = None, setEthnicityRaceType = None, setEthnicityRaceTypeCode = None, setModifiedTime = None, setNameID = None, setStateEthnicityRaceSubcategoryMNID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameEthnicityRaceSubcategoryMNID = False, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "delete")


def getEveryNameMergeRunHistory(searchConditions = [], EntityID = 1, returnNameMergeRunHistoryID = False, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameMergeRunHistory in the district.

    This function returns a dataframe of every NameMergeRunHistory in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, returnNameMergeRunHistoryID = False, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "get", return_params_list = return_params)

def modifyNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, setNameMergeRunHistoryID = None, setBirthDateFrom = None, setBirthDateTo = None, setCreatedTime = None, setFullNameLFMFrom = None, setFullNameLFMTo = None, setModifiedTime = None, setNameIDFrom = None, setNameIDTo = None, setNameUsedByFrom = None, setNameUsedByTo = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameMergeRunHistoryID = False, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameMergeRunHistory(EntityID = 1, setNameMergeRunHistoryID = None, setBirthDateFrom = None, setBirthDateTo = None, setCreatedTime = None, setFullNameLFMFrom = None, setFullNameLFMTo = None, setModifiedTime = None, setNameIDFrom = None, setNameIDTo = None, setNameUsedByFrom = None, setNameUsedByTo = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameMergeRunHistoryID = False, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "delete")


def getEveryNamePhone(searchConditions = [], EntityID = 1, returnNamePhoneID = False, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NamePhone in the district.

    This function returns a dataframe of every NamePhone in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNamePhone(NamePhoneID, EntityID = 1, returnNamePhoneID = False, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "get", return_params_list = return_params)

def modifyNamePhone(NamePhoneID, EntityID = 1, setNamePhoneID = None, setCreatedTime = None, setExtension = None, setFormattedPhoneNumber = None, setFormattedPhoneNumberCodeEEL = None, setFullPhoneNumber = None, setIsConfidential = None, setIsFax = None, setIsInternational = None, setIsPrimaryFax = None, setModifiedTime = None, setNameID = None, setNote = None, setPhoneNumber = None, setPhoneTypeID = None, setRank = None, setUsedByHealthProfessional = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNamePhoneID = False, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNamePhone(EntityID = 1, setNamePhoneID = None, setCreatedTime = None, setExtension = None, setFormattedPhoneNumber = None, setFormattedPhoneNumberCodeEEL = None, setFullPhoneNumber = None, setIsConfidential = None, setIsFax = None, setIsInternational = None, setIsPrimaryFax = None, setModifiedTime = None, setNameID = None, setNote = None, setPhoneNumber = None, setPhoneTypeID = None, setRank = None, setUsedByHealthProfessional = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNamePhoneID = False, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNamePhone(NamePhoneID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "delete")


def getEveryNameSuffix(searchConditions = [], EntityID = 1, returnNameSuffixID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameSuffix in the district.

    This function returns a dataframe of every NameSuffix in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameSuffix(NameSuffixID, EntityID = 1, returnNameSuffixID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "get", return_params_list = return_params)

def modifyNameSuffix(NameSuffixID, EntityID = 1, setNameSuffixID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameSuffixID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameSuffix(EntityID = 1, setNameSuffixID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameSuffixID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameSuffix(NameSuffixID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "delete")


def getEveryNameTitle(searchConditions = [], EntityID = 1, returnNameTitleID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameTitle in the district.

    This function returns a dataframe of every NameTitle in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameTitle(NameTitleID, EntityID = 1, returnNameTitleID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "get", return_params_list = return_params)

def modifyNameTitle(NameTitleID, EntityID = 1, setNameTitleID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameTitleID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameTitle(EntityID = 1, setNameTitleID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameTitleID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameTitle(NameTitleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "delete")


def getEveryNameVehicle(searchConditions = [], EntityID = 1, returnNameVehicleID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameVehicle in the district.

    This function returns a dataframe of every NameVehicle in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameVehicle(NameVehicleID, EntityID = 1, returnNameVehicleID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "get", return_params_list = return_params)

def modifyNameVehicle(NameVehicleID, EntityID = 1, setNameVehicleID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVehicleID = None, returnNameVehicleID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameVehicle(EntityID = 1, setNameVehicleID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVehicleID = None, returnNameVehicleID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameVehicle(NameVehicleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "delete")


def getEveryNameWebsite(searchConditions = [], EntityID = 1, returnNameWebsiteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every NameWebsite in the district.

    This function returns a dataframe of every NameWebsite in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getNameWebsite(NameWebsiteID, EntityID = 1, returnNameWebsiteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "get", return_params_list = return_params)

def modifyNameWebsite(NameWebsiteID, EntityID = 1, setNameWebsiteID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNote = None, setRank = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameWebsiteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNameWebsite(EntityID = 1, setNameWebsiteID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setNote = None, setRank = None, setURL = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnNameWebsiteID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNameWebsite(NameWebsiteID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "delete")


def getEveryOccupation(searchConditions = [], EntityID = 1, returnOccupationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Occupation in the district.

    This function returns a dataframe of every Occupation in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getOccupation(OccupationID, EntityID = 1, returnOccupationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "get", return_params_list = return_params)

def modifyOccupation(OccupationID, EntityID = 1, setOccupationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOccupationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOccupation(EntityID = 1, setOccupationID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOccupationID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOccupation(OccupationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "delete")


def getEveryPhoneType(searchConditions = [], EntityID = 1, returnPhoneTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every PhoneType in the district.

    This function returns a dataframe of every PhoneType in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getPhoneType(PhoneTypeID, EntityID = 1, returnPhoneTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "get", return_params_list = return_params)

def modifyPhoneType(PhoneTypeID, EntityID = 1, setPhoneTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setPreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPhoneTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createPhoneType(EntityID = 1, setPhoneTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setModifiedTime = None, setPreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnPhoneTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deletePhoneType(PhoneTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "delete")


def getEveryRaisersEdgeObjectMA(searchConditions = [], EntityID = 1, returnRaisersEdgeObjectMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnRaisersEdgeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every RaisersEdgeObjectMA in the district.

    This function returns a dataframe of every RaisersEdgeObjectMA in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRaisersEdgeObjectMA(RaisersEdgeObjectMAID, EntityID = 1, returnRaisersEdgeObjectMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnRaisersEdgeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/" + str(RaisersEdgeObjectMAID), verb = "get", return_params_list = return_params)

def modifyRaisersEdgeObjectMA(RaisersEdgeObjectMAID, EntityID = 1, setRaisersEdgeObjectMAID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setRaisersEdgeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRaisersEdgeObjectMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnRaisersEdgeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/" + str(RaisersEdgeObjectMAID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRaisersEdgeObjectMA(EntityID = 1, setRaisersEdgeObjectMAID = None, setCreatedTime = None, setModifiedTime = None, setNameID = None, setRaisersEdgeID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRaisersEdgeObjectMAID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnRaisersEdgeID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRaisersEdgeObjectMA(RaisersEdgeObjectMAID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/RaisersEdgeObjectMA/" + str(RaisersEdgeObjectMAID), verb = "delete")


def getEveryRelationship(searchConditions = [], EntityID = 1, returnRelationshipID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnGrandPeopleMAID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getRelationship(RelationshipID, EntityID = 1, returnRelationshipID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnGrandPeopleMAID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "get", return_params_list = return_params)

def modifyRelationship(RelationshipID, EntityID = 1, setRelationshipID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEdFiRelationTypeID = None, setGrandPeopleMAID = None, setModifiedTime = None, setRelationshipType = None, setRelationshipTypeCode = None, setShortenedDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRelationshipID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnGrandPeopleMAID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "post", return_params_list = return_params, payload = payload_params)

def createRelationship(EntityID = 1, setRelationshipID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setEdFiRelationTypeID = None, setGrandPeopleMAID = None, setModifiedTime = None, setRelationshipType = None, setRelationshipTypeCode = None, setShortenedDescription = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnRelationshipID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnGrandPeopleMAID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteRelationship(RelationshipID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "delete")


def getEveryStreet(searchConditions = [], EntityID = 1, returnStreetID = False, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Street in the district.

    This function returns a dataframe of every Street in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getStreet(StreetID, EntityID = 1, returnStreetID = False, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "get", return_params_list = return_params)

def modifyStreet(StreetID, EntityID = 1, setStreetID = None, setCreatedTime = None, setDirectionalID = None, setFormattedStreet = None, setModifiedTime = None, setName = None, setStreetNameWithDirectionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipID = None, returnStreetID = False, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStreet(EntityID = 1, setStreetID = None, setCreatedTime = None, setDirectionalID = None, setFormattedStreet = None, setModifiedTime = None, setName = None, setStreetNameWithDirectionCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipID = None, returnStreetID = False, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStreet(StreetID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "delete")


def getEveryTempACHAccount(searchConditions = [], EntityID = 1, returnTempACHAccountID = False, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempACHAccount in the district.

    This function returns a dataframe of every TempACHAccount in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempACHAccount(TempACHAccountID, EntityID = 1, returnTempACHAccountID = False, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "get", return_params_list = return_params)

def modifyTempACHAccount(TempACHAccountID, EntityID = 1, setTempACHAccountID = None, setAccountType = None, setACHAccountID = None, setACHAccountNumber = None, setCreatedTime = None, setIsEmployeeNetPayrollACH = None, setIsVendorAccountsPayableACH = None, setModifiedTime = None, setName = None, setRoutingNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseTaxAddenda = None, returnTempACHAccountID = False, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempACHAccount(EntityID = 1, setTempACHAccountID = None, setAccountType = None, setACHAccountID = None, setACHAccountNumber = None, setCreatedTime = None, setIsEmployeeNetPayrollACH = None, setIsVendorAccountsPayableACH = None, setModifiedTime = None, setName = None, setRoutingNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUseTaxAddenda = None, returnTempACHAccountID = False, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempACHAccount(TempACHAccountID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "delete")


def getEveryTempAddress(searchConditions = [], EntityID = 1, returnTempAddressID = False, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAddress in the district.

    This function returns a dataframe of every TempAddress in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAddress(TempAddressID, EntityID = 1, returnTempAddressID = False, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "get", return_params_list = return_params)

def modifyTempAddress(TempAddressID, EntityID = 1, setTempAddressID = None, setAddressID = None, setAddressUsedBy = None, setCreatedTime = None, setCurrentFormattedFullAddress = None, setFieldPathsToUpdate = None, setFieldsToUpdate = None, setModifiedTime = None, setNewFormattedFullAddress = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowErrors = None, returnTempAddressID = False, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAddress(EntityID = 1, setTempAddressID = None, setAddressID = None, setAddressUsedBy = None, setCreatedTime = None, setCurrentFormattedFullAddress = None, setFieldPathsToUpdate = None, setFieldsToUpdate = None, setModifiedTime = None, setNewFormattedFullAddress = None, setSelected = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowErrors = None, returnTempAddressID = False, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAddress(TempAddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "delete")


def getEveryTempAddressRangeDefault(searchConditions = [], EntityID = 1, returnTempAddressRangeDefaultID = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempAddressRangeDefault in the district.

    This function returns a dataframe of every TempAddressRangeDefault in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, returnTempAddressRangeDefaultID = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "get", return_params_list = return_params)

def modifyTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, setTempAddressRangeDefaultID = None, setCity = None, setCreatedTime = None, setDefaultSchools = None, setException = None, setModifiedTime = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSideCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, setZipCodeAddOn = None, returnTempAddressRangeDefaultID = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempAddressRangeDefault(EntityID = 1, setTempAddressRangeDefaultID = None, setCity = None, setCreatedTime = None, setDefaultSchools = None, setException = None, setModifiedTime = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSideCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, setZipCodeAddOn = None, returnTempAddressRangeDefaultID = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "delete")


def getEveryTempCertification(searchConditions = [], EntityID = 1, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCertification in the district.

    This function returns a dataframe of every TempCertification in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCertification(TempCertificationID, EntityID = 1, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "get", return_params_list = return_params)

def modifyTempCertification(TempCertificationID, EntityID = 1, setTempCertificationID = None, setCertificationID = None, setCertificationNumber = None, setCertificationTypeCode = None, setCertificationTypeCodeDescription = None, setCertificationTypeID = None, setComment = None, setCreatedTime = None, setErrorCount = None, setExpirationDate = None, setFullNameLFM = None, setHasErrors = None, setInstitutionID = None, setInstitutionName = None, setIssueDate = None, setLineNumber = None, setModifiedTime = None, setNameID = None, setStateDisplayName = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCertification(EntityID = 1, setTempCertificationID = None, setCertificationID = None, setCertificationNumber = None, setCertificationTypeCode = None, setCertificationTypeCodeDescription = None, setCertificationTypeID = None, setComment = None, setCreatedTime = None, setErrorCount = None, setExpirationDate = None, setFullNameLFM = None, setHasErrors = None, setInstitutionID = None, setInstitutionName = None, setIssueDate = None, setLineNumber = None, setModifiedTime = None, setNameID = None, setStateDisplayName = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCertification(TempCertificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "delete")


def getEveryTempCertificationDetail(searchConditions = [], EntityID = 1, returnTempCertificationDetailID = False, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCertificationDetail in the district.

    This function returns a dataframe of every TempCertificationDetail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCertificationDetail(TempCertificationDetailID, EntityID = 1, returnTempCertificationDetailID = False, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "get", return_params_list = return_params)

def modifyTempCertificationDetail(TempCertificationDetailID, EntityID = 1, setTempCertificationDetailID = None, setCertificationCompetencyCode = None, setCertificationCompetencyID = None, setCertificationGradeHighCodeDescription = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationGradeLowCodeDescription = None, setCertificationID = None, setCertificationLevelCode = None, setCertificationLevelID = None, setCertificationSubjectCode = None, setCertificationSubjectID = None, setCreatedTime = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setLineNumber = None, setModifiedTime = None, setTempCertificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationDetailID = False, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCertificationDetail(EntityID = 1, setTempCertificationDetailID = None, setCertificationCompetencyCode = None, setCertificationCompetencyID = None, setCertificationGradeHighCodeDescription = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationGradeLowCodeDescription = None, setCertificationID = None, setCertificationLevelCode = None, setCertificationLevelID = None, setCertificationSubjectCode = None, setCertificationSubjectID = None, setCreatedTime = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setLineNumber = None, setModifiedTime = None, setTempCertificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationDetailID = False, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCertificationDetail(TempCertificationDetailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "delete")


def getEveryTempCertificationError(searchConditions = [], EntityID = 1, returnTempCertificationErrorID = False, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempCertificationError in the district.

    This function returns a dataframe of every TempCertificationError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempCertificationError(TempCertificationErrorID, EntityID = 1, returnTempCertificationErrorID = False, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "get", return_params_list = return_params)

def modifyTempCertificationError(TempCertificationErrorID, EntityID = 1, setTempCertificationErrorID = None, setCertificationID = None, setCreatedTime = None, setError = None, setErrorDetail = None, setLineNumber = None, setModifiedTime = None, setNameLFM = None, setTempCertificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationErrorID = False, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCertificationError(EntityID = 1, setTempCertificationErrorID = None, setCertificationID = None, setCreatedTime = None, setError = None, setErrorDetail = None, setLineNumber = None, setModifiedTime = None, setNameLFM = None, setTempCertificationID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationErrorID = False, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCertificationError(TempCertificationErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "delete")


def getEveryTempEmergencyContact(searchConditions = [], EntityID = 1, returnTempEmergencyContactID = False, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempEmergencyContact in the district.

    This function returns a dataframe of every TempEmergencyContact in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnTempEmergencyContactID = False, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", return_params_list = return_params)

def modifyTempEmergencyContact(TempEmergencyContactID, EntityID = 1, setTempEmergencyContactID = None, setAllowPickUp = None, setCreatedTime = None, setEmergencyContactFor = None, setEmergencyContactName = None, setExceptionNote = None, setHasActiveRestrictedAccess = None, setHasExceptions = None, setModifiedTime = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipDescription = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEmergencyContactID = False, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEmergencyContact(EntityID = 1, setTempEmergencyContactID = None, setAllowPickUp = None, setCreatedTime = None, setEmergencyContactFor = None, setEmergencyContactName = None, setExceptionNote = None, setHasActiveRestrictedAccess = None, setHasExceptions = None, setModifiedTime = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipDescription = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEmergencyContactID = False, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "delete")


def getEveryTempException(searchConditions = [], EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempException(TempExceptionID, EntityID = 1, returnTempExceptionID = False, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "get", return_params_list = return_params)

def modifyTempException(TempExceptionID, EntityID = 1, setTempExceptionID = None, setCreatedTime = None, setLineNumber = None, setMessage = None, setModifiedTime = None, setNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempExceptionID = False, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempException(EntityID = 1, setTempExceptionID = None, setCreatedTime = None, setLineNumber = None, setMessage = None, setModifiedTime = None, setNameLFM = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempExceptionID = False, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempException(TempExceptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "delete")


def getEveryTempMassUpdateGeolocationAddress(searchConditions = [], EntityID = 1, returnTempMassUpdateGeolocationAddressID = False, returnAddressID = False, returnConfidenceRating = False, returnCreatedTime = False, returnCurrentGeoID = False, returnCurrentLatitude = False, returnCurrentLongitude = False, returnFullAddress = False, returnModifiedTime = False, returnPreviousWasAPILoaded = False, returnUpdatedGeoID = False, returnUpdatedLatitude = False, returnUpdatedLongitude = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempMassUpdateGeolocationAddress in the district.

    This function returns a dataframe of every TempMassUpdateGeolocationAddress in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempMassUpdateGeolocationAddress(TempMassUpdateGeolocationAddressID, EntityID = 1, returnTempMassUpdateGeolocationAddressID = False, returnAddressID = False, returnConfidenceRating = False, returnCreatedTime = False, returnCurrentGeoID = False, returnCurrentLatitude = False, returnCurrentLongitude = False, returnFullAddress = False, returnModifiedTime = False, returnPreviousWasAPILoaded = False, returnUpdatedGeoID = False, returnUpdatedLatitude = False, returnUpdatedLongitude = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/" + str(TempMassUpdateGeolocationAddressID), verb = "get", return_params_list = return_params)

def modifyTempMassUpdateGeolocationAddress(TempMassUpdateGeolocationAddressID, EntityID = 1, setTempMassUpdateGeolocationAddressID = None, setAddressID = None, setConfidenceRating = None, setCreatedTime = None, setCurrentGeoID = None, setCurrentLatitude = None, setCurrentLongitude = None, setFullAddress = None, setModifiedTime = None, setPreviousWasAPILoaded = None, setUpdatedGeoID = None, setUpdatedLatitude = None, setUpdatedLongitude = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMassUpdateGeolocationAddressID = False, returnAddressID = False, returnConfidenceRating = False, returnCreatedTime = False, returnCurrentGeoID = False, returnCurrentLatitude = False, returnCurrentLongitude = False, returnFullAddress = False, returnModifiedTime = False, returnPreviousWasAPILoaded = False, returnUpdatedGeoID = False, returnUpdatedLatitude = False, returnUpdatedLongitude = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/" + str(TempMassUpdateGeolocationAddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempMassUpdateGeolocationAddress(EntityID = 1, setTempMassUpdateGeolocationAddressID = None, setAddressID = None, setConfidenceRating = None, setCreatedTime = None, setCurrentGeoID = None, setCurrentLatitude = None, setCurrentLongitude = None, setFullAddress = None, setModifiedTime = None, setPreviousWasAPILoaded = None, setUpdatedGeoID = None, setUpdatedLatitude = None, setUpdatedLongitude = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempMassUpdateGeolocationAddressID = False, returnAddressID = False, returnConfidenceRating = False, returnCreatedTime = False, returnCurrentGeoID = False, returnCurrentLatitude = False, returnCurrentLongitude = False, returnFullAddress = False, returnModifiedTime = False, returnPreviousWasAPILoaded = False, returnUpdatedGeoID = False, returnUpdatedLatitude = False, returnUpdatedLongitude = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempMassUpdateGeolocationAddress(TempMassUpdateGeolocationAddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempMassUpdateGeolocationAddress/" + str(TempMassUpdateGeolocationAddressID), verb = "delete")


def getEveryTempNameAddress(searchConditions = [], EntityID = 1, returnTempNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameAddress in the district.

    This function returns a dataframe of every TempNameAddress in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameAddress(TempNameAddressID, EntityID = 1, returnTempNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "get", return_params_list = return_params)

def modifyTempNameAddress(TempNameAddressID, EntityID = 1, setTempNameAddressID = None, setAddressID = None, setCreatedTime = None, setFullAddress = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsRemitTo = None, setIsW2 = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameAddress(EntityID = 1, setTempNameAddressID = None, setAddressID = None, setCreatedTime = None, setFullAddress = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsRemitTo = None, setIsW2 = None, setModifiedTime = None, setNameID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameAddressID = False, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameAddress(TempNameAddressID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "delete")


def getEveryTempNameEmail(searchConditions = [], EntityID = 1, returnTempNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnErrorCount = False, returnFullNameFML = False, returnModifiedTime = False, returnNameEmailID = False, returnNameID = False, returnNote = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameEmail in the district.

    This function returns a dataframe of every TempNameEmail in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameEmail(TempNameEmailID, EntityID = 1, returnTempNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnErrorCount = False, returnFullNameFML = False, returnModifiedTime = False, returnNameEmailID = False, returnNameID = False, returnNote = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/" + str(TempNameEmailID), verb = "get", return_params_list = return_params)

def modifyTempNameEmail(TempNameEmailID, EntityID = 1, setTempNameEmailID = None, setCreatedTime = None, setEmailAddress = None, setEmailTypeID = None, setErrorCount = None, setFullNameFML = None, setModifiedTime = None, setNameEmailID = None, setNameID = None, setNote = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnErrorCount = False, returnFullNameFML = False, returnModifiedTime = False, returnNameEmailID = False, returnNameID = False, returnNote = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/" + str(TempNameEmailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameEmail(EntityID = 1, setTempNameEmailID = None, setCreatedTime = None, setEmailAddress = None, setEmailTypeID = None, setErrorCount = None, setFullNameFML = None, setModifiedTime = None, setNameEmailID = None, setNameID = None, setNote = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameEmailID = False, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnErrorCount = False, returnFullNameFML = False, returnModifiedTime = False, returnNameEmailID = False, returnNameID = False, returnNote = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameEmail(TempNameEmailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmail/" + str(TempNameEmailID), verb = "delete")


def getEveryTempNameEmailError(searchConditions = [], EntityID = 1, returnTempNameEmailErrorID = False, returnCreatedTime = False, returnErrorField = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameEmailError in the district.

    This function returns a dataframe of every TempNameEmailError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameEmailError(TempNameEmailErrorID, EntityID = 1, returnTempNameEmailErrorID = False, returnCreatedTime = False, returnErrorField = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/" + str(TempNameEmailErrorID), verb = "get", return_params_list = return_params)

def modifyTempNameEmailError(TempNameEmailErrorID, EntityID = 1, setTempNameEmailErrorID = None, setCreatedTime = None, setErrorField = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameEmailErrorID = False, returnCreatedTime = False, returnErrorField = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/" + str(TempNameEmailErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameEmailError(EntityID = 1, setTempNameEmailErrorID = None, setCreatedTime = None, setErrorField = None, setErrorNumber = None, setErrorText = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameEmailErrorID = False, returnCreatedTime = False, returnErrorField = False, returnErrorNumber = False, returnErrorText = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameEmailError(TempNameEmailErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameEmailError/" + str(TempNameEmailErrorID), verb = "delete")


def getEveryTempNameError(searchConditions = [], EntityID = 1, returnTempNameErrorID = False, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameError in the district.

    This function returns a dataframe of every TempNameError in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameError(TempNameErrorID, EntityID = 1, returnTempNameErrorID = False, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "get", return_params_list = return_params)

def modifyTempNameError(TempNameErrorID, EntityID = 1, setTempNameErrorID = None, setCreatedTime = None, setFirstName = None, setLastName = None, setModifiedTime = None, setNameID = None, setNote = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameErrorID = False, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameError(EntityID = 1, setTempNameErrorID = None, setCreatedTime = None, setFirstName = None, setLastName = None, setModifiedTime = None, setNameID = None, setNote = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNameErrorID = False, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameError(TempNameErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "delete")


def getEveryTempNameNumber(searchConditions = [], EntityID = 1, returnTempNameNumberID = False, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every TempNameNumber in the district.

    This function returns a dataframe of every TempNameNumber in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getTempNameNumber(TempNameNumberID, EntityID = 1, returnTempNameNumberID = False, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "get", return_params_list = return_params)

def modifyTempNameNumber(TempNameNumberID, EntityID = 1, setTempNameNumberID = None, setConflictReason = None, setCreatedTime = None, setEmployeeID = None, setFullNameLFM = None, setHasConflicts = None, setModifiedTime = None, setNameID = None, setNameNumber = None, setNewEmployeeNumber = None, setNewVendorNumber = None, setOldEmployeeNumber = None, setOldVendorNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorID = None, returnTempNameNumberID = False, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNameNumber(EntityID = 1, setTempNameNumberID = None, setConflictReason = None, setCreatedTime = None, setEmployeeID = None, setFullNameLFM = None, setHasConflicts = None, setModifiedTime = None, setNameID = None, setNameNumber = None, setNewEmployeeNumber = None, setNewVendorNumber = None, setOldEmployeeNumber = None, setOldVendorNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVendorID = None, returnTempNameNumberID = False, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNameNumber(TempNameNumberID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "delete")


def getEveryVehicle(searchConditions = [], EntityID = 1, returnVehicleID = False, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Vehicle in the district.

    This function returns a dataframe of every Vehicle in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getVehicle(VehicleID, EntityID = 1, returnVehicleID = False, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "get", return_params_list = return_params)

def modifyVehicle(VehicleID, EntityID = 1, setVehicleID = None, setColor = None, setCreatedTime = None, setLicensePlateNumber = None, setMakeModel = None, setModifiedTime = None, setPermitDate = None, setPermitNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVIN = None, setYear = None, returnVehicleID = False, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "post", return_params_list = return_params, payload = payload_params)

def createVehicle(EntityID = 1, setVehicleID = None, setColor = None, setCreatedTime = None, setLicensePlateNumber = None, setMakeModel = None, setModifiedTime = None, setPermitDate = None, setPermitNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVIN = None, setYear = None, returnVehicleID = False, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteVehicle(VehicleID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "delete")


def getEveryZip(searchConditions = [], EntityID = 1, returnZipID = False, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnEdFiCountryID = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

    """Get every Zip in the district.

    This function returns a dataframe of every Zip in the district filtered by search conditions.

    """

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):
        return_params = list(return_params.assign(Value = True).Param)
    else:
        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    if len(searchConditions) > 0:

        searchConditions = params.query('Param == "searchConditions"').Value[0]

        payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

    else:
        return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)

def getZip(ZipID, EntityID = 1, returnZipID = False, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnEdFiCountryID = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "get", return_params_list = return_params)

def modifyZip(ZipID, EntityID = 1, setZipID = None, setCity = None, setCityState = None, setCityStateCode = None, setCityStateZip = None, setCityZipCode = None, setCountryCode = None, setCreatedTime = None, setEdFiCountryID = None, setFreeFormCountry = None, setFreeFormState = None, setIsPreferredByUSPS = None, setModifiedTime = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, returnZipID = False, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnEdFiCountryID = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    payload_params["DataObject"].update(dict({params.Param[0]:params.Value[0]}))

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "post", return_params_list = return_params, payload = payload_params)

def createZip(EntityID = 1, setZipID = None, setCity = None, setCityState = None, setCityStateCode = None, setCityStateZip = None, setCityZipCode = None, setCountryCode = None, setCreatedTime = None, setEdFiCountryID = None, setFreeFormCountry = None, setFreeFormState = None, setIsPreferredByUSPS = None, setModifiedTime = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setZipCode = None, returnZipID = False, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnEdFiCountryID = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteZip(ZipID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "delete")