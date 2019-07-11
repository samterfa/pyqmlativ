# This module contains OnlineForm functions.

from .Utilities import make_request

import pandas as pd

def getEveryElement(EntityID = 1, page = 1, pageSize = 100, returnElementID = True, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getElement(ElementID, EntityID = 1, returnreturnElementID = False, returnreturnAdminCanEdit = False, returnreturnAgreementMessage = False, returnreturnAllowsUserInteraction = False, returnreturnApprovalType = False, returnreturnApprovalTypeCode = False, returnreturnCodeListFieldName = False, returnreturnCodeListFieldPath = False, returnreturnCodeListType = False, returnreturnCodeListTypeCode = False, returnreturnCodeListTypeLabel = False, returnreturnComboboxDefaultValue = False, returnreturnComboboxTextValue = False, returnreturnCommonColorPickerValue = False, returnreturnCommonFontAlignmentValue = False, returnreturnCommonTextValue = False, returnreturnCommonType = False, returnreturnCommonTypeCode = False, returnreturnCoverageEndDate = False, returnreturnCoverageStartDate = False, returnreturnCreatedTime = False, returnreturnDataGridXML = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnElementGroupID = False, returnreturnEmbeddedLinkFullFilename = False, returnreturnEmbeddedLinkProtocol = False, returnreturnEmbeddedLinkProtocolCode = False, returnreturnEmbeddedLinkURL = False, returnreturnEmergencyContact = False, returnreturnFieldDisplayName = False, returnreturnFieldGroup = False, returnreturnFieldGroupCode = False, returnreturnFieldID = False, returnreturnFieldIsRelationship = False, returnreturnFieldLabel = False, returnreturnFieldName = False, returnreturnFieldPath = False, returnreturnFieldRelationship = False, returnreturnHasBackingObject = False, returnreturnHasSharedValue = False, returnreturnHealthConditionIDs = False, returnreturnHealthProviderExcludeDentalInsurance = False, returnreturnHealthProviderExcludeDentist = False, returnreturnHealthProviderExcludeDentistOffice = False, returnreturnHealthProviderExcludeEmail = False, returnreturnHealthProviderExcludeHealthInsurance = False, returnreturnHealthProviderExcludeHospital = False, returnreturnHealthProviderExcludePhone = False, returnreturnHealthProviderExcludePrimaryPhysician = False, returnreturnHtmlDescription = False, returnreturnHtmlLabel = False, returnreturnHtmlOptions = False, returnreturnIncludeCECSInStudentSelector = False, returnreturnIsNewStudentEnrollmentElement = False, returnreturnIsRequiredElement = False, returnreturnLabelOverrides = False, returnreturnLanguageOption = False, returnreturnLanguageOptionCode = False, returnreturnLinkProtocol = False, returnreturnLinkProtocolCode = False, returnreturnMaxNumberEmergencyContacts = False, returnreturnMaxUploadFileSize = False, returnreturnMaxUploadFileSizeUnit = False, returnreturnMaxUploadFileSizeUnitCode = False, returnreturnMediaID = False, returnreturnMergeMarkupSet = False, returnreturnMergeMarkupSetDescription = False, returnreturnMergeMarkupSetLabel = False, returnreturnModifiedTime = False, returnreturnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnreturnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnreturnNewStudentEnrollmentShowCustodialInformation = False, returnreturnNewStudentEnrollmentUseAddSecondFamily = False, returnreturnOrder = False, returnreturnParameterData = False, returnreturnParameters = False, returnreturnPaymentEndDate = False, returnreturnPaymentStartDate = False, returnreturnPlanID = False, returnreturnPostfixText = False, returnreturnPrefixText = False, returnreturnRaceEthnicityMessage = False, returnreturnRaceEthnicityMessageInSpanish = False, returnreturnRenderAgreement = False, returnreturnRenderInstructions = False, returnreturnRenderLanguageOptions = False, returnreturnRenderWeight = False, returnreturnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnreturnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnreturnSharedValueUsesNotShared = False, returnreturnShowCustodialOnFamilyInformation = False, returnreturnShowVehicleInformationOnEmergencyContact = False, returnreturnShowVehicleOnFamilyInformation = False, returnreturnStepID = False, returnreturnSupportsLabelOverrides = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUploadType = False, returnreturnUploadTypeCode = False, returnreturnUrl = False, returnreturnUrlDisplayName = False, returnreturnUserDownloadDisplayText = False, returnreturnUserDownloadInstructions = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserUploadDescription = False, returnreturnUserUploadLabel = False, returnreturnValidUploadFileTypes = False, returnreturnYesNoResponse = False, returnreturnYesNoResponseCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "get", params_list = params_list)

	return(response)

def deleteElement(ElementID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "delete")

	return(response)

def getEveryElementGroup(EntityID = 1, page = 1, pageSize = 100, returnElementGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getElementGroup(ElementGroupID, EntityID = 1, returnreturnElementGroupID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnSkywardID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "get", params_list = params_list)

	return(response)

def deleteElementGroup(ElementGroupID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "delete")

	return(response)

def getEveryElementGroupTemplate(EntityID = 1, page = 1, pageSize = 100, returnElementGroupTemplateID = True, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getElementGroupTemplate(ElementGroupTemplateID, EntityID = 1, returnreturnElementGroupTemplateID = False, returnreturnCreatedTime = False, returnreturnElementGroupID = False, returnreturnModifiedTime = False, returnreturnOrder = False, returnreturnParameterData = False, returnreturnSkywardID = False, returnreturnType = False, returnreturnTypeCode = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "get", params_list = params_list)

	return(response)

def deleteElementGroupTemplate(ElementGroupTemplateID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "delete")

	return(response)

def getEveryElementStatus(EntityID = 1, page = 1, pageSize = 100, returnElementStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getElementStatus(ElementStatusID, EntityID = 1, returnreturnElementStatusID = False, returnreturnCreatedTime = False, returnreturnDenialMessage = False, returnreturnElementID = False, returnreturnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnreturnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnreturnIsReadOnly = False, returnreturnMediaIDAttachment = False, returnreturnModifiedTime = False, returnreturnNeedsAdminReviewSave = False, returnreturnOriginalValue = False, returnreturnReportDataOriginalValue = False, returnreturnReportDataRequestedValue = False, returnreturnRequestedValue = False, returnreturnSharedElementStatusID = False, returnreturnStatusType = False, returnreturnStatusTypeCode = False, returnreturnStepStatusID = False, returnreturnUserIDApprover = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserSubmitted = False, returnreturnValidationMessage = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "get", params_list = params_list)

	return(response)

def deleteElementStatus(ElementStatusID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "delete")

	return(response)

def getEveryElementStatusSurveyAnswer(EntityID = 1, page = 1, pageSize = 100, returnElementStatusSurveyAnswerID = True, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1, returnreturnElementStatusSurveyAnswerID = False, returnreturnColumnName = False, returnreturnCreatedTime = False, returnreturnElementStatusID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnOnlineFormID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "get", params_list = params_list)

	return(response)

def deleteElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "delete")

	return(response)

def getEveryMassPrintHistory(EntityID = 1, page = 1, pageSize = 100, returnMassPrintHistoryID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getMassPrintHistory(MassPrintHistoryID, EntityID = 1, returnreturnMassPrintHistoryID = False, returnreturnCreatedTime = False, returnreturnMediaID = False, returnreturnModifiedTime = False, returnreturnOnlineFormID = False, returnreturnRequestIdentifier = False, returnreturnSendMessageOnComplete = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWorkflowInstanceID = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "get", params_list = params_list)

	return(response)

def deleteMassPrintHistory(MassPrintHistoryID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "delete")

	return(response)

def getEveryNewStudentEnrollmentGuardianData(EntityID = 1, page = 1, pageSize = 100, returnNewStudentEnrollmentGuardianDataID = True, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1, returnreturnNewStudentEnrollmentGuardianDataID = False, returnreturnAddGuardian = False, returnreturnAllowStudentPickup = False, returnreturnColor = False, returnreturnCreatedTime = False, returnreturnCreateNewGuardian = False, returnreturnDeleteGuardian = False, returnreturnDriversLicenseNumber = False, returnreturnFamilyGuardianID = False, returnreturnFirstName = False, returnreturnGender = False, returnreturnGenderCode = False, returnreturnIsCustodialGuardian = False, returnreturnLastName = False, returnreturnLicensePlateNumber = False, returnreturnMakeModel = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNameSuffixID = False, returnreturnNameVehicleID = False, returnreturnOnScreenID = False, returnreturnRank = False, returnreturnRelationshipID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnVehicleID = False, returnreturnVIN = False, returnreturnYear = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "get", params_list = params_list)

	return(response)

def deleteNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "delete")

	return(response)

def getEveryNewStudentEnrollmentUserData(EntityID = 1, page = 1, pageSize = 100, returnNewStudentEnrollmentUserDataID = True, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1, returnreturnNewStudentEnrollmentUserDataID = False, returnreturnCity = False, returnreturnCreatedTime = False, returnreturnEmailAddress = False, returnreturnModifiedTime = False, returnreturnPhoneNumber = False, returnreturnPhysicalStreetName = False, returnreturnPhysicalStreetNumber = False, returnreturnPreviouslyInDistrict = False, returnreturnState = False, returnreturnUnit = False, returnreturnUnitNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDSubmittedBy = False, returnreturnZipCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "get", params_list = params_list)

	return(response)

def deleteNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "delete")

	return(response)

def getEveryOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormID = True, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineForm(OnlineFormID, EntityID = 1, returnreturnOnlineFormID = False, returnreturnActivitiesSearchConditionFilter = False, returnreturnAdministrativeSearchConditionFilter = False, returnreturnAllowContact = False, returnreturnAllowMultipleFormsPerUser = False, returnreturnContactHash = False, returnreturnCreatedTime = False, returnreturnCutoffTime = False, returnreturnDescription = False, returnreturnDisplayForNonPrimaryFamily = False, returnreturnEmployeeSearchConditionFilter = False, returnreturnEmployeeStandardFilterCollectionJson = False, returnreturnEndDate = False, returnreturnFamilySearchConditionFilter = False, returnreturnFilter = False, returnreturnFilterSubType = False, returnreturnFilterSubTypeCode = False, returnreturnHideCurrentValueOnApproval = False, returnreturnIconCode = False, returnreturnIncludeAdobeAcrobatLink = False, returnreturnIncludeInActivitiesPortal = False, returnreturnIncludeInAdministrativePortal = False, returnreturnIncludeInEmployeePortal = False, returnreturnIncludeInFamilyPortal = False, returnreturnIncludeInNewStudentEnrollmentPortal = False, returnreturnIncludeInStudentPortal = False, returnreturnIncludeInTeacherPortal = False, returnreturnInUseByUsers = False, returnreturnIsPublished = False, returnreturnIsUserInitiated = False, returnreturnLimitToOnePerDay = False, returnreturnMainPageEmbeddedLinkFullFilename = False, returnreturnMainPageEmbeddedLinkProtocol = False, returnreturnMainPageEmbeddedLinkProtocolCode = False, returnreturnMainPageEmbeddedLinkUrl = False, returnreturnMessage = False, returnreturnMessageAfterSubmission = False, returnreturnMessageForNonPrimaryFamily = False, returnreturnModifiedTime = False, returnreturnModule = False, returnreturnName = False, returnreturnNewStudentEnrollmentSearchConditionFilter = False, returnreturnNoApprovalNeeded = False, returnreturnObject = False, returnreturnOnlineFormIDClonedFrom = False, returnreturnOnlineFormStatusExistsToday = False, returnreturnOnlineFormTypeID = False, returnreturnPortals = False, returnreturnPortalsIncludedIn = False, returnreturnPortalType = False, returnreturnPortalTypeCode = False, returnreturnReviewStepMessage = False, returnreturnSchoolYearID = False, returnreturnSendFamilyAccessEmail = False, returnreturnShowDescriptionOnTile = False, returnreturnSkipInstructionsPage = False, returnreturnSkipReviewPage = False, returnreturnSkipThankYouPage = False, returnreturnStartDate = False, returnreturnStudentSearchConditionFilter = False, returnreturnTeacherSearchConditionFilter = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnWithinCutoffTime = False, returnreturnYearType = False, returnreturnYearTypeCode = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineForm(OnlineFormID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "delete")

	return(response)

def getEveryOnlineFormClearance(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormClearanceID = True, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormClearance(OnlineFormClearanceID, EntityID = 1, returnreturnOnlineFormClearanceID = False, returnreturnCreatedTime = False, returnreturnGroupIDSecurity = False, returnreturnModifiedTime = False, returnreturnOnlineFormID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormClearance(OnlineFormClearanceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "delete")

	return(response)

def getEveryOnlineFormDateException(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormDateExceptionID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1, returnreturnOnlineFormDateExceptionID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnObjectID = False, returnreturnObjectPrimaryKey = False, returnreturnOnlineFormID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "delete")

	return(response)

def getEveryOnlineFormEntity(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormEntity(OnlineFormEntityID, EntityID = 1, returnreturnOnlineFormEntityID = False, returnreturnCreatedTime = False, returnreturnEntityID = False, returnreturnModifiedTime = False, returnreturnOnlineFormID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormEntity(OnlineFormEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "delete")

	return(response)

def getEveryOnlineFormStatus(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormStatusID = True, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormStatus(OnlineFormStatusID, EntityID = 1, returnreturnOnlineFormStatusID = False, returnreturnApprovalRevoked = False, returnreturnCompletedByAdmin = False, returnreturnCreatedTime = False, returnreturnDenialDateTime = False, returnreturnDenialMessage = False, returnreturnFullNameLFMSubmittedFor = False, returnreturnFullNameLFMSubmittedForOverride = False, returnreturnIsOutsideAddressRanges = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnOnlineFormEntityID = False, returnreturnSecondaryID = False, returnreturnStatusType = False, returnreturnStatusTypeCode = False, returnreturnSubmittedDateTime = False, returnreturnUserIDApprover = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnUserIDSubmittedBy = False, returnreturnWithinCutoffTime = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormStatus(OnlineFormStatusID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "delete")

	return(response)

def getEveryOnlineFormStatusName(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormStatusNameID = True, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1, returnreturnOnlineFormStatusNameID = False, returnreturnCreatedTime = False, returnreturnElementID = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnOnlineFormStatusID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "delete")

	return(response)

def getEveryOnlineFormType(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getOnlineFormType(OnlineFormTypeID, EntityID = 1, returnreturnOnlineFormTypeID = False, returnreturnCode = False, returnreturnCodeDescription = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnDistrictID = False, returnreturnLimitUsersToOneFormOfThisTypePerYear = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteOnlineFormType(OnlineFormTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "delete")

	return(response)

def getEverySharedElementStatus(EntityID = 1, page = 1, pageSize = 100, returnSharedElementStatusID = True, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getSharedElementStatus(SharedElementStatusID, EntityID = 1, returnreturnSharedElementStatusID = False, returnreturnCreatedTime = False, returnreturnElementType = False, returnreturnElementTypeCode = False, returnreturnFieldGroupType = False, returnreturnFieldGroupTypeCode = False, returnreturnMediaIDAttachment = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnSchoolYearID = False, returnreturnSecondaryID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValue = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "get", params_list = params_list)

	return(response)

def deleteSharedElementStatus(SharedElementStatusID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "delete")

	return(response)

def getEveryStaffContact(EntityID = 1, page = 1, pageSize = 100, returnStaffContactID = True, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStaffContact(StaffContactID, EntityID = 1, returnreturnStaffContactID = False, returnreturnCreatedTime = False, returnreturnModifiedTime = False, returnreturnOnlineFormID = False, returnreturnStaffID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "get", params_list = params_list)

	return(response)

def deleteStaffContact(StaffContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "delete")

	return(response)

def getEveryStep(EntityID = 1, page = 1, pageSize = 100, returnStepID = True, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStep(StepID, EntityID = 1, returnreturnStepID = False, returnreturnCreatedTime = False, returnreturnIsActive = False, returnreturnIsReadOnlyForNonPrimaryFamily = False, returnreturnIsRequired = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnOnlineFormID = False, returnreturnOrder = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "get", params_list = params_list)

	return(response)

def deleteStep(StepID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "delete")

	return(response)

def getEveryStepStatus(EntityID = 1, page = 1, pageSize = 100, returnStepStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getStepStatus(StepStatusID, EntityID = 1, returnreturnStepStatusID = False, returnreturnCreatedTime = False, returnreturnDenialMessage = False, returnreturnHasNextStepStatus = False, returnreturnHasPreviousStepStatus = False, returnreturnModifiedTime = False, returnreturnNextStepStatusID = False, returnreturnOnlineFormStatusID = False, returnreturnPreviousStepStatusID = False, returnreturnStatusType = False, returnreturnStatusTypeCode = False, returnreturnStepID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnValidationMessage = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "get", params_list = params_list)

	return(response)

def deleteStepStatus(StepStatusID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "delete")

	return(response)

def getEveryTeacherOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormEntityID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTeacherOnlineForm(OnlineFormEntityID, EntityID = 1, returnreturnOnlineFormEntityID = False, returnreturnCreatedTime = False, returnreturnDisplayPeriodID = False, returnreturnEntityID = False, returnreturnFilterInformation = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnNoFormsExistOfSameType = False, returnreturnNoStartedFormsExist = False, returnreturnOnlineFormID = False, returnreturnOnlineFormStatusExistsToday = False, returnreturnOnlineFormStatusID = False, returnreturnOnlineFormTypeID = False, returnreturnSchoolYearID = False, returnreturnSecondaryID = False, returnreturnSectionID = False, returnreturnStatusType = False, returnreturnStatusTypeCode = False, returnreturnStatusTypeSortable = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "get", params_list = params_list)

	return(response)

def deleteTeacherOnlineForm(OnlineFormEntityID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "delete")

	return(response)

def getEveryTempCertification(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempCertification(TempCertificationID, EntityID = 1, returnreturnTempCertificationID = False, returnreturnCertificationID = False, returnreturnCertificationNumber = False, returnreturnCertificationTypeID = False, returnreturnCreatedTime = False, returnreturnEmployeeID = False, returnreturnExpirationDate = False, returnreturnInstitutionID = False, returnreturnIsDelete = False, returnreturnIssueDate = False, returnreturnModifiedTime = False, returnreturnOnScreenCount = False, returnreturnStateID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "get", params_list = params_list)

	return(response)

def deleteTempCertification(TempCertificationID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "delete")

	return(response)

def getEveryTempDataGridRow(EntityID = 1, page = 1, pageSize = 100, returnTempDataGridRowID = True, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempDataGridRow(TempDataGridRowID, EntityID = 1, returnreturnTempDataGridRowID = False, returnreturnColumnHeader = False, returnreturnControlType = False, returnreturnControlTypeCode = False, returnreturnCreatedTime = False, returnreturnDefaultValue = False, returnreturnModifiedTime = False, returnreturnOptions = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "get", params_list = params_list)

	return(response)

def deleteTempDataGridRow(TempDataGridRowID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "delete")

	return(response)

def getEveryTempDegree(EntityID = 1, page = 1, pageSize = 100, returnTempDegreeID = True, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempDegree(TempDegreeID, EntityID = 1, returnreturnTempDegreeID = False, returnreturnAdditionalCredits = False, returnreturnApprovedDate = False, returnreturnCreatedTime = False, returnreturnCredits = False, returnreturnDegreeID = False, returnreturnDegreeTypeID = False, returnreturnEmployeeID = False, returnreturnGPA = False, returnreturnInstitutionID = False, returnreturnIsDelete = False, returnreturnModifiedTime = False, returnreturnOnScreenCount = False, returnreturnReceivedDate = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "get", params_list = params_list)

	return(response)

def deleteTempDegree(TempDegreeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "delete")

	return(response)

def getEveryTempDependent(EntityID = 1, page = 1, pageSize = 100, returnTempDependentID = True, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempDependent(TempDependentID, EntityID = 1, returnreturnTempDependentID = False, returnreturnBirthDate = False, returnreturnCreatedTime = False, returnreturnDependentID = False, returnreturnFirstName = False, returnreturnIsDelete = False, returnreturnIsExistingRecord = False, returnreturnLastName = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnOnScreenCount = False, returnreturnRelationshipID = False, returnreturnSocialSecurityNumber = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "get", params_list = params_list)

	return(response)

def deleteTempDependent(TempDependentID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "delete")

	return(response)

def getEveryTempEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnTempEmergencyContactID = True, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnreturnTempEmergencyContactID = False, returnreturnAddEmergencyContact = False, returnreturnAllowStudentPickup = False, returnreturnComment = False, returnreturnCreatedTime = False, returnreturnCreateNewEmergencyContactName = False, returnreturnDeleteEmergencyContact = False, returnreturnDriversLicenseNumber = False, returnreturnEmergencyContactID = False, returnreturnFirstName = False, returnreturnForSecondFamily = False, returnreturnIsAlsoGuardian = False, returnreturnIsBusiness = False, returnreturnIsHealthProfessionalName = False, returnreturnLastName = False, returnreturnMiddleName = False, returnreturnModifiedTime = False, returnreturnNameID = False, returnreturnOnScreenID = False, returnreturnPrimaryEmailEmailAddress = False, returnreturnPrimaryEmailEmailTypeID = False, returnreturnPrimaryEmailNameEmailID = False, returnreturnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnreturnPrimaryPhoneExtension = False, returnreturnPrimaryPhoneNamePhoneID = False, returnreturnPrimaryPhonePhoneNumber = False, returnreturnPrimaryPhonePhoneTypeID = False, returnreturnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnreturnRank = False, returnreturnRelationshipID = False, returnreturnSecondEmailEmailAddress = False, returnreturnSecondEmailEmailTypeID = False, returnreturnSecondEmailNameEmailID = False, returnreturnSecondEmailPreventFamilyStudentAccessUpdates = False, returnreturnSecondPhoneExtension = False, returnreturnSecondPhoneNamePhoneID = False, returnreturnSecondPhonePhoneNumber = False, returnreturnSecondPhonePhoneTypeID = False, returnreturnSecondPhonePreventFamilyStudentAccessUpdates = False, returnreturnThirdEmailEmailAddress = False, returnreturnThirdEmailEmailTypeID = False, returnreturnThirdEmailNameEmailID = False, returnreturnThirdEmailPreventFamilyStudentAccessUpdates = False, returnreturnThirdPhoneExtension = False, returnreturnThirdPhoneNamePhoneID = False, returnreturnThirdPhonePhoneNumber = False, returnreturnThirdPhonePhoneTypeID = False, returnreturnThirdPhonePreventFamilyStudentAccessUpdates = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", params_list = params_list)

	return(response)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "delete")

	return(response)

def getEveryTempError(EntityID = 1, page = 1, pageSize = 100, returnTempErrorID = True, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempError(TempErrorID, EntityID = 1, returnreturnTempErrorID = False, returnreturnCreatedTime = False, returnreturnDescription = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempError(TempErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "delete")

	return(response)

def getEveryTempNewStudentEnrollmentGuardianEmail(EntityID = 1, page = 1, pageSize = 100, returnTempNewStudentEnrollmentGuardianEmailID = True, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1, returnreturnTempNewStudentEnrollmentGuardianEmailID = False, returnreturnAddEmail = False, returnreturnCreatedTime = False, returnreturnCreateNewEmail = False, returnreturnDeleteEmail = False, returnreturnEmailAddress = False, returnreturnEmailPreventFamilyStudentAccessUpdates = False, returnreturnEmailTypeID = False, returnreturnModifiedTime = False, returnreturnNameEmailID = False, returnreturnOnScreenID = False, returnreturnParentOnScreenID = False, returnreturnRank = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "delete")

	return(response)

def getEveryTempNewStudentEnrollmentGuardianPhone(EntityID = 1, page = 1, pageSize = 100, returnTempNewStudentEnrollmentGuardianPhoneID = True, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1, returnreturnTempNewStudentEnrollmentGuardianPhoneID = False, returnreturnAddPhone = False, returnreturnCreatedTime = False, returnreturnCreateNewPhone = False, returnreturnDeletePhone = False, returnreturnExtension = False, returnreturnIsConfidential = False, returnreturnModifiedTime = False, returnreturnNamePhoneID = False, returnreturnOnScreenID = False, returnreturnParentOnScreenID = False, returnreturnPhoneNumber = False, returnreturnPhonePreventFamilyStudentAccessUpdates = False, returnreturnPhoneTypeID = False, returnreturnRank = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "delete")

	return(response)

def getEveryTempStep(EntityID = 1, page = 1, pageSize = 100, returnTempStepID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorMessage = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStep(TempStepID, EntityID = 1, returnreturnTempStepID = False, returnreturnCreatedTime = False, returnreturnEntityGroupKey = False, returnreturnErrorMessage = False, returnreturnIsActive = False, returnreturnIsReadOnlyForNonPrimaryFamily = False, returnreturnIsRequired = False, returnreturnMessage = False, returnreturnModifiedTime = False, returnreturnName = False, returnreturnOnlineFormID = False, returnreturnOrder = False, returnreturnStepID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStep(TempStepID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "delete")

	return(response)

def getEveryTempStudentHealthCondition(EntityID = 1, page = 1, pageSize = 100, returnTempStudentHealthConditionID = True, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = []
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", params_list = params_list)

	if "error" in response.keys():
		raise Exception(response["error"])
	else:
		return(pd.DataFrame.from_dict(response.Objects))

def getTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1, returnreturnTempStudentHealthConditionID = False, returnreturnCreatedTime = False, returnreturnHealthConditionID = False, returnreturnIsDelete = False, returnreturnIsExistingStudentHealthCondition = False, returnreturnIsExistingStudentHealthConditionNote = False, returnreturnModifiedTime = False, returnreturnNote = False, returnreturnOnScreenCount = False, returnreturnStartDate = False, returnreturnStudentHealthConditionID = False, returnreturnStudentHealthConditionNoteID = False, returnreturnUserIDCreatedBy = False, returnreturnUserIDModifiedBy = False, returnreturnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "delete")

	return(response)