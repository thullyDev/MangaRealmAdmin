from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
from urllib.parse import quote
from ..resources import ROOT_FILE
from ..database import Database
from ..handlers import ResponseHandler, SiteHandler
import json
from pprint import pprint

database = Database()
site = SiteHandler()

class Base(APIView, ResponseHandler):
    def root(self, request, context={}, template=ROOT_FILE, titled=False):
        site_data = site.get_site_data()
        path = request.path.split("/")
        full_path = request.path_info
        paths = full_path.split('/')
        length = len(paths)
        page = paths[length - 2]

        maintenance = site_data.get("settings", {}).get("maintanence", {}).get("value")
        anime_page = site_data.get("settings", {}).get("anime", {}).get("value")
        watch_togather = site_data.get("settings", {}).get("watch_togather", {}).get("value")
        watch_page = site_data.get("settings", {}).get("watch", {}).get("value")
        schedule_page = site_data.get("settings", {}).get("schedule", {}).get("value")
        user_page = site_data.get("settings", {}).get("user", {}).get("value")

        if not anime_page and context.get("page") == "anime":
            return self.redirect_to_alert("anime not found", "The requested anime is probably blocked by the admins or taken down")
        if not watch_page and context.get("page") == "watch": 
            return self.redirect_to_alert("anime not found", "The requested anime is probably blocked by the admins or taken down")

        if not watch_togather and page == "watch_rooms": 
            return redirect("home")

        if not schedule_page and page == "schedule": 
            return redirect("home")
            
        if not user_page and page == "profile": 
            return redirect("home")

        if page not in { "alert", "maintenance" } and  maintenance == True: return redirect("maintenance")

        disabled_animes = site_data.get("disabled_animes", {})
        anime_slug = context.get("anime_slug", "none")

        if anime_slug.replace("/", "") in disabled_animes or \
            anime_slug in disabled_animes:
            return self.redirect_to_alert("Anime Disabled", "This anime has been disabled by the admin")

        page_url = request.build_absolute_uri()
        context["page_url"] = page_url 
        context["site_data"] = site_data
        context["titled"] = titled 

        if "page" in context: return render(request, template, context=context)

        context["page"] = page 

        return render(request, template, context=context)

    def redirect_to_alert(self, raw_message, raw_description):
        url = reverse('alert')
        message = quote(raw_message)
        description = quote(raw_description)
        url = f"{url}?message={message}&description={description}"
        
        return redirect(url)

    def process_request(self, data):
        if not data: return {}

        return json.loads(data)

    def set_context(self, data, context):
        for key, value in data.items():
            context[key] = value

    def logout(self, request):
        return self.successful_response(data={ "message": "successful logout" }, cookies=True, cookies_data={
            "email": None,
            "username": None,
            "temporary_id": None,
        })
    
    def paginate(self, data, page, limit=20):
        paginator = Paginator(data, limit) 

        try:
            paginated = paginator.page(page)
        except EmptyPage:
            paginated = paginator.page(paginator.num_pages)

        return paginated, paginator.num_pages

    def filter_url_data(self, data, keys):
        data = {
            key: value 
            for key, value in data.items()
            if key in keys
        }
        valid = all(key in data for key in keys)

        return data if valid else None
