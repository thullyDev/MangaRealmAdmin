from ..scraper import Scraper
from ..services.latanime import Latanime

class LatanimeScraper(Scraper, Latanime):
    def get_home(self):
    	return self.get(base=self.base, blueprint=self.blueprints["latanime_home"])

    def get_filter(self, data):
        params = { "letra": "false" }
        for key, value in data.items():
            if not value or key not in self.queries: continue

            if key == "type": 
                params["categoria"] = value
                continue

            if key == "letter": 
                params["letra"] = value
                continue

            if key == "genre": 
                params["genero"] = value
                continue

            if key == "year": 
                params["fecha"] = value
                continue

            if key == "page": 
                params["p"] = value
                continue

            params[key] = value

        return self.get(base=self.base, endpoint=self.animes_endpoint, blueprint=self.blueprints["latanime_filter"], params=params)

    def get_search(self, data):
        params = {}
        for key, value in data.items():
            if key not in self.queries: continue

            if key == "page": 
                params["p"] = value
                continue

            if key == "keywords": 
                params["q"] = value
                continue

        return self.get(base=self.base, endpoint=self.search_endpoint, blueprint=self.blueprints["latanime_filter"], params=params)

    def get_schedule(self): return self.get(base=self.base, endpoint=self.schedule_endpoint, blueprint=self.blueprints["latanime_schedule"])

    def get_anime(self, slug): return self.get(base=self.base, endpoint=f"{self.anime_endpoint}{slug}", blueprint=self.blueprints["latanime_anime"])
   
    def get_episode(self, slug): return self.get(base=self.base, endpoint=f"{self.watch_endpoint}{slug}", blueprint=self.blueprints["latanime_episode"])