from django.http import JsonResponse, HttpResponse
from .cookiesHandlers import set_cookies
from ..resources import (
	FORBIDDEN, 
	CRASH, 
	SUCCESSFUL, 
	NOT_FOUND_MSG, 
	NOT_FOUND, 
	FORBIDDEN_MSG, 
	CRASH_MSG, 
	SUCCESSFUL_MSG,
	BAD_REQUEST_MSG,
	BAD_REQUEST,
)

class ResponseHandler:
	def json_response(self, status_code, data, safe=False, cookies=False, cookies_data={}):
		response = JsonResponse(data=data, status=status_code, safe=safe) 

		if cookies:
			NINETY_DAYS = 2_592_000 * 3 #* 30 days (in seconds) * 3 = 90 days

			for key, val in cookies_data.items():
				if not val:
					response.delete_cookie(key)
					continue

				max_age = NINETY_DAYS

				response.set_cookie(
					key=key, 
					value=val, 
					max_age=max_age, 
					secure=True, 
					httponly=True
				)

		return response

	def data_processor(self, data, status_code, message):
		data = data if data else {}
		data["status_code"] = status_code
		if not data.get("message"): data["message"] = message

		return data

	def http_response(self, text, status_code):
		return HttpResponse(text, status=status_code)

	def forbidden_response(self, data={}, **kwargs):
		data = self.data_processor(data=data, status_code=FORBIDDEN, message=FORBIDDEN_MSG)
		return self.json_response(data=data, status_code=FORBIDDEN, **kwargs)

	def successful_response(self, data={}, **kwargs):
		data = self.data_processor(data=data, status_code=SUCCESSFUL, message=SUCCESSFUL_MSG)
		return self.json_response(data=data, status_code=SUCCESSFUL, **kwargs)

	def not_found_response(self, data={}, **kwargs):
		data = self.data_processor(data=data, status_code=NOT_FOUND, message=NOT_FOUND_MSG)
		return self.json_response(data=data, status_code=NOT_FOUND, **kwargs)

	def crash_response(self, data={}, **kwargs):
		data = self.data_processor(data=data, status_code=CRASH, message=CRASH_MSG)
		return self.json_response(data=data, status_code=CRASH, **kwargs)

	def bad_request_response(self, data={}, **kwargs):
		data = self.data_processor(data=data, status_code=BAD_REQUEST, message=BAD_REQUEST_MSG)
		return self.json_response(data=data, status_code=BAD_REQUEST, **kwargs)