# This module contains Demographics functions.

def deleteACHAccount(ACHAccountID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/ACHAccount/" + ACHAccountID, verb = "delete")

def deleteAddress(AddressID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Address/" + AddressID, verb = "delete")

def deleteAddressRangeDefault(AddressRangeDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressRangeDefault/" + AddressRangeDefaultID, verb = "delete")

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressRangeDefaultAddress/" + AddressRangeDefaultAddressID, verb = "delete")

def deleteAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressRangeDefaultSchool/" + AddressRangeDefaultSchoolID, verb = "delete")

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressRangeImportSchool/" + AddressRangeImportSchoolID, verb = "delete")

def deleteAddressSchoolPathOverride(AddressSchoolPathOverrideID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressSchoolPathOverride/" + AddressSchoolPathOverrideID, verb = "delete")

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/AddressSecondaryUnit/" + AddressSecondaryUnitID, verb = "delete")

def deleteCertification(CertificationID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Certification/" + CertificationID, verb = "delete")

def deleteCertificationCompetency(CertificationCompetencyID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationCompetency/" + CertificationCompetencyID, verb = "delete")

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationDelimitedFileFormat/" + CertificationDelimitedFileFormatID, verb = "delete")

def deleteCertificationDetail(CertificationDetailID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationDetail/" + CertificationDetailID, verb = "delete")

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationFixedLengthFileFormat/" + CertificationFixedLengthFileFormatID, verb = "delete")

def deleteCertificationGrade(CertificationGradeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationGrade/" + CertificationGradeID, verb = "delete")

def deleteCertificationLevel(CertificationLevelID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationLevel/" + CertificationLevelID, verb = "delete")

def deleteCertificationSubject(CertificationSubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationSubject/" + CertificationSubjectID, verb = "delete")

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormat/" + CertificationThirdPartyFormatID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + CertificationThirdPartyFormatCertificationCompetencyID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + CertificationThirdPartyFormatCertificationGradeID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + CertificationThirdPartyFormatCertificationLevelID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + CertificationThirdPartyFormatCertificationSubjectID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatCertificationType/" + CertificationThirdPartyFormatCertificationTypeID, verb = "delete")

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyFormatInstitution/" + CertificationThirdPartyFormatInstitutionID, verb = "delete")

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationThirdPartyImport/" + CertificationThirdPartyImportID, verb = "delete")

def deleteCertificationType(CertificationTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/CertificationType/" + CertificationTypeID, verb = "delete")

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/ConfigDistrict/" + ConfigDistrictID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteCounty(CountyID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/County/" + CountyID, verb = "delete")

def deleteDependent(DependentID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Dependent/" + DependentID, verb = "delete")

def deleteDirectional(DirectionalID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Directional/" + DirectionalID, verb = "delete")

def deleteEmailType(EmailTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/EmailType/" + EmailTypeID, verb = "delete")

def deleteEmergencyContact(EmergencyContactID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/EmergencyContact/" + EmergencyContactID, verb = "delete")

def deleteEmployer(EmployerID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Employer/" + EmployerID, verb = "delete")

def deleteInstitutionDefault(InstitutionDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/InstitutionDefault/" + InstitutionDefaultID, verb = "delete")

def deleteInstitution(InstitutionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Institution/" + InstitutionID, verb = "delete")

def deleteLanguage(LanguageID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Language/" + LanguageID, verb = "delete")

def deleteLanguageSchoolYear(LanguageSchoolYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/LanguageSchoolYear/" + LanguageSchoolYearID, verb = "delete")

def deleteLastNameNumber(LastNameNumberID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/LastNameNumber/" + LastNameNumberID, verb = "delete")

def deleteName(NameID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Name/" + NameID, verb = "delete")

def deleteNameAddress(NameAddressID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameAddress/" + NameAddressID, verb = "delete")

def deleteNameAlias(NameAliasID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameAlias/" + NameAliasID, verb = "delete")

def deleteNameEmail(NameEmailID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameEmail/" + NameEmailID, verb = "delete")

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameEthnicityRaceSubcategoryMN/" + NameEthnicityRaceSubcategoryMNID, verb = "delete")

def deleteNameMergeRunHistory(NameMergeRunHistoryID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameMergeRunHistory/" + NameMergeRunHistoryID, verb = "delete")

def deleteNamePhone(NamePhoneID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NamePhone/" + NamePhoneID, verb = "delete")

def deleteNameSuffix(NameSuffixID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameSuffix/" + NameSuffixID, verb = "delete")

def deleteNameTitle(NameTitleID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameTitle/" + NameTitleID, verb = "delete")

def deleteNameVehicle(NameVehicleID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameVehicle/" + NameVehicleID, verb = "delete")

def deleteNameWebsite(NameWebsiteID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/NameWebsite/" + NameWebsiteID, verb = "delete")

def deleteOccupation(OccupationID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Occupation/" + OccupationID, verb = "delete")

def deletePhoneType(PhoneTypeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/PhoneType/" + PhoneTypeID, verb = "delete")

def deleteRelationship(RelationshipID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Relationship/" + RelationshipID, verb = "delete")

def deleteStreet(StreetID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Street/" + StreetID, verb = "delete")

def deleteTempACHAccount(TempACHAccountID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempACHAccount/" + TempACHAccountID, verb = "delete")

def deleteTempAddress(TempAddressID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempAddress/" + TempAddressID, verb = "delete")

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempAddressRangeDefault/" + TempAddressRangeDefaultID, verb = "delete")

def deleteTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempAddressSchoolPathOverride/" + TempAddressSchoolPathOverrideID, verb = "delete")

def deleteTempCertification(TempCertificationID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempCertification/" + TempCertificationID, verb = "delete")

def deleteTempCertificationDetail(TempCertificationDetailID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempCertificationDetail/" + TempCertificationDetailID, verb = "delete")

def deleteTempCertificationError(TempCertificationErrorID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempCertificationError/" + TempCertificationErrorID, verb = "delete")

def deleteTempEmergencyContact(TempEmergencyContactID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempEmergencyContact/" + TempEmergencyContactID, verb = "delete")

def deleteTempException(TempExceptionID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempException/" + TempExceptionID, verb = "delete")

def deleteTempNameAddress(TempNameAddressID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempNameAddress/" + TempNameAddressID, verb = "delete")

def deleteTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + TempNameAddressMoveAddressSchoolPathOverrideID, verb = "delete")

def deleteTempNameError(TempNameErrorID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempNameError/" + TempNameErrorID, verb = "delete")

def deleteTempNameNumber(TempNameNumberID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/TempNameNumber/" + TempNameNumberID, verb = "delete")

def deleteVehicle(VehicleID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Vehicle/" + VehicleID, verb = "delete")

def deleteZip(ZipID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Demographics/Zip/" + ZipID, verb = "delete")