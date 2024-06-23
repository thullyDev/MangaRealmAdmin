from django.shortcuts import render, redirect
from ..database import Cache
import time
import pprint

cache = Cache()

def recorder(request_func):
    def wrapper(request_obj, *args, **kwargs):
        start_time = time.time()
        request = args[0]
        GET = request.GET
        POST = request.POST
        COOKIES = request.COOKIES
        is_auth = False

        if "" not in [ COOKIES.get("email", ""), COOKIES.get("username", "") ]: is_auth = True

        increment_views()

        response = request_func(
            request_obj, 
            GET=GET, 
            POST=POST, 
            COOKIES=COOKIES, 
            context={ 
                "COOKIES": COOKIES, 
                "is_auth": is_auth 
            }, 
            *args, 
            **kwargs
        )
        end_time = time.time()
        elapsed_time = end_time - start_time
        FUNCTION_NAME = request_func.__name__.upper()
        print(f"{FUNCTION_NAME} ===> {elapsed_time:.4f} seconds")

        return response

    return wrapper

def increment_views():
    views = cache.cget(name="site_views")
    views = 0 + 1 if not views else int(views) + 1
    one_week = 604_800 # in secs
    cache.cset(name="site_views", value=views, expiry=one_week)