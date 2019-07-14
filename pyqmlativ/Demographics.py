# This module contains Demographics functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryACHAccount(EntityID = 1, page = 1, pageSize = 100, returnACHAccountID = True, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getACHAccount(ACHAccountID, EntityID = 1, returnACHAccountID = True, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "get", return_params_list = return_params_list)

def modifyACHAccount(ACHAccountID, EntityID = 1, setAccountType = None, setAccountTypeCode = None, setACHAccountNumber = None, setClass = None, setClassCode = None, setCompanyEntryDescription = None, setIsActive = None, setIsStateDisbursementUnit = None, setNameID = None, setPrenoteDate = None, setReceivingCompany = None, setRoutingNumber = None, setStateIDSDU = None, setRelationships = None, returnACHAccountID = True, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createACHAccount(EntityID = 1, setAccountType = None, setAccountTypeCode = None, setACHAccountNumber = None, setClass = None, setClassCode = None, setCompanyEntryDescription = None, setIsActive = None, setIsStateDisbursementUnit = None, setNameID = None, setPrenoteDate = None, setReceivingCompany = None, setRoutingNumber = None, setStateIDSDU = None, setRelationships = None, returnACHAccountID = True, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteACHAccount(ACHAccountID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddress(EntityID = 1, page = 1, pageSize = 100, returnAddressID = True, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddress(AddressID, EntityID = 1, returnAddressID = True, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "get", return_params_list = return_params_list)

def modifyAddress(AddressID, EntityID = 1, setAddressLine2 = None, setAddressRangeNumericStreetNumber = None, setAddressSecondaryUnitID = None, setAddressType = None, setAddressTypeCode = None, setCountyID = None, setFreeformAddress = None, setFullAddress = None, setInternationalAddress1 = None, setInternationalAddress2 = None, setInternationalAddress3 = None, setInternationalAddress4 = None, setLatitude = None, setLongitude = None, setPOBox = None, setSecondaryUnitNumber = None, setStreetID = None, setStreetNumber = None, setZipCodeAddOn = None, setZipID = None, setRelationships = None, returnAddressID = True, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddress(EntityID = 1, setAddressLine2 = None, setAddressRangeNumericStreetNumber = None, setAddressSecondaryUnitID = None, setAddressType = None, setAddressTypeCode = None, setCountyID = None, setFreeformAddress = None, setFullAddress = None, setInternationalAddress1 = None, setInternationalAddress2 = None, setInternationalAddress3 = None, setInternationalAddress4 = None, setLatitude = None, setLongitude = None, setPOBox = None, setSecondaryUnitNumber = None, setStreetID = None, setStreetNumber = None, setZipCodeAddOn = None, setZipID = None, setRelationships = None, returnAddressID = True, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddress(AddressID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultID = True, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, returnAddressRangeDefaultID = True, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "get", return_params_list = return_params_list)

def modifyAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, setAddressRangeDefaultIDClonedFrom = None, setCity = None, setDistrictID = None, setIsManual = None, setSchoolYearID = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSide = None, setStreetSideCode = None, setZipCode = None, setZipCodeAddOn = None, setRelationships = None, returnAddressRangeDefaultID = True, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressRangeDefault(EntityID = 1, setAddressRangeDefaultIDClonedFrom = None, setCity = None, setDistrictID = None, setIsManual = None, setSchoolYearID = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSide = None, setStreetSideCode = None, setZipCode = None, setZipCodeAddOn = None, setRelationships = None, returnAddressRangeDefaultID = True, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressRangeDefault(AddressRangeDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressRangeDefaultAddress(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultAddressID = True, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, returnAddressRangeDefaultAddressID = True, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "get", return_params_list = return_params_list)

def modifyAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, setAddressID = None, setAddressRangeDefaultID = None, setRelationships = None, returnAddressRangeDefaultAddressID = True, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressRangeDefaultAddress(EntityID = 1, setAddressID = None, setAddressRangeDefaultID = None, setRelationships = None, returnAddressRangeDefaultAddressID = True, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressRangeDefaultSchool(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultSchoolID = True, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1, returnAddressRangeDefaultSchoolID = True, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "get", return_params_list = return_params_list)

def modifyAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1, setAddressRangeDefaultID = None, setAddressRangeDefaultSchoolIDClonedFrom = None, setOrder = None, setSchoolID = None, setRelationships = None, returnAddressRangeDefaultSchoolID = True, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressRangeDefaultSchool(EntityID = 1, setAddressRangeDefaultID = None, setAddressRangeDefaultSchoolIDClonedFrom = None, setOrder = None, setSchoolID = None, setRelationships = None, returnAddressRangeDefaultSchoolID = True, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressRangeImportSchool(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeImportSchoolID = True, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, returnAddressRangeImportSchoolID = True, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "get", return_params_list = return_params_list)

def modifyAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, setAddressRangeImportSchoolIDClonedFrom = None, setDescription = None, setImportSchoolCode = None, setSchoolID = None, setRelationships = None, returnAddressRangeImportSchoolID = True, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressRangeImportSchool(EntityID = 1, setAddressRangeImportSchoolIDClonedFrom = None, setDescription = None, setImportSchoolCode = None, setSchoolID = None, setRelationships = None, returnAddressRangeImportSchoolID = True, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1, returnAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "get", return_params_list = return_params_list)

def modifyAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1, setOrder = None, setSchoolID = None, setStudentID = None, setRelationships = None, returnAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressSchoolPathOverride(EntityID = 1, setOrder = None, setSchoolID = None, setStudentID = None, setRelationships = None, returnAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryAddressSecondaryUnit(EntityID = 1, page = 1, pageSize = 100, returnAddressSecondaryUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, returnAddressSecondaryUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "get", return_params_list = return_params_list)

def modifyAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, setCode = None, setDescription = None, setRequiresNumber = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAddressSecondaryUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createAddressSecondaryUnit(EntityID = 1, setCode = None, setDescription = None, setRequiresNumber = None, setSkywardHash = None, setSkywardID = None, setRelationships = None, returnAddressSecondaryUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertification(EntityID = 1, page = 1, pageSize = 100, returnCertificationID = True, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertification(CertificationID, EntityID = 1, returnCertificationID = True, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "get", return_params_list = return_params_list)

def modifyCertification(CertificationID, EntityID = 1, setCertificationNumber = None, setCertificationThirdPartyImportID = None, setCertificationTypeID = None, setComment = None, setExpirationDate = None, setInstitutionID = None, setIssueDate = None, setNameID = None, setStateID = None, setRelationships = None, returnCertificationID = True, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertification(EntityID = 1, setCertificationNumber = None, setCertificationThirdPartyImportID = None, setCertificationTypeID = None, setComment = None, setExpirationDate = None, setInstitutionID = None, setIssueDate = None, setNameID = None, setStateID = None, setRelationships = None, returnCertificationID = True, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertification(CertificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationCompetency(EntityID = 1, page = 1, pageSize = 100, returnCertificationCompetencyID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationCompetency(CertificationCompetencyID, EntityID = 1, returnCertificationCompetencyID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "get", return_params_list = return_params_list)

def modifyCertificationCompetency(CertificationCompetencyID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationCompetencyID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationCompetency(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationCompetencyID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationCompetency(CertificationCompetencyID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationDelimitedFileFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationDelimitedFileFormatID = True, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, returnCertificationDelimitedFileFormatID = True, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "get", return_params_list = return_params_list)

def modifyCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, setCertificationCompetencyColumnNumber = None, setCertificationDetailExpirationDateColumnNumber = None, setCertificationDetailIssueDateColumnNumber = None, setCertificationLevelColumnNumber = None, setCertificationNumberColumnNumber = None, setCertificationSubjectColumnNumber = None, setCertificationThirdPartyFormatID = None, setCertificationTypeColumnNumber = None, setCommentColumnNumber = None, setDelimiterCharacter = None, setDelimiterType = None, setDelimiterTypeCode = None, setEmployeeColumnNumber = None, setExpirationDateColumnNumber = None, setHighCertificationGradeColumnNumber = None, setHighlyQualifiedColumnNumber = None, setInstitutionNameColumnNumber = None, setIssueDateColumnNumber = None, setLowCertificationGradeColumnNumber = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateColumnNumber = None, setRelationships = None, returnCertificationDelimitedFileFormatID = True, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationDelimitedFileFormat(EntityID = 1, setCertificationCompetencyColumnNumber = None, setCertificationDetailExpirationDateColumnNumber = None, setCertificationDetailIssueDateColumnNumber = None, setCertificationLevelColumnNumber = None, setCertificationNumberColumnNumber = None, setCertificationSubjectColumnNumber = None, setCertificationThirdPartyFormatID = None, setCertificationTypeColumnNumber = None, setCommentColumnNumber = None, setDelimiterCharacter = None, setDelimiterType = None, setDelimiterTypeCode = None, setEmployeeColumnNumber = None, setExpirationDateColumnNumber = None, setHighCertificationGradeColumnNumber = None, setHighlyQualifiedColumnNumber = None, setInstitutionNameColumnNumber = None, setIssueDateColumnNumber = None, setLowCertificationGradeColumnNumber = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateColumnNumber = None, setRelationships = None, returnCertificationDelimitedFileFormatID = True, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationDetail(EntityID = 1, page = 1, pageSize = 100, returnCertificationDetailID = True, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationDetail(CertificationDetailID, EntityID = 1, returnCertificationDetailID = True, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "get", return_params_list = return_params_list)

def modifyCertificationDetail(CertificationDetailID, EntityID = 1, setCertificationCompetencyID = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationID = None, setCertificationLevelID = None, setCertificationSubjectID = None, setCertificationThirdPartyImportID = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setRelationships = None, returnCertificationDetailID = True, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationDetail(EntityID = 1, setCertificationCompetencyID = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationID = None, setCertificationLevelID = None, setCertificationSubjectID = None, setCertificationThirdPartyImportID = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setRelationships = None, returnCertificationDetailID = True, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationDetail(CertificationDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationFixedLengthFileFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationFixedLengthFileFormatID = True, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, returnCertificationFixedLengthFileFormatID = True, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "get", return_params_list = return_params_list)

def modifyCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, setCertificationCompetencyLength = None, setCertificationCompetencyStartPosition = None, setCertificationDetailExpirationDateLength = None, setCertificationDetailExpirationDateStartPosition = None, setCertificationDetailIssueDateLength = None, setCertificationDetailIssueDateStartPosition = None, setCertificationLevelLength = None, setCertificationLevelStartPosition = None, setCertificationNumberLength = None, setCertificationNumberStartPosition = None, setCertificationSubjectLength = None, setCertificationSubjectStartPosition = None, setCertificationThirdPartyFormatID = None, setCertificationTypeLength = None, setCertificationTypeStartPosition = None, setCommentLength = None, setCommentStartPosition = None, setEmployeeLength = None, setEmployeeStartPosition = None, setExpirationDateLength = None, setExpirationDateStartPosition = None, setHighCertificationGradeLength = None, setHighCertificationGradeStartPosition = None, setHighlyQualifiedLength = None, setHighlyQualifiedStartPosition = None, setInstitutionNameLength = None, setInstitutionNameStartPosition = None, setIssueDateLength = None, setIssueDateStartPosition = None, setLowCertificationGradeLength = None, setLowCertificationGradeStartPosition = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateLength = None, setStateStartPosition = None, setRelationships = None, returnCertificationFixedLengthFileFormatID = True, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationFixedLengthFileFormat(EntityID = 1, setCertificationCompetencyLength = None, setCertificationCompetencyStartPosition = None, setCertificationDetailExpirationDateLength = None, setCertificationDetailExpirationDateStartPosition = None, setCertificationDetailIssueDateLength = None, setCertificationDetailIssueDateStartPosition = None, setCertificationLevelLength = None, setCertificationLevelStartPosition = None, setCertificationNumberLength = None, setCertificationNumberStartPosition = None, setCertificationSubjectLength = None, setCertificationSubjectStartPosition = None, setCertificationThirdPartyFormatID = None, setCertificationTypeLength = None, setCertificationTypeStartPosition = None, setCommentLength = None, setCommentStartPosition = None, setEmployeeLength = None, setEmployeeStartPosition = None, setExpirationDateLength = None, setExpirationDateStartPosition = None, setHighCertificationGradeLength = None, setHighCertificationGradeStartPosition = None, setHighlyQualifiedLength = None, setHighlyQualifiedStartPosition = None, setInstitutionNameLength = None, setInstitutionNameStartPosition = None, setIssueDateLength = None, setIssueDateStartPosition = None, setLowCertificationGradeLength = None, setLowCertificationGradeStartPosition = None, setNumberOfHeaderRows = None, setSkywardHash = None, setSkywardID = None, setStateLength = None, setStateStartPosition = None, setRelationships = None, returnCertificationFixedLengthFileFormatID = True, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationGrade(EntityID = 1, page = 1, pageSize = 100, returnCertificationGradeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationGrade(CertificationGradeID, EntityID = 1, returnCertificationGradeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "get", return_params_list = return_params_list)

def modifyCertificationGrade(CertificationGradeID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationGradeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationGrade(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationGradeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationGrade(CertificationGradeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationLevel(EntityID = 1, page = 1, pageSize = 100, returnCertificationLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationLevel(CertificationLevelID, EntityID = 1, returnCertificationLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "get", return_params_list = return_params_list)

def modifyCertificationLevel(CertificationLevelID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationLevel(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationLevel(CertificationLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationSubject(EntityID = 1, page = 1, pageSize = 100, returnCertificationSubjectID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationSubject(CertificationSubjectID, EntityID = 1, returnCertificationSubjectID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "get", return_params_list = return_params_list)

def modifyCertificationSubject(CertificationSubjectID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationSubjectID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationSubject(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnCertificationSubjectID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationSubject(CertificationSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, returnCertificationThirdPartyFormatID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, setCode = None, setDateFormat = None, setDateFormatCode = None, setDescription = None, setDistrictID = None, setImportType = None, setImportTypeCode = None, setNameIdentification = None, setNameIdentificationCode = None, setSkywardHash = None, setSkywardID = None, setSkywardIDClonedFrom = None, setRelationships = None, returnCertificationThirdPartyFormatID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormat(EntityID = 1, setCode = None, setDateFormat = None, setDateFormatCode = None, setDescription = None, setDistrictID = None, setImportType = None, setImportTypeCode = None, setNameIdentification = None, setNameIdentificationCode = None, setSkywardHash = None, setSkywardID = None, setSkywardIDClonedFrom = None, setRelationships = None, returnCertificationThirdPartyFormatID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatCertificationCompetency(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationCompetencyID = True, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, returnCertificationThirdPartyFormatCertificationCompetencyID = True, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, setCertificationCompetencyID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationCompetencyID = True, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatCertificationCompetency(EntityID = 1, setCertificationCompetencyID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationCompetencyID = True, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatCertificationGrade(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationGradeID = True, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, returnCertificationThirdPartyFormatCertificationGradeID = True, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, setCertificationGradeID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationGradeID = True, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatCertificationGrade(EntityID = 1, setCertificationGradeID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationGradeID = True, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatCertificationLevel(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationLevelID = True, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, returnCertificationThirdPartyFormatCertificationLevelID = True, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, setCertificationLevelID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationLevelID = True, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatCertificationLevel(EntityID = 1, setCertificationLevelID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationLevelID = True, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatCertificationSubject(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationSubjectID = True, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, returnCertificationThirdPartyFormatCertificationSubjectID = True, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, setCertificationSubjectID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationSubjectID = True, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatCertificationSubject(EntityID = 1, setCertificationSubjectID = None, setCertificationThirdPartyFormatID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationSubjectID = True, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatCertificationType(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationTypeID = True, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, returnCertificationThirdPartyFormatCertificationTypeID = True, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, setCertificationThirdPartyFormatID = None, setCertificationTypeID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationTypeID = True, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatCertificationType(EntityID = 1, setCertificationThirdPartyFormatID = None, setCertificationTypeID = None, setImportValue = None, setRelationships = None, returnCertificationThirdPartyFormatCertificationTypeID = True, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyFormatInstitution(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatInstitutionID = True, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, returnCertificationThirdPartyFormatInstitutionID = True, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, setCertificationThirdPartyFormatID = None, setImportValue = None, setInstitutionID = None, setRelationships = None, returnCertificationThirdPartyFormatInstitutionID = True, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyFormatInstitution(EntityID = 1, setCertificationThirdPartyFormatID = None, setImportValue = None, setInstitutionID = None, setRelationships = None, returnCertificationThirdPartyFormatInstitutionID = True, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationThirdPartyImport(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyImportID = True, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, returnCertificationThirdPartyImportID = True, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "get", return_params_list = return_params_list)

def modifyCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, setImportTime = None, setMediaID = None, setMediaIDFailedResult = None, setThirdPartyFormatID = None, setRelationships = None, returnCertificationThirdPartyImportID = True, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationThirdPartyImport(EntityID = 1, setImportTime = None, setMediaID = None, setMediaIDFailedResult = None, setThirdPartyFormatID = None, setRelationships = None, returnCertificationThirdPartyImportID = True, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCertificationType(EntityID = 1, page = 1, pageSize = 100, returnCertificationTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCertificationType(CertificationTypeID, EntityID = 1, returnCertificationTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "get", return_params_list = return_params_list)

def modifyCertificationType(CertificationTypeID, EntityID = 1, setCode = None, setDescription = None, setIsCRDCCertified = None, setRelationships = None, returnCertificationTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCertificationType(EntityID = 1, setCode = None, setDescription = None, setIsCRDCCertified = None, setRelationships = None, returnCertificationTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCertificationType(CertificationTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnConfigDistrictID = True, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", return_params_list = return_params_list)

def modifyConfigDistrict(ConfigDistrictID, EntityID = 1, setAutoAddSchoolPathOverride = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setPermitIDAutoAdd = None, setRelationships = None, returnConfigDistrictID = True, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigDistrict(EntityID = 1, setAutoAddSchoolPathOverride = None, setDistrictID = None, setEnforceAddressRangeDefaults = None, setPermitIDAutoAdd = None, setRelationships = None, returnConfigDistrictID = True, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnConfigSystemID = True, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "get", return_params_list = return_params_list)

def modifyConfigSystem(ConfigSystemID, EntityID = 1, setDefaultCaseAddressType = None, setDefaultCaseAddressTypeCode = None, setDefaultCaseNameType = None, setDefaultCaseNameTypeCode = None, setNameNumberLength = None, setUseSyncedNameNumber = None, setRelationships = None, returnConfigSystemID = True, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createConfigSystem(EntityID = 1, setDefaultCaseAddressType = None, setDefaultCaseAddressTypeCode = None, setDefaultCaseNameType = None, setDefaultCaseNameTypeCode = None, setNameNumberLength = None, setUseSyncedNameNumber = None, setRelationships = None, returnConfigSystemID = True, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryCounty(EntityID = 1, page = 1, pageSize = 100, returnCountyID = True, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getCounty(CountyID, EntityID = 1, returnCountyID = True, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "get", return_params_list = return_params_list)

def modifyCounty(CountyID, EntityID = 1, setName = None, setStateCountyMNID = None, setStateID = None, setRelationships = None, returnCountyID = True, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createCounty(EntityID = 1, setName = None, setStateCountyMNID = None, setStateID = None, setRelationships = None, returnCountyID = True, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteCounty(CountyID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDependent(EntityID = 1, page = 1, pageSize = 100, returnDependentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDependent(DependentID, EntityID = 1, returnDependentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "get", return_params_list = return_params_list)

def modifyDependent(DependentID, EntityID = 1, setNameIDDependent = None, setNameIDOwner = None, setRelationshipID = None, setRelationships = None, returnDependentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDependent(EntityID = 1, setNameIDDependent = None, setNameIDOwner = None, setRelationshipID = None, setRelationships = None, returnDependentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDependent(DependentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryDirectional(EntityID = 1, page = 1, pageSize = 100, returnDirectionalID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getDirectional(DirectionalID, EntityID = 1, returnDirectionalID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "get", return_params_list = return_params_list)

def modifyDirectional(DirectionalID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnDirectionalID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createDirectional(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnDirectionalID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteDirectional(DirectionalID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEmailType(EntityID = 1, page = 1, pageSize = 100, returnEmailTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEmailType(EmailTypeID, EntityID = 1, returnEmailTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "get", return_params_list = return_params_list)

def modifyEmailType(EmailTypeID, EntityID = 1, setCode = None, setDescription = None, setPreventFamilyStudentAccessUpdates = None, setRelationships = None, returnEmailTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEmailType(EntityID = 1, setCode = None, setDescription = None, setPreventFamilyStudentAccessUpdates = None, setRelationships = None, returnEmailTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEmailType(EmailTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnEmergencyContactID = True, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEmergencyContact(EmergencyContactID, EntityID = 1, returnEmergencyContactID = True, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "get", return_params_list = return_params_list)

def modifyEmergencyContact(EmergencyContactID, EntityID = 1, setAllowPickUp = None, setComment = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipID = None, setRelationships = None, returnEmergencyContactID = True, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEmergencyContact(EntityID = 1, setAllowPickUp = None, setComment = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipID = None, setRelationships = None, returnEmergencyContactID = True, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEmergencyContact(EmergencyContactID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryEmployer(EntityID = 1, page = 1, pageSize = 100, returnEmployerID = True, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getEmployer(EmployerID, EntityID = 1, returnEmployerID = True, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "get", return_params_list = return_params_list)

def modifyEmployer(EmployerID, EntityID = 1, setACATransmitterControlCode = None, setDistrictID = None, setEEO4ControlNumber = None, setEEO4JurisdictionName = None, setEEO5NameOfCertifyingOfficial = None, setEEO5OfficeOfSchoolNumber = None, setEEO5SchoolDistrictName = None, setEEOCTitleOfCertifyingOfficial = None, setFederalEEO4FunctionID = None, setNameID = None, setPERAEmployerNumber = None, setTRACountyGroupNumber = None, setTRADistrictUnitNumber = None, setUnemploymentInsuranceAccountNumber = None, setRelationships = None, returnEmployerID = True, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createEmployer(EntityID = 1, setACATransmitterControlCode = None, setDistrictID = None, setEEO4ControlNumber = None, setEEO4JurisdictionName = None, setEEO5NameOfCertifyingOfficial = None, setEEO5OfficeOfSchoolNumber = None, setEEO5SchoolDistrictName = None, setEEOCTitleOfCertifyingOfficial = None, setFederalEEO4FunctionID = None, setNameID = None, setPERAEmployerNumber = None, setTRACountyGroupNumber = None, setTRADistrictUnitNumber = None, setUnemploymentInsuranceAccountNumber = None, setRelationships = None, returnEmployerID = True, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteEmployer(EmployerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryInstitutionDefault(EntityID = 1, page = 1, pageSize = 100, returnInstitutionDefaultID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getInstitutionDefault(InstitutionDefaultID, EntityID = 1, returnInstitutionDefaultID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "get", return_params_list = return_params_list)

def modifyInstitutionDefault(InstitutionDefaultID, EntityID = 1, setCEEBCode = None, setMCCCCollegeCode = None, setName = None, setSkywardHash = None, setSkywardID = None, setStateID = None, setRelationships = None, returnInstitutionDefaultID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createInstitutionDefault(EntityID = 1, setCEEBCode = None, setMCCCCollegeCode = None, setName = None, setSkywardHash = None, setSkywardID = None, setStateID = None, setRelationships = None, returnInstitutionDefaultID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteInstitutionDefault(InstitutionDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryInstitution(EntityID = 1, page = 1, pageSize = 100, returnInstitutionID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getInstitution(InstitutionID, EntityID = 1, returnInstitutionID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "get", return_params_list = return_params_list)

def modifyInstitution(InstitutionID, EntityID = 1, setCEEBCode = None, setInstitutionDefaultID = None, setMCCCCollegeCode = None, setNameID = None, setStateID = None, setRelationships = None, returnInstitutionID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createInstitution(EntityID = 1, setCEEBCode = None, setInstitutionDefaultID = None, setMCCCCollegeCode = None, setNameID = None, setStateID = None, setRelationships = None, returnInstitutionID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteInstitution(InstitutionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLanguage(EntityID = 1, page = 1, pageSize = 100, returnLanguageID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLanguage(LanguageID, EntityID = 1, returnLanguageID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "get", return_params_list = return_params_list)

def modifyLanguage(LanguageID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnLanguageID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLanguage(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnLanguageID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLanguage(LanguageID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLanguageSchoolYear(EntityID = 1, page = 1, pageSize = 100, returnLanguageSchoolYearID = True, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, returnLanguageSchoolYearID = True, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "get", return_params_list = return_params_list)

def modifyLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, setEdFiLanguageID = None, setLanguageID = None, setLanguageSchoolYearIDClonedFrom = None, setSchoolYearID = None, setStateHeadStartLanguageMNID = None, setStateLanguageCodeMNID = None, setRelationships = None, returnLanguageSchoolYearID = True, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLanguageSchoolYear(EntityID = 1, setEdFiLanguageID = None, setLanguageID = None, setLanguageSchoolYearIDClonedFrom = None, setSchoolYearID = None, setStateHeadStartLanguageMNID = None, setStateLanguageCodeMNID = None, setRelationships = None, returnLanguageSchoolYearID = True, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryLastNameNumber(EntityID = 1, page = 1, pageSize = 100, returnLastNameNumberID = True, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getLastNameNumber(LastNameNumberID, EntityID = 1, returnLastNameNumberID = True, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "get", return_params_list = return_params_list)

def modifyLastNameNumber(LastNameNumberID, EntityID = 1, setConfigSystemID = None, setNameNumber = None, setRelationships = None, returnLastNameNumberID = True, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createLastNameNumber(EntityID = 1, setConfigSystemID = None, setNameNumber = None, setRelationships = None, returnLastNameNumberID = True, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteLastNameNumber(LastNameNumberID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryName(EntityID = 1, page = 1, pageSize = 100, returnNameID = True, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getName(NameID, EntityID = 1, returnNameID = True, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "get", return_params_list = return_params_list)

def modifyName(NameID, EntityID = 1, setBirthDate = None, setBirthMonthDay = None, setBypassStudentRaceValidation = None, setContactPerson = None, setConversionKey = None, setDriversLicenseNumber = None, setExternalUniqueIdentifier = None, setFederalEIN = None, setFirstName = None, setFirstNameLegal = None, setGender = None, setGenderCode = None, setIsAlaskan = None, setIsAsian = None, setIsBlack = None, setIsBusiness = None, setIsEmergencyContactName = None, setIsEmployeeName = None, setIsFeeManagementCustomerName = None, setIsFeeManagementPayorName = None, setIsFoodServiceCustomerName = None, setIsFoodServicePayorName = None, setIsGuardianName = None, setIsHawaiian = None, setIsHealthProfessionalName = None, setIsHispanic = None, setIsInstitution = None, setIsPayorName = None, setIsPlaceOfEmployment = None, setIsSingleLegalName = None, setIsStaffName = None, setIsStudentName = None, setIsUserName = None, setIsVendorName = None, setIsWhite = None, setLastName = None, setLastNameLegal = None, setMaritalStatus = None, setMaritalStatusCode = None, setMediaIDPhoto = None, setMiddleName = None, setMiddleNameLegal = None, setNameIDPlaceOfEmployment = None, setNameKey = None, setNameNumber = None, setNameSuffixID = None, setNameSuffixIDLegal = None, setNameTitleID = None, setNameTitleIDLegal = None, setOccupationID = None, setRaceVerifiedBy = None, setRaceVerifiedByCode = None, setRaceVerifiedDate = None, setSkywardHash = None, setSkywardID = None, setSocialSecurityNumber = None, setSpecifySeparateLegalName = None, setRelationships = None, returnNameID = True, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createName(EntityID = 1, setBirthDate = None, setBirthMonthDay = None, setBypassStudentRaceValidation = None, setContactPerson = None, setConversionKey = None, setDriversLicenseNumber = None, setExternalUniqueIdentifier = None, setFederalEIN = None, setFirstName = None, setFirstNameLegal = None, setGender = None, setGenderCode = None, setIsAlaskan = None, setIsAsian = None, setIsBlack = None, setIsBusiness = None, setIsEmergencyContactName = None, setIsEmployeeName = None, setIsFeeManagementCustomerName = None, setIsFeeManagementPayorName = None, setIsFoodServiceCustomerName = None, setIsFoodServicePayorName = None, setIsGuardianName = None, setIsHawaiian = None, setIsHealthProfessionalName = None, setIsHispanic = None, setIsInstitution = None, setIsPayorName = None, setIsPlaceOfEmployment = None, setIsSingleLegalName = None, setIsStaffName = None, setIsStudentName = None, setIsUserName = None, setIsVendorName = None, setIsWhite = None, setLastName = None, setLastNameLegal = None, setMaritalStatus = None, setMaritalStatusCode = None, setMediaIDPhoto = None, setMiddleName = None, setMiddleNameLegal = None, setNameIDPlaceOfEmployment = None, setNameKey = None, setNameNumber = None, setNameSuffixID = None, setNameSuffixIDLegal = None, setNameTitleID = None, setNameTitleIDLegal = None, setOccupationID = None, setRaceVerifiedBy = None, setRaceVerifiedByCode = None, setRaceVerifiedDate = None, setSkywardHash = None, setSkywardID = None, setSocialSecurityNumber = None, setSpecifySeparateLegalName = None, setRelationships = None, returnNameID = True, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteName(NameID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameAddress(EntityID = 1, page = 1, pageSize = 100, returnNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameAddress(NameAddressID, EntityID = 1, returnNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "get", return_params_list = return_params_list)

def modifyNameAddress(NameAddressID, EntityID = 1, setAddressID = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsPrimaryGuardian = None, setIsRemitTo = None, setIsW2 = None, setNameID = None, setRelationships = None, returnNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameAddress(EntityID = 1, setAddressID = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsPrimaryGuardian = None, setIsRemitTo = None, setIsW2 = None, setNameID = None, setRelationships = None, returnNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameAddress(NameAddressID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameAlias(EntityID = 1, page = 1, pageSize = 100, returnNameAliasID = True, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameAlias(NameAliasID, EntityID = 1, returnNameAliasID = True, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "get", return_params_list = return_params_list)

def modifyNameAlias(NameAliasID, EntityID = 1, setEffectiveDate = None, setFirstName = None, setIsBusiness = None, setIsLegalName = None, setIsMaidenName = None, setIsSingleLegalName = None, setLastName = None, setMiddleName = None, setNameID = None, setNameSuffixID = None, setNameTitleID = None, setRank = None, setRelationships = None, returnNameAliasID = True, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameAlias(EntityID = 1, setEffectiveDate = None, setFirstName = None, setIsBusiness = None, setIsLegalName = None, setIsMaidenName = None, setIsSingleLegalName = None, setLastName = None, setMiddleName = None, setNameID = None, setNameSuffixID = None, setNameTitleID = None, setRank = None, setRelationships = None, returnNameAliasID = True, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameAlias(NameAliasID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameEmail(EntityID = 1, page = 1, pageSize = 100, returnNameEmailID = True, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameEmail(NameEmailID, EntityID = 1, returnNameEmailID = True, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "get", return_params_list = return_params_list)

def modifyNameEmail(NameEmailID, EntityID = 1, setEmailAddress = None, setEmailTypeID = None, setNameID = None, setNote = None, setRank = None, setRelationships = None, returnNameEmailID = True, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameEmail(EntityID = 1, setEmailAddress = None, setEmailTypeID = None, setNameID = None, setNote = None, setRank = None, setRelationships = None, returnNameEmailID = True, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameEmail(NameEmailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameEthnicityRaceSubcategoryMN(EntityID = 1, page = 1, pageSize = 100, returnNameEthnicityRaceSubcategoryMNID = True, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, returnNameEthnicityRaceSubcategoryMNID = True, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "get", return_params_list = return_params_list)

def modifyNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, setEthnicityRaceType = None, setEthnicityRaceTypeCode = None, setNameID = None, setStateEthnicityRaceSubcategoryMNID = None, setRelationships = None, returnNameEthnicityRaceSubcategoryMNID = True, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameEthnicityRaceSubcategoryMN(EntityID = 1, setEthnicityRaceType = None, setEthnicityRaceTypeCode = None, setNameID = None, setStateEthnicityRaceSubcategoryMNID = None, setRelationships = None, returnNameEthnicityRaceSubcategoryMNID = True, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameMergeRunHistory(EntityID = 1, page = 1, pageSize = 100, returnNameMergeRunHistoryID = True, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, returnNameMergeRunHistoryID = True, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "get", return_params_list = return_params_list)

def modifyNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, setBirthDateFrom = None, setBirthDateTo = None, setFullNameLFMFrom = None, setFullNameLFMTo = None, setNameIDFrom = None, setNameIDTo = None, setNameUsedByFrom = None, setNameUsedByTo = None, setRelationships = None, returnNameMergeRunHistoryID = True, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameMergeRunHistory(EntityID = 1, setBirthDateFrom = None, setBirthDateTo = None, setFullNameLFMFrom = None, setFullNameLFMTo = None, setNameIDFrom = None, setNameIDTo = None, setNameUsedByFrom = None, setNameUsedByTo = None, setRelationships = None, returnNameMergeRunHistoryID = True, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNamePhone(EntityID = 1, page = 1, pageSize = 100, returnNamePhoneID = True, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNamePhone(NamePhoneID, EntityID = 1, returnNamePhoneID = True, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "get", return_params_list = return_params_list)

def modifyNamePhone(NamePhoneID, EntityID = 1, setExtension = None, setIsConfidential = None, setIsFax = None, setIsInternational = None, setNameID = None, setNote = None, setPhoneNumber = None, setPhoneTypeID = None, setRank = None, setRelationships = None, returnNamePhoneID = True, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNamePhone(EntityID = 1, setExtension = None, setIsConfidential = None, setIsFax = None, setIsInternational = None, setNameID = None, setNote = None, setPhoneNumber = None, setPhoneTypeID = None, setRank = None, setRelationships = None, returnNamePhoneID = True, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNamePhone(NamePhoneID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameSuffix(EntityID = 1, page = 1, pageSize = 100, returnNameSuffixID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameSuffix(NameSuffixID, EntityID = 1, returnNameSuffixID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "get", return_params_list = return_params_list)

def modifyNameSuffix(NameSuffixID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnNameSuffixID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameSuffix(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnNameSuffixID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameSuffix(NameSuffixID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameTitle(EntityID = 1, page = 1, pageSize = 100, returnNameTitleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameTitle(NameTitleID, EntityID = 1, returnNameTitleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "get", return_params_list = return_params_list)

def modifyNameTitle(NameTitleID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnNameTitleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameTitle(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnNameTitleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameTitle(NameTitleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameVehicle(EntityID = 1, page = 1, pageSize = 100, returnNameVehicleID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameVehicle(NameVehicleID, EntityID = 1, returnNameVehicleID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "get", return_params_list = return_params_list)

def modifyNameVehicle(NameVehicleID, EntityID = 1, setNameID = None, setVehicleID = None, setRelationships = None, returnNameVehicleID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameVehicle(EntityID = 1, setNameID = None, setVehicleID = None, setRelationships = None, returnNameVehicleID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameVehicle(NameVehicleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNameWebsite(EntityID = 1, page = 1, pageSize = 100, returnNameWebsiteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNameWebsite(NameWebsiteID, EntityID = 1, returnNameWebsiteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "get", return_params_list = return_params_list)

def modifyNameWebsite(NameWebsiteID, EntityID = 1, setNameID = None, setNote = None, setRank = None, setURL = None, setRelationships = None, returnNameWebsiteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNameWebsite(EntityID = 1, setNameID = None, setNote = None, setRank = None, setURL = None, setRelationships = None, returnNameWebsiteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNameWebsite(NameWebsiteID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOccupation(EntityID = 1, page = 1, pageSize = 100, returnOccupationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOccupation(OccupationID, EntityID = 1, returnOccupationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "get", return_params_list = return_params_list)

def modifyOccupation(OccupationID, EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnOccupationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOccupation(EntityID = 1, setCode = None, setDescription = None, setRelationships = None, returnOccupationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOccupation(OccupationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryPhoneType(EntityID = 1, page = 1, pageSize = 100, returnPhoneTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getPhoneType(PhoneTypeID, EntityID = 1, returnPhoneTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "get", return_params_list = return_params_list)

def modifyPhoneType(PhoneTypeID, EntityID = 1, setCode = None, setDescription = None, setPreventFamilyStudentAccessUpdates = None, setRelationships = None, returnPhoneTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createPhoneType(EntityID = 1, setCode = None, setDescription = None, setPreventFamilyStudentAccessUpdates = None, setRelationships = None, returnPhoneTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deletePhoneType(PhoneTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryRelationship(EntityID = 1, page = 1, pageSize = 100, returnRelationshipID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getRelationship(RelationshipID, EntityID = 1, returnRelationshipID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "get", return_params_list = return_params_list)

def modifyRelationship(RelationshipID, EntityID = 1, setCode = None, setDescription = None, setEdFiRelationTypeID = None, setRelationshipType = None, setRelationshipTypeCode = None, setRelationships = None, returnRelationshipID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createRelationship(EntityID = 1, setCode = None, setDescription = None, setEdFiRelationTypeID = None, setRelationshipType = None, setRelationshipTypeCode = None, setRelationships = None, returnRelationshipID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteRelationship(RelationshipID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStreet(EntityID = 1, page = 1, pageSize = 100, returnStreetID = True, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStreet(StreetID, EntityID = 1, returnStreetID = True, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "get", return_params_list = return_params_list)

def modifyStreet(StreetID, EntityID = 1, setDirectionalID = None, setName = None, setZipID = None, setRelationships = None, returnStreetID = True, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStreet(EntityID = 1, setDirectionalID = None, setName = None, setZipID = None, setRelationships = None, returnStreetID = True, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStreet(StreetID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempACHAccount(EntityID = 1, page = 1, pageSize = 100, returnTempACHAccountID = True, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempACHAccount(TempACHAccountID, EntityID = 1, returnTempACHAccountID = True, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "get", return_params_list = return_params_list)

def modifyTempACHAccount(TempACHAccountID, EntityID = 1, setAccountType = None, setACHAccountID = None, setACHAccountNumber = None, setIsEmployeeNetPayrollACH = None, setIsVendorAccountsPayableACH = None, setName = None, setRoutingNumber = None, setUseTaxAddenda = None, setRelationships = None, returnTempACHAccountID = True, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempACHAccount(EntityID = 1, setAccountType = None, setACHAccountID = None, setACHAccountNumber = None, setIsEmployeeNetPayrollACH = None, setIsVendorAccountsPayableACH = None, setName = None, setRoutingNumber = None, setUseTaxAddenda = None, setRelationships = None, returnTempACHAccountID = True, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempACHAccount(TempACHAccountID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAddress(EntityID = 1, page = 1, pageSize = 100, returnTempAddressID = True, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAddress(TempAddressID, EntityID = 1, returnTempAddressID = True, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "get", return_params_list = return_params_list)

def modifyTempAddress(TempAddressID, EntityID = 1, setAddressID = None, setAddressUsedBy = None, setCurrentFormattedFullAddress = None, setFieldPathsToUpdate = None, setFieldsToUpdate = None, setNewFormattedFullAddress = None, setSelected = None, setWorkflowErrors = None, setRelationships = None, returnTempAddressID = True, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAddress(EntityID = 1, setAddressID = None, setAddressUsedBy = None, setCurrentFormattedFullAddress = None, setFieldPathsToUpdate = None, setFieldsToUpdate = None, setNewFormattedFullAddress = None, setSelected = None, setWorkflowErrors = None, setRelationships = None, returnTempAddressID = True, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAddress(TempAddressID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAddressRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnTempAddressRangeDefaultID = True, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, returnTempAddressRangeDefaultID = True, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "get", return_params_list = return_params_list)

def modifyTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, setCity = None, setDefaultSchools = None, setException = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSideCode = None, setZipCode = None, setZipCodeAddOn = None, setRelationships = None, returnTempAddressRangeDefaultID = True, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAddressRangeDefault(EntityID = 1, setCity = None, setDefaultSchools = None, setException = None, setStateAbbreviation = None, setStreetDirection = None, setStreetName = None, setStreetNumberHigh = None, setStreetNumberLow = None, setStreetSideCode = None, setZipCode = None, setZipCodeAddOn = None, setRelationships = None, returnTempAddressRangeDefaultID = True, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnTempAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1, returnTempAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "get", return_params_list = return_params_list)

def modifyTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1, setExceptionNote = None, setHasExceptions = None, setOrder = None, setSchoolCodeName = None, setSchoolID = None, setSchoolIDClonedTo = None, setStudentID = None, setStudentName = None, setRelationships = None, returnTempAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempAddressSchoolPathOverride(EntityID = 1, setExceptionNote = None, setHasExceptions = None, setOrder = None, setSchoolCodeName = None, setSchoolID = None, setSchoolIDClonedTo = None, setStudentID = None, setStudentName = None, setRelationships = None, returnTempAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCertification(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCertification(TempCertificationID, EntityID = 1, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "get", return_params_list = return_params_list)

def modifyTempCertification(TempCertificationID, EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationTypeCode = None, setCertificationTypeCodeDescription = None, setCertificationTypeID = None, setComment = None, setErrorCount = None, setExpirationDate = None, setFullNameLFM = None, setHasErrors = None, setInstitutionID = None, setInstitutionName = None, setIssueDate = None, setLineNumber = None, setNameID = None, setStateDisplayName = None, setStateID = None, setRelationships = None, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCertification(EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationTypeCode = None, setCertificationTypeCodeDescription = None, setCertificationTypeID = None, setComment = None, setErrorCount = None, setExpirationDate = None, setFullNameLFM = None, setHasErrors = None, setInstitutionID = None, setInstitutionName = None, setIssueDate = None, setLineNumber = None, setNameID = None, setStateDisplayName = None, setStateID = None, setRelationships = None, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCertification(TempCertificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCertificationDetail(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationDetailID = True, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCertificationDetail(TempCertificationDetailID, EntityID = 1, returnTempCertificationDetailID = True, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "get", return_params_list = return_params_list)

def modifyTempCertificationDetail(TempCertificationDetailID, EntityID = 1, setCertificationCompetencyCode = None, setCertificationCompetencyID = None, setCertificationGradeHighCodeDescription = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationGradeLowCodeDescription = None, setCertificationID = None, setCertificationLevelCode = None, setCertificationLevelID = None, setCertificationSubjectCode = None, setCertificationSubjectID = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setLineNumber = None, setTempCertificationID = None, setRelationships = None, returnTempCertificationDetailID = True, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCertificationDetail(EntityID = 1, setCertificationCompetencyCode = None, setCertificationCompetencyID = None, setCertificationGradeHighCodeDescription = None, setCertificationGradeIDHigh = None, setCertificationGradeIDLow = None, setCertificationGradeLowCodeDescription = None, setCertificationID = None, setCertificationLevelCode = None, setCertificationLevelID = None, setCertificationSubjectCode = None, setCertificationSubjectID = None, setExpirationDate = None, setIsHighlyQualified = None, setIssueDate = None, setLineNumber = None, setTempCertificationID = None, setRelationships = None, returnTempCertificationDetailID = True, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCertificationDetail(TempCertificationDetailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCertificationError(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationErrorID = True, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCertificationError(TempCertificationErrorID, EntityID = 1, returnTempCertificationErrorID = True, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempCertificationError(TempCertificationErrorID, EntityID = 1, setCertificationID = None, setError = None, setErrorDetail = None, setLineNumber = None, setNameLFM = None, setTempCertificationID = None, setRelationships = None, returnTempCertificationErrorID = True, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCertificationError(EntityID = 1, setCertificationID = None, setError = None, setErrorDetail = None, setLineNumber = None, setNameLFM = None, setTempCertificationID = None, setRelationships = None, returnTempCertificationErrorID = True, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCertificationError(TempCertificationErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnTempEmergencyContactID = True, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnTempEmergencyContactID = True, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", return_params_list = return_params_list)

def modifyTempEmergencyContact(TempEmergencyContactID, EntityID = 1, setAllowPickUp = None, setEmergencyContactFor = None, setEmergencyContactName = None, setExceptionNote = None, setHasActiveRestrictedAccess = None, setHasExceptions = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipDescription = None, setRelationshipID = None, setRelationships = None, returnTempEmergencyContactID = True, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEmergencyContact(EntityID = 1, setAllowPickUp = None, setEmergencyContactFor = None, setEmergencyContactName = None, setExceptionNote = None, setHasActiveRestrictedAccess = None, setHasExceptions = None, setNameID = None, setNameIDEmergencyContact = None, setRank = None, setRelationshipDescription = None, setRelationshipID = None, setRelationships = None, returnTempEmergencyContactID = True, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempException(EntityID = 1, page = 1, pageSize = 100, returnTempExceptionID = True, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempException(TempExceptionID, EntityID = 1, returnTempExceptionID = True, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "get", return_params_list = return_params_list)

def modifyTempException(TempExceptionID, EntityID = 1, setLineNumber = None, setMessage = None, setNameLFM = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempException(EntityID = 1, setLineNumber = None, setMessage = None, setNameLFM = None, setRelationships = None, returnTempExceptionID = True, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempException(TempExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNameAddress(EntityID = 1, page = 1, pageSize = 100, returnTempNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNameAddress(TempNameAddressID, EntityID = 1, returnTempNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "get", return_params_list = return_params_list)

def modifyTempNameAddress(TempNameAddressID, EntityID = 1, setAddressID = None, setFullAddress = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsRemitTo = None, setIsW2 = None, setNameID = None, setRelationships = None, returnTempNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNameAddress(EntityID = 1, setAddressID = None, setFullAddress = None, setIs1099 = None, setIsBusDropoff = None, setIsBusPickup = None, setIsMailing = None, setIsOrderFrom = None, setIsPhysical = None, setIsRemitTo = None, setIsW2 = None, setNameID = None, setRelationships = None, returnTempNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNameAddress(TempNameAddressID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNameAddressMoveAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnTempNameAddressMoveAddressSchoolPathOverrideID = True, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1, returnTempNameAddressMoveAddressSchoolPathOverrideID = True, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "get", return_params_list = return_params_list)

def modifyTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1, setAddressSchoolPathOverrideID = None, setIsCreateOverride = None, setIsOverrideExists = None, setIsRemoveOverride = None, setIsRemovePermit = None, setIsUpdateOverride = None, setOrder = None, setSchoolID = None, setSchoolNameOverriddingTo = None, setSchoolNameToOverride = None, setSchoolYearDescription = None, setStudentFullNameLFM = None, setStudentID = None, setRelationships = None, returnTempNameAddressMoveAddressSchoolPathOverrideID = True, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNameAddressMoveAddressSchoolPathOverride(EntityID = 1, setAddressSchoolPathOverrideID = None, setIsCreateOverride = None, setIsOverrideExists = None, setIsRemoveOverride = None, setIsRemovePermit = None, setIsUpdateOverride = None, setOrder = None, setSchoolID = None, setSchoolNameOverriddingTo = None, setSchoolNameToOverride = None, setSchoolYearDescription = None, setStudentFullNameLFM = None, setStudentID = None, setRelationships = None, returnTempNameAddressMoveAddressSchoolPathOverrideID = True, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNameError(EntityID = 1, page = 1, pageSize = 100, returnTempNameErrorID = True, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNameError(TempNameErrorID, EntityID = 1, returnTempNameErrorID = True, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempNameError(TempNameErrorID, EntityID = 1, setFirstName = None, setLastName = None, setNameID = None, setNote = None, setRelationships = None, returnTempNameErrorID = True, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNameError(EntityID = 1, setFirstName = None, setLastName = None, setNameID = None, setNote = None, setRelationships = None, returnTempNameErrorID = True, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNameError(TempNameErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNameNumber(EntityID = 1, page = 1, pageSize = 100, returnTempNameNumberID = True, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNameNumber(TempNameNumberID, EntityID = 1, returnTempNameNumberID = True, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "get", return_params_list = return_params_list)

def modifyTempNameNumber(TempNameNumberID, EntityID = 1, setConflictReason = None, setEmployeeID = None, setFullNameLFM = None, setHasConflicts = None, setNameID = None, setNameNumber = None, setNewEmployeeNumber = None, setNewVendorNumber = None, setOldEmployeeNumber = None, setOldVendorNumber = None, setVendorID = None, setRelationships = None, returnTempNameNumberID = True, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNameNumber(EntityID = 1, setConflictReason = None, setEmployeeID = None, setFullNameLFM = None, setHasConflicts = None, setNameID = None, setNameNumber = None, setNewEmployeeNumber = None, setNewVendorNumber = None, setOldEmployeeNumber = None, setOldVendorNumber = None, setVendorID = None, setRelationships = None, returnTempNameNumberID = True, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNameNumber(TempNameNumberID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryVehicle(EntityID = 1, page = 1, pageSize = 100, returnVehicleID = True, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getVehicle(VehicleID, EntityID = 1, returnVehicleID = True, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "get", return_params_list = return_params_list)

def modifyVehicle(VehicleID, EntityID = 1, setColor = None, setLicensePlateNumber = None, setMakeModel = None, setPermitDate = None, setPermitNumber = None, setVIN = None, setYear = None, setRelationships = None, returnVehicleID = True, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createVehicle(EntityID = 1, setColor = None, setLicensePlateNumber = None, setMakeModel = None, setPermitDate = None, setPermitNumber = None, setVIN = None, setYear = None, setRelationships = None, returnVehicleID = True, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteVehicle(VehicleID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryZip(EntityID = 1, page = 1, pageSize = 100, returnZipID = True, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getZip(ZipID, EntityID = 1, returnZipID = True, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "get", return_params_list = return_params_list)

def modifyZip(ZipID, EntityID = 1, setCity = None, setCountryCode = None, setFreeFormCountry = None, setFreeFormState = None, setIsPreferredByUSPS = None, setStateID = None, setZipCode = None, setRelationships = None, returnZipID = True, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createZip(EntityID = 1, setCity = None, setCountryCode = None, setFreeFormCountry = None, setFreeFormState = None, setIsPreferredByUSPS = None, setStateID = None, setZipCode = None, setRelationships = None, returnZipID = True, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteZip(ZipID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")