from datetime import datetime
from functools import lru_cache
from decouple import config



def global_static_data(request):
	admin_menu_items = [
		  {
		    "path": "/admin/dashboard",
		    "label": "dashboard",
		    "icon": "fas fa-tachometer-alt",
		  },
		  {
		    "path": "/admin/scripts",
		    "label": "scripts",
		    "icon": "fas fa-code",
		  },
		  {
		    "path": "/admin/general",
		    "label": "general",
		    "icon": "fas fa-sliders-h",
		  },
		  {
		    "path": "/admin/advance",
		    "label": "advance",
		    "icon": "fas fa-cogs",
		  },
		  {
		    "path": "/admin/admins",
		    "label": "admins",
		    "icon": "fas fa-user-cog",
		  },
	]
	auths = {
		"signup": [
			{
				"input": "text",
				"key": "user",
				"icon": "fas fa-user",
			},
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
			{
				"input": "password",
				"key": "confirm",
				"icon": "fas fa-key",
			},
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
		],
		"login": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
		],
		"forgot_password": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
		],
		"resend": [
			{
				"input": "text",
				"key": "email",
				"icon": "fas fa-envelope",
			},
		],
		"verify": [
			{
				"input": "number",
				"key": "code",
				"icon": "fas fa-key",
			},
		],
		"renew_password": [
			{
				"input": "password",
				"key": "password",
				"icon": "fas fa-key",
			},
			{
				"input": "password",
				"key": "confirm",
				"icon": "fas fa-key",
			},
			{
				"input": "hidden",
				"key": "code",
				"icon": "",
			},
		],
	}
	SITE = config("SITE")
	data = {
		"admin_menu_items": admin_menu_items,
		"auths": auths,
		"SITE": SITE
	}
	return data

@lru_cache(maxsize=None)
def get_years(start_year=1950):
    current_year = datetime.now().year
    years = [ {"value": i, "name": i} for i in range(current_year, start_year - 1, -1) ]
    return years