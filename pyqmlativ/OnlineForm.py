# This module contains OnlineForm functions.

from .Utilities import make_request

import pandas as pd

import json

import re

def getEveryElement(EntityID = 1, page = 1, pageSize = 100, returnElementID = True, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElement(ElementID, EntityID = 1, returnElementID = True, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "get", return_params_list = return_params_list)

def modifyElement(ElementID, EntityID = 1, setAgreementMessage = None, setApprovalType = None, setApprovalTypeCode = None, setCodeListType = None, setCodeListTypeCode = None, setCodeListTypeLabel = None, setComboboxDefaultValue = None, setComboboxTextValue = None, setCommonColorPickerValue = None, setCommonFontAlignmentValue = None, setCommonTextValue = None, setCommonType = None, setCommonTypeCode = None, setCoverageEndDate = None, setCoverageStartDate = None, setDataGridXML = None, setDistrictID = None, setElementGroupID = None, setEmbeddedLinkProtocol = None, setEmbeddedLinkProtocolCode = None, setEmbeddedLinkURL = None, setEmergencyContact = None, setFieldDisplayName = None, setFieldGroup = None, setFieldGroupCode = None, setFieldID = None, setFieldIsRelationship = None, setFieldLabel = None, setFieldName = None, setFieldPath = None, setHealthConditionIDs = None, setHealthProviderExcludeDentalInsurance = None, setHealthProviderExcludeDentist = None, setHealthProviderExcludeDentistOffice = None, setHealthProviderExcludeEmail = None, setHealthProviderExcludeHealthInsurance = None, setHealthProviderExcludeHospital = None, setHealthProviderExcludePhone = None, setHealthProviderExcludePrimaryPhysician = None, setHtmlDescription = None, setHtmlLabel = None, setHtmlOptions = None, setIncludeCECSInStudentSelector = None, setIsRequiredElement = None, setLabelOverrides = None, setLanguageOption = None, setLanguageOptionCode = None, setLinkProtocol = None, setLinkProtocolCode = None, setMaxNumberEmergencyContacts = None, setMaxUploadFileSize = None, setMaxUploadFileSizeUnit = None, setMaxUploadFileSizeUnitCode = None, setMediaID = None, setMergeMarkupSet = None, setMergeMarkupSetDescription = None, setMergeMarkupSetLabel = None, setNewStudentEnrollmentGuardianRequireDriversLicense = None, setNewStudentEnrollmentGuardianUseVehicleInformation = None, setNewStudentEnrollmentShowCustodialInformation = None, setNewStudentEnrollmentUseAddSecondFamily = None, setOrder = None, setParameterData = None, setParameters = None, setPaymentEndDate = None, setPaymentStartDate = None, setPlanID = None, setPostfixText = None, setPrefixText = None, setRaceEthnicityMessage = None, setRaceEthnicityMessageInSpanish = None, setRenderAgreement = None, setRenderInstructions = None, setRenderLanguageOptions = None, setRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = None, setRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = None, setShowCustodialOnFamilyInformation = None, setShowVehicleInformationOnEmergencyContact = None, setShowVehicleOnFamilyInformation = None, setStepID = None, setType = None, setTypeCode = None, setUploadType = None, setUploadTypeCode = None, setUrl = None, setUrlDisplayName = None, setUserDownloadDisplayText = None, setUserDownloadInstructions = None, setUserUploadDescription = None, setUserUploadLabel = None, setValidUploadFileTypes = None, setYesNoResponse = None, setYesNoResponseCode = None, setRelationships = None, returnElementID = True, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElement(EntityID = 1, setAgreementMessage = None, setApprovalType = None, setApprovalTypeCode = None, setCodeListType = None, setCodeListTypeCode = None, setCodeListTypeLabel = None, setComboboxDefaultValue = None, setComboboxTextValue = None, setCommonColorPickerValue = None, setCommonFontAlignmentValue = None, setCommonTextValue = None, setCommonType = None, setCommonTypeCode = None, setCoverageEndDate = None, setCoverageStartDate = None, setDataGridXML = None, setDistrictID = None, setElementGroupID = None, setEmbeddedLinkProtocol = None, setEmbeddedLinkProtocolCode = None, setEmbeddedLinkURL = None, setEmergencyContact = None, setFieldDisplayName = None, setFieldGroup = None, setFieldGroupCode = None, setFieldID = None, setFieldIsRelationship = None, setFieldLabel = None, setFieldName = None, setFieldPath = None, setHealthConditionIDs = None, setHealthProviderExcludeDentalInsurance = None, setHealthProviderExcludeDentist = None, setHealthProviderExcludeDentistOffice = None, setHealthProviderExcludeEmail = None, setHealthProviderExcludeHealthInsurance = None, setHealthProviderExcludeHospital = None, setHealthProviderExcludePhone = None, setHealthProviderExcludePrimaryPhysician = None, setHtmlDescription = None, setHtmlLabel = None, setHtmlOptions = None, setIncludeCECSInStudentSelector = None, setIsRequiredElement = None, setLabelOverrides = None, setLanguageOption = None, setLanguageOptionCode = None, setLinkProtocol = None, setLinkProtocolCode = None, setMaxNumberEmergencyContacts = None, setMaxUploadFileSize = None, setMaxUploadFileSizeUnit = None, setMaxUploadFileSizeUnitCode = None, setMediaID = None, setMergeMarkupSet = None, setMergeMarkupSetDescription = None, setMergeMarkupSetLabel = None, setNewStudentEnrollmentGuardianRequireDriversLicense = None, setNewStudentEnrollmentGuardianUseVehicleInformation = None, setNewStudentEnrollmentShowCustodialInformation = None, setNewStudentEnrollmentUseAddSecondFamily = None, setOrder = None, setParameterData = None, setParameters = None, setPaymentEndDate = None, setPaymentStartDate = None, setPlanID = None, setPostfixText = None, setPrefixText = None, setRaceEthnicityMessage = None, setRaceEthnicityMessageInSpanish = None, setRenderAgreement = None, setRenderInstructions = None, setRenderLanguageOptions = None, setRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = None, setRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = None, setShowCustodialOnFamilyInformation = None, setShowVehicleInformationOnEmergencyContact = None, setShowVehicleOnFamilyInformation = None, setStepID = None, setType = None, setTypeCode = None, setUploadType = None, setUploadTypeCode = None, setUrl = None, setUrlDisplayName = None, setUserDownloadDisplayText = None, setUserDownloadInstructions = None, setUserUploadDescription = None, setUserUploadLabel = None, setValidUploadFileTypes = None, setYesNoResponse = None, setYesNoResponseCode = None, setRelationships = None, returnElementID = True, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElement(ElementID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryElementGroup(EntityID = 1, page = 1, pageSize = 100, returnElementGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElementGroup(ElementGroupID, EntityID = 1, returnElementGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "get", return_params_list = return_params_list)

def modifyElementGroup(ElementGroupID, EntityID = 1, setName = None, setSkywardID = None, setRelationships = None, returnElementGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElementGroup(EntityID = 1, setName = None, setSkywardID = None, setRelationships = None, returnElementGroupID = True, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElementGroup(ElementGroupID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryElementGroupTemplate(EntityID = 1, page = 1, pageSize = 100, returnElementGroupTemplateID = True, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElementGroupTemplate(ElementGroupTemplateID, EntityID = 1, returnElementGroupTemplateID = True, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "get", return_params_list = return_params_list)

def modifyElementGroupTemplate(ElementGroupTemplateID, EntityID = 1, setElementGroupID = None, setOrder = None, setParameterData = None, setSkywardID = None, setType = None, setTypeCode = None, setRelationships = None, returnElementGroupTemplateID = True, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElementGroupTemplate(EntityID = 1, setElementGroupID = None, setOrder = None, setParameterData = None, setSkywardID = None, setType = None, setTypeCode = None, setRelationships = None, returnElementGroupTemplateID = True, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElementGroupTemplate(ElementGroupTemplateID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryElementStatus(EntityID = 1, page = 1, pageSize = 100, returnElementStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElementStatus(ElementStatusID, EntityID = 1, returnElementStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "get", return_params_list = return_params_list)

def modifyElementStatus(ElementStatusID, EntityID = 1, setDenialMessage = None, setElementID = None, setIsReadOnly = None, setMediaIDAttachment = None, setOriginalValue = None, setRequestedValue = None, setSharedElementStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepStatusID = None, setUserIDApprover = None, setUserSubmitted = None, setValidationMessage = None, setRelationships = None, returnElementStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElementStatus(EntityID = 1, setDenialMessage = None, setElementID = None, setIsReadOnly = None, setMediaIDAttachment = None, setOriginalValue = None, setRequestedValue = None, setSharedElementStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepStatusID = None, setUserIDApprover = None, setUserSubmitted = None, setValidationMessage = None, setRelationships = None, returnElementStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElementStatus(ElementStatusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryElementStatusSurveyAnswer(EntityID = 1, page = 1, pageSize = 100, returnElementStatusSurveyAnswerID = True, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1, returnElementStatusSurveyAnswerID = True, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "get", return_params_list = return_params_list)

def modifyElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1, setColumnName = None, setElementStatusID = None, setNameID = None, setOnlineFormID = None, setValue = None, setRelationships = None, returnElementStatusSurveyAnswerID = True, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createElementStatusSurveyAnswer(EntityID = 1, setColumnName = None, setElementStatusID = None, setNameID = None, setOnlineFormID = None, setValue = None, setRelationships = None, returnElementStatusSurveyAnswerID = True, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryMassPrintHistory(EntityID = 1, page = 1, pageSize = 100, returnMassPrintHistoryID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getMassPrintHistory(MassPrintHistoryID, EntityID = 1, returnMassPrintHistoryID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "get", return_params_list = return_params_list)

def modifyMassPrintHistory(MassPrintHistoryID, EntityID = 1, setMediaID = None, setOnlineFormID = None, setRequestIdentifier = None, setSendMessageOnComplete = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintHistoryID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createMassPrintHistory(EntityID = 1, setMediaID = None, setOnlineFormID = None, setRequestIdentifier = None, setSendMessageOnComplete = None, setWorkflowInstanceID = None, setRelationships = None, returnMassPrintHistoryID = True, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteMassPrintHistory(MassPrintHistoryID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNewStudentEnrollmentGuardianData(EntityID = 1, page = 1, pageSize = 100, returnNewStudentEnrollmentGuardianDataID = True, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1, returnNewStudentEnrollmentGuardianDataID = True, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "get", return_params_list = return_params_list)

def modifyNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1, setAddGuardian = None, setAllowStudentPickup = None, setColor = None, setCreateNewGuardian = None, setDeleteGuardian = None, setDriversLicenseNumber = None, setFamilyGuardianID = None, setFirstName = None, setGenderCode = None, setIsCustodialGuardian = None, setLastName = None, setLicensePlateNumber = None, setMakeModel = None, setMiddleName = None, setNameID = None, setNameSuffixID = None, setNameVehicleID = None, setOnScreenID = None, setRank = None, setRelationshipID = None, setVehicleID = None, setVIN = None, setYear = None, setRelationships = None, returnNewStudentEnrollmentGuardianDataID = True, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNewStudentEnrollmentGuardianData(EntityID = 1, setAddGuardian = None, setAllowStudentPickup = None, setColor = None, setCreateNewGuardian = None, setDeleteGuardian = None, setDriversLicenseNumber = None, setFamilyGuardianID = None, setFirstName = None, setGenderCode = None, setIsCustodialGuardian = None, setLastName = None, setLicensePlateNumber = None, setMakeModel = None, setMiddleName = None, setNameID = None, setNameSuffixID = None, setNameVehicleID = None, setOnScreenID = None, setRank = None, setRelationshipID = None, setVehicleID = None, setVIN = None, setYear = None, setRelationships = None, returnNewStudentEnrollmentGuardianDataID = True, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryNewStudentEnrollmentUserData(EntityID = 1, page = 1, pageSize = 100, returnNewStudentEnrollmentUserDataID = True, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1, returnNewStudentEnrollmentUserDataID = True, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "get", return_params_list = return_params_list)

def modifyNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1, setCity = None, setEmailAddress = None, setPhoneNumber = None, setPhysicalStreetName = None, setPhysicalStreetNumber = None, setPreviouslyInDistrict = None, setState = None, setUnit = None, setUnitNumber = None, setUserIDSubmittedBy = None, setZipCode = None, setRelationships = None, returnNewStudentEnrollmentUserDataID = True, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createNewStudentEnrollmentUserData(EntityID = 1, setCity = None, setEmailAddress = None, setPhoneNumber = None, setPhysicalStreetName = None, setPhysicalStreetNumber = None, setPreviouslyInDistrict = None, setState = None, setUnit = None, setUnitNumber = None, setUserIDSubmittedBy = None, setZipCode = None, setRelationships = None, returnNewStudentEnrollmentUserDataID = True, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormID = True, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineForm(OnlineFormID, EntityID = 1, returnOnlineFormID = True, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "get", return_params_list = return_params_list)

def modifyOnlineForm(OnlineFormID, EntityID = 1, setActivitiesSearchConditionFilter = None, setAdministrativeSearchConditionFilter = None, setAllowContact = None, setAllowMultipleFormsPerUser = None, setCutoffTime = None, setDescription = None, setDisplayForNonPrimaryFamily = None, setEmployeeSearchConditionFilter = None, setEmployeeStandardFilterCollectionJson = None, setEndDate = None, setFamilySearchConditionFilter = None, setFilter = None, setFilterSubType = None, setFilterSubTypeCode = None, setHideCurrentValueOnApproval = None, setIconCode = None, setIncludeAdobeAcrobatLink = None, setIsPublished = None, setIsUserInitiated = None, setLimitToOnePerDay = None, setMainPageEmbeddedLinkProtocol = None, setMainPageEmbeddedLinkProtocolCode = None, setMainPageEmbeddedLinkUrl = None, setMessage = None, setMessageAfterSubmission = None, setMessageForNonPrimaryFamily = None, setName = None, setNewStudentEnrollmentSearchConditionFilter = None, setNoApprovalNeeded = None, setOnlineFormIDClonedFrom = None, setOnlineFormTypeID = None, setPortalType = None, setPortalTypeCode = None, setReviewStepMessage = None, setSchoolYearID = None, setSendFamilyAccessEmail = None, setShowDescriptionOnTile = None, setSkipInstructionsPage = None, setSkipReviewPage = None, setSkipThankYouPage = None, setStartDate = None, setStudentSearchConditionFilter = None, setTeacherSearchConditionFilter = None, setYearType = None, setYearTypeCode = None, setRelationships = None, returnOnlineFormID = True, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineForm(EntityID = 1, setActivitiesSearchConditionFilter = None, setAdministrativeSearchConditionFilter = None, setAllowContact = None, setAllowMultipleFormsPerUser = None, setCutoffTime = None, setDescription = None, setDisplayForNonPrimaryFamily = None, setEmployeeSearchConditionFilter = None, setEmployeeStandardFilterCollectionJson = None, setEndDate = None, setFamilySearchConditionFilter = None, setFilter = None, setFilterSubType = None, setFilterSubTypeCode = None, setHideCurrentValueOnApproval = None, setIconCode = None, setIncludeAdobeAcrobatLink = None, setIsPublished = None, setIsUserInitiated = None, setLimitToOnePerDay = None, setMainPageEmbeddedLinkProtocol = None, setMainPageEmbeddedLinkProtocolCode = None, setMainPageEmbeddedLinkUrl = None, setMessage = None, setMessageAfterSubmission = None, setMessageForNonPrimaryFamily = None, setName = None, setNewStudentEnrollmentSearchConditionFilter = None, setNoApprovalNeeded = None, setOnlineFormIDClonedFrom = None, setOnlineFormTypeID = None, setPortalType = None, setPortalTypeCode = None, setReviewStepMessage = None, setSchoolYearID = None, setSendFamilyAccessEmail = None, setShowDescriptionOnTile = None, setSkipInstructionsPage = None, setSkipReviewPage = None, setSkipThankYouPage = None, setStartDate = None, setStudentSearchConditionFilter = None, setTeacherSearchConditionFilter = None, setYearType = None, setYearTypeCode = None, setRelationships = None, returnOnlineFormID = True, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineForm(OnlineFormID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormClearance(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormClearanceID = True, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormClearance(OnlineFormClearanceID, EntityID = 1, returnOnlineFormClearanceID = True, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormClearance(OnlineFormClearanceID, EntityID = 1, setGroupIDSecurity = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormClearanceID = True, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormClearance(EntityID = 1, setGroupIDSecurity = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormClearanceID = True, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormClearance(OnlineFormClearanceID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormDateException(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormDateExceptionID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1, returnOnlineFormDateExceptionID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1, setObjectID = None, setObjectPrimaryKey = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormDateExceptionID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormDateException(EntityID = 1, setObjectID = None, setObjectPrimaryKey = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormDateExceptionID = True, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormEntity(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormEntity(OnlineFormEntityID, EntityID = 1, returnOnlineFormEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormEntity(OnlineFormEntityID, EntityID = 1, setEntityID = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormEntity(EntityID = 1, setEntityID = None, setOnlineFormID = None, setRelationships = None, returnOnlineFormEntityID = True, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormEntity(OnlineFormEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormStatus(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormStatusID = True, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormStatus(OnlineFormStatusID, EntityID = 1, returnOnlineFormStatusID = True, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormStatus(OnlineFormStatusID, EntityID = 1, setApprovalRevoked = None, setCompletedByAdmin = None, setDenialDateTime = None, setDenialMessage = None, setFullNameLFMSubmittedForOverride = None, setIsOutsideAddressRanges = None, setNameID = None, setOnlineFormEntityID = None, setSecondaryID = None, setStatusType = None, setStatusTypeCode = None, setSubmittedDateTime = None, setUserIDApprover = None, setUserIDSubmittedBy = None, setRelationships = None, returnOnlineFormStatusID = True, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormStatus(EntityID = 1, setApprovalRevoked = None, setCompletedByAdmin = None, setDenialDateTime = None, setDenialMessage = None, setFullNameLFMSubmittedForOverride = None, setIsOutsideAddressRanges = None, setNameID = None, setOnlineFormEntityID = None, setSecondaryID = None, setStatusType = None, setStatusTypeCode = None, setSubmittedDateTime = None, setUserIDApprover = None, setUserIDSubmittedBy = None, setRelationships = None, returnOnlineFormStatusID = True, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormStatus(OnlineFormStatusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormStatusName(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormStatusNameID = True, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1, returnOnlineFormStatusNameID = True, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1, setElementID = None, setNameID = None, setOnlineFormStatusID = None, setRelationships = None, returnOnlineFormStatusNameID = True, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormStatusName(EntityID = 1, setElementID = None, setNameID = None, setOnlineFormStatusID = None, setRelationships = None, returnOnlineFormStatusNameID = True, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryOnlineFormType(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getOnlineFormType(OnlineFormTypeID, EntityID = 1, returnOnlineFormTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "get", return_params_list = return_params_list)

def modifyOnlineFormType(OnlineFormTypeID, EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setLimitUsersToOneFormOfThisTypePerYear = None, setRelationships = None, returnOnlineFormTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createOnlineFormType(EntityID = 1, setCode = None, setDescription = None, setDistrictID = None, setLimitUsersToOneFormOfThisTypePerYear = None, setRelationships = None, returnOnlineFormTypeID = True, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteOnlineFormType(OnlineFormTypeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEverySharedElementStatus(EntityID = 1, page = 1, pageSize = 100, returnSharedElementStatusID = True, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getSharedElementStatus(SharedElementStatusID, EntityID = 1, returnSharedElementStatusID = True, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "get", return_params_list = return_params_list)

def modifySharedElementStatus(SharedElementStatusID, EntityID = 1, setElementType = None, setElementTypeCode = None, setFieldGroupType = None, setFieldGroupTypeCode = None, setMediaIDAttachment = None, setNameID = None, setSchoolYearID = None, setSecondaryID = None, setValue = None, setRelationships = None, returnSharedElementStatusID = True, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createSharedElementStatus(EntityID = 1, setElementType = None, setElementTypeCode = None, setFieldGroupType = None, setFieldGroupTypeCode = None, setMediaIDAttachment = None, setNameID = None, setSchoolYearID = None, setSecondaryID = None, setValue = None, setRelationships = None, returnSharedElementStatusID = True, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteSharedElementStatus(SharedElementStatusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStaffContact(EntityID = 1, page = 1, pageSize = 100, returnStaffContactID = True, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStaffContact(StaffContactID, EntityID = 1, returnStaffContactID = True, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "get", return_params_list = return_params_list)

def modifyStaffContact(StaffContactID, EntityID = 1, setOnlineFormID = None, setStaffID = None, setRelationships = None, returnStaffContactID = True, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStaffContact(EntityID = 1, setOnlineFormID = None, setStaffID = None, setRelationships = None, returnStaffContactID = True, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStaffContact(StaffContactID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStep(EntityID = 1, page = 1, pageSize = 100, returnStepID = True, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStep(StepID, EntityID = 1, returnStepID = True, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "get", return_params_list = return_params_list)

def modifyStep(StepID, EntityID = 1, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setName = None, setOnlineFormID = None, setOrder = None, setRelationships = None, returnStepID = True, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStep(EntityID = 1, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setName = None, setOnlineFormID = None, setOrder = None, setRelationships = None, returnStepID = True, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStep(StepID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryStepStatus(EntityID = 1, page = 1, pageSize = 100, returnStepStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getStepStatus(StepStatusID, EntityID = 1, returnStepStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "get", return_params_list = return_params_list)

def modifyStepStatus(StepStatusID, EntityID = 1, setDenialMessage = None, setOnlineFormStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepID = None, setValidationMessage = None, setRelationships = None, returnStepStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createStepStatus(EntityID = 1, setDenialMessage = None, setOnlineFormStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepID = None, setValidationMessage = None, setRelationships = None, returnStepStatusID = True, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteStepStatus(StepStatusID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTeacherOnlineForm(EntityID = 1, page = 1, pageSize = 100, returnOnlineFormEntityID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTeacherOnlineForm(OnlineFormEntityID, EntityID = 1, returnOnlineFormEntityID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "get", return_params_list = return_params_list)

def modifyTeacherOnlineForm(OnlineFormEntityID, EntityID = 1, setStatusType = None, setStatusTypeCode = None, setRelationships = None, returnOnlineFormEntityID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTeacherOnlineForm(EntityID = 1, setStatusType = None, setStatusTypeCode = None, setRelationships = None, returnOnlineFormEntityID = True, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTeacherOnlineForm(OnlineFormEntityID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempCertification(EntityID = 1, page = 1, pageSize = 100, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempCertification(TempCertificationID, EntityID = 1, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "get", return_params_list = return_params_list)

def modifyTempCertification(TempCertificationID, EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationTypeID = None, setEmployeeID = None, setExpirationDate = None, setInstitutionID = None, setIsDelete = None, setIssueDate = None, setOnScreenCount = None, setStateID = None, setRelationships = None, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempCertification(EntityID = 1, setCertificationID = None, setCertificationNumber = None, setCertificationTypeID = None, setEmployeeID = None, setExpirationDate = None, setInstitutionID = None, setIsDelete = None, setIssueDate = None, setOnScreenCount = None, setStateID = None, setRelationships = None, returnTempCertificationID = True, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempCertification(TempCertificationID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDataGridRow(EntityID = 1, page = 1, pageSize = 100, returnTempDataGridRowID = True, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDataGridRow(TempDataGridRowID, EntityID = 1, returnTempDataGridRowID = True, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "get", return_params_list = return_params_list)

def modifyTempDataGridRow(TempDataGridRowID, EntityID = 1, setColumnHeader = None, setControlType = None, setControlTypeCode = None, setDefaultValue = None, setOptions = None, setRelationships = None, returnTempDataGridRowID = True, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDataGridRow(EntityID = 1, setColumnHeader = None, setControlType = None, setControlTypeCode = None, setDefaultValue = None, setOptions = None, setRelationships = None, returnTempDataGridRowID = True, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDataGridRow(TempDataGridRowID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDegree(EntityID = 1, page = 1, pageSize = 100, returnTempDegreeID = True, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDegree(TempDegreeID, EntityID = 1, returnTempDegreeID = True, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "get", return_params_list = return_params_list)

def modifyTempDegree(TempDegreeID, EntityID = 1, setAdditionalCredits = None, setApprovedDate = None, setCredits = None, setDegreeID = None, setDegreeTypeID = None, setEmployeeID = None, setGPA = None, setInstitutionID = None, setIsDelete = None, setOnScreenCount = None, setReceivedDate = None, setRelationships = None, returnTempDegreeID = True, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDegree(EntityID = 1, setAdditionalCredits = None, setApprovedDate = None, setCredits = None, setDegreeID = None, setDegreeTypeID = None, setEmployeeID = None, setGPA = None, setInstitutionID = None, setIsDelete = None, setOnScreenCount = None, setReceivedDate = None, setRelationships = None, returnTempDegreeID = True, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDegree(TempDegreeID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempDependent(EntityID = 1, page = 1, pageSize = 100, returnTempDependentID = True, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempDependent(TempDependentID, EntityID = 1, returnTempDependentID = True, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "get", return_params_list = return_params_list)

def modifyTempDependent(TempDependentID, EntityID = 1, setBirthDate = None, setDependentID = None, setFirstName = None, setIsDelete = None, setIsExistingRecord = None, setLastName = None, setMiddleName = None, setOnScreenCount = None, setRelationshipID = None, setSocialSecurityNumber = None, setRelationships = None, returnTempDependentID = True, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempDependent(EntityID = 1, setBirthDate = None, setDependentID = None, setFirstName = None, setIsDelete = None, setIsExistingRecord = None, setLastName = None, setMiddleName = None, setOnScreenCount = None, setRelationshipID = None, setSocialSecurityNumber = None, setRelationships = None, returnTempDependentID = True, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempDependent(TempDependentID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempEmergencyContact(EntityID = 1, page = 1, pageSize = 100, returnTempEmergencyContactID = True, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnTempEmergencyContactID = True, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", return_params_list = return_params_list)

def modifyTempEmergencyContact(TempEmergencyContactID, EntityID = 1, setAddEmergencyContact = None, setAllowStudentPickup = None, setComment = None, setCreateNewEmergencyContactName = None, setDeleteEmergencyContact = None, setDriversLicenseNumber = None, setEmergencyContactID = None, setFirstName = None, setForSecondFamily = None, setIsAlsoGuardian = None, setIsBusiness = None, setIsHealthProfessionalName = None, setLastName = None, setMiddleName = None, setNameID = None, setOnScreenID = None, setPrimaryEmailEmailAddress = None, setPrimaryEmailEmailTypeID = None, setPrimaryEmailNameEmailID = None, setPrimaryEmailPreventFamilyStudentAccessUpdates = None, setPrimaryPhoneExtension = None, setPrimaryPhoneNamePhoneID = None, setPrimaryPhonePhoneNumber = None, setPrimaryPhonePhoneTypeID = None, setPrimaryPhonePreventFamilyStudentAccessUpdates = None, setRank = None, setRelationshipID = None, setSecondEmailEmailAddress = None, setSecondEmailEmailTypeID = None, setSecondEmailNameEmailID = None, setSecondEmailPreventFamilyStudentAccessUpdates = None, setSecondPhoneExtension = None, setSecondPhoneNamePhoneID = None, setSecondPhonePhoneNumber = None, setSecondPhonePhoneTypeID = None, setSecondPhonePreventFamilyStudentAccessUpdates = None, setThirdEmailEmailAddress = None, setThirdEmailEmailTypeID = None, setThirdEmailNameEmailID = None, setThirdEmailPreventFamilyStudentAccessUpdates = None, setThirdPhoneExtension = None, setThirdPhoneNamePhoneID = None, setThirdPhonePhoneNumber = None, setThirdPhonePhoneTypeID = None, setThirdPhonePreventFamilyStudentAccessUpdates = None, setRelationships = None, returnTempEmergencyContactID = True, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempEmergencyContact(EntityID = 1, setAddEmergencyContact = None, setAllowStudentPickup = None, setComment = None, setCreateNewEmergencyContactName = None, setDeleteEmergencyContact = None, setDriversLicenseNumber = None, setEmergencyContactID = None, setFirstName = None, setForSecondFamily = None, setIsAlsoGuardian = None, setIsBusiness = None, setIsHealthProfessionalName = None, setLastName = None, setMiddleName = None, setNameID = None, setOnScreenID = None, setPrimaryEmailEmailAddress = None, setPrimaryEmailEmailTypeID = None, setPrimaryEmailNameEmailID = None, setPrimaryEmailPreventFamilyStudentAccessUpdates = None, setPrimaryPhoneExtension = None, setPrimaryPhoneNamePhoneID = None, setPrimaryPhonePhoneNumber = None, setPrimaryPhonePhoneTypeID = None, setPrimaryPhonePreventFamilyStudentAccessUpdates = None, setRank = None, setRelationshipID = None, setSecondEmailEmailAddress = None, setSecondEmailEmailTypeID = None, setSecondEmailNameEmailID = None, setSecondEmailPreventFamilyStudentAccessUpdates = None, setSecondPhoneExtension = None, setSecondPhoneNamePhoneID = None, setSecondPhonePhoneNumber = None, setSecondPhonePhoneTypeID = None, setSecondPhonePreventFamilyStudentAccessUpdates = None, setThirdEmailEmailAddress = None, setThirdEmailEmailTypeID = None, setThirdEmailNameEmailID = None, setThirdEmailPreventFamilyStudentAccessUpdates = None, setThirdPhoneExtension = None, setThirdPhoneNamePhoneID = None, setThirdPhonePhoneNumber = None, setThirdPhonePhoneTypeID = None, setThirdPhonePreventFamilyStudentAccessUpdates = None, setRelationships = None, returnTempEmergencyContactID = True, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempError(EntityID = 1, page = 1, pageSize = 100, returnTempErrorID = True, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempError(TempErrorID, EntityID = 1, returnTempErrorID = True, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "get", return_params_list = return_params_list)

def modifyTempError(TempErrorID, EntityID = 1, setDescription = None, setMessage = None, setRelationships = None, returnTempErrorID = True, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempError(EntityID = 1, setDescription = None, setMessage = None, setRelationships = None, returnTempErrorID = True, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempError(TempErrorID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNewStudentEnrollmentGuardianEmail(EntityID = 1, page = 1, pageSize = 100, returnTempNewStudentEnrollmentGuardianEmailID = True, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1, returnTempNewStudentEnrollmentGuardianEmailID = True, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "get", return_params_list = return_params_list)

def modifyTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1, setAddEmail = None, setCreateNewEmail = None, setDeleteEmail = None, setEmailAddress = None, setEmailPreventFamilyStudentAccessUpdates = None, setEmailTypeID = None, setNameEmailID = None, setOnScreenID = None, setParentOnScreenID = None, setRank = None, setRelationships = None, returnTempNewStudentEnrollmentGuardianEmailID = True, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNewStudentEnrollmentGuardianEmail(EntityID = 1, setAddEmail = None, setCreateNewEmail = None, setDeleteEmail = None, setEmailAddress = None, setEmailPreventFamilyStudentAccessUpdates = None, setEmailTypeID = None, setNameEmailID = None, setOnScreenID = None, setParentOnScreenID = None, setRank = None, setRelationships = None, returnTempNewStudentEnrollmentGuardianEmailID = True, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempNewStudentEnrollmentGuardianPhone(EntityID = 1, page = 1, pageSize = 100, returnTempNewStudentEnrollmentGuardianPhoneID = True, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1, returnTempNewStudentEnrollmentGuardianPhoneID = True, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "get", return_params_list = return_params_list)

def modifyTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1, setAddPhone = None, setCreateNewPhone = None, setDeletePhone = None, setExtension = None, setIsConfidential = None, setNamePhoneID = None, setOnScreenID = None, setParentOnScreenID = None, setPhoneNumber = None, setPhonePreventFamilyStudentAccessUpdates = None, setPhoneTypeID = None, setRank = None, setRelationships = None, returnTempNewStudentEnrollmentGuardianPhoneID = True, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempNewStudentEnrollmentGuardianPhone(EntityID = 1, setAddPhone = None, setCreateNewPhone = None, setDeletePhone = None, setExtension = None, setIsConfidential = None, setNamePhoneID = None, setOnScreenID = None, setParentOnScreenID = None, setPhoneNumber = None, setPhonePreventFamilyStudentAccessUpdates = None, setPhoneTypeID = None, setRank = None, setRelationships = None, returnTempNewStudentEnrollmentGuardianPhoneID = True, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStep(EntityID = 1, page = 1, pageSize = 100, returnTempStepID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorMessage = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStep(TempStepID, EntityID = 1, returnTempStepID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorMessage = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "get", return_params_list = return_params_list)

def modifyTempStep(TempStepID, EntityID = 1, setEntityGroupKey = None, setErrorMessage = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setName = None, setOnlineFormID = None, setOrder = None, setStepID = None, setRelationships = None, returnTempStepID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorMessage = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStep(EntityID = 1, setEntityGroupKey = None, setErrorMessage = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setName = None, setOnlineFormID = None, setOrder = None, setStepID = None, setRelationships = None, returnTempStepID = True, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorMessage = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStep(TempStepID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")

def getEveryTempStudentHealthCondition(EntityID = 1, page = 1, pageSize = 100, returnTempStudentHealthConditionID = True, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[3,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(page) + "/" + str(pageSize), verb = "get", return_params_list = return_params_list)

def getTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1, returnTempStudentHealthConditionID = True, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params[[(value is True) for value in params.value]].index)
	if params.iloc[2,:].name == "".join(return_params_list):
		return_params_list = list(params[[("return" in name) for name in params.index.to_series()]].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "get", return_params_list = return_params_list)

def modifyTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1, setHealthConditionID = None, setIsDelete = None, setIsExistingStudentHealthCondition = None, setIsExistingStudentHealthConditionNote = None, setNote = None, setOnScreenCount = None, setStartDate = None, setStudentHealthConditionID = None, setStudentHealthConditionNoteID = None, setRelationships = None, returnTempStudentHealthConditionID = True, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(), :]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "post", return_params_list = return_params_list, payload = payload_params)

def createTempStudentHealthCondition(EntityID = 1, setHealthConditionID = None, setIsDelete = None, setIsExistingStudentHealthCondition = None, setIsExistingStudentHealthConditionNote = None, setNote = None, setOnScreenCount = None, setStartDate = None, setStudentHealthConditionID = None, setStudentHealthConditionNoteID = None, setRelationships = None, returnTempStudentHealthConditionID = True, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])

	return_params_list = list(params.loc[lambda x: ((x.value & (x.index.to_series().str.contains("return"))) | (~(x.value.isnull()) & (x.index.to_series().str.contains("set")))) & (x.index.to_series() != "EntityID"),:].index)
	return_params_list = [re.sub("^return", "", param) for param in return_params_list]
	return_params_list = [re.sub("^set", "", param) for param in return_params_list]
	return_params_list = list(set(return_params_list))

	payload_params = params.loc[lambda x: x.index.to_series().str.contains("set") & ~x.value.isnull(),:]
	payload_params.index = [re.sub("^set", "", name) for name in payload_params.index]
	payload_params = dict({"DataObject": dict(payload_params["value"])})
	payload_params = json.dumps(payload_params)

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/", verb = "put", return_params_list = return_params_list, payload = payload_params)

def deleteTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1):

	return make_request(endpoint = "/Generic/" + str(EntityID) + "/Attendance/AttendancePeriod/" + str(AttendancePeriodID), verb = "delete")