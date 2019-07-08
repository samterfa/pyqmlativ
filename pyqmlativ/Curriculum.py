# This module contains Curriculum functions.

def deleteAcademicStandard(AcademicStandardID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandard/" + AcademicStandardID, verb = "delete")

def deleteAcademicStandardDefault(AcademicStandardDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardDefault/" + AcademicStandardDefaultID, verb = "delete")

def deleteAcademicStandardGradeRange(AcademicStandardGradeRangeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardGradeRange/" + AcademicStandardGradeRangeID, verb = "delete")

def deleteAcademicStandardGradeRangeDefault(AcademicStandardGradeRangeDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardGradeRangeDefault/" + AcademicStandardGradeRangeDefaultID, verb = "delete")

def deleteAcademicStandardHierarchyDepth(AcademicStandardHierarchyDepthID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardHierarchyDepth/" + AcademicStandardHierarchyDepthID, verb = "delete")

def deleteAcademicStandardSet(AcademicStandardSetID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardSet/" + AcademicStandardSetID, verb = "delete")

def deleteAcademicStandardSetDefault(AcademicStandardSetDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardSetDefault/" + AcademicStandardSetDefaultID, verb = "delete")

def deleteAcademicStandardSubject(AcademicStandardSubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardSubject/" + AcademicStandardSubjectID, verb = "delete")

def deleteAcademicStandardSubjectDefault(AcademicStandardSubjectDefaultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AcademicStandardSubjectDefault/" + AcademicStandardSubjectDefaultID, verb = "delete")

def deleteAssessmentToolMN(AssessmentToolMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/AssessmentToolMN/" + AssessmentToolMNID, verb = "delete")

def deleteCurriculum(CurriculumID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/Curriculum/" + CurriculumID, verb = "delete")

def deleteCurriculumAcademicStandard(CurriculumAcademicStandardID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumAcademicStandard/" + CurriculumAcademicStandardID, verb = "delete")

def deleteCurriculumCustomRequirement(CurriculumCustomRequirementID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumCustomRequirement/" + CurriculumCustomRequirementID, verb = "delete")

def deleteCurriculumGradeLevel(CurriculumGradeLevelID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumGradeLevel/" + CurriculumGradeLevelID, verb = "delete")

def deleteCurriculumProgramMN(CurriculumProgramMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumProgramMN/" + CurriculumProgramMNID, verb = "delete")

def deleteCurriculumSubject(CurriculumSubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumSubject/" + CurriculumSubjectID, verb = "delete")

def deleteCurriculumSubjectAcademicStandard(CurriculumSubjectAcademicStandardID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumSubjectAcademicStandard/" + CurriculumSubjectAcademicStandardID, verb = "delete")

def deleteCurriculumYear(CurriculumYearID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/CurriculumYear/" + CurriculumYearID, verb = "delete")

def deleteEarlyEducationInstructionalApproachMN(EarlyEducationInstructionalApproachMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/EarlyEducationInstructionalApproachMN/" + EarlyEducationInstructionalApproachMNID, verb = "delete")

def deleteEarlyEducationProgramMN(EarlyEducationProgramMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/EarlyEducationProgramMN/" + EarlyEducationProgramMNID, verb = "delete")

def deleteHierarchyDepth(HierarchyDepthID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/HierarchyDepth/" + HierarchyDepthID, verb = "delete")

def deletePrerequisite(PrerequisiteID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/Prerequisite/" + PrerequisiteID, verb = "delete")

def deletePrerequisiteCurriculum(PrerequisiteCurriculumID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/PrerequisiteCurriculum/" + PrerequisiteCurriculumID, verb = "delete")

def deleteSiteBasedInitiativeMN(SiteBasedInitiativeMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/SiteBasedInitiativeMN/" + SiteBasedInitiativeMNID, verb = "delete")

def deleteStandardPlacementMN(StandardPlacementMNID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/StandardPlacementMN/" + StandardPlacementMNID, verb = "delete")

def deleteSubject(SubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/Subject/" + SubjectID, verb = "delete")

def deleteTempAcademicStandard(TempAcademicStandardID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempAcademicStandard/" + TempAcademicStandardID, verb = "delete")

def deleteTempAcademicStandardGradeRange(TempAcademicStandardGradeRangeID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempAcademicStandardGradeRange/" + TempAcademicStandardGradeRangeID, verb = "delete")

def deleteTempAcademicStandardSet(TempAcademicStandardSetID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempAcademicStandardSet/" + TempAcademicStandardSetID, verb = "delete")

def deleteTempAcademicStandardSubject(TempAcademicStandardSubjectID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempAcademicStandardSubject/" + TempAcademicStandardSubjectID, verb = "delete")

def deleteTempGradeRangeCopyResult(TempGradeRangeCopyResultID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempGradeRangeCopyResult/" + TempGradeRangeCopyResultID, verb = "delete")

def deleteTempHierarchyDepth(TempHierarchyDepthID, EntityID = 1):

	makeRequest(endpoint = "/Generic/" + EntityID + "/Curriculum/TempHierarchyDepth/" + TempHierarchyDepthID, verb = "delete")