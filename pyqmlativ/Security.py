# This module contains Security functions.

def deleteAuthenticationAssertion(AuthenticationAssertionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/AuthenticationAssertion/" + AuthenticationAssertionID, verb = "delete")

def deleteAuthenticationMethod(AuthenticationMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/AuthenticationMethod/" + AuthenticationMethodID, verb = "delete")

def deleteAuthenticationRole(AuthenticationRoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/AuthenticationRole/" + AuthenticationRoleID, verb = "delete")

def deleteAuthenticationRoleLDAPProvider(AuthenticationRoleLDAPProviderID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/AuthenticationRoleLDAPProvider/" + AuthenticationRoleLDAPProviderID, verb = "delete")

def deleteAuthenticationRoleMethod(AuthenticationRoleMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/AuthenticationRoleMethod/" + AuthenticationRoleMethodID, verb = "delete")

def deleteBrowseFieldPath(BrowseFieldPathID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/BrowseFieldPath/" + BrowseFieldPathID, verb = "delete")

def deleteConfigSystem(ConfigSystemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/ConfigSystem/" + ConfigSystemID, verb = "delete")

def deleteDataObjectFieldPath(DataObjectFieldPathID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/DataObjectFieldPath/" + DataObjectFieldPathID, verb = "delete")

def deleteDeniedField(DeniedFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/DeniedField/" + DeniedFieldID, verb = "delete")

def deleteElectronicSignature(ElectronicSignatureID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/ElectronicSignature/" + ElectronicSignatureID, verb = "delete")

def deleteFieldRestriction(FieldRestrictionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/FieldRestriction/" + FieldRestrictionID, verb = "delete")

def deleteFieldRestrictionRole(FieldRestrictionRoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/FieldRestrictionRole/" + FieldRestrictionRoleID, verb = "delete")

def deleteFieldRestrictionScreen(FieldRestrictionScreenID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/FieldRestrictionScreen/" + FieldRestrictionScreenID, verb = "delete")

def deleteGroup(GroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/Group/" + GroupID, verb = "delete")

def deleteGroupEntityAutoAdd(GroupEntityAutoAddID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/GroupEntityAutoAdd/" + GroupEntityAutoAddID, verb = "delete")

def deleteGroupImpersonationRole(GroupImpersonationRoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/GroupImpersonationRole/" + GroupImpersonationRoleID, verb = "delete")

def deleteGroupLDAPSynchronization(GroupLDAPSynchronizationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/GroupLDAPSynchronization/" + GroupLDAPSynchronizationID, verb = "delete")

def deleteGroupMembership(GroupMembershipID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/GroupMembership/" + GroupMembershipID, verb = "delete")

def deleteGroupRole(GroupRoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/GroupRole/" + GroupRoleID, verb = "delete")

def deleteImpersonation(ImpersonationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/Impersonation/" + ImpersonationID, verb = "delete")

def deleteIPRange(IPRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/IPRange/" + IPRangeID, verb = "delete")

def deleteLDAPGroup(LDAPGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/LDAPGroup/" + LDAPGroupID, verb = "delete")

def deleteLDAPProvider(LDAPProviderID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/LDAPProvider/" + LDAPProviderID, verb = "delete")

def deleteMenuSecurityItem(MenuSecurityItemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/MenuSecurityItem/" + MenuSecurityItemID, verb = "delete")

def deleteMobileSSO(MobileSSOID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/MobileSSO/" + MobileSSOID, verb = "delete")

def deleteMultifactorAuthentication(MultifactorAuthenticationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/MultifactorAuthentication/" + MultifactorAuthenticationID, verb = "delete")

def deleteMultifactorAuthenticationAssertion(MultifactorAuthenticationAssertionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/MultifactorAuthenticationAssertion/" + MultifactorAuthenticationAssertionID, verb = "delete")

def deleteProduct(ProductID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/Product/" + ProductID, verb = "delete")

def deleteProductModulePath(ProductModulePathID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/ProductModulePath/" + ProductModulePathID, verb = "delete")

def deleteProductOwned(ProductOwnedID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/ProductOwned/" + ProductOwnedID, verb = "delete")

def deleteRole(RoleID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/Role/" + RoleID, verb = "delete")

def deleteRoleField(RoleFieldID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/RoleField/" + RoleFieldID, verb = "delete")

def deleteRoleIPRange(RoleIPRangeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/RoleIPRange/" + RoleIPRangeID, verb = "delete")

def deleteRoleMenuSecurityItem(RoleMenuSecurityItemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/RoleMenuSecurityItem/" + RoleMenuSecurityItemID, verb = "delete")

def deleteRoleModulePath(RoleModulePathID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/RoleModulePath/" + RoleModulePathID, verb = "delete")

def deleteRolePortal(RolePortalID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/RolePortal/" + RolePortalID, verb = "delete")

def deleteSecurityLocation(SecurityLocationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/SecurityLocation/" + SecurityLocationID, verb = "delete")

def deleteSecurityLocationMenuSecurityItem(SecurityLocationMenuSecurityItemID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/SecurityLocationMenuSecurityItem/" + SecurityLocationMenuSecurityItemID, verb = "delete")

def deleteSessionFileUpload(SessionFileUploadID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/SessionFileUpload/" + SessionFileUploadID, verb = "delete")

def deleteSkywardSupportAccess(SkywardSupportAccessID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/SkywardSupportAccess/" + SkywardSupportAccessID, verb = "delete")

def deleteSkywardSupportAccessLoginHistory(SkywardSupportAccessLoginHistoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/SkywardSupportAccessLoginHistory/" + SkywardSupportAccessLoginHistoryID, verb = "delete")

def deleteTempDeletedPortalAccessSecurityUser(TempDeletedPortalAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempDeletedPortalAccessSecurityUser/" + TempDeletedPortalAccessSecurityUserID, verb = "delete")

def deleteTempEmployeeAccessSecurityUser(TempEmployeeAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempEmployeeAccessSecurityUser/" + TempEmployeeAccessSecurityUserID, verb = "delete")

def deleteTempEntityForClone(TempEntityForCloneID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempEntityForClone/" + TempEntityForCloneID, verb = "delete")

def deleteTempFailedPortalAccessSecurityUser(TempFailedPortalAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempFailedPortalAccessSecurityUser/" + TempFailedPortalAccessSecurityUserID, verb = "delete")

def deleteTempFamilyAccessSecurityUser(TempFamilyAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempFamilyAccessSecurityUser/" + TempFamilyAccessSecurityUserID, verb = "delete")

def deleteTempImpersonationRoleForClone(TempImpersonationRoleForCloneID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempImpersonationRoleForClone/" + TempImpersonationRoleForCloneID, verb = "delete")

def deleteTempRoleForClone(TempRoleForCloneID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempRoleForClone/" + TempRoleForCloneID, verb = "delete")

def deleteTempSecurityImportError(TempSecurityImportErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempSecurityImportError/" + TempSecurityImportErrorID, verb = "delete")

def deleteTempSecurityImportGroupMembership(TempSecurityImportGroupMembershipID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempSecurityImportGroupMembership/" + TempSecurityImportGroupMembershipID, verb = "delete")

def deleteTempSecurityImportPreview(TempSecurityImportPreviewID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempSecurityImportPreview/" + TempSecurityImportPreviewID, verb = "delete")

def deleteTempSpecialtyAccessGroup(TempSpecialtyAccessGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempSpecialtyAccessGroup/" + TempSpecialtyAccessGroupID, verb = "delete")

def deleteTempStudentAccessSecurityUser(TempStudentAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempStudentAccessSecurityUser/" + TempStudentAccessSecurityUserID, verb = "delete")

def deleteTempTeacherAccessSecurityUser(TempTeacherAccessSecurityUserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TempTeacherAccessSecurityUser/" + TempTeacherAccessSecurityUserID, verb = "delete")

def deleteTrustedDevice(TrustedDeviceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/TrustedDevice/" + TrustedDeviceID, verb = "delete")

def deleteUserAuthenticationMethod(UserAuthenticationMethodID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserAuthenticationMethod/" + UserAuthenticationMethodID, verb = "delete")

def deleteUserCalendarPreference(UserCalendarPreferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserCalendarPreference/" + UserCalendarPreferenceID, verb = "delete")

def deleteUserImport(UserImportID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserImport/" + UserImportID, verb = "delete")

def deleteUserImportResult(UserImportResultID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserImportResult/" + UserImportResultID, verb = "delete")

def deleteUserImportResultError(UserImportResultErrorID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserImportResultError/" + UserImportResultErrorID, verb = "delete")

def deleteUserPasswordReset(UserPasswordResetID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserPasswordReset/" + UserPasswordResetID, verb = "delete")

def deleteUserPreference(UserPreferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserPreference/" + UserPreferenceID, verb = "delete")

def deleteUserProfileData(UserProfileDataID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserProfileData/" + UserProfileDataID, verb = "delete")

def deleteUserProfileTabStatus(UserProfileTabStatusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserProfileTabStatus/" + UserProfileTabStatusID, verb = "delete")

def deleteUserSetting(UserSettingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserSetting/" + UserSettingID, verb = "delete")

def deleteUserStudentCalendarPreference(UserStudentCalendarPreferenceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/UserStudentCalendarPreference/" + UserStudentCalendarPreferenceID, verb = "delete")

def deleteUser(UserID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Security/User/" + UserID, verb = "delete")