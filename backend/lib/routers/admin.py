from rest_framework.views import APIView
from django.shortcuts import redirect, render
from django.core.paginator import Paginator, EmptyPage
from ..decorators import adminValidator, timer
from ..handlers import ResponseHandler, SiteHandler
from ..scraping import LatanimeScraper
from ..database import AdminDatabase
# from .base import Base
from pprint import pprint
import json

admin_database = AdminDatabase()
latanime = LatanimeScraper()
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
        latanime_keyword = GET.get("latanime_keyword", "")
        latanime_page = GET.get("latanime_page", 1)

        admins = admin_database.get_admins()
        views = admin_database.cget(name="site_views")
        views = 0 if not views else views 
        scripts = site_data.get("scripts", "")

        count = 0
        for inner_key, inner_scripts in scripts.items():
            for key, script in inner_scripts.items():
                if script['value']: count += 1

        raw_latanimes = latanime.get_filter(data={ "page": latanime_page, "keywords": latanime_keyword })
        latanimes = self.filter_data_processing(rawdata=raw_latanimes)

        analytics = [
            {"icon": "fas fa-user-cog", "numbers": len(admins), "label": "Admins"},
            {"icon": "fas fa-eye", "numbers": views, "label": "Weekly Views"},
            {"icon": "fas fa-code", "numbers": count, "label": "Scripts"},
        ]

        disabled_animes = site_data["disabled_animes"]

        self.set_context(context=context, data={
            "analytics": analytics,
            "disabled_animes": disabled_animes,
            "latanimes": latanimes["animes"],
            "latanimes_pages": {
                "page": latanimes["page"],
                "pages": latanimes["pages"],
            },
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


    def filter_data_processing(self, rawdata):
        if not rawdata: return {
            "page": 1,
            "page": 0,
            "animes": [],
        } 
        animes = rawdata.get("animes")
        pages = rawdata.get("pages")[0]
        data = {
            "page": int(rawdata.get("page")[0].get("page", {}).get("text", "1")),
            "pages": "1" if not pages else int(pages[len(pages) - 2]),
            "animes": []
        }

        disabled_animes = site.get_save_to_data("disabled_animes")

        for anime in animes:
            title = anime.get("title").get("text")
            temp = title.split(" ")
            watch_type = temp[len(temp) - 1]
            slug = anime.get("anime_slug").get("slug").replace(f"https://{latanime.base}/anime", "")
            data["animes"].append({
                "image_url": anime.get("image").get("url"),
                "title": title,
                "slug": slug,
                "year": anime.get("year").get("text").strip(),
                "type": watch_type,
                "disabled": False if slug not in disabled_animes else True,
            })

        return data    
