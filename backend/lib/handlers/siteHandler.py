from ..database import Database

database = Database()

class SiteHandler:
    def save_site_data(self, data, name):
        site_data = self.get_site_data()
        site_data[name] =  data
        database.hset(name="site_data", data=site_data, expiry=False)

    def update_data(self, new_data, old_data):
        for key, value in new_data.items():
            if not value and key in old_data: break 
            old_data[key] = value

    def get_site_data(self): 
        site_data = database.hget("site_data", {})
        if site_data:
            return site_data

        return self.set_default_site_data()

    def get_save_to_data(self, name):
        site_data = self.get_site_data()
        return site_data.get(name, {})

    def get_amount(self, amount_type):
        if amount_type not in { "settings", "values", "attributes", "scripts" }:
            raise ValueError(f"Invalid value for amount_type: {amount_type}. It must be one of 'settings', 'values', 'attributes', or 'scripts'") 

        site_data = self.get_site_data()
        return len(site_data.get(amount_type, ""))


    def set_default_site_data(self):
        site_data = self.get_default_site_data()
        database.hset(name="site_data", data=site_data, expiry=False)
        return site_data

    def get_default_site_data(self):
        return {
            "scripts": {
                "head_scripts": {
                    "global_head": {"name": "global_head", "value": ""},
                    "home_head": {"name": "home_head", "value": ""},
                    "filter_head": {"name": "filter_head", "value": ""},
                    "profile_head": {"name": "profile_head", "value": ""},
                    "anime_head": {"name": "anime_head", "value": ""},
                    "watch_head": {"name": "watch_head", "value": ""},
                    "schedule_head": {"name": "schedule_head", "value": ""},
                    "watch_together_browsing_head": {"name": "watch_together_browsing_head", "value": ""},
                },
                "foot_scripts": {
                    "global_foot": {"name": "global_foot", "value": ""},
                    "home_foot": {"name": "home_foot", "value": ""},
                    "filter_foot": {"name": "filter_foot", "value": ""},
                    "profile_foot": {"name": "profile_foot", "value": ""},
                    "anime_foot": {"name": "anime_foot", "value": ""},
                    "watch_foot": {"name": "watch_foot", "value": ""},
                    "schedule_foot": {"name": "schedule_foot", "value": ""},
                    "watch_together_browsing_foot": {"name": "watch_together_browsing_foot", "value": ""},
                },
                "ads_scripts": {
                    "top_advertisement": {"name": "top_advertisement", "value": "", "height": "0px"},
                    "bottom_advertisement": {"name": "bottom_advertisement", "value": "", "height": "0px"},
                    "middle_advertisement": {"name": "middle_advertisement", "value": "", "height": "0px"},
                    "under_player_advertisement": {"name": "under_player_advertisement", "value": "", "height": "0px"},
                    "above_comments_advertisement": {"name": "above_comments_advertisement", "value": "", "height": "0px"},
                },
            },
            "values": {
                "images": {
                    "site_logo": {"name": "site_logo", "value": "/static/images/site-logo.png"},
                    "favicon_logo": {"name": "favicon_logo", "value": "/static/images/favicon.png"},
                    "alert": {"name": "alert", "value": "/static/images/gifs/alert.gif"},
                    "maintenance": {"name": "maintenance", "value": "/static/images/gifs/maintenance.gif"},
                    # "empty": {"name": "empty", "value": "/static/images/gifs/empty.gif"},
                    "admin_background": {"name": "admin_background", "value": "/static/images/gifs/admin-login-background.gif"},
                    "authentication_background": {"name": "authentication_background", "value": "/static/images/auth-bg-image.png"},
                    "default_account_image": {"name": "default_account_image", "value": "/static/images/default-pfp.jpg"},
                },
                "inputs": {
                    "site_name": {"value": "AnimeHoshi", "name": "site_name"},
                    "email": {"value": "", "name": "email"},
                    "title": {"value": "Watch Anime On AnimeHoshi For No ads", "name": "title"},
                    "site_description": {
                        "value": "AnimeHoshi is a vibrant online platform offering a diverse collection of anime content for free streaming. With an extensive library spanning genres and popular titles, AnimeHoshi provides enthusiasts with an immersive experience. User-friendly navigation and high-quality playback make it a go-to destination for anime lovers seeking free, accessible entertainment.",
                        "name": "site_description",
                        "type": "field",
                    },
                    "site_notice": {
                        "value": "",
                        "name": "site_notice",
                        "type": "field",
                    },
                },
                "socials": {
                    "discord": {"value": "https://discord.com/", "name": "discord"},
                    "twitter": {"value": "https://twitter.com/", "name": "twitter"},
                    "reddit": {"value": "https://reddit.com/", "name": "reddit"},
                    "donate": {"value": "https://ko-fi.com/", "name": "donate"},
                },
            },
            "settings": {
                "maintanence": {"name": "maintanence", "value": False},
                "dev_tools_detection": {"name": "dev_tools_detection", "value": False},
                "adblocker_detection": {"name": "adblocker_detection", "value": False},
                # "alert": {"name": "alert", "value": True},
                "authentication": {"name": "authentication", "value": True},
                "anime": {"name": "anime", "value": True},
                "watch": {"name": "watch", "value": True},
                "random": {"name": "random", "value": True},
                "comments": {"name": "comments", "value": True},
                "watch_togather": {"name": "watch_togather", "value": True},
                "add_list": {"name": "add_list", "value": True},
                "user": {"name": "user", "value": True},
                "schedule": {"name": "schedule", "value": True},
                "features": {"name": "features", "value": True},
                "footer": {"name": "footer", "value": True},
                # "landing": {"name": "landing", "value": True},
                "title": {"name": "title", "value": True},
                "donation": {"name": "donation", "value": True},
                "socials": {"name": "socials", "value": True},
                "contact": {"name": "contact", "value": True},
                "loader": {"name": "loader", "value": True},
                "home_animes": {"name": "home_animes", "value": True},
                # "dark_mode": {"name": "dark_mode", "value": True},
            },
            "disabled_animes": {},
        }

