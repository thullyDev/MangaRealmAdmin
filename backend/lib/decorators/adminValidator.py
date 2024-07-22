from django.shortcuts import render, redirect
from ..resources import generate_unique_id
from ..handlers import ResponseHandler, SiteHandler
from ..database import AdminDatabase
from ..handlers import set_cookies
import time

response_handler = ResponseHandler()
site = SiteHandler()
database = AdminDatabase()

def adminValidator(request_func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        FUNCTION_NAME = request_func.__name__
        request = args[0]
        GET = request.GET
        POST = request.POST
        admin = get_admin(request)

        ajax = is_ajax(request)

        if FUNCTION_NAME != "admin_login" and not admin:
            return redirect("admin_login") if not ajax else response_handler.forbidden_response()

        if FUNCTION_NAME == "admin_login":
            admin = {
                "email": "",
                "username": "",
                "temporary_id": "",
            }

        site_data = site.get_site_data()

        response = request_func(
            request_obj,
            GET=GET, 
            POST=POST,
            site_data=site_data, 
            context={ "admin": admin, "site_data": site_data }, 
            email=admin["email"], 
            username=admin["username"], 
            temporary_id=admin["temporary_id"], 
            *args, 
            **kwargs
            )
        SIXTY_DAYS = 2_592_000 * 2  #* 30 days (in seconds) * 2 = 60 days

        set_cookies(response=response,
            key="temporary_id", 
            value=admin["temporary_id"], 
            age=SIXTY_DAYS, 
        )
        set_cookies(response=response,
            key="email", 
            value=admin["email"], 
            age=SIXTY_DAYS, 
        )
        set_cookies(response=response,
            key="username", 
            value=admin["username"], 
            age=SIXTY_DAYS, 
        )

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{FUNCTION_NAME.upper()} ===> {elapsed_time:.4f} seconds")

        return response

    return wrapper

def get_admin(request):
    cookies = request.COOKIES
    email = cookies.get('email')
    username = cookies.get('username')
    temporary_id = cookies.get('temporary_id')

    if None in [email, username, temporary_id]:
        return 

    admin = database.get_admin(email=email)

    if admin == None:
        return 

    # if temporary_id != admin["temporary_id"]:
    #     return 

    admin = database.update_admin(data={ "email": email, "temporary_id": generate_unique_id() })

    del admin["password"]

    return admin

def is_ajax(request):
    meta = request.META
    path = meta.get("PATH_INFO")
    parts = path.split("/")

    return "ajax" in parts