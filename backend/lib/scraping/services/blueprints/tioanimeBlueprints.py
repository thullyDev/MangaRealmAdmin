class TioanimeBlueprints:
    tioanime_home_blueprint = { 
            "latest_episodes": {
                "parent_selector": ".episodes > .col-6.col-sm-4.col-md-3",
                "children": { 
                    "episode_slug": {
                        "selector": ".episode > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                            "title": "alt"
                        }
                    },
                }
            },
            "latest_animes": {
                "parent_selector": ".col-6.col-sm-4.col-md-3.col-xl-2",
                "children": {
                    "anime_slug": {
                        "selector": ".anime > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                            "title": "alt"
                        }
                    },
                }
            },
        }
    tioanime_filter_blueprint = { 
            "animes": {
                "parent_selector": ".col-6.col-sm-4.col-md-3.col-xl-2",
                "children": {
                    "anime_slug": {
                        "selector": ".anime > a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "page": {
                "parent_selector": ".pagination",
                "children": {
                    "page": {
                        "selector": ".page-item.active",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "pages": {
                "parent_selector": ".pagination",
                "children": {
                    "page": {
                        "selector": ".page-item",
                        "return_type": "list",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
        }
    tioanime_schedule_blueprint = { 
            "monday": {
                "parent_selector": "#Monday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "tuesday": {
                "parent_selector": "#Tuesday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "wednesday": {
                "parent_selector": "#Wednesday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "thursday": {
                "parent_selector": "#Thursday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "friday": {
                "parent_selector": "#Friday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "saturday": {
                "parent_selector": "#Saturday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "sunday": {
                "parent_selector": "#Sunday > .episode",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".title",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": ".fa-play-circle > img",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
        }
    tioanime_anime_blueprint = {
        "title": {
            "parent_selector": "h1.title",
            "attribute": "text_content",
            "single_select": True,
            "key": "title",
        },
        "original_title": {
            "parent_selector": "p.original-title",
            "attribute": "text_content",
            "single_select": True,
            "key": "original_title",
        },
        "type": {
            "parent_selector": "span.anime-type-peli",
            "attribute": "text_content",
            "single_select": True,
            "key": "type",
        },
        "year": {
            "parent_selector": "span.year",
            "attribute": "text_content",
            "single_select": True,
            "key": "year",
        },
        "season": {
            "parent_selector": "span.season > .season",
            "attribute": "text_content",
            "single_select": True,
            "key": "season",
        },
        "score": {
            "parent_selector": ".mal",
            "attribute": "text_content",
            "single_select": True,
            "key": "score",
        },
        "votes": {
            "parent_selector": ".total > span",
            "attribute": "text_content",
            "single_select": True,
            "key": "votes",
        },
        "description": {
            "parent_selector": ".sinopsis",
            "attribute": "text_content",
            "single_select": True,
            "key": "description",
        },
        "status": {
            "parent_selector": ".btn.btn-block.status",
            "attribute": "text_content",
            "single_select": True,
            "key": "status",
        },
        "poster_image": {
            "parent_selector": ".thumb img",
            "attribute": "src",
            "single_select": True,
            "key": "poster_image",
        },
        "background_image": {
            "parent_selector": ".backdrop > img",
            "attribute": "src",
            "single_select": True,
            "key": "background_image",
        },
        "genres": {
            "parent_selector": ".genres",
            "attribute": "html",
            "single_select": True,
            "key": "genres_html",
        },
        "last_scripts": {
            "parent_selector": "script",
            "attribute": "text_content",
            "single_select": True,
            "key": "episodes_script",
        },
    }
    tioanime_episode_blueprint = {
        "episode_title": {
            "parent_selector": ".anime-title.text-center.mb-4",
            "attribute": "text_content",
            "single_select": True,
            "key": "title",
        },
        "script": {
            "parent_selector": "script",
            "attribute": "html",
            "single_select": True,
            "key": "embed_script",
        },
    }
    blueprints = {
        "tioanime_home": tioanime_home_blueprint,
        "tioanime_filter": tioanime_filter_blueprint,
        "tioanime_schedule": tioanime_schedule_blueprint,
        "tioanime_anime": tioanime_anime_blueprint,
    	"tioanime_episode": tioanime_episode_blueprint,
    }