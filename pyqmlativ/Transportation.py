# This module contains Transportation functions.

def deleteBus(BusID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/Bus/" + BusID, verb = "delete")

def deleteBusRoute(BusRouteID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/BusRoute/" + BusRouteID, verb = "delete")

def deleteBusStop(BusStopID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/BusStop/" + BusStopID, verb = "delete")

def deleteStudentBusStop(StudentBusStopID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/StudentBusStop/" + StudentBusStopID, verb = "delete")

def deleteStudentTransportation(StudentTransportationID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/StudentTransportation/" + StudentTransportationID, verb = "delete")

def deleteTransportationCategory(TransportationCategoryID, entity_id = 1):

	make_request(endpoint = "/Generic/" + entity_id + "/Transportation/TransportationCategory/" + TransportationCategoryID, verb = "delete")