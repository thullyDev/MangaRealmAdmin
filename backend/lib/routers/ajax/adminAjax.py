from django.shortcuts import redirect
from ...decorators import timer, adminValidator
from ...handlers import SiteHandler
from ...database import AdminDatabase, Storage
from ...resources import get_data_from_string
from ..base import Base
from ...resources import SITE_KEY, SITE
import json
import requests

admin_database = AdminDatabase()
site = SiteHandler()
storage = Storage()

class AdminAjax(Base):
    @adminValidator
    def save_data(self, request, POST, site_data, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        data = get_data_from_string(POST.get("save_data"))
        save = POST.get("save")

        if save not in { "settings", "values", "scripts" }:
            return self.bad_request_response()

        save_data = site_data.get(save, {})

        self.update_data(save, data, save_data)

        if save == "values": 
            self.process_images(data, save_data)

        # print("site_logo2 ====> ", save_data["images"]["site_logo"]["value"])
        self.save_site_data(save_data, save)
        self.alert_site()
        
        return self.successful_response()

    def update_data(self, save, new_data, old_data):
        if not old_data:
            return

        if save == "settings":
            for key, value in old_data.items():
                old_data[key]["value"] = new_data[key]
            return

        for type_key, type_values in old_data.items():
            for key, value in type_values.items():
                old_data[type_key][key]["value"] = new_data[key]


    def save_site_data(self, data, name):
        site_data = self.get_site_data()
        site_data[name] =  data
        admin_database.hset(name="site_data", data=site_data, expiry=False)


    def process_images(self, new_data, old_data):
        images_keys = list(old_data["images"].keys())
        images = []

        for key, value in new_data.items():
            if key not in images_keys or (old_data["images"][key]["value"] == value and len(value) < 1000):
                continue 

            images.append({
                "name": key,
                "value": value.replace("data:image/jpeg;base64,", ""),
            })
            
        if not images:
            return

        for img in images:
            name = img.get("name")
            value = img.get("value")
            image_url = storage.upload_base64_image(name=name, base64_img=value)

            if image_url: 
                old_data["images"][name]["value"] = image_url

        print("site_logo ====> ", old_data["images"]["site_logo"]["value"])


    @adminValidator
    def reset_settings(self, request, POST, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        site_key = POST.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })
            
        site.set_default_site_data()
        return self.successful_response()

    @adminValidator
    def add_admin(self, request, POST, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        site_key = POST.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })

        data = get_data_from_string(POST.get("data"))
        is_valid = self.validate(
            username=data["username"],
            email=data["email"],
            password=data["password"],
            confirm=data["confirm"],
            )

        if not is_valid:
            return self.bad_request_response()

        del data["confirm"]
        admin_database.set_admin(email=data["email"], data=data)
        return self.successful_response()

    @adminValidator
    def update_admin(self, request, POST, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        site_key = POST.get("site_key")

        if SITE_KEY != site_key:
            return self.forbidden_response(data={ "message": "site key is invalid" })

        data = get_data_from_string(POST.get("data"))

        admin_database.update_admin(data=data)
        return self.successful_response()

    @adminValidator
    def update_user(self, request, POST, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        email = POST.get("id")
        data = get_data_from_string(POST.get("data"))
        deleted = bool(data["deleted"])
        deleted = False if deleted else True

        data["email"] = email
        data["deleted"] = deleted

        data = admin_database.update_users(data=data)
        return self.successful_response(data={ "data": { "deleted": data["deleted"] }})

    @adminValidator
    def update_anime(self, request, POST, site_data, *args, **kwargs):
        if not POST:
            return redirect("admin_login")

        slug = POST.get("id")
        disabled_animes = site_data["disabled_animes"]

        if slug in disabled_animes:
            del disabled_animes[slug]
            site.save_site_data(name="disabled_animes", data=disabled_animes)
            return self.successful_response(data={ "data": { "deleted": False }})

        disabled_animes[slug] = 0
        site.save_site_data(name="disabled_animes", data=disabled_animes)
        return self.successful_response(data={ "data": { "deleted": True }})

    @timer
    def create_owner(self, request, GET, **kwargs):
        req_site_key = GET.get("key")
        password = GET.get("password")
        
        if req_site_key != SITE_KEY:
            return self.forbidden_response()

        if None in [ password ]:
            return self.bad_request_response()

        if len(password) < 8:
            return self.bad_request_response(data={ "message": "password too short, it should be atleast 8 letters" })

        email = "owner@gmail.com"
        username = "owner"

        admin_data = {
            "email": email,
            "password": password,
            "username": username,
            "deleted": False,
            "profile_image": None,
            "role": "owner",
        }

        res_data = admin_database.update_admin(data=admin_data)
        return self.successful_response(data={ "message": "owner was created" })

    def alert_site(self):
        requests.get(f"{SITE}/admin_refresh?site_key={SITE_KEY}", timeout=1)

    def get_site_data(self):
        data = admin_database.hget("site_data") 
        return data if data else {}

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})


    def validate(self, username, email, password, confirm):
        if None in [username, email, password, confirm] or \
            password != confirm or \
            len(confirm) < 8:
            return False

        return True
