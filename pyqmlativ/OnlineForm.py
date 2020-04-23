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

def getElement(ElementID, EntityID = 1, returnElementID = False, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnGUIDFieldPath = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentRelationshipRequired = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRelationshipRequiredOnFamilyInformation = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "get", return_params_list = return_params)

def modifyElement(ElementID, EntityID = 1, setElementID = None, setAdminCanEdit = None, setAgreementMessage = None, setAllowsUserInteraction = None, setApprovalType = None, setApprovalTypeCode = None, setCodeListFieldName = None, setCodeListFieldPath = None, setCodeListType = None, setCodeListTypeCode = None, setCodeListTypeLabel = None, setComboboxDefaultValue = None, setComboboxTextValue = None, setCommonColorPickerValue = None, setCommonFontAlignmentValue = None, setCommonTextValue = None, setCommonType = None, setCommonTypeCode = None, setCoverageEndDate = None, setCoverageStartDate = None, setCreatedTime = None, setDataGridXML = None, setDescription = None, setDistrictID = None, setElementGroupID = None, setEmbeddedLinkFullFilename = None, setEmbeddedLinkProtocol = None, setEmbeddedLinkProtocolCode = None, setEmbeddedLinkURL = None, setEmergencyContact = None, setFieldDisplayName = None, setFieldGroup = None, setFieldGroupCode = None, setFieldID = None, setFieldIsRelationship = None, setFieldLabel = None, setFieldName = None, setFieldPath = None, setFieldRelationship = None, setGUIDFieldPath = None, setHasBackingObject = None, setHasSharedValue = None, setHealthConditionIDs = None, setHealthProviderExcludeDentalInsurance = None, setHealthProviderExcludeDentist = None, setHealthProviderExcludeDentistOffice = None, setHealthProviderExcludeEmail = None, setHealthProviderExcludeHealthInsurance = None, setHealthProviderExcludeHospital = None, setHealthProviderExcludePhone = None, setHealthProviderExcludePrimaryPhysician = None, setHtmlDescription = None, setHtmlLabel = None, setHtmlOptions = None, setIncludeCECSInStudentSelector = None, setIsNewStudentEnrollmentElement = None, setIsRequiredElement = None, setLabelOverrides = None, setLanguageOption = None, setLanguageOptionCode = None, setLinkProtocol = None, setLinkProtocolCode = None, setMaxNumberEmergencyContacts = None, setMaxUploadFileSize = None, setMaxUploadFileSizeUnit = None, setMaxUploadFileSizeUnitCode = None, setMediaID = None, setMergeMarkupSet = None, setMergeMarkupSetDescription = None, setMergeMarkupSetLabel = None, setModifiedTime = None, setNewStudentEnrollmentGuardianRequireDriversLicense = None, setNewStudentEnrollmentGuardianUseVehicleInformation = None, setNewStudentEnrollmentRelationshipRequired = None, setNewStudentEnrollmentShowCustodialInformation = None, setNewStudentEnrollmentUseAddSecondFamily = None, setOrder = None, setParameterData = None, setParameters = None, setPaymentEndDate = None, setPaymentStartDate = None, setPlanID = None, setPostfixText = None, setPrefixText = None, setRaceEthnicityMessage = None, setRaceEthnicityMessageInSpanish = None, setRelationshipRequiredOnFamilyInformation = None, setRenderAgreement = None, setRenderInstructions = None, setRenderLanguageOptions = None, setRenderWeight = None, setRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = None, setRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = None, setSharedValueUsesNotShared = None, setShowCustodialOnFamilyInformation = None, setShowVehicleInformationOnEmergencyContact = None, setShowVehicleOnFamilyInformation = None, setStepID = None, setSupportsLabelOverrides = None, setType = None, setTypeCode = None, setUploadType = None, setUploadTypeCode = None, setUrl = None, setUrlDisplayName = None, setUserDownloadDisplayText = None, setUserDownloadInstructions = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserUploadDescription = None, setUserUploadLabel = None, setValidUploadFileTypes = None, setYesNoResponse = None, setYesNoResponseCode = None, returnElementID = False, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnGUIDFieldPath = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentRelationshipRequired = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRelationshipRequiredOnFamilyInformation = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElement(EntityID = 1, setElementID = None, setAdminCanEdit = None, setAgreementMessage = None, setAllowsUserInteraction = None, setApprovalType = None, setApprovalTypeCode = None, setCodeListFieldName = None, setCodeListFieldPath = None, setCodeListType = None, setCodeListTypeCode = None, setCodeListTypeLabel = None, setComboboxDefaultValue = None, setComboboxTextValue = None, setCommonColorPickerValue = None, setCommonFontAlignmentValue = None, setCommonTextValue = None, setCommonType = None, setCommonTypeCode = None, setCoverageEndDate = None, setCoverageStartDate = None, setCreatedTime = None, setDataGridXML = None, setDescription = None, setDistrictID = None, setElementGroupID = None, setEmbeddedLinkFullFilename = None, setEmbeddedLinkProtocol = None, setEmbeddedLinkProtocolCode = None, setEmbeddedLinkURL = None, setEmergencyContact = None, setFieldDisplayName = None, setFieldGroup = None, setFieldGroupCode = None, setFieldID = None, setFieldIsRelationship = None, setFieldLabel = None, setFieldName = None, setFieldPath = None, setFieldRelationship = None, setGUIDFieldPath = None, setHasBackingObject = None, setHasSharedValue = None, setHealthConditionIDs = None, setHealthProviderExcludeDentalInsurance = None, setHealthProviderExcludeDentist = None, setHealthProviderExcludeDentistOffice = None, setHealthProviderExcludeEmail = None, setHealthProviderExcludeHealthInsurance = None, setHealthProviderExcludeHospital = None, setHealthProviderExcludePhone = None, setHealthProviderExcludePrimaryPhysician = None, setHtmlDescription = None, setHtmlLabel = None, setHtmlOptions = None, setIncludeCECSInStudentSelector = None, setIsNewStudentEnrollmentElement = None, setIsRequiredElement = None, setLabelOverrides = None, setLanguageOption = None, setLanguageOptionCode = None, setLinkProtocol = None, setLinkProtocolCode = None, setMaxNumberEmergencyContacts = None, setMaxUploadFileSize = None, setMaxUploadFileSizeUnit = None, setMaxUploadFileSizeUnitCode = None, setMediaID = None, setMergeMarkupSet = None, setMergeMarkupSetDescription = None, setMergeMarkupSetLabel = None, setModifiedTime = None, setNewStudentEnrollmentGuardianRequireDriversLicense = None, setNewStudentEnrollmentGuardianUseVehicleInformation = None, setNewStudentEnrollmentRelationshipRequired = None, setNewStudentEnrollmentShowCustodialInformation = None, setNewStudentEnrollmentUseAddSecondFamily = None, setOrder = None, setParameterData = None, setParameters = None, setPaymentEndDate = None, setPaymentStartDate = None, setPlanID = None, setPostfixText = None, setPrefixText = None, setRaceEthnicityMessage = None, setRaceEthnicityMessageInSpanish = None, setRelationshipRequiredOnFamilyInformation = None, setRenderAgreement = None, setRenderInstructions = None, setRenderLanguageOptions = None, setRenderWeight = None, setRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = None, setRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = None, setSharedValueUsesNotShared = None, setShowCustodialOnFamilyInformation = None, setShowVehicleInformationOnEmergencyContact = None, setShowVehicleOnFamilyInformation = None, setStepID = None, setSupportsLabelOverrides = None, setType = None, setTypeCode = None, setUploadType = None, setUploadTypeCode = None, setUrl = None, setUrlDisplayName = None, setUserDownloadDisplayText = None, setUserDownloadInstructions = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserUploadDescription = None, setUserUploadLabel = None, setValidUploadFileTypes = None, setYesNoResponse = None, setYesNoResponseCode = None, returnElementID = False, returnAdminCanEdit = False, returnAgreementMessage = False, returnAllowsUserInteraction = False, returnApprovalType = False, returnApprovalTypeCode = False, returnCodeListFieldName = False, returnCodeListFieldPath = False, returnCodeListType = False, returnCodeListTypeCode = False, returnCodeListTypeLabel = False, returnComboboxDefaultValue = False, returnComboboxTextValue = False, returnCommonColorPickerValue = False, returnCommonFontAlignmentValue = False, returnCommonTextValue = False, returnCommonType = False, returnCommonTypeCode = False, returnCoverageEndDate = False, returnCoverageStartDate = False, returnCreatedTime = False, returnDataGridXML = False, returnDescription = False, returnDistrictID = False, returnElementGroupID = False, returnEmbeddedLinkFullFilename = False, returnEmbeddedLinkProtocol = False, returnEmbeddedLinkProtocolCode = False, returnEmbeddedLinkURL = False, returnEmergencyContact = False, returnFieldDisplayName = False, returnFieldGroup = False, returnFieldGroupCode = False, returnFieldID = False, returnFieldIsRelationship = False, returnFieldLabel = False, returnFieldName = False, returnFieldPath = False, returnFieldRelationship = False, returnGUIDFieldPath = False, returnHasBackingObject = False, returnHasSharedValue = False, returnHealthConditionIDs = False, returnHealthProviderExcludeDentalInsurance = False, returnHealthProviderExcludeDentist = False, returnHealthProviderExcludeDentistOffice = False, returnHealthProviderExcludeEmail = False, returnHealthProviderExcludeHealthInsurance = False, returnHealthProviderExcludeHospital = False, returnHealthProviderExcludePhone = False, returnHealthProviderExcludePrimaryPhysician = False, returnHtmlDescription = False, returnHtmlLabel = False, returnHtmlOptions = False, returnIncludeCECSInStudentSelector = False, returnIsNewStudentEnrollmentElement = False, returnIsRequiredElement = False, returnLabelOverrides = False, returnLanguageOption = False, returnLanguageOptionCode = False, returnLinkProtocol = False, returnLinkProtocolCode = False, returnMaxNumberEmergencyContacts = False, returnMaxUploadFileSize = False, returnMaxUploadFileSizeUnit = False, returnMaxUploadFileSizeUnitCode = False, returnMediaID = False, returnMergeMarkupSet = False, returnMergeMarkupSetDescription = False, returnMergeMarkupSetLabel = False, returnModifiedTime = False, returnNewStudentEnrollmentGuardianRequireDriversLicense = False, returnNewStudentEnrollmentGuardianUseVehicleInformation = False, returnNewStudentEnrollmentRelationshipRequired = False, returnNewStudentEnrollmentShowCustodialInformation = False, returnNewStudentEnrollmentUseAddSecondFamily = False, returnOrder = False, returnParameterData = False, returnParameters = False, returnPaymentEndDate = False, returnPaymentStartDate = False, returnPlanID = False, returnPostfixText = False, returnPrefixText = False, returnRaceEthnicityMessage = False, returnRaceEthnicityMessageInSpanish = False, returnRelationshipRequiredOnFamilyInformation = False, returnRenderAgreement = False, returnRenderInstructions = False, returnRenderLanguageOptions = False, returnRenderWeight = False, returnRequireDriversLicenseIfAllowStudentPickupOnEmergencyContact = False, returnRequireDriversLicenseIfAllowStudentPickupOnFamilyInformation = False, returnSharedValueUsesNotShared = False, returnShowCustodialOnFamilyInformation = False, returnShowVehicleInformationOnEmergencyContact = False, returnShowVehicleOnFamilyInformation = False, returnStepID = False, returnSupportsLabelOverrides = False, returnType = False, returnTypeCode = False, returnUploadType = False, returnUploadTypeCode = False, returnUrl = False, returnUrlDisplayName = False, returnUserDownloadDisplayText = False, returnUserDownloadInstructions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserUploadDescription = False, returnUserUploadLabel = False, returnValidUploadFileTypes = False, returnYesNoResponse = False, returnYesNoResponseCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElement(ElementID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Element/" + str(ElementID), verb = "delete")


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

def getElementGroup(ElementGroupID, EntityID = 1, returnElementGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "get", return_params_list = return_params)

def modifyElementGroup(ElementGroupID, EntityID = 1, setElementGroupID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElementGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElementGroup(EntityID = 1, setElementGroupID = None, setCreatedTime = None, setModifiedTime = None, setName = None, setSkywardHash = None, setSkywardID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElementGroupID = False, returnCreatedTime = False, returnModifiedTime = False, returnName = False, returnSkywardHash = False, returnSkywardID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElementGroup(ElementGroupID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroup/" + str(ElementGroupID), verb = "delete")


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

def getElementGroupTemplate(ElementGroupTemplateID, EntityID = 1, returnElementGroupTemplateID = False, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "get", return_params_list = return_params)

def modifyElementGroupTemplate(ElementGroupTemplateID, EntityID = 1, setElementGroupTemplateID = None, setCreatedTime = None, setElementGroupID = None, setModifiedTime = None, setOrder = None, setParameterData = None, setSkywardHash = None, setSkywardID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElementGroupTemplateID = False, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElementGroupTemplate(EntityID = 1, setElementGroupTemplateID = None, setCreatedTime = None, setElementGroupID = None, setModifiedTime = None, setOrder = None, setParameterData = None, setSkywardHash = None, setSkywardID = None, setType = None, setTypeCode = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnElementGroupTemplateID = False, returnCreatedTime = False, returnElementGroupID = False, returnModifiedTime = False, returnOrder = False, returnParameterData = False, returnSkywardHash = False, returnSkywardID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElementGroupTemplate(ElementGroupTemplateID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementGroupTemplate/" + str(ElementGroupTemplateID), verb = "delete")


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

def getElementStatus(ElementStatusID, EntityID = 1, returnElementStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "get", return_params_list = return_params)

def modifyElementStatus(ElementStatusID, EntityID = 1, setElementStatusID = None, setCreatedTime = None, setDenialMessage = None, setElementID = None, setFieldGroupLabelAndFieldFieldGroupOriginalValue = None, setFieldGroupLabelAndFieldFieldGroupRequestedValue = None, setIsReadOnly = None, setMediaIDAttachment = None, setModifiedTime = None, setNeedsAdminReviewSave = None, setOriginalValue = None, setReportDataOriginalValue = None, setReportDataRequestedValue = None, setRequestedValue = None, setSharedElementStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepStatusID = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserSubmitted = None, setValidationMessage = None, returnElementStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElementStatus(EntityID = 1, setElementStatusID = None, setCreatedTime = None, setDenialMessage = None, setElementID = None, setFieldGroupLabelAndFieldFieldGroupOriginalValue = None, setFieldGroupLabelAndFieldFieldGroupRequestedValue = None, setIsReadOnly = None, setMediaIDAttachment = None, setModifiedTime = None, setNeedsAdminReviewSave = None, setOriginalValue = None, setReportDataOriginalValue = None, setReportDataRequestedValue = None, setRequestedValue = None, setSharedElementStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepStatusID = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserSubmitted = None, setValidationMessage = None, returnElementStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnElementID = False, returnFieldGroupLabelAndFieldFieldGroupOriginalValue = False, returnFieldGroupLabelAndFieldFieldGroupRequestedValue = False, returnIsReadOnly = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNeedsAdminReviewSave = False, returnOriginalValue = False, returnReportDataOriginalValue = False, returnReportDataRequestedValue = False, returnRequestedValue = False, returnSharedElementStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepStatusID = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserSubmitted = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElementStatus(ElementStatusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatus/" + str(ElementStatusID), verb = "delete")


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

def getElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1, returnElementStatusSurveyAnswerID = False, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "get", return_params_list = return_params)

def modifyElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1, setElementStatusSurveyAnswerID = None, setColumnName = None, setCreatedTime = None, setElementStatusID = None, setModifiedTime = None, setNameID = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnElementStatusSurveyAnswerID = False, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "post", return_params_list = return_params, payload = payload_params)

def createElementStatusSurveyAnswer(EntityID = 1, setElementStatusSurveyAnswerID = None, setColumnName = None, setCreatedTime = None, setElementStatusID = None, setModifiedTime = None, setNameID = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnElementStatusSurveyAnswerID = False, returnColumnName = False, returnCreatedTime = False, returnElementStatusID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteElementStatusSurveyAnswer(ElementStatusSurveyAnswerID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/ElementStatusSurveyAnswer/" + str(ElementStatusSurveyAnswerID), verb = "delete")


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

def getMassPrintHistory(MassPrintHistoryID, EntityID = 1, returnMassPrintHistoryID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "get", return_params_list = return_params)

def modifyMassPrintHistory(MassPrintHistoryID, EntityID = 1, setMassPrintHistoryID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setOnlineFormID = None, setRequestIdentifier = None, setSendMessageOnComplete = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnMassPrintHistoryID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "post", return_params_list = return_params, payload = payload_params)

def createMassPrintHistory(EntityID = 1, setMassPrintHistoryID = None, setCreatedTime = None, setMediaID = None, setModifiedTime = None, setOnlineFormID = None, setRequestIdentifier = None, setSendMessageOnComplete = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWorkflowInstanceID = None, returnMassPrintHistoryID = False, returnCreatedTime = False, returnMediaID = False, returnModifiedTime = False, returnOnlineFormID = False, returnRequestIdentifier = False, returnSendMessageOnComplete = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWorkflowInstanceID = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteMassPrintHistory(MassPrintHistoryID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/MassPrintHistory/" + str(MassPrintHistoryID), verb = "delete")


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

def getNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1, returnNewStudentEnrollmentGuardianDataID = False, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "get", return_params_list = return_params)

def modifyNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1, setNewStudentEnrollmentGuardianDataID = None, setAddGuardian = None, setAllowStudentPickup = None, setColor = None, setCreatedTime = None, setCreateNewGuardian = None, setDeleteGuardian = None, setDriversLicenseNumber = None, setFamilyGuardianID = None, setFirstName = None, setGender = None, setGenderCode = None, setIsCustodialGuardian = None, setLastName = None, setLicensePlateNumber = None, setMakeModel = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNameSuffixID = None, setNameVehicleID = None, setOnScreenID = None, setRank = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVehicleID = None, setVIN = None, setYear = None, returnNewStudentEnrollmentGuardianDataID = False, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNewStudentEnrollmentGuardianData(EntityID = 1, setNewStudentEnrollmentGuardianDataID = None, setAddGuardian = None, setAllowStudentPickup = None, setColor = None, setCreatedTime = None, setCreateNewGuardian = None, setDeleteGuardian = None, setDriversLicenseNumber = None, setFamilyGuardianID = None, setFirstName = None, setGender = None, setGenderCode = None, setIsCustodialGuardian = None, setLastName = None, setLicensePlateNumber = None, setMakeModel = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setNameSuffixID = None, setNameVehicleID = None, setOnScreenID = None, setRank = None, setRelationshipID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setVehicleID = None, setVIN = None, setYear = None, returnNewStudentEnrollmentGuardianDataID = False, returnAddGuardian = False, returnAllowStudentPickup = False, returnColor = False, returnCreatedTime = False, returnCreateNewGuardian = False, returnDeleteGuardian = False, returnDriversLicenseNumber = False, returnFamilyGuardianID = False, returnFirstName = False, returnGender = False, returnGenderCode = False, returnIsCustodialGuardian = False, returnLastName = False, returnLicensePlateNumber = False, returnMakeModel = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNameSuffixID = False, returnNameVehicleID = False, returnOnScreenID = False, returnRank = False, returnRelationshipID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnVehicleID = False, returnVIN = False, returnYear = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNewStudentEnrollmentGuardianData(NewStudentEnrollmentGuardianDataID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentGuardianData/" + str(NewStudentEnrollmentGuardianDataID), verb = "delete")


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

def getNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1, returnNewStudentEnrollmentUserDataID = False, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "get", return_params_list = return_params)

def modifyNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1, setNewStudentEnrollmentUserDataID = None, setCity = None, setCreatedTime = None, setEmailAddress = None, setModifiedTime = None, setPhoneNumber = None, setPhysicalStreetName = None, setPhysicalStreetNumber = None, setPreviouslyInDistrict = None, setState = None, setUnit = None, setUnitNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSubmittedBy = None, setZipCode = None, returnNewStudentEnrollmentUserDataID = False, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "post", return_params_list = return_params, payload = payload_params)

def createNewStudentEnrollmentUserData(EntityID = 1, setNewStudentEnrollmentUserDataID = None, setCity = None, setCreatedTime = None, setEmailAddress = None, setModifiedTime = None, setPhoneNumber = None, setPhysicalStreetName = None, setPhysicalStreetNumber = None, setPreviouslyInDistrict = None, setState = None, setUnit = None, setUnitNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSubmittedBy = None, setZipCode = None, returnNewStudentEnrollmentUserDataID = False, returnCity = False, returnCreatedTime = False, returnEmailAddress = False, returnModifiedTime = False, returnPhoneNumber = False, returnPhysicalStreetName = False, returnPhysicalStreetNumber = False, returnPreviouslyInDistrict = False, returnState = False, returnUnit = False, returnUnitNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnZipCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteNewStudentEnrollmentUserData(NewStudentEnrollmentUserDataID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/NewStudentEnrollmentUserData/" + str(NewStudentEnrollmentUserDataID), verb = "delete")


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

def getOnlineForm(OnlineFormID, EntityID = 1, returnOnlineFormID = False, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnThankYouPageLinkFullFilename = False, returnThankYouPageLinkProtocol = False, returnThankYouPageLinkProtocolCode = False, returnThankYouPageLinkUrl = False, returnThankYouPageLinkUrlDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "get", return_params_list = return_params)

def modifyOnlineForm(OnlineFormID, EntityID = 1, setOnlineFormID = None, setActivitiesSearchConditionFilter = None, setAdministrativeSearchConditionFilter = None, setAllowContact = None, setAllowMultipleFormsPerUser = None, setContactHash = None, setCreatedTime = None, setCutoffTime = None, setDescription = None, setDisplayForNonPrimaryFamily = None, setEmployeeSearchConditionFilter = None, setEmployeeStandardFilterCollectionJson = None, setEndDate = None, setFamilySearchConditionFilter = None, setFilter = None, setFilterSubType = None, setFilterSubTypeCode = None, setHideCurrentValueOnApproval = None, setIconCode = None, setIncludeAdobeAcrobatLink = None, setIncludeInActivitiesPortal = None, setIncludeInAdministrativePortal = None, setIncludeInEmployeePortal = None, setIncludeInFamilyPortal = None, setIncludeInNewStudentEnrollmentPortal = None, setIncludeInStudentPortal = None, setIncludeInTeacherPortal = None, setInUseByUsers = None, setIsPublished = None, setIsUserInitiated = None, setLimitToOnePerDay = None, setMainPageEmbeddedLinkFullFilename = None, setMainPageEmbeddedLinkProtocol = None, setMainPageEmbeddedLinkProtocolCode = None, setMainPageEmbeddedLinkUrl = None, setMessage = None, setMessageAfterSubmission = None, setMessageForNonPrimaryFamily = None, setModifiedTime = None, setModule = None, setName = None, setNewStudentEnrollmentSearchConditionFilter = None, setNoApprovalNeeded = None, setObject = None, setOnlineFormIDClonedFrom = None, setOnlineFormStatusExistsToday = None, setOnlineFormTypeID = None, setPortals = None, setPortalsIncludedIn = None, setPortalType = None, setPortalTypeCode = None, setReviewStepMessage = None, setSchoolYearID = None, setSendFamilyAccessEmail = None, setShowDescriptionOnTile = None, setSkipInstructionsPage = None, setSkipReviewPage = None, setSkipThankYouPage = None, setStartDate = None, setStudentSearchConditionFilter = None, setTeacherSearchConditionFilter = None, setThankYouPageLinkFullFilename = None, setThankYouPageLinkProtocol = None, setThankYouPageLinkProtocolCode = None, setThankYouPageLinkUrl = None, setThankYouPageLinkUrlDisplayName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithinCutoffTime = None, setYearType = None, setYearTypeCode = None, returnOnlineFormID = False, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnThankYouPageLinkFullFilename = False, returnThankYouPageLinkProtocol = False, returnThankYouPageLinkProtocolCode = False, returnThankYouPageLinkUrl = False, returnThankYouPageLinkUrlDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineForm(EntityID = 1, setOnlineFormID = None, setActivitiesSearchConditionFilter = None, setAdministrativeSearchConditionFilter = None, setAllowContact = None, setAllowMultipleFormsPerUser = None, setContactHash = None, setCreatedTime = None, setCutoffTime = None, setDescription = None, setDisplayForNonPrimaryFamily = None, setEmployeeSearchConditionFilter = None, setEmployeeStandardFilterCollectionJson = None, setEndDate = None, setFamilySearchConditionFilter = None, setFilter = None, setFilterSubType = None, setFilterSubTypeCode = None, setHideCurrentValueOnApproval = None, setIconCode = None, setIncludeAdobeAcrobatLink = None, setIncludeInActivitiesPortal = None, setIncludeInAdministrativePortal = None, setIncludeInEmployeePortal = None, setIncludeInFamilyPortal = None, setIncludeInNewStudentEnrollmentPortal = None, setIncludeInStudentPortal = None, setIncludeInTeacherPortal = None, setInUseByUsers = None, setIsPublished = None, setIsUserInitiated = None, setLimitToOnePerDay = None, setMainPageEmbeddedLinkFullFilename = None, setMainPageEmbeddedLinkProtocol = None, setMainPageEmbeddedLinkProtocolCode = None, setMainPageEmbeddedLinkUrl = None, setMessage = None, setMessageAfterSubmission = None, setMessageForNonPrimaryFamily = None, setModifiedTime = None, setModule = None, setName = None, setNewStudentEnrollmentSearchConditionFilter = None, setNoApprovalNeeded = None, setObject = None, setOnlineFormIDClonedFrom = None, setOnlineFormStatusExistsToday = None, setOnlineFormTypeID = None, setPortals = None, setPortalsIncludedIn = None, setPortalType = None, setPortalTypeCode = None, setReviewStepMessage = None, setSchoolYearID = None, setSendFamilyAccessEmail = None, setShowDescriptionOnTile = None, setSkipInstructionsPage = None, setSkipReviewPage = None, setSkipThankYouPage = None, setStartDate = None, setStudentSearchConditionFilter = None, setTeacherSearchConditionFilter = None, setThankYouPageLinkFullFilename = None, setThankYouPageLinkProtocol = None, setThankYouPageLinkProtocolCode = None, setThankYouPageLinkUrl = None, setThankYouPageLinkUrlDisplayName = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setWithinCutoffTime = None, setYearType = None, setYearTypeCode = None, returnOnlineFormID = False, returnActivitiesSearchConditionFilter = False, returnAdministrativeSearchConditionFilter = False, returnAllowContact = False, returnAllowMultipleFormsPerUser = False, returnContactHash = False, returnCreatedTime = False, returnCutoffTime = False, returnDescription = False, returnDisplayForNonPrimaryFamily = False, returnEmployeeSearchConditionFilter = False, returnEmployeeStandardFilterCollectionJson = False, returnEndDate = False, returnFamilySearchConditionFilter = False, returnFilter = False, returnFilterSubType = False, returnFilterSubTypeCode = False, returnHideCurrentValueOnApproval = False, returnIconCode = False, returnIncludeAdobeAcrobatLink = False, returnIncludeInActivitiesPortal = False, returnIncludeInAdministrativePortal = False, returnIncludeInEmployeePortal = False, returnIncludeInFamilyPortal = False, returnIncludeInNewStudentEnrollmentPortal = False, returnIncludeInStudentPortal = False, returnIncludeInTeacherPortal = False, returnInUseByUsers = False, returnIsPublished = False, returnIsUserInitiated = False, returnLimitToOnePerDay = False, returnMainPageEmbeddedLinkFullFilename = False, returnMainPageEmbeddedLinkProtocol = False, returnMainPageEmbeddedLinkProtocolCode = False, returnMainPageEmbeddedLinkUrl = False, returnMessage = False, returnMessageAfterSubmission = False, returnMessageForNonPrimaryFamily = False, returnModifiedTime = False, returnModule = False, returnName = False, returnNewStudentEnrollmentSearchConditionFilter = False, returnNoApprovalNeeded = False, returnObject = False, returnOnlineFormIDClonedFrom = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormTypeID = False, returnPortals = False, returnPortalsIncludedIn = False, returnPortalType = False, returnPortalTypeCode = False, returnReviewStepMessage = False, returnSchoolYearID = False, returnSendFamilyAccessEmail = False, returnShowDescriptionOnTile = False, returnSkipInstructionsPage = False, returnSkipReviewPage = False, returnSkipThankYouPage = False, returnStartDate = False, returnStudentSearchConditionFilter = False, returnTeacherSearchConditionFilter = False, returnThankYouPageLinkFullFilename = False, returnThankYouPageLinkProtocol = False, returnThankYouPageLinkProtocolCode = False, returnThankYouPageLinkUrl = False, returnThankYouPageLinkUrlDisplayName = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithinCutoffTime = False, returnYearType = False, returnYearTypeCode = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineForm(OnlineFormID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineForm/" + str(OnlineFormID), verb = "delete")


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

def getOnlineFormClearance(OnlineFormClearanceID, EntityID = 1, returnOnlineFormClearanceID = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "get", return_params_list = return_params)

def modifyOnlineFormClearance(OnlineFormClearanceID, EntityID = 1, setOnlineFormClearanceID = None, setCreatedTime = None, setGroupIDSecurity = None, setModifiedTime = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormClearanceID = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormClearance(EntityID = 1, setOnlineFormClearanceID = None, setCreatedTime = None, setGroupIDSecurity = None, setModifiedTime = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormClearanceID = False, returnCreatedTime = False, returnGroupIDSecurity = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormClearance(OnlineFormClearanceID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormClearance/" + str(OnlineFormClearanceID), verb = "delete")


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

def getOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1, returnOnlineFormDateExceptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "get", return_params_list = return_params)

def modifyOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1, setOnlineFormDateExceptionID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormDateExceptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormDateException(EntityID = 1, setOnlineFormDateExceptionID = None, setCreatedTime = None, setModifiedTime = None, setObjectID = None, setObjectPrimaryKey = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormDateExceptionID = False, returnCreatedTime = False, returnModifiedTime = False, returnObjectID = False, returnObjectPrimaryKey = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormDateException(OnlineFormDateExceptionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormDateException/" + str(OnlineFormDateExceptionID), verb = "delete")


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

def getOnlineFormEntity(OnlineFormEntityID, EntityID = 1, returnOnlineFormEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "get", return_params_list = return_params)

def modifyOnlineFormEntity(OnlineFormEntityID, EntityID = 1, setOnlineFormEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormEntity(EntityID = 1, setOnlineFormEntityID = None, setCreatedTime = None, setEntityID = None, setModifiedTime = None, setOnlineFormID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormEntityID = False, returnCreatedTime = False, returnEntityID = False, returnModifiedTime = False, returnOnlineFormID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormEntity(OnlineFormEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormEntity/" + str(OnlineFormEntityID), verb = "delete")


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

def getOnlineFormStatus(OnlineFormStatusID, EntityID = 1, returnOnlineFormStatusID = False, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnIsOutsideAddressRangeSchoolPaths = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "get", return_params_list = return_params)

def modifyOnlineFormStatus(OnlineFormStatusID, EntityID = 1, setOnlineFormStatusID = None, setApprovalRevoked = None, setCompletedByAdmin = None, setCreatedTime = None, setDenialDateTime = None, setDenialMessage = None, setFullNameLFMSubmittedFor = None, setFullNameLFMSubmittedForOverride = None, setIsOutsideAddressRanges = None, setIsOutsideAddressRangeSchoolPaths = None, setModifiedTime = None, setNameID = None, setOnlineFormEntityID = None, setSecondaryID = None, setStatusType = None, setStatusTypeCode = None, setSubmittedDateTime = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSubmittedBy = None, setWithinCutoffTime = None, returnOnlineFormStatusID = False, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnIsOutsideAddressRangeSchoolPaths = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormStatus(EntityID = 1, setOnlineFormStatusID = None, setApprovalRevoked = None, setCompletedByAdmin = None, setCreatedTime = None, setDenialDateTime = None, setDenialMessage = None, setFullNameLFMSubmittedFor = None, setFullNameLFMSubmittedForOverride = None, setIsOutsideAddressRanges = None, setIsOutsideAddressRangeSchoolPaths = None, setModifiedTime = None, setNameID = None, setOnlineFormEntityID = None, setSecondaryID = None, setStatusType = None, setStatusTypeCode = None, setSubmittedDateTime = None, setUserIDApprover = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setUserIDSubmittedBy = None, setWithinCutoffTime = None, returnOnlineFormStatusID = False, returnApprovalRevoked = False, returnCompletedByAdmin = False, returnCreatedTime = False, returnDenialDateTime = False, returnDenialMessage = False, returnFullNameLFMSubmittedFor = False, returnFullNameLFMSubmittedForOverride = False, returnIsOutsideAddressRanges = False, returnIsOutsideAddressRangeSchoolPaths = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormEntityID = False, returnSecondaryID = False, returnStatusType = False, returnStatusTypeCode = False, returnSubmittedDateTime = False, returnUserIDApprover = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnUserIDSubmittedBy = False, returnWithinCutoffTime = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormStatus(OnlineFormStatusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatus/" + str(OnlineFormStatusID), verb = "delete")


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

def getOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1, returnOnlineFormStatusNameID = False, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "get", return_params_list = return_params)

def modifyOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1, setOnlineFormStatusNameID = None, setCreatedTime = None, setElementID = None, setModifiedTime = None, setNameID = None, setOnlineFormStatusID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormStatusNameID = False, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormStatusName(EntityID = 1, setOnlineFormStatusNameID = None, setCreatedTime = None, setElementID = None, setModifiedTime = None, setNameID = None, setOnlineFormStatusID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormStatusNameID = False, returnCreatedTime = False, returnElementID = False, returnModifiedTime = False, returnNameID = False, returnOnlineFormStatusID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormStatusName(OnlineFormStatusNameID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormStatusName/" + str(OnlineFormStatusNameID), verb = "delete")


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

def getOnlineFormType(OnlineFormTypeID, EntityID = 1, returnOnlineFormTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "get", return_params_list = return_params)

def modifyOnlineFormType(OnlineFormTypeID, EntityID = 1, setOnlineFormTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setLimitUsersToOneFormOfThisTypePerYear = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createOnlineFormType(EntityID = 1, setOnlineFormTypeID = None, setCode = None, setCodeDescription = None, setCreatedTime = None, setDescription = None, setDistrictID = None, setLimitUsersToOneFormOfThisTypePerYear = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormTypeID = False, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnLimitUsersToOneFormOfThisTypePerYear = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteOnlineFormType(OnlineFormTypeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/OnlineFormType/" + str(OnlineFormTypeID), verb = "delete")


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

def getSharedElementStatus(SharedElementStatusID, EntityID = 1, returnSharedElementStatusID = False, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "get", return_params_list = return_params)

def modifySharedElementStatus(SharedElementStatusID, EntityID = 1, setSharedElementStatusID = None, setCreatedTime = None, setElementType = None, setElementTypeCode = None, setFieldGroupType = None, setFieldGroupTypeCode = None, setMediaIDAttachment = None, setModifiedTime = None, setNameID = None, setSchoolYearID = None, setSecondaryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSharedElementStatusID = False, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createSharedElementStatus(EntityID = 1, setSharedElementStatusID = None, setCreatedTime = None, setElementType = None, setElementTypeCode = None, setFieldGroupType = None, setFieldGroupTypeCode = None, setMediaIDAttachment = None, setModifiedTime = None, setNameID = None, setSchoolYearID = None, setSecondaryID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValue = None, returnSharedElementStatusID = False, returnCreatedTime = False, returnElementType = False, returnElementTypeCode = False, returnFieldGroupType = False, returnFieldGroupTypeCode = False, returnMediaIDAttachment = False, returnModifiedTime = False, returnNameID = False, returnSchoolYearID = False, returnSecondaryID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValue = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteSharedElementStatus(SharedElementStatusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/SharedElementStatus/" + str(SharedElementStatusID), verb = "delete")


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

def getStaffContact(StaffContactID, EntityID = 1, returnStaffContactID = False, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "get", return_params_list = return_params)

def modifyStaffContact(StaffContactID, EntityID = 1, setStaffContactID = None, setCreatedTime = None, setModifiedTime = None, setOnlineFormID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffContactID = False, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStaffContact(EntityID = 1, setStaffContactID = None, setCreatedTime = None, setModifiedTime = None, setOnlineFormID = None, setStaffID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStaffContactID = False, returnCreatedTime = False, returnModifiedTime = False, returnOnlineFormID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStaffContact(StaffContactID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StaffContact/" + str(StaffContactID), verb = "delete")


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

def getStep(StepID, EntityID = 1, returnStepID = False, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "get", return_params_list = return_params)

def modifyStep(StepID, EntityID = 1, setStepID = None, setCreatedTime = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setModifiedTime = None, setName = None, setOnlineFormID = None, setOrder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStepID = False, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStep(EntityID = 1, setStepID = None, setCreatedTime = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setModifiedTime = None, setName = None, setOnlineFormID = None, setOrder = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnStepID = False, returnCreatedTime = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStep(StepID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/Step/" + str(StepID), verb = "delete")


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

def getStepStatus(StepStatusID, EntityID = 1, returnStepStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "get", return_params_list = return_params)

def modifyStepStatus(StepStatusID, EntityID = 1, setStepStatusID = None, setCreatedTime = None, setDenialMessage = None, setHasNextStepStatus = None, setHasPreviousStepStatus = None, setModifiedTime = None, setNextStepStatusID = None, setOnlineFormStatusID = None, setPreviousStepStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidationMessage = None, returnStepStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "post", return_params_list = return_params, payload = payload_params)

def createStepStatus(EntityID = 1, setStepStatusID = None, setCreatedTime = None, setDenialMessage = None, setHasNextStepStatus = None, setHasPreviousStepStatus = None, setModifiedTime = None, setNextStepStatusID = None, setOnlineFormStatusID = None, setPreviousStepStatusID = None, setStatusType = None, setStatusTypeCode = None, setStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, setValidationMessage = None, returnStepStatusID = False, returnCreatedTime = False, returnDenialMessage = False, returnHasNextStepStatus = False, returnHasPreviousStepStatus = False, returnModifiedTime = False, returnNextStepStatusID = False, returnOnlineFormStatusID = False, returnPreviousStepStatusID = False, returnStatusType = False, returnStatusTypeCode = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnValidationMessage = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteStepStatus(StepStatusID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/StepStatus/" + str(StepStatusID), verb = "delete")


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

def getTeacherOnlineForm(OnlineFormEntityID, EntityID = 1, returnOnlineFormEntityID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "get", return_params_list = return_params)

def modifyTeacherOnlineForm(OnlineFormEntityID, EntityID = 1, setOnlineFormEntityID = None, setCreatedTime = None, setDisplayPeriodID = None, setEntityID = None, setFilterInformation = None, setModifiedTime = None, setNameID = None, setNoFormsExistOfSameType = None, setNoStartedFormsExist = None, setOnlineFormID = None, setOnlineFormStatusExistsToday = None, setOnlineFormStatusID = None, setOnlineFormTypeID = None, setSchoolYearID = None, setSecondaryID = None, setSectionID = None, setStatusType = None, setStatusTypeCode = None, setStatusTypeSortable = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormEntityID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTeacherOnlineForm(EntityID = 1, setOnlineFormEntityID = None, setCreatedTime = None, setDisplayPeriodID = None, setEntityID = None, setFilterInformation = None, setModifiedTime = None, setNameID = None, setNoFormsExistOfSameType = None, setNoStartedFormsExist = None, setOnlineFormID = None, setOnlineFormStatusExistsToday = None, setOnlineFormStatusID = None, setOnlineFormTypeID = None, setSchoolYearID = None, setSecondaryID = None, setSectionID = None, setStatusType = None, setStatusTypeCode = None, setStatusTypeSortable = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnOnlineFormEntityID = False, returnCreatedTime = False, returnDisplayPeriodID = False, returnEntityID = False, returnFilterInformation = False, returnModifiedTime = False, returnNameID = False, returnNoFormsExistOfSameType = False, returnNoStartedFormsExist = False, returnOnlineFormID = False, returnOnlineFormStatusExistsToday = False, returnOnlineFormStatusID = False, returnOnlineFormTypeID = False, returnSchoolYearID = False, returnSecondaryID = False, returnSectionID = False, returnStatusType = False, returnStatusTypeCode = False, returnStatusTypeSortable = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTeacherOnlineForm(OnlineFormEntityID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TeacherOnlineForm/" + str(OnlineFormEntityID), verb = "delete")


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

def getTempCertification(TempCertificationID, EntityID = 1, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "get", return_params_list = return_params)

def modifyTempCertification(TempCertificationID, EntityID = 1, setTempCertificationID = None, setCertificationID = None, setCertificationNumber = None, setCertificationTypeID = None, setCreatedTime = None, setEmployeeID = None, setExpirationDate = None, setInstitutionID = None, setIsDelete = None, setIssueDate = None, setModifiedTime = None, setOnScreenCount = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempCertification(EntityID = 1, setTempCertificationID = None, setCertificationID = None, setCertificationNumber = None, setCertificationTypeID = None, setCreatedTime = None, setEmployeeID = None, setExpirationDate = None, setInstitutionID = None, setIsDelete = None, setIssueDate = None, setModifiedTime = None, setOnScreenCount = None, setStateID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempCertificationID = False, returnCertificationID = False, returnCertificationNumber = False, returnCertificationTypeID = False, returnCreatedTime = False, returnEmployeeID = False, returnExpirationDate = False, returnInstitutionID = False, returnIsDelete = False, returnIssueDate = False, returnModifiedTime = False, returnOnScreenCount = False, returnStateID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempCertification(TempCertificationID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempCertification/" + str(TempCertificationID), verb = "delete")


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

def getTempDataGridRow(TempDataGridRowID, EntityID = 1, returnTempDataGridRowID = False, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "get", return_params_list = return_params)

def modifyTempDataGridRow(TempDataGridRowID, EntityID = 1, setTempDataGridRowID = None, setColumnHeader = None, setControlType = None, setControlTypeCode = None, setCreatedTime = None, setDefaultValue = None, setModifiedTime = None, setOptions = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDataGridRowID = False, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDataGridRow(EntityID = 1, setTempDataGridRowID = None, setColumnHeader = None, setControlType = None, setControlTypeCode = None, setCreatedTime = None, setDefaultValue = None, setModifiedTime = None, setOptions = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDataGridRowID = False, returnColumnHeader = False, returnControlType = False, returnControlTypeCode = False, returnCreatedTime = False, returnDefaultValue = False, returnModifiedTime = False, returnOptions = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDataGridRow(TempDataGridRowID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDataGridRow/" + str(TempDataGridRowID), verb = "delete")


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

def getTempDegree(TempDegreeID, EntityID = 1, returnTempDegreeID = False, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "get", return_params_list = return_params)

def modifyTempDegree(TempDegreeID, EntityID = 1, setTempDegreeID = None, setAdditionalCredits = None, setApprovedDate = None, setCreatedTime = None, setCredits = None, setDegreeID = None, setDegreeTypeID = None, setEmployeeID = None, setGPA = None, setInstitutionID = None, setIsDelete = None, setModifiedTime = None, setOnScreenCount = None, setReceivedDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDegreeID = False, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDegree(EntityID = 1, setTempDegreeID = None, setAdditionalCredits = None, setApprovedDate = None, setCreatedTime = None, setCredits = None, setDegreeID = None, setDegreeTypeID = None, setEmployeeID = None, setGPA = None, setInstitutionID = None, setIsDelete = None, setModifiedTime = None, setOnScreenCount = None, setReceivedDate = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDegreeID = False, returnAdditionalCredits = False, returnApprovedDate = False, returnCreatedTime = False, returnCredits = False, returnDegreeID = False, returnDegreeTypeID = False, returnEmployeeID = False, returnGPA = False, returnInstitutionID = False, returnIsDelete = False, returnModifiedTime = False, returnOnScreenCount = False, returnReceivedDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDegree(TempDegreeID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDegree/" + str(TempDegreeID), verb = "delete")


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

def getTempDependent(TempDependentID, EntityID = 1, returnTempDependentID = False, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "get", return_params_list = return_params)

def modifyTempDependent(TempDependentID, EntityID = 1, setTempDependentID = None, setBirthDate = None, setCreatedTime = None, setDependentID = None, setFirstName = None, setIsDelete = None, setIsExistingRecord = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setOnScreenCount = None, setRelationshipID = None, setSocialSecurityNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDependentID = False, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempDependent(EntityID = 1, setTempDependentID = None, setBirthDate = None, setCreatedTime = None, setDependentID = None, setFirstName = None, setIsDelete = None, setIsExistingRecord = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setOnScreenCount = None, setRelationshipID = None, setSocialSecurityNumber = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempDependentID = False, returnBirthDate = False, returnCreatedTime = False, returnDependentID = False, returnFirstName = False, returnIsDelete = False, returnIsExistingRecord = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnOnScreenCount = False, returnRelationshipID = False, returnSocialSecurityNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempDependent(TempDependentID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempDependent/" + str(TempDependentID), verb = "delete")


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

def getTempEmergencyContact(TempEmergencyContactID, EntityID = 1, returnTempEmergencyContactID = False, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "get", return_params_list = return_params)

def modifyTempEmergencyContact(TempEmergencyContactID, EntityID = 1, setTempEmergencyContactID = None, setAddEmergencyContact = None, setAllowStudentPickup = None, setComment = None, setCreatedTime = None, setCreateNewEmergencyContactName = None, setDeleteEmergencyContact = None, setDriversLicenseNumber = None, setEmergencyContactID = None, setFirstName = None, setForSecondFamily = None, setIsAlsoGuardian = None, setIsBusiness = None, setIsHealthProfessionalName = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setOnScreenID = None, setPrimaryEmailEmailAddress = None, setPrimaryEmailEmailTypeID = None, setPrimaryEmailNameEmailID = None, setPrimaryEmailPreventFamilyStudentAccessUpdates = None, setPrimaryPhoneExtension = None, setPrimaryPhoneNamePhoneID = None, setPrimaryPhonePhoneNumber = None, setPrimaryPhonePhoneTypeID = None, setPrimaryPhonePreventFamilyStudentAccessUpdates = None, setRank = None, setRelationshipID = None, setSecondEmailEmailAddress = None, setSecondEmailEmailTypeID = None, setSecondEmailNameEmailID = None, setSecondEmailPreventFamilyStudentAccessUpdates = None, setSecondPhoneExtension = None, setSecondPhoneNamePhoneID = None, setSecondPhonePhoneNumber = None, setSecondPhonePhoneTypeID = None, setSecondPhonePreventFamilyStudentAccessUpdates = None, setThirdEmailEmailAddress = None, setThirdEmailEmailTypeID = None, setThirdEmailNameEmailID = None, setThirdEmailPreventFamilyStudentAccessUpdates = None, setThirdPhoneExtension = None, setThirdPhoneNamePhoneID = None, setThirdPhonePhoneNumber = None, setThirdPhonePhoneTypeID = None, setThirdPhonePreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEmergencyContactID = False, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempEmergencyContact(EntityID = 1, setTempEmergencyContactID = None, setAddEmergencyContact = None, setAllowStudentPickup = None, setComment = None, setCreatedTime = None, setCreateNewEmergencyContactName = None, setDeleteEmergencyContact = None, setDriversLicenseNumber = None, setEmergencyContactID = None, setFirstName = None, setForSecondFamily = None, setIsAlsoGuardian = None, setIsBusiness = None, setIsHealthProfessionalName = None, setLastName = None, setMiddleName = None, setModifiedTime = None, setNameID = None, setOnScreenID = None, setPrimaryEmailEmailAddress = None, setPrimaryEmailEmailTypeID = None, setPrimaryEmailNameEmailID = None, setPrimaryEmailPreventFamilyStudentAccessUpdates = None, setPrimaryPhoneExtension = None, setPrimaryPhoneNamePhoneID = None, setPrimaryPhonePhoneNumber = None, setPrimaryPhonePhoneTypeID = None, setPrimaryPhonePreventFamilyStudentAccessUpdates = None, setRank = None, setRelationshipID = None, setSecondEmailEmailAddress = None, setSecondEmailEmailTypeID = None, setSecondEmailNameEmailID = None, setSecondEmailPreventFamilyStudentAccessUpdates = None, setSecondPhoneExtension = None, setSecondPhoneNamePhoneID = None, setSecondPhonePhoneNumber = None, setSecondPhonePhoneTypeID = None, setSecondPhonePreventFamilyStudentAccessUpdates = None, setThirdEmailEmailAddress = None, setThirdEmailEmailTypeID = None, setThirdEmailNameEmailID = None, setThirdEmailPreventFamilyStudentAccessUpdates = None, setThirdPhoneExtension = None, setThirdPhoneNamePhoneID = None, setThirdPhonePhoneNumber = None, setThirdPhonePhoneTypeID = None, setThirdPhonePreventFamilyStudentAccessUpdates = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempEmergencyContactID = False, returnAddEmergencyContact = False, returnAllowStudentPickup = False, returnComment = False, returnCreatedTime = False, returnCreateNewEmergencyContactName = False, returnDeleteEmergencyContact = False, returnDriversLicenseNumber = False, returnEmergencyContactID = False, returnFirstName = False, returnForSecondFamily = False, returnIsAlsoGuardian = False, returnIsBusiness = False, returnIsHealthProfessionalName = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnOnScreenID = False, returnPrimaryEmailEmailAddress = False, returnPrimaryEmailEmailTypeID = False, returnPrimaryEmailNameEmailID = False, returnPrimaryEmailPreventFamilyStudentAccessUpdates = False, returnPrimaryPhoneExtension = False, returnPrimaryPhoneNamePhoneID = False, returnPrimaryPhonePhoneNumber = False, returnPrimaryPhonePhoneTypeID = False, returnPrimaryPhonePreventFamilyStudentAccessUpdates = False, returnRank = False, returnRelationshipID = False, returnSecondEmailEmailAddress = False, returnSecondEmailEmailTypeID = False, returnSecondEmailNameEmailID = False, returnSecondEmailPreventFamilyStudentAccessUpdates = False, returnSecondPhoneExtension = False, returnSecondPhoneNamePhoneID = False, returnSecondPhonePhoneNumber = False, returnSecondPhonePhoneTypeID = False, returnSecondPhonePreventFamilyStudentAccessUpdates = False, returnThirdEmailEmailAddress = False, returnThirdEmailEmailTypeID = False, returnThirdEmailNameEmailID = False, returnThirdEmailPreventFamilyStudentAccessUpdates = False, returnThirdPhoneExtension = False, returnThirdPhoneNamePhoneID = False, returnThirdPhonePhoneNumber = False, returnThirdPhonePhoneTypeID = False, returnThirdPhonePreventFamilyStudentAccessUpdates = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempEmergencyContact/" + str(TempEmergencyContactID), verb = "delete")


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

def getTempError(TempErrorID, EntityID = 1, returnTempErrorID = False, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "get", return_params_list = return_params)

def modifyTempError(TempErrorID, EntityID = 1, setTempErrorID = None, setCreatedTime = None, setDescription = None, setMessage = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempErrorID = False, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempError(EntityID = 1, setTempErrorID = None, setCreatedTime = None, setDescription = None, setMessage = None, setModifiedTime = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempErrorID = False, returnCreatedTime = False, returnDescription = False, returnMessage = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempError(TempErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempError/" + str(TempErrorID), verb = "delete")


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

def getTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1, returnTempNewStudentEnrollmentGuardianEmailID = False, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "get", return_params_list = return_params)

def modifyTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1, setTempNewStudentEnrollmentGuardianEmailID = None, setAddEmail = None, setCreatedTime = None, setCreateNewEmail = None, setDeleteEmail = None, setEmailAddress = None, setEmailPreventFamilyStudentAccessUpdates = None, setEmailTypeID = None, setModifiedTime = None, setNameEmailID = None, setOnScreenID = None, setParentOnScreenID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNewStudentEnrollmentGuardianEmailID = False, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNewStudentEnrollmentGuardianEmail(EntityID = 1, setTempNewStudentEnrollmentGuardianEmailID = None, setAddEmail = None, setCreatedTime = None, setCreateNewEmail = None, setDeleteEmail = None, setEmailAddress = None, setEmailPreventFamilyStudentAccessUpdates = None, setEmailTypeID = None, setModifiedTime = None, setNameEmailID = None, setOnScreenID = None, setParentOnScreenID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNewStudentEnrollmentGuardianEmailID = False, returnAddEmail = False, returnCreatedTime = False, returnCreateNewEmail = False, returnDeleteEmail = False, returnEmailAddress = False, returnEmailPreventFamilyStudentAccessUpdates = False, returnEmailTypeID = False, returnModifiedTime = False, returnNameEmailID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNewStudentEnrollmentGuardianEmail(TempNewStudentEnrollmentGuardianEmailID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianEmail/" + str(TempNewStudentEnrollmentGuardianEmailID), verb = "delete")


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

def getTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1, returnTempNewStudentEnrollmentGuardianPhoneID = False, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "get", return_params_list = return_params)

def modifyTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1, setTempNewStudentEnrollmentGuardianPhoneID = None, setAddPhone = None, setCreatedTime = None, setCreateNewPhone = None, setDeletePhone = None, setExtension = None, setIsConfidential = None, setModifiedTime = None, setNamePhoneID = None, setOnScreenID = None, setParentOnScreenID = None, setPhoneNumber = None, setPhonePreventFamilyStudentAccessUpdates = None, setPhoneTypeID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNewStudentEnrollmentGuardianPhoneID = False, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempNewStudentEnrollmentGuardianPhone(EntityID = 1, setTempNewStudentEnrollmentGuardianPhoneID = None, setAddPhone = None, setCreatedTime = None, setCreateNewPhone = None, setDeletePhone = None, setExtension = None, setIsConfidential = None, setModifiedTime = None, setNamePhoneID = None, setOnScreenID = None, setParentOnScreenID = None, setPhoneNumber = None, setPhonePreventFamilyStudentAccessUpdates = None, setPhoneTypeID = None, setRank = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempNewStudentEnrollmentGuardianPhoneID = False, returnAddPhone = False, returnCreatedTime = False, returnCreateNewPhone = False, returnDeletePhone = False, returnExtension = False, returnIsConfidential = False, returnModifiedTime = False, returnNamePhoneID = False, returnOnScreenID = False, returnParentOnScreenID = False, returnPhoneNumber = False, returnPhonePreventFamilyStudentAccessUpdates = False, returnPhoneTypeID = False, returnRank = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempNewStudentEnrollmentGuardianPhone(TempNewStudentEnrollmentGuardianPhoneID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempNewStudentEnrollmentGuardianPhone/" + str(TempNewStudentEnrollmentGuardianPhoneID), verb = "delete")


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

def getTempStep(TempStepID, EntityID = 1, returnTempStepID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorCount = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "get", return_params_list = return_params)

def modifyTempStep(TempStepID, EntityID = 1, setTempStepID = None, setCreatedTime = None, setEntityGroupKey = None, setErrorCount = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setModifiedTime = None, setName = None, setOnlineFormID = None, setOrder = None, setStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStepID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorCount = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStep(EntityID = 1, setTempStepID = None, setCreatedTime = None, setEntityGroupKey = None, setErrorCount = None, setIsActive = None, setIsReadOnlyForNonPrimaryFamily = None, setIsRequired = None, setMessage = None, setModifiedTime = None, setName = None, setOnlineFormID = None, setOrder = None, setStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStepID = False, returnCreatedTime = False, returnEntityGroupKey = False, returnErrorCount = False, returnIsActive = False, returnIsReadOnlyForNonPrimaryFamily = False, returnIsRequired = False, returnMessage = False, returnModifiedTime = False, returnName = False, returnOnlineFormID = False, returnOrder = False, returnStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStep(TempStepID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStep/" + str(TempStepID), verb = "delete")


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

def getTempStepError(TempStepErrorID, EntityID = 1, returnTempStepErrorID = False, returnCreatedTime = False, returnError = False, returnErrorMessage = False, returnModifiedTime = False, returnTempStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/" + str(TempStepErrorID), verb = "get", return_params_list = return_params)

def modifyTempStepError(TempStepErrorID, EntityID = 1, setTempStepErrorID = None, setCreatedTime = None, setError = None, setErrorMessage = None, setModifiedTime = None, setTempStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStepErrorID = False, returnCreatedTime = False, returnError = False, returnErrorMessage = False, returnModifiedTime = False, returnTempStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/" + str(TempStepErrorID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStepError(EntityID = 1, setTempStepErrorID = None, setCreatedTime = None, setError = None, setErrorMessage = None, setModifiedTime = None, setTempStepID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStepErrorID = False, returnCreatedTime = False, returnError = False, returnErrorMessage = False, returnModifiedTime = False, returnTempStepID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStepError(TempStepErrorID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStepError/" + str(TempStepErrorID), verb = "delete")


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

def getTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1, returnTempStudentHealthConditionID = False, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "get", return_params_list = return_params)

def modifyTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1, setTempStudentHealthConditionID = None, setCreatedTime = None, setHealthConditionID = None, setIsDelete = None, setIsExistingStudentHealthCondition = None, setIsExistingStudentHealthConditionNote = None, setModifiedTime = None, setNote = None, setOnScreenCount = None, setStartDate = None, setStudentHealthConditionID = None, setStudentHealthConditionNoteID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentHealthConditionID = False, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

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

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "post", return_params_list = return_params, payload = payload_params)

def createTempStudentHealthCondition(EntityID = 1, setTempStudentHealthConditionID = None, setCreatedTime = None, setHealthConditionID = None, setIsDelete = None, setIsExistingStudentHealthCondition = None, setIsExistingStudentHealthConditionNote = None, setModifiedTime = None, setNote = None, setOnScreenCount = None, setStartDate = None, setStudentHealthConditionID = None, setStudentHealthConditionNoteID = None, setUserIDCreatedBy = None, setUserIDModifiedBy = None, returnTempStudentHealthConditionID = False, returnCreatedTime = False, returnHealthConditionID = False, returnIsDelete = False, returnIsExistingStudentHealthCondition = False, returnIsExistingStudentHealthConditionNote = False, returnModifiedTime = False, returnNote = False, returnOnScreenCount = False, returnStartDate = False, returnStudentHealthConditionID = False, returnStudentHealthConditionNoteID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False):

    params = locals()

    params = pd.DataFrame(list(zip(params.keys(), params.values())), columns = ["Param", "Value"])

    return_params = params.query('Param.str.startswith("return")', engine = 'python')

    if not any(return_params.Value):

        return_params = list(return_params.assign(Value = True).Param)
    else:

        return_params = list(return_params.query('Value == True').Param)

    return_params = [re.sub("^return", '', param) for param in return_params]

    payload_params = params.query('Param.str.startswith("set") and not Value.isnull()', engine = 'python')

    payload_params = payload_params.assign(Param = payload_params["Param"].str.replace("^set", ""))

    payload_params = pd.DataFrame(list(payload_params.Value), index = list(payload_params.Param)).transpose()

    payload_params = json.loads(payload_params.to_json(orient = "records"))[0]

    payload_params = dict({"DataObject": payload_params})

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/", verb = "put", return_params_list = return_params, payload = payload_params)

def deleteTempStudentHealthCondition(TempStudentHealthConditionID, EntityID = 1):

    return make_request(endpoint = "/Generic/" + str(EntityID) + "/OnlineForm/TempStudentHealthCondition/" + str(TempStudentHealthConditionID), verb = "delete")