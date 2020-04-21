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