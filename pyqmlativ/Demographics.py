# This module contains Demographics functions.

def deleteACHAccount(ACHAccountID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/ACHAccount/" + ACHAccountID, verb = "delete")

def deleteAddress(AddressID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Address/" + AddressID, verb = "delete")

def deleteAddressRangeDefault(AddressRangeDefaultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressRangeDefault/" + AddressRangeDefaultID, verb = "delete")

def deleteAddressRangeDefaultAddress(AddressRangeDefaultAddressID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressRangeDefaultAddress/" + AddressRangeDefaultAddressID, verb = "delete")

def deleteAddressRangeDefaultSchool(AddressRangeDefaultSchoolID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressRangeDefaultSchool/" + AddressRangeDefaultSchoolID, verb = "delete")

def deleteAddressRangeImportSchool(AddressRangeImportSchoolID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressRangeImportSchool/" + AddressRangeImportSchoolID, verb = "delete")

def deleteAddressSchoolPathOverride(AddressSchoolPathOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressSchoolPathOverride/" + AddressSchoolPathOverrideID, verb = "delete")

def deleteAddressSecondaryUnit(AddressSecondaryUnitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/AddressSecondaryUnit/" + AddressSecondaryUnitID, verb = "delete")

def deleteCertification(CertificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Certification/" + CertificationID, verb = "delete")

def deleteCertificationCompetency(CertificationCompetencyID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationCompetency/" + CertificationCompetencyID, verb = "delete")

def deleteCertificationDelimitedFileFormat(CertificationDelimitedFileFormatID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationDelimitedFileFormat/" + CertificationDelimitedFileFormatID, verb = "delete")

def deleteCertificationDetail(CertificationDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationDetail/" + CertificationDetailID, verb = "delete")

def deleteCertificationFixedLengthFileFormat(CertificationFixedLengthFileFormatID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationFixedLengthFileFormat/" + CertificationFixedLengthFileFormatID, verb = "delete")

def deleteCertificationGrade(CertificationGradeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationGrade/" + CertificationGradeID, verb = "delete")

def deleteCertificationLevel(CertificationLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationLevel/" + CertificationLevelID, verb = "delete")

def deleteCertificationSubject(CertificationSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationSubject/" + CertificationSubjectID, verb = "delete")

def deleteCertificationThirdPartyFormat(CertificationThirdPartyFormatID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormat/" + CertificationThirdPartyFormatID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationCompetency(CertificationThirdPartyFormatCertificationCompetencyID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatCertificationCompetency/" + CertificationThirdPartyFormatCertificationCompetencyID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationGrade(CertificationThirdPartyFormatCertificationGradeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatCertificationGrade/" + CertificationThirdPartyFormatCertificationGradeID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationLevel(CertificationThirdPartyFormatCertificationLevelID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatCertificationLevel/" + CertificationThirdPartyFormatCertificationLevelID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationSubject(CertificationThirdPartyFormatCertificationSubjectID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatCertificationSubject/" + CertificationThirdPartyFormatCertificationSubjectID, verb = "delete")

def deleteCertificationThirdPartyFormatCertificationType(CertificationThirdPartyFormatCertificationTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatCertificationType/" + CertificationThirdPartyFormatCertificationTypeID, verb = "delete")

def deleteCertificationThirdPartyFormatInstitution(CertificationThirdPartyFormatInstitutionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyFormatInstitution/" + CertificationThirdPartyFormatInstitutionID, verb = "delete")

def deleteCertificationThirdPartyImport(CertificationThirdPartyImportID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationThirdPartyImport/" + CertificationThirdPartyImportID, verb = "delete")

def deleteCertificationType(CertificationTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/CertificationType/" + CertificationTypeID, verb = "delete")

def deleteConfigDistrict(ConfigDistrictID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/ConfigDistrict/" + ConfigDistrictID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteCounty(CountyID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/County/" + CountyID, verb = "delete")

def deleteDependent(DependentID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Dependent/" + DependentID, verb = "delete")

def deleteDirectional(DirectionalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Directional/" + DirectionalID, verb = "delete")

def deleteEmailType(EmailTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/EmailType/" + EmailTypeID, verb = "delete")

def deleteEmergencyContact(EmergencyContactID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/EmergencyContact/" + EmergencyContactID, verb = "delete")

def deleteEmployer(EmployerID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Employer/" + EmployerID, verb = "delete")

def deleteInstitutionDefault(InstitutionDefaultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/InstitutionDefault/" + InstitutionDefaultID, verb = "delete")

def deleteInstitution(InstitutionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Institution/" + InstitutionID, verb = "delete")

def deleteLanguage(LanguageID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Language/" + LanguageID, verb = "delete")

def deleteLanguageSchoolYear(LanguageSchoolYearID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/LanguageSchoolYear/" + LanguageSchoolYearID, verb = "delete")

def deleteLastNameNumber(LastNameNumberID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/LastNameNumber/" + LastNameNumberID, verb = "delete")

def deleteName(NameID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Name/" + NameID, verb = "delete")

def deleteNameAddress(NameAddressID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameAddress/" + NameAddressID, verb = "delete")

def deleteNameAlias(NameAliasID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameAlias/" + NameAliasID, verb = "delete")

def deleteNameEmail(NameEmailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameEmail/" + NameEmailID, verb = "delete")

def deleteNameEthnicityRaceSubcategoryMN(NameEthnicityRaceSubcategoryMNID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameEthnicityRaceSubcategoryMN/" + NameEthnicityRaceSubcategoryMNID, verb = "delete")

def deleteNameMergeRunHistory(NameMergeRunHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameMergeRunHistory/" + NameMergeRunHistoryID, verb = "delete")

def deleteNamePhone(NamePhoneID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NamePhone/" + NamePhoneID, verb = "delete")

def deleteNameSuffix(NameSuffixID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameSuffix/" + NameSuffixID, verb = "delete")

def deleteNameTitle(NameTitleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameTitle/" + NameTitleID, verb = "delete")

def deleteNameVehicle(NameVehicleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameVehicle/" + NameVehicleID, verb = "delete")

def deleteNameWebsite(NameWebsiteID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/NameWebsite/" + NameWebsiteID, verb = "delete")

def deleteOccupation(OccupationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Occupation/" + OccupationID, verb = "delete")

def deletePhoneType(PhoneTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/PhoneType/" + PhoneTypeID, verb = "delete")

def deleteRelationship(RelationshipID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Relationship/" + RelationshipID, verb = "delete")

def deleteStreet(StreetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Street/" + StreetID, verb = "delete")

def deleteTempACHAccount(TempACHAccountID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempACHAccount/" + TempACHAccountID, verb = "delete")

def deleteTempAddress(TempAddressID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempAddress/" + TempAddressID, verb = "delete")

def deleteTempAddressRangeDefault(TempAddressRangeDefaultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempAddressRangeDefault/" + TempAddressRangeDefaultID, verb = "delete")

def deleteTempAddressSchoolPathOverride(TempAddressSchoolPathOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempAddressSchoolPathOverride/" + TempAddressSchoolPathOverrideID, verb = "delete")

def deleteTempCertification(TempCertificationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempCertification/" + TempCertificationID, verb = "delete")

def deleteTempCertificationDetail(TempCertificationDetailID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempCertificationDetail/" + TempCertificationDetailID, verb = "delete")

def deleteTempCertificationError(TempCertificationErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempCertificationError/" + TempCertificationErrorID, verb = "delete")

def deleteTempEmergencyContact(TempEmergencyContactID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempEmergencyContact/" + TempEmergencyContactID, verb = "delete")

def deleteTempException(TempExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempException/" + TempExceptionID, verb = "delete")

def deleteTempNameAddress(TempNameAddressID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempNameAddress/" + TempNameAddressID, verb = "delete")

def deleteTempNameAddressMoveAddressSchoolPathOverride(TempNameAddressMoveAddressSchoolPathOverrideID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempNameAddressMoveAddressSchoolPathOverride/" + TempNameAddressMoveAddressSchoolPathOverrideID, verb = "delete")

def deleteTempNameError(TempNameErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempNameError/" + TempNameErrorID, verb = "delete")

def deleteTempNameNumber(TempNameNumberID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/TempNameNumber/" + TempNameNumberID, verb = "delete")

def deleteVehicle(VehicleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Vehicle/" + VehicleID, verb = "delete")

def deleteZip(ZipID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Demographics/Zip/" + ZipID, verb = "delete")