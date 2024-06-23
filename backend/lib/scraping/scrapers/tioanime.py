from ..scraper import Scraper
from ..services.tioanime import Tioanime

class TioanimeScraper(Scraper, Tioanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["tioanime_home"])

    def get_filter(self, data):
        params = {}
        for key, value in data.items():
            if not value or key not in self.queries: continue
            
            if key == "type": 
                params["type%5B%5D"] = value
                continue

            if key == "genre": 
                params["genero%5B%5D"] = value
                continue

            if key == "keywords": 
                params["q"] = value
                continue

            if key == "page": 
                params["p"] = value
                continue

            params[key] = value

        return self.get(base=self.base, endpoint=self.animes_endpoint, blueprint=self.blueprints["tioanime_filter"], params=params)

    def get_schedule(self):
        return self.get(base=self.base, endpoint=self.schedule_endpoint, blueprint=self.blueprints["tioanime_schedule"])

    def get_anime(self, slug):
        return self.get(base=self.base, endpoint=f"{self.anime_endpoint}{slug}", blueprint=self.blueprints["tioanime_anime"])

    def get_episode(self, slug): return self.get(base=self.base, endpoint=f"{self.watch_endpoint}{slug}", blueprint=self.blueprints["tioanime_episode"])
