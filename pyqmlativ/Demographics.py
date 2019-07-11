# This module contains Demographics functions.

from .Utilities import make_request

import pandas as pd

def getEveryACHAccount(EntityID = 1, page = 1, pageSize = 100, returnACHAccountID = True, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getACHAccount(ACHAccountID, EntityID = 1, returnreturnACHAccountID = False, returnreturnAccountType = False, returnreturnAccountTypeCode = False, returnreturnACHAccountNumber = False, returnreturnClass = False, returnreturnClassCode = False, returnreturnCompanyEntryDescription = False, returnreturnCreatedTime = False, returnreturnIsActive = False, returnreturnIsEmployeeChildSupportACH = False, returnreturnIsEmployeeNetPayrollACH = False, returnreturnIsStateDisbursementUnit = False, returnreturnIsVendorAccountsPayableACH = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnPrenoteDate = False, returnreturnReceivingCompany = False, returnreturnRoutingNumber = False, returnreturnStateIDSDU = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "get", params_list = params_list)

	return(response)

def deleteACHAccount(ACHAccountID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "delete")

	return(response)

def getEveryAddress(EntityID = 1, page = 1, pageSize = 100, returnAddressID = True, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddress(AddressID, EntityID = 1, returnreturnAddressID = False, returnreturnAddressLine2 = False, returnreturnAddressRangeNumericStreetNumber = False, returnreturnAddressRangeNumericStreetNumberIsOdd = False, returnreturnAddressSecondaryUnitID = False, returnreturnAddressType = False, returnreturnAddressTypeCode = False, returnreturnCountyID = False, returnreturnCreatedTime = False, returnreturnFormattedFullAddress = False, returnreturnFreeformAddress = False, returnreturnFullAddress = False, returnreturnInternationalAddress1 = False, returnreturnInternationalAddress2 = False, returnreturnInternationalAddress3 = False, returnreturnInternationalAddress4 = False, returnreturnLatitude = False, returnreturnLongitude = False, returnreturnModifiedTime = False, returnreturnPOBox = False, returnreturnPrintableHTMLAddress = False, returnreturnSecondaryUnitNumber = False, returnreturnStreetID = False, returnreturnStreetNumber = False, returnreturnStreetNumberAndName = False, returnreturnStreetNumberAndNameIncludeSecondaryUnit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnZipCodeAddOn = False, returnreturnZipCodeWithAddon = False, returnreturnZipCodeWithAddonNoHyphen = False, returnreturnZipID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "get", params_list = params_list)

	return(response)

def deleteAddress(AddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "delete")

	return(response)

def getEveryAddressRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultID = True, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, returnreturnAddressRangeDefaultID = False, returnreturnAddressRangeDefaultIDClonedFrom = False, returnreturnAddressRangeDefaultIDClonedTo = False, returnreturnCity = False, returnreturnCreatedTime = False, returnreturnDefaultSchools = False, returnreturnDistrictID = False, returnreturnFullAddressRange = False, returnreturnIsManual = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStateAbbreviation = False, returnreturnStreetDirection = False, returnreturnStreetName = False, returnreturnStreetNumberHigh = False, returnreturnStreetNumberLow = False, returnreturnStreetSide = False, returnreturnStreetSideCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnZipCode = False, returnreturnZipCodeAddOn = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefault(AddressRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "delete")

	return(response)

def getEveryAddressRangeDefaultAddress(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultAddressID = True, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, returnreturnAddressRangeDefaultAddressID = False, returnreturnAddressID = False, returnreturnAddressRangeDefaultID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "delete")

	return(response)

def getEveryAddressRangeDefaultSchool(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeDefaultSchoolID = True, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1, returnreturnAddressRangeDefaultSchoolID = False, returnreturnAddressRangeDefaultID = False, returnreturnAddressRangeDefaultSchoolIDClonedFrom = False, returnreturnCreatedTime = False, returnreturnIsOverridenForStudent = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnOverriddenSchoolID = False, returnreturnOverriddenSchoolName = False, returnreturnSchoolID = False, returnreturnStudentHasPermit = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "delete")

	return(response)

def getEveryAddressRangeImportSchool(EntityID = 1, page = 1, pageSize = 100, returnAddressRangeImportSchoolID = True, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, returnreturnAddressRangeImportSchoolID = False, returnreturnAddressRangeImportSchoolIDClonedFrom = False, returnreturnAddressRangeImportSchoolIDClonedTo = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnImportSchoolCode = False, returnreturnModifiedTime = False, returnreturnSchoolID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "delete")

	return(response)

def getEveryAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1, returnreturnAddressSchoolPathOverrideID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnSchoolID = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getEveryAddressSecondaryUnit(EntityID = 1, page = 1, pageSize = 100, returnAddressSecondaryUnitID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, returnreturnAddressSecondaryUnitID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnRequiresNumber = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "delete")

	return(response)

def getEveryCertification(EntityID = 1, page = 1, pageSize = 100, returnCertificationID = True, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertification(CertificationID, EntityID = 1, returnreturnCertificationID = False, returnreturnCertificationNumber = False, returnreturnCertificationThirdPartyImportID = False, returnreturnCertificationTypeID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnExpirationDate = False, returnreturnInstitutionID = False, returnreturnIssueDate = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "get", params_list = params_list)

	return(response)

def deleteCertification(CertificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "delete")

	return(response)

def getEveryCertificationCompetency(EntityID = 1, page = 1, pageSize = 100, returnCertificationCompetencyID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationCompetency(CertificationCompetencyID, EntityID = 1, returnreturnCertificationCompetencyID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationCompetency(CertificationCompetencyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "delete")

	return(response)

def getEveryCertificationDelimitedFileFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationDelimitedFileFormatID = True, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, returnreturnCertificationDelimitedFileFormatID = False, returnreturnCertificationCompetencyColumnNumber = False, returnreturnCertificationDetailExpirationDateColumnNumber = False, returnreturnCertificationDetailIssueDateColumnNumber = False, returnreturnCertificationLevelColumnNumber = False, returnreturnCertificationNumberColumnNumber = False, returnreturnCertificationSubjectColumnNumber = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCertificationTypeColumnNumber = False, returnreturnCommentColumnNumber = False, returnreturnCreatedTime = False, returnreturnDelimiterCharacter = False, returnreturnDelimiterType = False, returnreturnDelimiterTypeCode = False, returnreturnEmployeeColumnNumber = False, returnreturnExpirationDateColumnNumber = False, returnreturnHighCertificationGradeColumnNumber = False, returnreturnHighlyQualifiedColumnNumber = False, returnreturnInstitutionNameColumnNumber = False, returnreturnIssueDateColumnNumber = False, returnreturnLowCertificationGradeColumnNumber = False, returnreturnModifiedTime = False, returnreturnNumberOfHeaderRows = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnStateColumnNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "delete")

	return(response)

def getEveryCertificationDetail(EntityID = 1, page = 1, pageSize = 100, returnCertificationDetailID = True, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationDetail(CertificationDetailID, EntityID = 1, returnreturnCertificationDetailID = False, returnreturnCertificationCompetencyID = False, returnreturnCertificationGradeIDHigh = False, returnreturnCertificationGradeIDLow = False, returnreturnCertificationID = False, returnreturnCertificationLevelID = False, returnreturnCertificationSubjectID = False, returnreturnCertificationThirdPartyImportID = False, returnreturnCreatedTime = False, returnreturnExpirationDate = False, returnreturnIsHighlyQualified = False, returnreturnIssueDate = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationDetail(CertificationDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "delete")

	return(response)

def getEveryCertificationFixedLengthFileFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationFixedLengthFileFormatID = True, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, returnreturnCertificationFixedLengthFileFormatID = False, returnreturnCertificationCompetencyLength = False, returnreturnCertificationCompetencyStartPosition = False, returnreturnCertificationDetailExpirationDateLength = False, returnreturnCertificationDetailExpirationDateStartPosition = False, returnreturnCertificationDetailIssueDateLength = False, returnreturnCertificationDetailIssueDateStartPosition = False, returnreturnCertificationLevelLength = False, returnreturnCertificationLevelStartPosition = False, returnreturnCertificationNumberLength = False, returnreturnCertificationNumberStartPosition = False, returnreturnCertificationSubjectLength = False, returnreturnCertificationSubjectStartPosition = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCertificationTypeLength = False, returnreturnCertificationTypeStartPosition = False, returnreturnCommentLength = False, returnreturnCommentStartPosition = False, returnreturnCreatedTime = False, returnreturnEmployeeLength = False, returnreturnEmployeeStartPosition = False, returnreturnExpirationDateLength = False, returnreturnExpirationDateStartPosition = False, returnreturnHighCertificationGradeLength = False, returnreturnHighCertificationGradeStartPosition = False, returnreturnHighlyQualifiedLength = False, returnreturnHighlyQualifiedStartPosition = False, returnreturnInstitutionNameLength = False, returnreturnInstitutionNameStartPosition = False, returnreturnIssueDateLength = False, returnreturnIssueDateStartPosition = False, returnreturnLowCertificationGradeLength = False, returnreturnLowCertificationGradeStartPosition = False, returnreturnModifiedTime = False, returnreturnNumberOfHeaderRows = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnStateLength = False, returnreturnStateStartPosition = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "delete")

	return(response)

def getEveryCertificationGrade(EntityID = 1, page = 1, pageSize = 100, returnCertificationGradeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationGrade(CertificationGradeID, EntityID = 1, returnreturnCertificationGradeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationGrade(CertificationGradeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "delete")

	return(response)

def getEveryCertificationLevel(EntityID = 1, page = 1, pageSize = 100, returnCertificationLevelID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationLevel(CertificationLevelID, EntityID = 1, returnreturnCertificationLevelID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationLevel(CertificationLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "delete")

	return(response)

def getEveryCertificationSubject(EntityID = 1, page = 1, pageSize = 100, returnCertificationSubjectID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationSubject(CertificationSubjectID, EntityID = 1, returnreturnCertificationSubjectID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationSubject(CertificationSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormat(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, returnreturnCertificationThirdPartyFormatID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDateFormat = False, returnreturnDateFormatCode = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnImportType = False, returnreturnImportTypeCode = False, returnreturnIsSystemLoaded = False, returnreturnModifiedTime = False, returnreturnNameIdentification = False, returnreturnNameIdentificationCode = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnSkywardIDClonedFrom = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatCertificationCompetency(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationCompetencyID = True, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, returnreturnCertificationThirdPartyFormatCertificationCompetencyID = False, returnreturnCertificationCompetencyID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatCertificationGrade(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationGradeID = True, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, returnreturnCertificationThirdPartyFormatCertificationGradeID = False, returnreturnCertificationGradeID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatCertificationLevel(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationLevelID = True, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, returnreturnCertificationThirdPartyFormatCertificationLevelID = False, returnreturnCertificationLevelID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatCertificationSubject(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationSubjectID = True, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, returnreturnCertificationThirdPartyFormatCertificationSubjectID = False, returnreturnCertificationSubjectID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatCertificationType(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatCertificationTypeID = True, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, returnreturnCertificationThirdPartyFormatCertificationTypeID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCertificationTypeID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyFormatInstitution(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyFormatInstitutionID = True, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, returnreturnCertificationThirdPartyFormatInstitutionID = False, returnreturnCertificationThirdPartyFormatID = False, returnreturnCreatedTime = False, returnreturnImportValue = False, returnreturnInstitutionID = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "delete")

	return(response)

def getEveryCertificationThirdPartyImport(EntityID = 1, page = 1, pageSize = 100, returnCertificationThirdPartyImportID = True, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, returnreturnCertificationThirdPartyImportID = False, returnreturnCreatedTime = False, returnreturnImportTime = False, returnreturnMediaID = False, returnreturnMediaIDFailedResult = False, returnreturnModifiedTime = False, returnreturnThirdPartyFormatID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "delete")

	return(response)

def getEveryCertificationType(EntityID = 1, page = 1, pageSize = 100, returnCertificationTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCertificationType(CertificationTypeID, EntityID = 1, returnreturnCertificationTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnIsCRDCCertified = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationType(CertificationTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "delete")

	return(response)

def getEveryConfigDistrict(EntityID = 1, page = 1, pageSize = 100, returnConfigDistrictID = True, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnreturnConfigDistrictID = False, returnreturnAutoAddSchoolPathOverride = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEnforceAddressRangeDefaults = False, returnreturnModifiedTime = False, returnreturnPermitIDAutoAdd = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getEveryConfigSystem(EntityID = 1, page = 1, pageSize = 100, returnConfigSystemID = True, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getConfigSystem(ConfigSystemID, EntityID = 1, returnreturnConfigSystemID = False, returnreturnCreatedTime = False, returnreturnDefaultCaseAddressType = False, returnreturnDefaultCaseAddressTypeCode = False, returnreturnDefaultCaseNameType = False, returnreturnDefaultCaseNameTypeCode = False, returnreturnModifiedTime = False, returnreturnNameNumberLength = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseSyncedNameNumber = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getEveryCounty(EntityID = 1, page = 1, pageSize = 100, returnCountyID = True, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getCounty(CountyID, EntityID = 1, returnreturnCountyID = False, returnreturnCountyMNID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnStateCountyMNID = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "get", params_list = params_list)

	return(response)

def deleteCounty(CountyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "delete")

	return(response)

def getEveryDependent(EntityID = 1, page = 1, pageSize = 100, returnDependentID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDependent(DependentID, EntityID = 1, returnreturnDependentID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameIDDependent = False, returnreturnNameIDOwner = False, returnreturnRelationshipID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "get", params_list = params_list)

	return(response)

def deleteDependent(DependentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "delete")

	return(response)

def getEveryDirectional(EntityID = 1, page = 1, pageSize = 100, returnDirectionalID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getDirectional(DirectionalID, EntityID = 1, returnreturnDirectionalID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "get", params_list = params_list)

	return(response)

def deleteDirectional(DirectionalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "delete")

	return(response)

def getEveryEmailType(EntityID = 1, page = 1, pageSize = 100, returnEmailTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEmailType(EmailTypeID, EntityID = 1, returnreturnEmailTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnPreventFamilyStudentAccessUpdates = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteEmailType(EmailTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "delete")

	return(response)

def getEveryEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnEmergencyContactID = True, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEmergencyContact(EmergencyContactID, EntityID = 1, returnreturnEmergencyContactID = False, returnreturnAllowPickUp = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameIDEmergencyContact = False, returnreturnRank = False, returnreturnRelationshipID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "get", params_list = params_list)

	return(response)

def deleteEmergencyContact(EmergencyContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "delete")

	return(response)

def getEveryEmployer(EntityID = 1, page = 1, pageSize = 100, returnEmployerID = True, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getEmployer(EmployerID, EntityID = 1, returnreturnEmployerID = False, returnreturnACATransmitterControlCode = False, returnreturnCreatedTime = False, returnreturnDistrictID = False, returnreturnEEO4ControlNumber = False, returnreturnEEO4JurisdictionName = False, returnreturnEEO5NameOfCertifyingOfficial = False, returnreturnEEO5OfficeOfSchoolNumber = False, returnreturnEEO5SchoolDistrictName = False, returnreturnEEOCTitleOfCertifyingOfficial = False, returnreturnEmployerMNID = False, returnreturnFederalEEO4FunctionID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnPERAEmployerNumber = False, returnreturnTRACountyGroupNumber = False, returnreturnTRADistrictUnitNumber = False, returnreturnUnemploymentInsuranceAccountNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "get", params_list = params_list)

	return(response)

def deleteEmployer(EmployerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "delete")

	return(response)

def getEveryInstitutionDefault(EntityID = 1, page = 1, pageSize = 100, returnInstitutionDefaultID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInstitutionDefault(InstitutionDefaultID, EntityID = 1, returnreturnInstitutionDefaultID = False, returnreturnCEEBCode = False, returnreturnCreatedTime = False, returnreturnInstitutionDefaultMNID = False, returnreturnMCCCCollegeCode = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteInstitutionDefault(InstitutionDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "delete")

	return(response)

def getEveryInstitution(EntityID = 1, page = 1, pageSize = 100, returnInstitutionID = True, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getInstitution(InstitutionID, EntityID = 1, returnreturnInstitutionID = False, returnreturnCEEBCode = False, returnreturnCreatedTime = False, returnreturnInstitutionDefaultID = False, returnreturnInstitutionMNID = False, returnreturnMCCCCollegeCode = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "get", params_list = params_list)

	return(response)

def deleteInstitution(InstitutionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "delete")

	return(response)

def getEveryLanguage(EntityID = 1, page = 1, pageSize = 100, returnLanguageID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getLanguage(LanguageID, EntityID = 1, returnreturnLanguageID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnCurrentStateLanguage = False, returnreturnCurrentStateLanguageCode = False, returnreturnCurrentStateLanguageID = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "get", params_list = params_list)

	return(response)

def deleteLanguage(LanguageID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "delete")

	return(response)

def getEveryLanguageSchoolYear(EntityID = 1, page = 1, pageSize = 100, returnLanguageSchoolYearID = True, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, returnreturnLanguageSchoolYearID = False, returnreturnCreatedTime = False, returnreturnEdFiLanguageID = False, returnreturnLanguageID = False, returnreturnLanguageSchoolYearIDClonedFrom = False, returnreturnLanguageSchoolYearMNID = False, returnreturnModifiedTime = False, returnreturnSchoolYearID = False, returnreturnStateHeadStartLanguageMNID = False, returnreturnStateLanguageCodeMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "delete")

	return(response)

def getEveryLastNameNumber(EntityID = 1, page = 1, pageSize = 100, returnLastNameNumberID = True, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getLastNameNumber(LastNameNumberID, EntityID = 1, returnreturnLastNameNumberID = False, returnreturnConfigSystemID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteLastNameNumber(LastNameNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "delete")

	return(response)

def getEveryName(EntityID = 1, page = 1, pageSize = 100, returnNameID = True, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getName(NameID, EntityID = 1, returnreturnNameID = False, returnreturnAge = False, returnreturnBirthDate = False, returnreturnBirthMonthDay = False, returnreturnBirthYear = False, returnreturnBypassStudentRaceValidation = False, returnreturnCalculatedPrimaryFormattedPhoneNumber = False, returnreturnContactPerson = False, returnreturnConversionKey = False, returnreturnCreatedTime = False, returnreturnDatePhysicalAddressLastChanged = False, returnreturnDriversLicenseNumber = False, returnreturnEthnicity = False, returnreturnEthnicityAndRace = False, returnreturnExternalUniqueIdentifier = False, returnreturnFederalEIN = False, returnreturnFirstInitial = False, returnreturnFirstInitialLastName = False, returnreturnFirstInitialLastNameLegal = False, returnreturnFirstInitialLegal = False, returnreturnFirstName = False, returnreturnFirstNameLegal = False, returnreturnFullNameFL = False, returnreturnFullNameFMIL = False, returnreturnFullNameFML = False, returnreturnFullNameLegalFL = False, returnreturnFullNameLegalFML = False, returnreturnFullNameLegalLFM = False, returnreturnFullNameLF = False, returnreturnFullNameLFM = False, returnreturnGender = False, returnreturnGenderCode = False, returnreturnGetNameUse = False, returnreturnHasMailingOrPhysicalAddress = False, returnreturnInitials = False, returnreturnInitialsLegal = False, returnreturnIsAlaskan = False, returnreturnIsAsian = False, returnreturnIsBlack = False, returnreturnIsBusiness = False, returnreturnIsCurrentStudent = False, returnreturnIsEmergencyContactName = False, returnreturnIsEmployeeName = False, returnreturnIsEmployeeNameForDistrict = False, returnreturnIsEmployeeNameOrInEmployeeFamily = False, returnreturnIsFeeManagementCustomerName = False, returnreturnIsFeeManagementPayorName = False, returnreturnIsFoodServiceCustomerName = False, returnreturnIsFoodServicePayorName = False, returnreturnIsGuardianName = False, returnreturnIsHawaiian = False, returnreturnIsHealthProfessionalName = False, returnreturnIsHispanic = False, returnreturnIsInstitution = False, returnreturnIsPayorName = False, returnreturnIsPayorNameForDistrict = False, returnreturnIsPlaceOfEmployment = False, returnreturnIsSingleLegalName = False, returnreturnIsSkyward = False, returnreturnIsStaffName = False, returnreturnIsStudentInDistrict = False, returnreturnIsStudentName = False, returnreturnIsUserName = False, returnreturnIsVendorName = False, returnreturnIsVendorNameForDistrict = False, returnreturnIsWhite = False, returnreturnLastInitial = False, returnreturnLastInitialLegal = False, returnreturnLastName = False, returnreturnLastNameFirstInitial = False, returnreturnLastNameLegal = False, returnreturnMaritalStatus = False, returnreturnMaritalStatusCode = False, returnreturnMaskedSocialSecurityNumber = False, returnreturnMediaIDPhoto = False, returnreturnMiddleInitial = False, returnreturnMiddleInitialLegal = False, returnreturnMiddleName = False, returnreturnMiddleNameLegal = False, returnreturnModifiedTime = False, returnreturnNameAddressMailingID = False, returnreturnNameIDPlaceOfEmployment = False, returnreturnNameKey = False, returnreturnNameNumber = False, returnreturnNameSuffixID = False, returnreturnNameSuffixIDLegal = False, returnreturnNameTitleID = False, returnreturnNameTitleIDLegal = False, returnreturnOccupationID = False, returnreturnRace = False, returnreturnRaceEduphoriaCode = False, returnreturnRaceVerifiedBy = False, returnreturnRaceVerifiedByCode = False, returnreturnRaceVerifiedDate = False, returnreturnSkywardHash = False, returnreturnSkywardID = False, returnreturnSocialSecurityNumber = False, returnreturnSpecifySeparateLegalName = False, returnreturnTitledName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "get", params_list = params_list)

	return(response)

def deleteName(NameID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "delete")

	return(response)

def getEveryNameAddress(EntityID = 1, page = 1, pageSize = 100, returnNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameAddress(NameAddressID, EntityID = 1, returnreturnNameAddressID = False, returnreturnAddressID = False, returnreturnCreatedTime = False, returnreturnGetAddressType = False, returnreturnIs1099 = False, returnreturnIsBusDropoff = False, returnreturnIsBusPickup = False, returnreturnIsMailing = False, returnreturnIsOrderFrom = False, returnreturnIsPhysical = False, returnreturnIsPrimaryGuardian = False, returnreturnIsRemitTo = False, returnreturnIsW2 = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteNameAddress(NameAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "delete")

	return(response)

def getEveryNameAlias(EntityID = 1, page = 1, pageSize = 100, returnNameAliasID = True, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameAlias(NameAliasID, EntityID = 1, returnreturnNameAliasID = False, returnreturnCreatedTime = False, returnreturnEffectiveDate = False, returnreturnFirstName = False, returnreturnFullNameFL = False, returnreturnFullNameLF = False, returnreturnIsBusiness = False, returnreturnIsLegalName = False, returnreturnIsMaidenName = False, returnreturnIsSingleLegalName = False, returnreturnLastName = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameSuffixID = False, returnreturnNameTitleID = False, returnreturnRank = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "get", params_list = params_list)

	return(response)

def deleteNameAlias(NameAliasID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "delete")

	return(response)

def getEveryNameEmail(EntityID = 1, page = 1, pageSize = 100, returnNameEmailID = True, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameEmail(NameEmailID, EntityID = 1, returnreturnNameEmailID = False, returnreturnCreatedTime = False, returnreturnEmailAddress = False, returnreturnEmailTypeID = False, returnreturnIsAccountsPayableDirectDepositNotificationEmail = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNote = False, returnreturnRank = False, returnreturnUsedByHealthProfessional = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "get", params_list = params_list)

	return(response)

def deleteNameEmail(NameEmailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "delete")

	return(response)

def getEveryNameEthnicityRaceSubcategoryMN(EntityID = 1, page = 1, pageSize = 100, returnNameEthnicityRaceSubcategoryMNID = True, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, returnreturnNameEthnicityRaceSubcategoryMNID = False, returnreturnCreatedTime = False, returnreturnEthnicityRaceType = False, returnreturnEthnicityRaceTypeCode = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnStateEthnicityRaceSubcategoryMNID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "get", params_list = params_list)

	return(response)

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "delete")

	return(response)

def getEveryNameMergeRunHistory(EntityID = 1, page = 1, pageSize = 100, returnNameMergeRunHistoryID = True, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, returnreturnNameMergeRunHistoryID = False, returnreturnBirthDateFrom = False, returnreturnBirthDateTo = False, returnreturnCreatedTime = False, returnreturnFullNameLFMFrom = False, returnreturnFullNameLFMTo = False, returnreturnModifiedTime = False, returnreturnNameIDFrom = False, returnreturnNameIDTo = False, returnreturnNameUsedByFrom = False, returnreturnNameUsedByTo = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "delete")

	return(response)

def getEveryNamePhone(EntityID = 1, page = 1, pageSize = 100, returnNamePhoneID = True, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNamePhone(NamePhoneID, EntityID = 1, returnreturnNamePhoneID = False, returnreturnCreatedTime = False, returnreturnExtension = False, returnreturnFormattedPhoneNumber = False, returnreturnFormattedPhoneNumberCodeEEL = False, returnreturnFullPhoneNumber = False, returnreturnIsConfidential = False, returnreturnIsFax = False, returnreturnIsInternational = False, returnreturnIsPrimaryFax = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNote = False, returnreturnPhoneNumber = False, returnreturnPhoneTypeID = False, returnreturnRank = False, returnreturnUsedByHealthProfessional = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "get", params_list = params_list)

	return(response)

def deleteNamePhone(NamePhoneID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "delete")

	return(response)

def getEveryNameSuffix(EntityID = 1, page = 1, pageSize = 100, returnNameSuffixID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameSuffix(NameSuffixID, EntityID = 1, returnreturnNameSuffixID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "get", params_list = params_list)

	return(response)

def deleteNameSuffix(NameSuffixID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "delete")

	return(response)

def getEveryNameTitle(EntityID = 1, page = 1, pageSize = 100, returnNameTitleID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameTitle(NameTitleID, EntityID = 1, returnreturnNameTitleID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "get", params_list = params_list)

	return(response)

def deleteNameTitle(NameTitleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "delete")

	return(response)

def getEveryNameVehicle(EntityID = 1, page = 1, pageSize = 100, returnNameVehicleID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameVehicle(NameVehicleID, EntityID = 1, returnreturnNameVehicleID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVehicleID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "get", params_list = params_list)

	return(response)

def deleteNameVehicle(NameVehicleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "delete")

	return(response)

def getEveryNameWebsite(EntityID = 1, page = 1, pageSize = 100, returnNameWebsiteID = True, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNameWebsite(NameWebsiteID, EntityID = 1, returnreturnNameWebsiteID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNote = False, returnreturnRank = False, returnreturnURL = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameWebsite(NameWebsiteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "delete")

	return(response)

def getEveryOccupation(EntityID = 1, page = 1, pageSize = 100, returnOccupationID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOccupation(OccupationID, EntityID = 1, returnreturnOccupationID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "get", params_list = params_list)

	return(response)

def deleteOccupation(OccupationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "delete")

	return(response)

def getEveryPhoneType(EntityID = 1, page = 1, pageSize = 100, returnPhoneTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getPhoneType(PhoneTypeID, EntityID = 1, returnreturnPhoneTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnModifiedTime = False, returnreturnPreventFamilyStudentAccessUpdates = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "get", params_list = params_list)

	return(response)

def deletePhoneType(PhoneTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "delete")

	return(response)

def getEveryRelationship(EntityID = 1, page = 1, pageSize = 100, returnRelationshipID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getRelationship(RelationshipID, EntityID = 1, returnreturnRelationshipID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnEdFiRelationTypeID = False, returnreturnModifiedTime = False, returnreturnRelationshipType = False, returnreturnRelationshipTypeCode = False, returnreturnShortenedDescription = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "get", params_list = params_list)

	return(response)

def deleteRelationship(RelationshipID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "delete")

	return(response)

def getEveryStreet(EntityID = 1, page = 1, pageSize = 100, returnStreetID = True, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStreet(StreetID, EntityID = 1, returnreturnStreetID = False, returnreturnCreatedTime = False, returnreturnDirectionalID = False, returnreturnFormattedStreet = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnStreetNameWithDirectionCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnZipID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "get", params_list = params_list)

	return(response)

def deleteStreet(StreetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "delete")

	return(response)

def getEveryTempACHAccount(EntityID = 1, page = 1, pageSize = 100, returnTempACHAccountID = True, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempACHAccount(TempACHAccountID, EntityID = 1, returnreturnTempACHAccountID = False, returnreturnAccountType = False, returnreturnACHAccountID = False, returnreturnACHAccountNumber = False, returnreturnCreatedTime = False, returnreturnIsEmployeeNetPayrollACH = False, returnreturnIsVendorAccountsPayableACH = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnRoutingNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUseTaxAddenda = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "get", params_list = params_list)

	return(response)

def deleteTempACHAccount(TempACHAccountID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "delete")

	return(response)

def getEveryTempAddress(EntityID = 1, page = 1, pageSize = 100, returnTempAddressID = True, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAddress(TempAddressID, EntityID = 1, returnreturnTempAddressID = False, returnreturnAddressID = False, returnreturnAddressUsedBy = False, returnreturnCreatedTime = False, returnreturnCurrentFormattedFullAddress = False, returnreturnFieldPathsToUpdate = False, returnreturnFieldsToUpdate = False, returnreturnModifiedTime = False, returnreturnNewFormattedFullAddress = False, returnreturnSelected = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWorkflowErrors = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddress(TempAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "delete")

	return(response)

def getEveryTempAddressRangeDefault(EntityID = 1, page = 1, pageSize = 100, returnTempAddressRangeDefaultID = True, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, returnreturnTempAddressRangeDefaultID = False, returnreturnCity = False, returnreturnCreatedTime = False, returnreturnDefaultSchools = False, returnreturnException = False, returnreturnModifiedTime = False, returnreturnStateAbbreviation = False, returnreturnStreetDirection = False, returnreturnStreetName = False, returnreturnStreetNumberHigh = False, returnreturnStreetNumberLow = False, returnreturnStreetSideCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnZipCode = False, returnreturnZipCodeAddOn = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "delete")

	return(response)

def getEveryTempAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnTempAddressSchoolPathOverrideID = True, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1, returnreturnTempAddressSchoolPathOverrideID = False, returnreturnCreatedTime = False, returnreturnExceptionNote = False, returnreturnHasExceptions = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnSchoolCodeName = False, returnreturnSchoolID = False, returnreturnSchoolIDClonedTo = False, returnreturnStudentID = False, returnreturnStudentName = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getEveryTempCertification(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCertification(TempCertificationID, EntityID = 1, returnreturnTempCertificationID = False, returnreturnCertificationID = False, returnreturnCertificationNumber = False, returnreturnCertificationTypeCode = False, returnreturnCertificationTypeCodeDescription = False, returnreturnCertificationTypeID = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnErrorCount = False, returnreturnExpirationDate = False, returnreturnFullNameLFM = False, returnreturnHasErrors = False, returnreturnInstitutionID = False, returnreturnInstitutionName = False, returnreturnIssueDate = False, returnreturnLineNumber = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnStateDisplayName = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertification(TempCertificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "delete")

	return(response)

def getEveryTempCertificationDetail(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationDetailID = True, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCertificationDetail(TempCertificationDetailID, EntityID = 1, returnreturnTempCertificationDetailID = False, returnreturnCertificationCompetencyCode = False, returnreturnCertificationCompetencyID = False, returnreturnCertificationGradeHighCodeDescription = False, returnreturnCertificationGradeIDHigh = False, returnreturnCertificationGradeIDLow = False, returnreturnCertificationGradeLowCodeDescription = False, returnreturnCertificationID = False, returnreturnCertificationLevelCode = False, returnreturnCertificationLevelID = False, returnreturnCertificationSubjectCode = False, returnreturnCertificationSubjectID = False, returnreturnCreatedTime = False, returnreturnExpirationDate = False, returnreturnIsHighlyQualified = False, returnreturnIssueDate = False, returnreturnLineNumber = False, returnreturnModifiedTime = False, returnreturnTempCertificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertificationDetail(TempCertificationDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "delete")

	return(response)

def getEveryTempCertificationError(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationErrorID = True, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCertificationError(TempCertificationErrorID, EntityID = 1, returnreturnTempCertificationErrorID = False, returnreturnCertificationID = False, returnreturnCreatedTime = False, returnreturnError = False, returnreturnErrorDetail = False, returnreturnLineNumber = False, returnreturnModifiedTime = False, returnreturnNameLFM = False, returnreturnTempCertificationID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertificationError(TempCertificationErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "delete")

	return(response)

def getEveryTempEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnTempEmergencyContactID = True, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnreturnTempEmergencyContactID = False, returnreturnAllowPickUp = False, returnreturnCreatedTime = False, returnreturnEmergencyContactFor = False, returnreturnEmergencyContactName = False, returnreturnExceptionNote = False, returnreturnHasActiveRestrictedAccess = False, returnreturnHasExceptions = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameIDEmergencyContact = False, returnreturnRank = False, returnreturnRelationshipDescription = False, returnreturnRelationshipID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "delete")

	return(response)

def getEveryTempException(EntityID = 1, page = 1, pageSize = 100, returnTempExceptionID = True, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempException(TempExceptionID, EntityID = 1, returnreturnTempExceptionID = False, returnreturnCreatedTime = False, returnreturnLineNumber = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnNameLFM = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempException(TempExceptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "delete")

	return(response)

def getEveryTempNameAddress(EntityID = 1, page = 1, pageSize = 100, returnTempNameAddressID = True, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNameAddress(TempNameAddressID, EntityID = 1, returnreturnTempNameAddressID = False, returnreturnAddressID = False, returnreturnCreatedTime = False, returnreturnFullAddress = False, returnreturnIs1099 = False, returnreturnIsBusDropoff = False, returnreturnIsBusPickup = False, returnreturnIsMailing = False, returnreturnIsOrderFrom = False, returnreturnIsPhysical = False, returnreturnIsRemitTo = False, returnreturnIsW2 = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameAddress(TempNameAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "delete")

	return(response)

def getEveryTempNameAddressMoveAddressSchoolPathOverride(EntityID = 1, page = 1, pageSize = 100, returnTempNameAddressMoveAddressSchoolPathOverrideID = True, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1, returnreturnTempNameAddressMoveAddressSchoolPathOverrideID = False, returnreturnAddressSchoolPathOverrideID = False, returnreturnCreatedTime = False, returnreturnIsCreateOverride = False, returnreturnIsOverrideExists = False, returnreturnIsRemoveOverride = False, returnreturnIsRemovePermit = False, returnreturnIsUpdateOverride = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnSchoolID = False, returnreturnSchoolNameOverriddingTo = False, returnreturnSchoolNameToOverride = False, returnreturnSchoolYearDescription = False, returnreturnStudentFullNameLFM = False, returnreturnStudentID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getEveryTempNameError(EntityID = 1, page = 1, pageSize = 100, returnTempNameErrorID = True, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNameError(TempNameErrorID, EntityID = 1, returnreturnTempNameErrorID = False, returnreturnCreatedTime = False, returnreturnFirstName = False, returnreturnLastName = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNote = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameError(TempNameErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "delete")

	return(response)

def getEveryTempNameNumber(EntityID = 1, page = 1, pageSize = 100, returnTempNameNumberID = True, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNameNumber(TempNameNumberID, EntityID = 1, returnreturnTempNameNumberID = False, returnreturnConflictReason = False, returnreturnCreatedTime = False, returnreturnEmployeeID = False, returnreturnFullNameLFM = False, returnreturnHasConflicts = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameNumber = False, returnreturnNewEmployeeNumber = False, returnreturnNewVendorNumber = False, returnreturnOldEmployeeNumber = False, returnreturnOldVendorNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVendorID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameNumber(TempNameNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "delete")

	return(response)

def getEveryVehicle(EntityID = 1, page = 1, pageSize = 100, returnVehicleID = True, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getVehicle(VehicleID, EntityID = 1, returnreturnVehicleID = False, returnreturnColor = False, returnreturnCreatedTime = False, returnreturnLicensePlateNumber = False, returnreturnMakeModel = False, returnreturnModifiedTime = False, returnreturnPermitDate = False, returnreturnPermitNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVIN = False, returnreturnYear = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "get", params_list = params_list)

	return(response)

def deleteVehicle(VehicleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "delete")

	return(response)

def getEveryZip(EntityID = 1, page = 1, pageSize = 100, returnZipID = True, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getZip(ZipID, EntityID = 1, returnreturnZipID = False, returnreturnCity = False, returnreturnCityState = False, returnreturnCityStateCode = False, returnreturnCityStateZip = False, returnreturnCityZipCode = False, returnreturnCountryCode = False, returnreturnCreatedTime = False, returnreturnFreeFormCountry = False, returnreturnFreeFormState = False, returnreturnIsPreferredByUSPS = False, returnreturnModifiedTime = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnZipCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "get", params_list = params_list)

	return(response)

def deleteZip(ZipID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "delete")

	return(response)