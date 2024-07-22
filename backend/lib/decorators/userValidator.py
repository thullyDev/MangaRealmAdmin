from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote
from ..resources import generate_unique_id
from ..handlers import SiteHandler, ResponseHandler
from ..database import UserDatabase
from ..handlers import set_cookies
import time

response_handler = ResponseHandler()
database = UserDatabase()

def userValidator(request_func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        GET = request.GET
        POST = request.POST
        COOKIES = request.COOKIES
        user = get_user(request)
        ajax = is_ajax(request)

        if not user:
            return redirect("home") if not ajax else response_handler.forbidden_response({ "message": "login" })

        if user["deleted"] == True:
            url = reverse('alert')
            message = quote("Disabled User Alert")
            description = quote("this user has been disabled")
            url = f"{url}?message={message}&description={description}"
            
            return self.redirect(url) if not ajax else response_handler.forbidden_response({ "message": "this user has been disabled" })


        response = request_func(
            request_obj, 
            GET=GET, 
            POST=POST,
            COOKIES=COOKIES, 
            user=user,
            context={ "user_data": user }, 
            email=user["email"], 
            username=user["username"], 
            temporary_id=user["temporary_id"], 
            *args, 
            **kwargs
            )

        SIXTY_DAYS = 2_592_000 * 2  #* 30 days (in seconds) * 2 = 60 days
        set_cookies(response=response,
            key="temporary_id", 
            value=user["temporary_id"], 
            age=SIXTY_DAYS, 
        )
        set_cookies(response=response,
            key="email", 
            value=user["email"], 
            age=SIXTY_DAYS, 
        )
        set_cookies(response=response,
            key="username", 
            value=user["username"], 
            age=SIXTY_DAYS, 
        )
        set_cookies(response=response,
            key="profile_image", 
            value=user["profile_image"], 
            age=SIXTY_DAYS, 
        )

        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = request_func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")

        return response

    return wrapper

def get_user(request):
    cookies = request.COOKIES
    email = cookies.get('email')
    username = cookies.get('username')
    temporary_id = cookies.get('temporary_id')

    if None in [email, username, temporary_id]:
        return 

    user = database.get_user(data={ "email": email })

    if user == None:
        return 

    # if temporary_id != user["temporary_id"]:
    #     return 

    user = database.update_user(data={ "email": email, "temporary_id": generate_unique_id() })

    del user["password"]

    return user

def is_ajax(request):
    meta = request.META
    path = meta.get("PATH_INFO")
    parts = path.split("/")

    return "ajax" in parts