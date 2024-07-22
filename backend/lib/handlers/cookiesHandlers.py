def set_cookies(response, key, value, age=2_592_000):  #* 30 days (in seconds)
	response.set_cookie(
		key=key, 
		value=value, 
		max_age=age, 
		secure=True, 
		httponly=True
	)

