from django.urls import path
from django.core.exceptions import ValidationError

def produce_urlpatterns(routes):
	hashnames = set()

	for route in routes:
		name = route.get("name")
		route_path = route.get("route")

		if not name: 
			continue

		if route_path in hashnames or name in hashnames:
			raise ValidationError(f"Duplicate URL route: {name}****{route_path}")

		hashnames.add(name)
		
	hashnames.clear()
	return [ path(request["route"], request["view"], name=request.get("name")) for request in routes ]

def route_producer(route, view, name=None):
	route_data = {
		"name": name,
		"route": route,
		"view": view,
	}
	return route_data