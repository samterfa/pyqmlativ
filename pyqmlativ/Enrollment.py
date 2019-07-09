# This module contains Enrollment functions.

from . import make_request

def getAwardsListMA(AwardsListMAID, EntityID = 1, returnAwardID = False, returnCreatedTime = False, returnModifiedTime = False, returnSchoolYearID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "get", params_list = params_list)

	return(response)

def deleteAwardsListMA(AwardsListMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsListMA/" + str(AwardsListMAID), verb = "delete")

	return(response)

def getAwardsMA(AwardsMAID, EntityID = 1, returnAward = False, returnCode = False, returnCreatedTime = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "get", params_list = params_list)

	return(response)

def deleteAwardsMA(AwardsMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/AwardsMA/" + str(AwardsMAID), verb = "delete")

	return(response)

def getConfigDistrict(ConfigDistrictID, EntityID = 1, returnAllowDualEnrollment = False, returnCreatedTime = False, returnDistrictID = False, returnEntryDaysBeforeCalendarStart = False, returnModifiedTime = False, returnNumberDaysBackdateEntry = False, returnNumberDaysBackdateWithdrawal = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDaysAfterCalendarEnd = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrict(ConfigDistrictID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrict/" + str(ConfigDistrictID), verb = "delete")

	return(response)

def getConfigDistrictYear(ConfigDistrictYearID, EntityID = 1, returnConfigDistrictYearIDClonedFrom = False, returnCreatedTime = False, returnDistrictID = False, returnEnableNoShow = False, returnEnrolledDifferentEntityNoShowActionType = False, returnEnrolledDifferentEntityNoShowActionTypeCode = False, returnEnrolledDifferentEntityNoShowEntryDate = False, returnEnrolledDifferentEntityNoShowWithdrawalDate = False, returnModifiedTime = False, returnNoDistrictEnrollmentNoShowActionType = False, returnNoDistrictEnrollmentNoShowActionTypeCode = False, returnNoDistrictEnrollmentNoShowEntryDate = False, returnNoDistrictEnrollmentNoShowWithdrawalDate = False, returnPreviouslyEnrolledSameEntityNoShowActionType = False, returnPreviouslyEnrolledSameEntityNoShowActionTypeCode = False, returnPreviouslyEnrolledSameEntityNoShowEntryDate = False, returnPreviouslyEnrolledSameEntityNoShowWithdrawalDate = False, returnPriorNoShowRecord = False, returnPriorNoShowRecordCode = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYear(ConfigDistrictYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYear/" + str(ConfigDistrictYearID), verb = "delete")

	return(response)

def getConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1, returnConfigDistrictYearID = False, returnConfigDistrictYearWithdrawalCodeIDClonedFrom = False, returnCreatedTime = False, returnModifiedTime = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteConfigDistrictYearWithdrawalCode(ConfigDistrictYearWithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/ConfigDistrictYearWithdrawalCode/" + str(ConfigDistrictYearWithdrawalCodeID), verb = "delete")

	return(response)

def getEntitySchool(EntitySchoolID, EntityID = 1, returnCreatedTime = False, returnEntityID = False, returnEntitySchoolIDClonedFrom = False, returnEntitySchoolIDClonedTo = False, returnIsDefaultEntityForSchool = False, returnIsDefaultSchoolForEntity = False, returnIsOnlySchoolInEntity = False, returnModifiedTime = False, returnSchoolID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteEntitySchool(EntitySchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchool/" + str(EntitySchoolID), verb = "delete")

	return(response)

def getEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1, returnBuildingID = False, returnCreatedTime = False, returnEntitySchoolBuildingIDClonedFrom = False, returnEntitySchoolID = False, returnIsPrimary = False, returnModifiedTime = False, returnSchoolYearID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "get", params_list = params_list)

	return(response)

def deleteEntitySchoolBuilding(EntitySchoolBuildingID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntitySchoolBuilding/" + str(EntitySchoolBuildingID), verb = "delete")

	return(response)

def getEntryCode(EntryCodeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEntryCodeIDClonedFrom = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteEntryCode(EntryCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryCode/" + str(EntryCodeID), verb = "delete")

	return(response)

def getEntryWithdrawal(EntryWithdrawalID, EntityID = 1, returnAttendanceDays = False, returnCalendarID = False, returnCreatedTime = False, returnEndDate = False, returnEnrolledAtLeastOneDay = False, returnEntityID = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalIDStatusChangePrevious = False, returnEntryWithdrawalMNID = False, returnGradeReferenceID = False, returnHasMessageCenterAllowedWithdrawalCodeOverride = False, returnIsCombinedEnrollmentFullTime = False, returnIsCrossEntityCourseEnrollment = False, returnIsCurrentOrFutureEnrollment = False, returnIsDefaultEntity = False, returnIsHistoricalEnrollment = False, returnIsIndependentStudy = False, returnIsNoShow = False, returnIsPostSecondaryOption = False, returnIsPSEOConcurrentEnrollment = False, returnIsStartDateOnOrAfterFirstDayOfSchool = False, returnMembershipDays = False, returnModifiedTime = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnPSEOHours = False, returnRenderDeleteOption = False, returnRenderNoShowOption = False, returnRenderPrintWithdrawalFormOption = False, returnRenderUndoStatusChangeOption = False, returnRenderWithdrawalAndStatusChangeOptions = False, returnSchoolID = False, returnSchoolYearID = False, returnSpecialEdServiceHours = False, returnStartDate = False, returnStateAidCategoryCodeMNID = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStatusChangeEntry = False, returnStatusChangeWithdrawal = False, returnStudentID = False, returnStudentTypeID = False, returnTotalMembershipDays = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "get", params_list = params_list)

	return(response)

def deleteEntryWithdrawal(EntryWithdrawalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/EntryWithdrawal/" + str(EntryWithdrawalID), verb = "delete")

	return(response)

def getGradeLevel(GradeLevelID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnFederalGradeLevel = False, returnFederalGradeLevelCode = False, returnModifiedTime = False, returnNumericValue = False, returnStateGradeLevel = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeLevel(GradeLevelID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeLevel/" + str(GradeLevelID), verb = "delete")

	return(response)

def getGradeReference(GradeReferenceID, EntityID = 1, returnCreatedTime = False, returnDistrictGroupKey = False, returnGradeLevelID = False, returnGradeReferenceIDClonedFrom = False, returnGradeReferenceIDClonedTo = False, returnGradeReferenceMNID = False, returnGradYear = False, returnMinutesPresentFullDay = False, returnMinutesPresentHalfDay = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateGradeLevel = False, returnStateSTARGradeLevelMNID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "get", params_list = params_list)

	return(response)

def deleteGradeReference(GradeReferenceID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/GradeReference/" + str(GradeReferenceID), verb = "delete")

	return(response)

def getHomeroom(HomeroomID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnEntityID = False, returnHomeroomDetails = False, returnHomeroomIDClonedFrom = False, returnHomeroomIDClonedTo = False, returnModifiedTime = False, returnRoomID = False, returnSchoolYearID = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "get", params_list = params_list)

	return(response)

def deleteHomeroom(HomeroomID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Homeroom/" + str(HomeroomID), verb = "delete")

	return(response)

def getPaymentPlanMA(PaymentPlanMAID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnDescription = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "get", params_list = params_list)

	return(response)

def deletePaymentPlanMA(PaymentPlanMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/PaymentPlanMA/" + str(PaymentPlanMAID), verb = "delete")

	return(response)

def getPermit(PermitID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictID = False, returnEndDate = False, returnModifiedTime = False, returnStartDate = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "get", params_list = params_list)

	return(response)

def deletePermit(PermitID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/Permit/" + str(PermitID), verb = "delete")

	return(response)

def getSchool(SchoolID, EntityID = 1, returnAllowsSchoolDevices = False, returnAllowsStudentDevices = False, returnBuildingID = False, returnCampusAccountabilityRatingID = False, returnCEEBCode = False, returnCode = False, returnCodeName = False, returnCreatedTime = False, returnDaysInRegularSchoolYear = False, returnDaysPriorForAlgebraICounts = False, returnDistrictID = False, returnEdFiSchoolCategoryID = False, returnEdFiSchoolID = False, returnEducationalProgramHoursPerWeek = False, returnExcludeFromCRDC = False, returnFaxNumber = False, returnFaxNumberIsInternational = False, returnFederalAlternativeSchoolDetailID = False, returnFederalJusticeFacilityTypeID = False, returnFederalNCESSchoolID = False, returnFormattedFaxNumber = False, returnFormattedPhoneNumber = False, returnGradeLevelIDHigh = False, returnGradeLevelIDLow = False, returnHasAlcoholDrugEducation = False, returnHasAntiBullying = False, returnHasAntiViolence = False, returnHasAPCourses = False, returnHasAPSelfSelection = False, returnHasCorporalPunishment = False, returnHasCreditRecovery = False, returnHasCrisisPlan = False, returnHasDualEnrollment = False, returnHasFiberOptic = False, returnHasGifted = False, returnHasHomicideOccurred = False, returnHasIBDiplomaProgramme = False, returnHasPreschoolNonIDEAAge3 = False, returnHasPreschoolNonIDEAAge4 = False, returnHasPreschoolNonIDEAAge5 = False, returnHasSafetyPlan = False, returnHasShootingOccurred = False, returnHasSingleSexAthletics = False, returnHasSingleSexClasses = False, returnHasUngraded = False, returnHasUngradedMainlyElementary = False, returnHasUngradedMainlyHighSchool = False, returnHasUngradedMainlyMiddleSchool = False, returnHasWiFi = False, returnHasZeroTolerance = False, returnIsALCSchool = False, returnIsAlternative = False, returnIsCEP = False, returnIsCharter = False, returnIsCRDCCollectedForSchoolYear = False, returnIsEntireSchoolMagnet = False, returnIsMagnet = False, returnIsNonLEA = False, returnIsSpecialEducation = False, returnIsTitleIII = False, returnModifiedTime = False, returnName = False, returnNameIDSafetySpecialist = False, returnNumberWiFiDevices = False, returnPhoneNumber = False, returnPhoneNumberIsInternational = False, returnSchoolIDClonedFrom = False, returnSchoolIDClonedTo = False, returnSchoolMNID = False, returnSchoolNumber = False, returnSchoolYearID = False, returnStaffIDPrincipal = False, returnStateKindergartenScheduleIndicatorCodeMNID = False, returnStateSchoolMNID = False, returnStateTitleISchoolIndicatorCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "get", params_list = params_list)

	return(response)

def deleteSchool(SchoolID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/School/" + str(SchoolID), verb = "delete")

	return(response)

def getStudentAccountsMA(StudentAccountsMAID, EntityID = 1, returnCreatedTime = False, returnFinancialAid = False, returniPadLease = False, returnModifiedTime = False, returnPaymentPlanMAID = False, returnPlaceofWorship = False, returnReligionID = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentAccountsMA(StudentAccountsMAID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentAccountsMA/" + str(StudentAccountsMAID), verb = "delete")

	return(response)

def getStudentEntityYear(StudentEntityYearID, EntityID = 1, returnChromebookDocumentsReturned = False, returnCreatedTime = False, returnDaysAbsentYTD = False, returnDaysEnrolledYTD = False, returnDaysExcusedYTD = False, returnDaysOtherYTD = False, returnDaysUnexcusedYTD = False, returnEntityID = False, returnEntryWithdrawalIDLatest = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExistsConflictedStudentCourseRequests = False, returnExistsUnscheduleableStudentSections = False, returnFeeAmountDue = False, returnFeeChargeAmount = False, returnFeePaidAmount = False, returnFeePaidAndWaivedAmount = False, returnFeeUnappliedAmount = False, returnFeeWaivedAmount = False, returnFirstName = False, returnFlaggedMissingAssignmentsCount = False, returnGrade = False, returnHandbookSigned = False, returnHasActiveCareerPlanDeclarationTimePeriod = False, returnHasActiveEndorsementDeclarationTimePeriod = False, returnHasConflictedStudentCourseRequest = False, returnHasFlaggedMissingAssignments = False, returnHasMissingAssignments = False, returnHasNoAttendanceToday = False, returnHasOpenDisplayPeriodsInRegularSchoolDay = False, returnHasOverscheduledPeriod = False, returnHasValidStudentPlan = False, returnHomeroomCodeFollettDestiny = False, returnHomeroomID = False, returnHomeroomPeriodFollettDestiny = False, returnHomeroomStaffNameFollettDestiny = False, returnIncludeAsProspectiveRank = False, returnIsActive = False, returnIsCrossEntityCourseEnrollment = False, returnIsDefaultEntity = False, returnIsTransportationRequested = False, returnLastName = False, returnMiddleName = False, returnModifiedTime = False, returnNameID = False, returnNumberOfStudentCourseRequests = False, returnNumberOfStudentSections = False, returnOptOutOfMedia = False, returnSchedulingCategories = False, returnSchedulingTeamID = False, returnSchoolYearID = False, returnSectionLengthAbsent = False, returnSectionLengthEnrolled = False, returnSemester2Absent = False, returnSemester2Enrolled = False, returnSignedAcceptableUsePolicy = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStudentID = False, returnStudentNumber = False, returnTardyCountYTD = False, returnTardyKioskTotals = False, returnTotalEarnedCreditsPossibleAnticipatedNonTransferStudentSectionsNonAlternateRequestCredits = False, returnTotalMissedAssignmentCount = False, returnUILFeeReceived = False, returnUnscheduleableStudentSectionCount = False, returnUnscheduledStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalDate = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentEntityYear(StudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentEntityYear/" + str(StudentEntityYearID), verb = "delete")

	return(response)

def getStudentType(StudentTypeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnModifiedTime = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "get", params_list = params_list)

	return(response)

def deleteStudentType(StudentTypeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/StudentType/" + str(StudentTypeID), verb = "delete")

	return(response)

def getTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1, returnAction = False, returnActionCode = False, returnActionMessage = False, returnAffectedPrimaryKey = False, returnCourseID = False, returnCreatedTime = False, returnDescription = False, returnEndDate = False, returnEntityID = False, returnHasAttendance = False, returnHasFutureAttendance = False, returnHasFutureGrades = False, returnHasGrades = False, returnHasPartiallyPaidFees = False, returnIsFutureEntryWithdrawal = False, returnModifiedTime = False, returnMostFutureGradeStartDate = False, returnNameIDRequestedBy = False, returnNewEndDate = False, returnRecordType = False, returnRecordTypeCode = False, returnSchoolYearID = False, returnSection = False, returnSectionID = False, returnStartDate = False, returnStudentID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempAffectedWithdrawalRecord(TempAffectedWithdrawalRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempAffectedWithdrawalRecord/" + str(TempAffectedWithdrawalRecordID), verb = "delete")

	return(response)

def getTempHomeroomError(TempHomeroomErrorID, EntityID = 1, returnCode = False, returnCreatedTime = False, returnFailureReason = False, returnModifiedTime = False, returnTempHomeroomRecordID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHomeroomError(TempHomeroomErrorID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomError/" + str(TempHomeroomErrorID), verb = "delete")

	return(response)

def getTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1, returnBuilding = False, returnBuildingID = False, returnCode = False, returnColumnIndex = False, returnCreatedTime = False, returnHasSaveError = False, returnHomeroomID = False, returnIsOverwrite = False, returnModifiedTime = False, returnRoom = False, returnRoomID = False, returnSchoolYear = False, returnSchoolYearID = False, returnStaff = False, returnStaffID = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempHomeroomRecord(TempHomeroomRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempHomeroomRecord/" + str(TempHomeroomRecordID), verb = "delete")

	return(response)

def getTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1, returnCreatedTime = False, returnDisplayAction = False, returnDisplayActionCode = False, returnEndDate = False, returnEntity = False, returnEntryCode = False, returnEntryWithdrawalID = False, returnFailureReason = False, returnGradeLevel = False, returnModifiedTime = False, returnNoShowAction = False, returnNoShowActionCode = False, returnNoShowEntryWithdrawalType = False, returnNoShowEntryWithdrawalTypeCode = False, returnNoShowTypeOfNoShow = False, returnNoShowTypeOfNoShowCode = False, returnSchoolYear = False, returnSchoolYearID = False, returnStartDate = False, returnStudent = False, returnStudentID = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "get", params_list = params_list)

	return(response)

def deleteTempNoShowEntryWithdrawal(TempNoShowEntryWithdrawalID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempNoShowEntryWithdrawal/" + str(TempNoShowEntryWithdrawalID), verb = "delete")

	return(response)

def getTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1, returnAdvisorFullName = False, returnCalendarCode = False, returnCalendarID = False, returnCompletedSchoolYearOverride = False, returnCreatedTime = False, returnCreateFeeManagementCustomer = False, returnCreateFeeManagementCustomerEntityYear = False, returnDisciplineOfficerFullName = False, returnEdFiDistrictIDResidence = False, returnEdFiDistrictIDTransfer = False, returnEdFiDistrictResidenceCodeDescription = False, returnEdFiSchoolIDTransfer = False, returnEndDate = False, returnEnrollIntoEntityCode = False, returnEnrollmentMoveable = False, returnEntityCode = False, returnEntityID = False, returnEntryCode = False, returnEntryCodeID = False, returnEntryComment = False, returnEntryWithdrawalID = False, returnExcludeFromHonorRoll = False, returnExcludeFromRank = False, returnExcludeFromThirdFridaySeptemberCount = False, returnFailureReason = False, returnFeeManagementCustomerID = False, returnGradeLevelCode = False, returnGradeReferenceID = False, returnGradYear = False, returnGSAADAClaimableOverrideCode = False, returnGSAADAClaimableOverrideCodeDisplayName = False, returnHomeroomCode = False, returnHomeroomID = False, returnIncludeAsProspectiveRank = False, returnIsCurrentActive = False, returnIsDefaultEntityForEntryWithdrawal = False, returnIsDefaultEntityForStudentEntityYear = False, returnIsPermanentExit = False, returnIsPrivateSchoolChoiceStudent = False, returnIsTuitionPaidOutOfDistrict = False, returnModifiedTime = False, returnNumericYear = False, returnOutgoingStudent = False, returnPercentEnrolled = False, returnPromotionStatus = False, returnPromotionStatusCode = False, returnScheduledSectionCount = False, returnSchoolCode = False, returnSchoolID = False, returnSchoolYearID = False, returnServingRCDTSOverrideCode = False, returnServingRCDTSOverrideCodeDisplayName = False, returnServingRCDTSOverrideID = False, returnSourceEntryWithdrawalID = False, returnStaffIDAdvisor = False, returnStaffIDDisciplineOfficer = False, returnStartDate = False, returnStateAidCategoryMNID = False, returnStateDistrictMNCodeName = False, returnStateDistrictMNID = False, returnStateLastAttendanceLocationCodeMNID = False, returnStudentCourseRequestNotMoveableCount = False, returnStudentCourseRequestToDeleteCount = False, returnStudentFullName = False, returnStudentID = False, returnStudentNumber = False, returnStudentTypeCode = False, returnStudentTypeID = False, returnTestingSchoolCode = False, returnTestingSchoolCodeDisplayName = False, returnTestingSchoolRCDTSOverrideCode = False, returnTestingSchoolRCDTSOverrideCodeDisplayName = False, returnTestingSchoolRCDTSOverrideID = False, returnTotalStudentCourseRequestCount = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCode = False, returnWithdrawalCodeID = False, returnWithdrawalComment = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentEnrollmentRecord(TempStudentEnrollmentRecordID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEnrollmentRecord/" + str(TempStudentEnrollmentRecordID), verb = "delete")

	return(response)

def getTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1, returnAdvisorDetails = False, returnCreatedTime = False, returnCurrentAdvisorDetails = False, returnCurrentHomeroomDetails = False, returnGenderCode = False, returnGradeLevelCodeDescription = False, returnHomeroomDetails = False, returnHomeroomID = False, returnIsActive = False, returnMessage = False, returnModifiedTime = False, returnStaffIDAdvisor = False, returnStudentEntityYearID = False, returnStudentFullName = False, returnStudentNumber = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "get", params_list = params_list)

	return(response)

def deleteTempStudentEntityYear(TempStudentEntityYearID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/TempStudentEntityYear/" + str(TempStudentEntityYearID), verb = "delete")

	return(response)

def getWithdrawalCode(WithdrawalCodeID, EntityID = 1, returnCode = False, returnCodeDescription = False, returnCreatedTime = False, returnDescription = False, returnDistrictGroupKey = False, returnDistrictID = False, returnEdFiExitWithdrawID = False, returnIsCrossEntityCourseEnrollment = False, returnModifiedTime = False, returnSchoolYearID = False, returnStateStatusEndCodeMNID = False, returnType = False, returnTypeCode = False, returnUserIDCreatedBy = False, returnUserIDModifiedBy = False, returnWithdrawalCodeIDClonedFrom = False, returnWithdrawalCodeMNID = False, returnRelationships = False):

	params = pd.DataFrame.from_dict(locals(), orient = "index", columns = ["value"])
	params_list = [params.index[0]]
	params_list.extend(list(params[[(value is True) for value in params.value]].index))
	params_list = [ param.replace("return", "") for param in params_list ]

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "get", params_list = params_list)

	return(response)

def deleteWithdrawalCode(WithdrawalCodeID, EntityID = 1):

	response = make_request(endpoint = "/Generic/" + str(EntityID) + "/Enrollment/WithdrawalCode/" + str(WithdrawalCodeID), verb = "delete")

	return(response)