from .blueprints import TioanimeBlueprints

class Tioanime(TioanimeBlueprints):
    base = "tioanime.com"
    animes_endpoint = "/directorio"
    anime_endpoint = "/anime/"
    watch_endpoint = "/ver/"
    schedule_endpoint = "/programacion"
    queries = {
        "keywords",
        "page",
        "type",
        "genre",
        "status",
        "sort",
        "year",
    }

