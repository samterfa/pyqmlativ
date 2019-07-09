# This module contains Demographics functions.

from . import make_request

def getACHAccount(ACHAccountID, EntityID = 1, returnAccountType = False, returnAccountTypeCode = False, returnACHAccountNumber = False, returnClass = False, returnClassCode = False, returnCompanyEntryDescription = False, returnCreatedTime = False, returnIsActive = False, returnIsEmployeeChildSupportACH = False, returnIsEmployeeNetPayrollACH = False, returnIsStateDisbursementUnit = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnNameID = False, returnPrenoteDate = False, returnReceivingCompany = False, returnRoutingNumber = False, returnStateIDSDU = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "get", params_list = params_list)

	return(response)

def deleteACHAccount(ACHAccountID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ACHAccount/" + str(ACHAccountID), verb = "delete")

	return(response)

def getAddress(AddressID, EntityID = 1, returnAddressLine2 = False, returnAddressRangeNumericStreetNumber = False, returnAddressRangeNumericStreetNumberIsOdd = False, returnAddressSecondaryUnitID = False, returnAddressType = False, returnAddressTypeCode = False, returnCountyID = False, returnCreatedTime = False, returnFormattedFullAddress = False, returnFreeformAddress = False, returnFullAddress = False, returnInternationalAddress1 = False, returnInternationalAddress2 = False, returnInternationalAddress3 = False, returnInternationalAddress4 = False, returnLatitude = False, returnLongitude = False, returnModifiedTime = False, returnPOBox = False, returnPrintableHTMLAddress = False, returnSecondaryUnitNumber = False, returnStreetID = False, returnStreetNumber = False, returnStreetNumberAndName = False, returnStreetNumberAndNameIncludeSecondaryUnit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCodeAddOn = False, returnZipCodeWithAddon = False, returnZipCodeWithAddonNoHyphen = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "get", params_list = params_list)

	return(response)

def deleteAddress(AddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Address/" + str(AddressID), verb = "delete")

	return(response)

def getAddressRangeDefault(AddressRangeDefaultID, EntityID = 1, returnAddressRangeDefaultIDClonedFrom = False, returnAddressRangeDefaultIDClonedTo = False, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnDistrictID = False, returnFullAddressRange = False, returnIsManual = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSide = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefault(AddressRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefault/" + str(AddressRangeDefaultID), verb = "delete")

	return(response)

def getAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1, returnAddressID = False, returnAddressRangeDefaultID = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultAddress/" + str(AddressRangeDefaultAddressID), verb = "delete")

	return(response)

def getAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1, returnAddressRangeDefaultID = False, returnAddressRangeDefaultSchoolIDClonedFrom = False, returnCreatedTime = False, returnIsOverridenForStudent = False, returnModifiedTime = False, returnOrder = False, returnOverriddenSchoolID = False, returnOverriddenSchoolName = False, returnSchoolID = False, returnStudentHasPermit = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeDefaultSchool/" + str(AddressRangeDefaultSchoolID), verb = "delete")

	return(response)

def getAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1, returnAddressRangeImportSchoolIDClonedFrom = False, returnAddressRangeImportSchoolIDClonedTo = False, returnCreatedTime = False, returnDescription = False, returnImportSchoolCode = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressRangeImportSchool/" + str(AddressRangeImportSchoolID), verb = "delete")

	return(response)

def getAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSchoolPathOverride/" + str(AddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnRequiresNumber = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "get", params_list = params_list)

	return(response)

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/AddressSecondaryUnit/" + str(AddressSecondaryUnitID), verb = "delete")

	return(response)

def getCertification(CertificationID, EntityID = 1, returnCertificationNumber = False, returnCertificationThirdPartyImportID = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnExpirationDate = False, returnInstitutionID = False, returnIssueDate = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "get", params_list = params_list)

	return(response)

def deleteCertification(CertificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Certification/" + str(CertificationID), verb = "delete")

	return(response)

def getCertificationCompetency(CertificationCompetencyID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationCompetency(CertificationCompetencyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationCompetency/" + str(CertificationCompetencyID), verb = "delete")

	return(response)

def getCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1, returnCertificationCompetencyColumnNumber = False, returnCertificationDetailExpirationDateColumnNumber = False, returnCertificationDetailIssueDateColumnNumber = False, returnCertificationLevelColumnNumber = False, returnCertificationNumberColumnNumber = False, returnCertificationSubjectColumnNumber = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeColumnNumber = False, returnCommentColumnNumber = False, returnCreatedTime = False, returnDelimiterCharacter = False, returnDelimiterType = False, returnDelimiterTypeCode = False, returnEmployeeColumnNumber = False, returnExpirationDateColumnNumber = False, returnHighCertificationGradeColumnNumber = False, returnHighlyQualifiedColumnNumber = False, returnInstitutionNameColumnNumber = False, returnIssueDateColumnNumber = False, returnLowCertificationGradeColumnNumber = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateColumnNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDelimitedFileFormat/" + str(CertificationDelimitedFileFormatID), verb = "delete")

	return(response)

def getCertificationDetail(CertificationDetailID, EntityID = 1, returnCertificationCompetencyID = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationID = False, returnCertificationLevelID = False, returnCertificationSubjectID = False, returnCertificationThirdPartyImportID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationDetail(CertificationDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationDetail/" + str(CertificationDetailID), verb = "delete")

	return(response)

def getCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1, returnCertificationCompetencyLength = False, returnCertificationCompetencyStartPosition = False, returnCertificationDetailExpirationDateLength = False, returnCertificationDetailExpirationDateStartPosition = False, returnCertificationDetailIssueDateLength = False, returnCertificationDetailIssueDateStartPosition = False, returnCertificationLevelLength = False, returnCertificationLevelStartPosition = False, returnCertificationNumberLength = False, returnCertificationNumberStartPosition = False, returnCertificationSubjectLength = False, returnCertificationSubjectStartPosition = False, returnCertificationThirdPartyFormatID = False, returnCertificationTypeLength = False, returnCertificationTypeStartPosition = False, returnCommentLength = False, returnCommentStartPosition = False, returnCreatedTime = False, returnEmployeeLength = False, returnEmployeeStartPosition = False, returnExpirationDateLength = False, returnExpirationDateStartPosition = False, returnHighCertificationGradeLength = False, returnHighCertificationGradeStartPosition = False, returnHighlyQualifiedLength = False, returnHighlyQualifiedStartPosition = False, returnInstitutionNameLength = False, returnInstitutionNameStartPosition = False, returnIssueDateLength = False, returnIssueDateStartPosition = False, returnLowCertificationGradeLength = False, returnLowCertificationGradeStartPosition = False, returnModifiedTime = False, returnNumberOfHeaderRows = False, returnSkywardHash = False, returnSkywardID = False, returnStateLength = False, returnStateStartPosition = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationFixedLengthFileFormat/" + str(CertificationFixedLengthFileFormatID), verb = "delete")

	return(response)

def getCertificationGrade(CertificationGradeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationGrade(CertificationGradeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationGrade/" + str(CertificationGradeID), verb = "delete")

	return(response)

def getCertificationLevel(CertificationLevelID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationLevel(CertificationLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationLevel/" + str(CertificationLevelID), verb = "delete")

	return(response)

def getCertificationSubject(CertificationSubjectID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationSubject(CertificationSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationSubject/" + str(CertificationSubjectID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDateFormat = False, returnDateFormatCode = False, returnDescription = False, returnDistrictID = False, returnImportType = False, returnImportTypeCode = False, returnIsSystemLoaded = False, returnModifiedTime = False, returnNameIdentification = False, returnNameIdentificationCode = False, returnSkywardHash = False, returnSkywardID = False, returnSkywardIDClonedFrom = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormat/" + str(CertificationThirdPartyFormatID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1, returnCertificationCompetencyID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + str(CertificationThirdPartyFormatCertificationCompetencyID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1, returnCertificationGradeID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + str(CertificationThirdPartyFormatCertificationGradeID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1, returnCertificationLevelID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + str(CertificationThirdPartyFormatCertificationLevelID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1, returnCertificationSubjectID = False, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + str(CertificationThirdPartyFormatCertificationSubjectID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1, returnCertificationThirdPartyFormatID = False, returnCertificationTypeID = False, returnCreatedTime = False, returnImportValue = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatCertificationType/" + str(CertificationThirdPartyFormatCertificationTypeID), verb = "delete")

	return(response)

def getCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1, returnCertificationThirdPartyFormatID = False, returnCreatedTime = False, returnImportValue = False, returnInstitutionID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyFormatInstitution/" + str(CertificationThirdPartyFormatInstitutionID), verb = "delete")

	return(response)

def getCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1, returnCreatedTime = False, returnImportTime = False, returnMediaID = False, returnMediaIDFailedResult = False, returnModifiedTime = False, returnThirdPartyFormatID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationThirdPartyImport/" + str(CertificationThirdPartyImportID), verb = "delete")

	return(response)

def getCertificationType(CertificationTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnIsCRDCCertified = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteCertificationType(CertificationTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/CertificationType/" + str(CertificationTypeID), verb = "delete")

	return(response)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnAutoAddSchoolPathOverride = False, returnCreatedTime = False, returnDistrictID = False, returnEnforceAddressRangeDefaults = False, returnModifiedTime = False, returnPermitIDAutoAdd = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getConfigSystem(ConfigSystemID, EntityID = 1, returnCreatedTime = False, returnDefaultCaseAddressType = False, returnDefaultCaseAddressTypeCode = False, returnDefaultCaseNameType = False, returnDefaultCaseNameTypeCode = False, returnModifiedTime = False, returnNameNumberLength = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseSyncedNameNumber = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/ConfigSystem/" + str(ConfigSystemID), verb = "delete")

	return(response)

def getCounty(CountyID, EntityID = 1, returnCountyMNID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnStateCountyMNID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "get", params_list = params_list)

	return(response)

def deleteCounty(CountyID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/County/" + str(CountyID), verb = "delete")

	return(response)

def getDependent(DependentID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnNameIDDependent = False, returnNameIDOwner = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "get", params_list = params_list)

	return(response)

def deleteDependent(DependentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Dependent/" + str(DependentID), verb = "delete")

	return(response)

def getDirectional(DirectionalID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "get", params_list = params_list)

	return(response)

def deleteDirectional(DirectionalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Directional/" + str(DirectionalID), verb = "delete")

	return(response)

def getEmailType(EmailTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteEmailType(EmailTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmailType/" + str(EmailTypeID), verb = "delete")

	return(response)

def getEmergencyContact(EmergencyContactID, EntityID = 1, returnAllowPickUp = False, returnComment = False, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "get", params_list = params_list)

	return(response)

def deleteEmergencyContact(EmergencyContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/EmergencyContact/" + str(EmergencyContactID), verb = "delete")

	return(response)

def getEmployer(EmployerID, EntityID = 1, returnACATransmitterControlCode = False, returnCreatedTime = False, returnDistrictID = False, returnEEO4ControlNumber = False, returnEEO4JurisdictionName = False, returnEEO5NameOfCertifyingOfficial = False, returnEEO5OfficeOfSchoolNumber = False, returnEEO5SchoolDistrictName = False, returnEEOCTitleOfCertifyingOfficial = False, returnEmployerMNID = False, returnFederalEEO4FunctionID = False, returnModifiedTime = False, returnNameID = False, returnPERAEmployerNumber = False, returnTRACountyGroupNumber = False, returnTRADistrictUnitNumber = False, returnUnemploymentInsuranceAccountNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "get", params_list = params_list)

	return(response)

def deleteEmployer(EmployerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Employer/" + str(EmployerID), verb = "delete")

	return(response)

def getInstitutionDefault(InstitutionDefaultID, EntityID = 1, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteInstitutionDefault(InstitutionDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/InstitutionDefault/" + str(InstitutionDefaultID), verb = "delete")

	return(response)

def getInstitution(InstitutionID, EntityID = 1, returnCEEBCode = False, returnCreatedTime = False, returnInstitutionDefaultID = False, returnInstitutionMNID = False, returnMCCCCollegeCode = False, returnModifiedTime = False, returnNameID = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "get", params_list = params_list)

	return(response)

def deleteInstitution(InstitutionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Institution/" + str(InstitutionID), verb = "delete")

	return(response)

def getLanguage(LanguageID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnCurrentStateLanguage = False, returnCurrentStateLanguageCode = False, returnCurrentStateLanguageID = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "get", params_list = params_list)

	return(response)

def deleteLanguage(LanguageID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Language/" + str(LanguageID), verb = "delete")

	return(response)

def getLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1, returnCreatedTime = False, returnEdFiLanguageID = False, returnLanguageID = False, returnLanguageSchoolYearIDClonedFrom = False, returnLanguageSchoolYearMNID = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateHeadStartLanguageMNID = False, returnStateLanguageCodeMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "get", params_list = params_list)

	return(response)

def deleteLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LanguageSchoolYear/" + str(LanguageSchoolYearID), verb = "delete")

	return(response)

def getLastNameNumber(LastNameNumberID, EntityID = 1, returnConfigSystemID = False, returnCreatedTime = False, returnModifiedTime = False, returnNameNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteLastNameNumber(LastNameNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/LastNameNumber/" + str(LastNameNumberID), verb = "delete")

	return(response)

def getName(NameID, EntityID = 1, returnAge = False, returnBirthDate = False, returnBirthMonthDay = False, returnBirthYear = False, returnBypassStudentRaceValidation = False, returnCalculatedPrimaryFormattedPhoneNumber = False, returnContactPerson = False, returnConversionKey = False, returnCreatedTime = False, returnDatePhysicalAddressLastChanged = False, returnDriversLicenseNumber = False, returnEthnicity = False, returnEthnicityAndRace = False, returnExternalUniqueIdentifier = False, returnFederalEIN = False, returnFirstInitial = False, returnFirstInitialLastName = False, returnFirstInitialLastNameLegal = False, returnFirstInitialLegal = False, returnFirstName = False, returnFirstNameLegal = False, returnFullNameFL = False, returnFullNameFMIL = False, returnFullNameFML = False, returnFullNameLegalFL = False, returnFullNameLegalFML = False, returnFullNameLegalLFM = False, returnFullNameLF = False, returnFullNameLFM = False, returnGender = False, returnGenderCode = False, returnGetNameUse = False, returnHasMailingOrPhysicalAddress = False, returnInitials = False, returnInitialsLegal = False, returnIsAlaskan = False, returnIsAsian = False, returnIsBlack = False, returnIsBusiness = False, returnIsCurrentStudent = False, returnIsEmergencyContactName = False, returnIsEmployeeName = False, returnIsEmployeeNameForDistrict = False, returnIsEmployeeNameOrInEmployeeFamily = False, returnIsFeeManagementCustomerName = False, returnIsFeeManagementPayorName = False, returnIsFoodServiceCustomerName = False, returnIsFoodServicePayorName = False, returnIsGuardianName = False, returnIsHawaiian = False, returnIsHealthProfessionalName = False, returnIsHispanic = False, returnIsInstitution = False, returnIsPayorName = False, returnIsPayorNameForDistrict = False, returnIsPlaceOfEmployment = False, returnIsSingleLegalName = False, returnIsSkyward = False, returnIsStaffName = False, returnIsStudentInDistrict = False, returnIsStudentName = False, returnIsUserName = False, returnIsVendorName = False, returnIsVendorNameForDistrict = False, returnIsWhite = False, returnLastInitial = False, returnLastInitialLegal = False, returnLastName = False, returnLastNameFirstInitial = False, returnLastNameLegal = False, returnMaritalStatus = False, returnMaritalStatusCode = False, returnMaskedSocialSecurityNumber = False, returnMediaIDPhoto = False, returnMiddleInitial = False, returnMiddleInitialLegal = False, returnMiddleName = False, returnMiddleNameLegal = False, returnModifiedTime = False, returnNameAddressMailingID = False, returnNameIDPlaceOfEmployment = False, returnNameKey = False, returnNameNumber = False, returnNameSuffixID = False, returnNameSuffixIDLegal = False, returnNameTitleID = False, returnNameTitleIDLegal = False, returnOccupationID = False, returnRace = False, returnRaceEduphoriaCode = False, returnRaceVerifiedBy = False, returnRaceVerifiedByCode = False, returnRaceVerifiedDate = False, returnSkywardHash = False, returnSkywardID = False, returnSocialSecurityNumber = False, returnSpecifySeparateLegalName = False, returnTitledName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "get", params_list = params_list)

	return(response)

def deleteName(NameID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Name/" + str(NameID), verb = "delete")

	return(response)

def getNameAddress(NameAddressID, EntityID = 1, returnAddressID = False, returnCreatedTime = False, returnGetAddressType = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsPrimaryGuardian = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteNameAddress(NameAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAddress/" + str(NameAddressID), verb = "delete")

	return(response)

def getNameAlias(NameAliasID, EntityID = 1, returnCreatedTime = False, returnEffectiveDate = False, returnFirstName = False, returnFullNameFL = False, returnFullNameLF = False, returnIsBusiness = False, returnIsLegalName = False, returnIsMaidenName = False, returnIsSingleLegalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameTitleID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "get", params_list = params_list)

	return(response)

def deleteNameAlias(NameAliasID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameAlias/" + str(NameAliasID), verb = "delete")

	return(response)

def getNameEmail(NameEmailID, EntityID = 1, returnCreatedTime = False, returnEmailAddress = False, returnEmailTypeID = False, returnIsAccountsPayableDirectDepositNotificationEmail = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "get", params_list = params_list)

	return(response)

def deleteNameEmail(NameEmailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEmail/" + str(NameEmailID), verb = "delete")

	return(response)

def getNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1, returnCreatedTime = False, returnEthnicityRaceType = False, returnEthnicityRaceTypeCode = False, returnModifiedTime = False, returnNameID = False, returnStateEthnicityRaceSubcategoryMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "get", params_list = params_list)

	return(response)

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameEthnicityRaceSubcategoryMN/" + str(NameEthnicityRaceSubcategoryMNID), verb = "delete")

	return(response)

def getNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1, returnBirthDateFrom = False, returnBirthDateTo = False, returnCreatedTime = False, returnFullNameLFMFrom = False, returnFullNameLFMTo = False, returnModifiedTime = False, returnNameIDFrom = False, returnNameIDTo = False, returnNameUsedByFrom = False, returnNameUsedByTo = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameMergeRunHistory/" + str(NameMergeRunHistoryID), verb = "delete")

	return(response)

def getNamePhone(NamePhoneID, EntityID = 1, returnCreatedTime = False, returnExtension = False, returnFormattedPhoneNumber = False, returnFormattedPhoneNumberCodeEEL = False, returnFullPhoneNumber = False, returnIsConfidential = False, returnIsFax = False, returnIsInternational = False, returnIsPrimaryFax = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnPhoneNumber = False, returnPhoneTypeID = False, returnRank = False, returnUsedByHealthProfessional = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "get", params_list = params_list)

	return(response)

def deleteNamePhone(NamePhoneID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NamePhone/" + str(NamePhoneID), verb = "delete")

	return(response)

def getNameSuffix(NameSuffixID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "get", params_list = params_list)

	return(response)

def deleteNameSuffix(NameSuffixID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameSuffix/" + str(NameSuffixID), verb = "delete")

	return(response)

def getNameTitle(NameTitleID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "get", params_list = params_list)

	return(response)

def deleteNameTitle(NameTitleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameTitle/" + str(NameTitleID), verb = "delete")

	return(response)

def getNameVehicle(NameVehicleID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "get", params_list = params_list)

	return(response)

def deleteNameVehicle(NameVehicleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameVehicle/" + str(NameVehicleID), verb = "delete")

	return(response)

def getNameWebsite(NameWebsiteID, EntityID = 1, returnCreatedTime = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnRank = False, returnURL = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "get", params_list = params_list)

	return(response)

def deleteNameWebsite(NameWebsiteID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/NameWebsite/" + str(NameWebsiteID), verb = "delete")

	return(response)

def getOccupation(OccupationID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "get", params_list = params_list)

	return(response)

def deleteOccupation(OccupationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Occupation/" + str(OccupationID), verb = "delete")

	return(response)

def getPhoneType(PhoneTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnPreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "get", params_list = params_list)

	return(response)

def deletePhoneType(PhoneTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/PhoneType/" + str(PhoneTypeID), verb = "delete")

	return(response)

def getRelationship(RelationshipID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnEdFiRelationTypeID = False, returnModifiedTime = False, returnRelationshipType = False, returnRelationshipTypeCode = False, returnShortenedDescription = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "get", params_list = params_list)

	return(response)

def deleteRelationship(RelationshipID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Relationship/" + str(RelationshipID), verb = "delete")

	return(response)

def getStreet(StreetID, EntityID = 1, returnCreatedTime = False, returnDirectionalID = False, returnFormattedStreet = False, returnModifiedTime = False, returnName = False, returnStreetNameWithDirectionCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "get", params_list = params_list)

	return(response)

def deleteStreet(StreetID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Street/" + str(StreetID), verb = "delete")

	return(response)

def getTempACHAccount(TempACHAccountID, EntityID = 1, returnAccountType = False, returnACHAccountID = False, returnACHAccountNumber = False, returnCreatedTime = False, returnIsEmployeeNetPayrollACH = False, returnIsVendorAccountsPayableACH = False, returnModifiedTime = False, returnName = False, returnRoutingNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUseTaxAddenda = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "get", params_list = params_list)

	return(response)

def deleteTempACHAccount(TempACHAccountID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempACHAccount/" + str(TempACHAccountID), verb = "delete")

	return(response)

def getTempAddress(TempAddressID, EntityID = 1, returnAddressID = False, returnAddressUsedBy = False, returnCreatedTime = False, returnCurrentFormattedFullAddress = False, returnFieldPathsToUpdate = False, returnFieldsToUpdate = False, returnModifiedTime = False, returnNewFormattedFullAddress = False, returnSelected = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowErrors = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddress(TempAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddress/" + str(TempAddressID), verb = "delete")

	return(response)

def getTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1, returnCity = False, returnCreatedTime = False, returnDefaultSchools = False, returnException = False, returnModifiedTime = False, returnStateAbbreviation = False, returnStreetDirection = False, returnStreetName = False, returnStreetNumberHigh = False, returnStreetNumberLow = False, returnStreetSideCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnZipCodeAddOn = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressRangeDefault/" + str(TempAddressRangeDefaultID), verb = "delete")

	return(response)

def getTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1, returnCreatedTime = False, returnExceptionNote = False, returnHasExceptions = False, returnModifiedTime = False, returnOrder = False, returnSchoolCodeName = False, returnSchoolID = False, returnSchoolIDClonedTo = False, returnStudentID = False, returnStudentName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempAddressSchoolPathOverride/" + str(TempAddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getTempCertification(TempCertificationID, EntityID = 1, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeCode = False, returnCertificationTypeCodeDescription = False, returnCertificationTypeID = False, returnComment = False, returnCreatedTime = False, returnErrorCount = False, returnExpirationDate = False, returnFullNameLFM = False, returnHasErrors = False, returnInstitutionID = False, returnInstitutionName = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnNameID = False, returnStateDisplayName = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertification(TempCertificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertification/" + str(TempCertificationID), verb = "delete")

	return(response)

def getTempCertificationDetail(TempCertificationDetailID, EntityID = 1, returnCertificationCompetencyCode = False, returnCertificationCompetencyID = False, returnCertificationGradeHighCodeDescription = False, returnCertificationGradeIDHigh = False, returnCertificationGradeIDLow = False, returnCertificationGradeLowCodeDescription = False, returnCertificationID = False, returnCertificationLevelCode = False, returnCertificationLevelID = False, returnCertificationSubjectCode = False, returnCertificationSubjectID = False, returnCreatedTime = False, returnExpirationDate = False, returnIsHighlyQualified = False, returnIssueDate = False, returnLineNumber = False, returnModifiedTime = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertificationDetail(TempCertificationDetailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationDetail/" + str(TempCertificationDetailID), verb = "delete")

	return(response)

def getTempCertificationError(TempCertificationErrorID, EntityID = 1, returnCertificationID = False, returnCreatedTime = False, returnError = False, returnErrorDetail = False, returnLineNumber = False, returnModifiedTime = False, returnNameLFM = False, returnTempCertificationID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertificationError(TempCertificationErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempCertificationError/" + str(TempCertificationErrorID), verb = "delete")

	return(response)

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnAllowPickUp = False, returnCreatedTime = False, returnEmergencyContactFor = False, returnEmergencyContactName = False, returnExceptionNote = False, returnHasActiveRestrictedAccess = False, returnHasExceptions = False, returnModifiedTime = False, returnNameID = False, returnNameIDEmergencyContact = False, returnRank = False, returnRelationshipDescription = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "delete")

	return(response)

def getTempException(TempExceptionID, EntityID = 1, returnCreatedTime = False, returnLineNumber = False, returnMessage = False, returnModifiedTime = False, returnNameLFM = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempException(TempExceptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempException/" + str(TempExceptionID), verb = "delete")

	return(response)

def getTempNameAddress(TempNameAddressID, EntityID = 1, returnAddressID = False, returnCreatedTime = False, returnFullAddress = False, returnIs1099 = False, returnIsBusDropoff = False, returnIsBusPickup = False, returnIsMailing = False, returnIsOrderFrom = False, returnIsPhysical = False, returnIsRemitTo = False, returnIsW2 = False, returnModifiedTime = False, returnNameID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameAddress(TempNameAddressID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddress/" + str(TempNameAddressID), verb = "delete")

	return(response)

def getTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1, returnAddressSchoolPathOverrideID = False, returnCreatedTime = False, returnIsCreateOverride = False, returnIsOverrideExists = False, returnIsRemoveOverride = False, returnIsRemovePermit = False, returnIsUpdateOverride = False, returnModifiedTime = False, returnOrder = False, returnSchoolID = False, returnSchoolNameOverriddingTo = False, returnSchoolNameToOverride = False, returnSchoolYearDescription = False, returnStudentFullNameLFM = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + str(TempNameAddressMoveAddressSchoolPathOverrideID), verb = "delete")

	return(response)

def getTempNameError(TempNameErrorID, EntityID = 1, returnCreatedTime = False, returnFirstName = False, returnLastName = False, returnModifiedTime = False, returnNameID = False, returnNote = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameError(TempNameErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameError/" + str(TempNameErrorID), verb = "delete")

	return(response)

def getTempNameNumber(TempNameNumberID, EntityID = 1, returnConflictReason = False, returnCreatedTime = False, returnEmployeeID = False, returnFullNameLFM = False, returnHasConflicts = False, returnModifiedTime = False, returnNameID = False, returnNameNumber = False, returnNewEmployeeNumber = False, returnNewVendorNumber = False, returnOldEmployeeNumber = False, returnOldVendorNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVendorID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNameNumber(TempNameNumberID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/TempNameNumber/" + str(TempNameNumberID), verb = "delete")

	return(response)

def getVehicle(VehicleID, EntityID = 1, returnColor = False, returnCreatedTime = False, returnLicensePlateNumber = False, returnMakeModel = False, returnModifiedTime = False, returnPermitDate = False, returnPermitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "get", params_list = params_list)

	return(response)

def deleteVehicle(VehicleID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Vehicle/" + str(VehicleID), verb = "delete")

	return(response)

def getZip(ZipID, EntityID = 1, returnCity = False, returnCityState = False, returnCityStateCode = False, returnCityStateZip = False, returnCityZipCode = False, returnCountryCode = False, returnCreatedTime = False, returnFreeFormCountry = False, returnFreeFormState = False, returnIsPreferredByUSPS = False, returnModifiedTime = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "get", params_list = params_list)

	return(response)

def deleteZip(ZipID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Demographics/Zip/" + str(ZipID), verb = "delete")

	return(response)