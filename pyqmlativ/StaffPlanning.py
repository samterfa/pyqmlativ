# This module contains StaffPlanning functions.

def deleteAssignmentTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/AssignmentTypePlanPositionDistributionSummary/" + PlanPositionDistributionIDFirst, verb = "delete")

def deleteBuildingPlanPositionDistributionSummary(PlanPositionDistributionIDFirst, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/BuildingPlanPositionDistributionSummary/" + PlanPositionDistributionIDFirst, verb = "delete")

def deletePlan(PlanID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/Plan/" + PlanID, verb = "delete")

def deletePlanEmployee(PlanEmployeeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanEmployee/" + PlanEmployeeID, verb = "delete")

def deletePlanGroup(PlanGroupID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanGroup/" + PlanGroupID, verb = "delete")

def deletePlanGroupAssignmentType(PlanGroupAssignmentTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanGroupAssignmentType/" + PlanGroupAssignmentTypeID, verb = "delete")

def deletePlanGroupBuilding(PlanGroupBuildingID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanGroupBuilding/" + PlanGroupBuildingID, verb = "delete")

def deletePlanGroupClearance(PlanGroupClearanceID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanGroupClearance/" + PlanGroupClearanceID, verb = "delete")

def deletePlanGroupPositionType(PlanGroupPositionTypeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanGroupPositionType/" + PlanGroupPositionTypeID, verb = "delete")

def deletePlanPosition(PlanPositionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPosition/" + PlanPositionID, verb = "delete")

def deletePlanPositionBenefit(PlanPositionBenefitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionBenefit/" + PlanPositionBenefitID, verb = "delete")

def deletePlanPositionDistribution(PlanPositionDistributionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionDistribution/" + PlanPositionDistributionID, verb = "delete")

def deletePlanPositionPay(PlanPositionPayID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionPay/" + PlanPositionPayID, verb = "delete")

def deletePlanPositionPayAccountCalculation(PlanPositionPayAccountCalculationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionPayAccountCalculation/" + PlanPositionPayAccountCalculationID, verb = "delete")

def deletePlanPositionPayAccountDistribution(PlanPositionPayAccountDistributionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionPayAccountDistribution/" + PlanPositionPayAccountDistributionID, verb = "delete")

def deletePlanPositionPayBenefit(PlanPositionPayBenefitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionPayBenefit/" + PlanPositionPayBenefitID, verb = "delete")

def deletePlanPositionPayBenefitAccount(PlanPositionPayBenefitAccountID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionPayBenefitAccount/" + PlanPositionPayBenefitAccountID, verb = "delete")

def deletePlanPositionSupplement(PlanPositionSupplementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PlanPositionSupplement/" + PlanPositionSupplementID, verb = "delete")

def deletePositionTypePlanPositionDistributionSummary(PlanPositionDistributionIDFirst, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/PositionTypePlanPositionDistributionSummary/" + PlanPositionDistributionIDFirst, verb = "delete")

def deleteTempException(TempExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempException/" + TempExceptionID, verb = "delete")

def deleteTempPlanPositionBenefit(TempPlanPositionBenefitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionBenefit/" + TempPlanPositionBenefitID, verb = "delete")

def deleteTempPlanPositionDistribution(TempPlanPositionDistributionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionDistribution/" + TempPlanPositionDistributionID, verb = "delete")

def deleteTempPlanPositionEmployee(TempPlanPositionEmployeeID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionEmployee/" + TempPlanPositionEmployeeID, verb = "delete")

def deleteTempPlanPositionException(TempPlanPositionExceptionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionException/" + TempPlanPositionExceptionID, verb = "delete")

def deleteTempPlanPositionPay(TempPlanPositionPayID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionPay/" + TempPlanPositionPayID, verb = "delete")

def deleteTempPlanPositionPayAccountCalculation(TempPlanPositionPayAccountCalculationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionPayAccountCalculation/" + TempPlanPositionPayAccountCalculationID, verb = "delete")

def deleteTempPlanPositionPayAccountDistribution(TempPlanPositionPayAccountDistributionID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionPayAccountDistribution/" + TempPlanPositionPayAccountDistributionID, verb = "delete")

def deleteTempPlanPositionPayBenefit(TempPlanPositionPayBenefitID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionPayBenefit/" + TempPlanPositionPayBenefitID, verb = "delete")

def deleteTempPlanPositionPayBenefitAccount(TempPlanPositionPayBenefitAccountID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionPayBenefitAccount/" + TempPlanPositionPayBenefitAccountID, verb = "delete")

def deleteTempPlanPositionSupplement(TempPlanPositionSupplementID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/StaffPlanning/TempPlanPositionSupplement/" + TempPlanPositionSupplementID, verb = "delete")