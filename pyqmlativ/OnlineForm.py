# This module contains OnlineForm functions.

from .Utilities import *

import pandas as pd

import json

import re


def getEveryElement(searchConditions = [], EntityID = 1, returnElementID = False, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnGUIDFieldPath = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentRelationshipRequired = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRelationshipRequiredOnFamilyInformation = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Element in the district.

	This function returns a dataframe of every Element in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElementGroup(searchConditions = [], EntityID = 1, returnElementGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElementGroup in the district.

	This function returns a dataframe of every ElementGroup in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElementGroupTemplate(searchConditions = [], EntityID = 1, returnElementGroupTemplateID = False, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElementGroupTemplate in the district.

	This function returns a dataframe of every ElementGroupTemplate in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElementStatus(searchConditions = [], EntityID = 1, returnElementStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElementStatus in the district.

	This function returns a dataframe of every ElementStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryElementStatusSurveyAnswer(searchConditions = [], EntityID = 1, returnElementStatusSurveyAnswerID = False, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every ElementStatusSurveyAnswer in the district.

	This function returns a dataframe of every ElementStatusSurveyAnswer in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryMassPrintHistory(searchConditions = [], EntityID = 1, returnMassPrintHistoryID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every MassPrintHistory in the district.

	This function returns a dataframe of every MassPrintHistory in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNewStudentEnrollmentGuardianData(searchConditions = [], EntityID = 1, returnNewStudentEnrollmentGuardianDataID = False, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NewStudentEnrollmentGuardianData in the district.

	This function returns a dataframe of every NewStudentEnrollmentGuardianData in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryNewStudentEnrollmentUserData(searchConditions = [], EntityID = 1, returnNewStudentEnrollmentUserDataID = False, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every NewStudentEnrollmentUserData in the district.

	This function returns a dataframe of every NewStudentEnrollmentUserData in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineForm(searchConditions = [], EntityID = 1, returnOnlineFormID = False, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnThankYouPageLinkFullFilename = False, returnThankYouPageLinkProtocol = False, returnThankYouPageLinkProtocolCode = False, returnThankYouPageLinkUrl = False, returnThankYouPageLinkUrlDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineForm in the district.

	This function returns a dataframe of every OnlineForm in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormClearance(searchConditions = [], EntityID = 1, returnOnlineFormClearanceID = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormClearance in the district.

	This function returns a dataframe of every OnlineFormClearance in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormDateException(searchConditions = [], EntityID = 1, returnOnlineFormDateExceptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormDateException in the district.

	This function returns a dataframe of every OnlineFormDateException in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormEntity(searchConditions = [], EntityID = 1, returnOnlineFormEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormEntity in the district.

	This function returns a dataframe of every OnlineFormEntity in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormStatus(searchConditions = [], EntityID = 1, returnOnlineFormStatusID = False, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnIsOutsideAddressRangeSchoolPaths = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormStatus in the district.

	This function returns a dataframe of every OnlineFormStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormStatusName(searchConditions = [], EntityID = 1, returnOnlineFormStatusNameID = False, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormStatusName in the district.

	This function returns a dataframe of every OnlineFormStatusName in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryOnlineFormType(searchConditions = [], EntityID = 1, returnOnlineFormTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every OnlineFormType in the district.

	This function returns a dataframe of every OnlineFormType in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEverySharedElementStatus(searchConditions = [], EntityID = 1, returnSharedElementStatusID = False, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every SharedElementStatus in the district.

	This function returns a dataframe of every SharedElementStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStaffContact(searchConditions = [], EntityID = 1, returnStaffContactID = False, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StaffContact in the district.

	This function returns a dataframe of every StaffContact in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStep(searchConditions = [], EntityID = 1, returnStepID = False, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every Step in the district.

	This function returns a dataframe of every Step in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryStepStatus(searchConditions = [], EntityID = 1, returnStepStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every StepStatus in the district.

	This function returns a dataframe of every StepStatus in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTeacherOnlineForm(searchConditions = [], EntityID = 1, returnOnlineFormEntityID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TeacherOnlineForm in the district.

	This function returns a dataframe of every TeacherOnlineForm in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempCertification(searchConditions = [], EntityID = 1, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDataGridRow(searchConditions = [], EntityID = 1, returnTempDataGridRowID = False, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDataGridRow in the district.

	This function returns a dataframe of every TempDataGridRow in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDegree(searchConditions = [], EntityID = 1, returnTempDegreeID = False, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDegree in the district.

	This function returns a dataframe of every TempDegree in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempDependent(searchConditions = [], EntityID = 1, returnTempDependentID = False, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempDependent in the district.

	This function returns a dataframe of every TempDependent in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempEmergencyContact(searchConditions = [], EntityID = 1, returnTempEmergencyContactID = False, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

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

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempError(searchConditions = [], EntityID = 1, returnTempErrorID = False, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempError in the district.

	This function returns a dataframe of every TempError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNewStudentEnrollmentGuardianEmail(searchConditions = [], EntityID = 1, returnTempNewStudentEnrollmentGuardianEmailID = False, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNewStudentEnrollmentGuardianEmail in the district.

	This function returns a dataframe of every TempNewStudentEnrollmentGuardianEmail in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempNewStudentEnrollmentGuardianPhone(searchConditions = [], EntityID = 1, returnTempNewStudentEnrollmentGuardianPhoneID = False, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempNewStudentEnrollmentGuardianPhone in the district.

	This function returns a dataframe of every TempNewStudentEnrollmentGuardianPhone in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStep(searchConditions = [], EntityID = 1, returnTempStepID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorCount = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStep in the district.

	This function returns a dataframe of every TempStep in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStepError(searchConditions = [], EntityID = 1, returnTempStepErrorID = False, returnCreatedTime = False, returnError = False, returnErrorMessage = False, returnModifiedTime = False, returnTempStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStepError in the district.

	This function returns a dataframe of every TempStepError in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)


def getEveryTempStudentHealthCondition(searchConditions = [], EntityID = 1, returnTempStudentHealthConditionID = False, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, page = 1, pageSize = 100000, conditionGroupType = "And"):

	"""Get every TempStudentHealthCondition in the district.

	This function returns a dataframe of every TempStudentHealthCondition in the district filtered by search conditions.

	"""

	params = locals()

	params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

	return_params = params.query('Param.str.startswith("return")', engine = 'python')

	if not any(return_params.Value):
		return_params = list(return_params.assign(Value = True).Param)
	else:
		return_params = list(return_params.query('Value == True').Param)

	return_params = [re.sub("^return", '', param) for param in return_params]

	if len(searchConditions) > 0:

		searchConditions = params.query('Param == "searchConditions"').Value[0]

		payload_params = formatSearchConditionsPayload(searchConditions, conditionGroupType)

		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "post", return_params_list = return_params, payload = payload_params)

	else:
		return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params)