from .blueprints import LatanimeBlueprints

class Latanime(LatanimeBlueprints):
    base = "latanime.org"
    animes_endpoint = "/animes/"
    anime_endpoint = "/anime/"
    watch_endpoint = "/ver/"
    schedule_endpoint = "/calendario/"
    search_endpoint = "/buscar"
    queries = {
        "keywords",
        "page",
        "type",
        "genre",
        "year",
    }
