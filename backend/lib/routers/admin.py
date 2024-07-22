from rest_framework.views import APIView
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage
from ..resources import MANGA_API_URL
from ..decorators import adminValidator, timer
from ..handlers import ResponseHandler, SiteHandler, ApiHandler
from ..database import AdminDatabase
# from .base import Base
from pprint import pprint
import json
import requests

admin_database = AdminDatabase()
site = SiteHandler()

class Admin(APIView, ResponseHandler):
    @timer
    def base(self, request, **kwargs):
        return redirect("admin_login")

    @adminValidator
    def admin_login(self, request, context, **kwargs):
        return self.root(request=request, context=context, template="pages/admin/login.html")   
   
    @adminValidator
    def dashboard(self, request, GET, site_data, context, **kwargs):
        admins = admin_database.get_admins()
        views = admin_database.cget(name="site_views")
        views = 0 if not views else views 
        scripts = site_data.get("scripts", "")

        count = 0
        for inner_key, inner_scripts in scripts.items():
            for key, script in inner_scripts.items():
                if script['value']: count += 1

        analytics = [
            {"icon": "fas fa-user-cog", "numbers": len(admins), "label": "Admins"},
            {"icon": "fas fa-eye", "numbers": views, "label": "Weekly Views"},
            {"icon": "fas fa-code", "numbers": count, "label": "Scripts"},
        ]

        disabled_animes = site_data["disabled_animes"]

        data = get_mangas()
        pagination = data["pagination"]
        keyword = GET.get("keyword", "")
        query = ApiHandler().build_url(
                    base="", 
                    endpoint="/admin/dashboard/", 
                    params={ "page": pagination["pages"], "keyword": keyword }
                    )

        data["pagination"]["pages"] = int(data["pagination"]["pages"])
        data["pagination"]["page"] = int(data["pagination"]["page"])

        self.set_context(context=context, data={
            "analytics": analytics,
            "disabled_animes": disabled_animes,
            "mangas": data["mangas"],
            "pagination": pagination,
            "query": query,
        })
        return self.root(request=request, context=context, template="pages/admin/dashboard.html")

    @adminValidator
    def scripts(self, request, site_data, context, **kwargs):
        scripts = site_data["scripts"]
        head_scripts = scripts["head_scripts"]
        foot_scripts = scripts["foot_scripts"]
        ads_scripts = scripts["ads_scripts"]

        self.set_context(context=context, data={
            "head_scripts": head_scripts,
            "foot_scripts": foot_scripts,
            "ads_scripts": ads_scripts,
        })
        return self.root(request=request, context=context, template="pages/admin/scripts.html")

    @adminValidator
    def general(self, request, site_data, context, **kwargs):
        values = site_data["values"]
        images = values["images"]
        inputs = values["inputs"]
        socials = values["socials"]

        self.set_context(context=context, data={
            "images": images,
            "inputs": inputs,
            "socials": socials,
        })
        return self.root(request=request, context=context, template="pages/admin/general.html")

    @adminValidator
    def advance(self, request, site_data, context, **kwargs):
        settings = site_data["settings"]
        self.set_context(context=context, data={
            "settings": settings,
        })
        return self.root(request=request, context=context, template="pages/admin/advance.html")   

    @adminValidator
    def admins(self, request, site_data, context, **kwargs):
        admins = admin_database.get_admins()
        self.set_context(context=context, data={
            "admins": admins,
            "admins_count": len(admins),
        })
        return self.root(request=request, context=context, template="pages/admin/admins.html")   

    def root(self, request, template, context={}, titled=False): 
        page_url = request.build_absolute_uri()
        context["page_url"] = page_url 

        if "page" in context: return render(request, template, context=context)

        path = request.path.split("/")
        full_path = request.path_info
        paths = full_path.split('/')
        length = len(paths)
        page = paths[length - 2]

        context["page"] = page 
        context["titled"] = titled 

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


def get_mangas():
    try:
        response = requests.get(f"{MANGA_API_URL}/filter")
        response.raise_for_status() 
        data = response.json()

        if data["status_code"] != 200:
            return {
                "pagination": {
                    "page": "1",
                    "pages": "1"
                },
                "mangas": []
            }
        
        mangas_response = {
            "pagination": data["data"]["pagination"],
            "mangas": data["data"]["mangas"]
        }
        
        return mangas_response
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return {
            "pagination": {
                "page": "1",
                "pages": "1"
            },
            "mangas": []
        }
