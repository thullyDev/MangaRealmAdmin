class LatanimeBlueprints:
    latanime_home_blueprint = { 
            "slider": {
                "parent_selector": ".carousel-item",
                "children": { 
                    "anime_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "preview_image": {
                        "selector": ".lozad.preview-image",
                        "attributes": {
                            "url": "data-src",
                        }
                    },
                    "background_image": {
                        "selector": ".lozad.d-block.w-100",
                        "attributes": {
                            "url": "data-src",
                            "synopsis": "alt"
                        }
                    },
                    "description": {
                        "selector": ".p-slider",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                }
            },
            "latest_episodes": {
                "parent_selector": ".col-6.col-md-6.col-lg-3.mb-3",
                "children": {
                    "type": {
                        "selector": ".info_cap > span",
                        "attributes": {
                            "type": "text_content",
                        }
                    },
                    "episode_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".lozad.nxtmainimg",
                        "attributes": {
                            "url": "data-src",
                            "title": "alt"
                        }
                    },
                }
            },
        }
    latanime_filter_blueprint = { 
            "animes": {
                "parent_selector": ".col-md-4.col-lg-3.col-xl-2.col-6.my-3",
                "children": {
                    "anime_slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "image": {
                        "selector": ".img-fluid2.shadow-sm",
                        "attributes": {
                            "url": "src",
                        }
                    },
                    "title": {
                        "selector": "h3.my-1",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "year": {
                        "selector": "span",
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
    latanime_schedule_blueprint = { 
            "monday": {
                "parent_selector": ".accordionItem:nth-child(1) .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "tuesday": {
                "parent_selector": ".accordionItem:nth-child(2)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "wednesday": {
                "parent_selector": ".accordionItem:nth-child(3)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "thursday": {
                "parent_selector": ".accordionItem:nth-child(4)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "friday": {
                "parent_selector": ".accordionItem:nth-child(5)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "saturday": {
                "parent_selector": ".accordionItem:nth-child(6)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            "sunday": {
                "parent_selector": ".accordionItem:nth-child(7)  .col-lg-4",
                "children": {
                    "slug": {
                        "selector": "a",
                        "attributes": {
                            "slug": "href",
                        }
                    },
                    "title": {
                        "selector": ".my-2",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "type": {
                        "selector": ".btn",
                        "attributes": {
                            "text": "text_content",
                        }
                    },
                    "image": {
                        "selector": "img.w-100",
                        "attributes": {
                            "url": "src",
                        }
                    },
                }
            },
            # "no_date": {
            #     "parent_selector": ".accordionItem:nth-child(9)  .col-lg-4",
            #     "children": {
            #         "slug": {
            #             "selector": "a",
            #             "attributes": {
            #                 "slug": "href",
            #             }
            #         },
            #         "title": {
            #             "selector": ".my-2",
            #             "attributes": {
            #                 "text": "text_content",
            #             }
            #         },
            #         "type": {
            #             "selector": ".btn",
            #             "attributes": {
            #                 "text": "text_content",
            #             }
            #         },
            #         "image": {
            #             "selector": "img.w-100",
            #             "attributes": {
            #                 "url": "src",
            #             }
            #         },
            #     }
            # },
        }
    latanime_anime_blueprint = {
        "title": {
            "parent_selector": ".col-lg-9.col-md-8 > h2",
            "attribute": "text_content",
            "single_select": True,
            "key": "title",
        },
        "synonyms": {
            "parent_selector": ".col-lg-9.col-md-8 > h3.fs-6.text-light.opacity-75",
            "attribute": "text_content",
            "single_select": True,
            "key": "synonyms",
        },
        "synopsis": {
            "parent_selector": ".fs-6.text-light.opacity-75",
            "attribute": "text_content",
            "single_select": True,
            "key": "synopsis",
        },
        "description": {
            "parent_selector": ".my-2.opacity-75",
            "attribute": "text_content",
            "single_select": True,
            "key": "description",
        },
        "status": {
            "parent_selector": ".btn-estado",
            "attribute": "text_content",
            "single_select": True,
            "key": "status",
        },
        "poster_image": {
            "parent_selector": ".img-fluid2",
            "attribute": "src",
            "single_select": True,
            "key": "poster_image",
        },
        "genres": {
            "parent_selector": ".col-lg-9.col-md-8 > a",
            "children": {
                "slug": {
                    "selector": ".btn",
                    "attributes": {
                        "text": "text_content",
                    }
                },
            },
        },
        "chapters": {
            "parent_selector": ".col-lg-9.col-md-8 > .row",
            "attribute": "html",
            "single_select": True,
            "key": "chapters_html",
        }
    }
    Latanime_episode_blueprint = {
        "episode_title": {
            "parent_selector": ".mojon4.my-3",
            "attribute": "text_content",
            "single_select": True,
            "key": "title",
        },
        "embed_links": {
            "parent_selector": ".cap_repro.d-flex.flex-wrap > li",
            "children": {
                "link": {
                    "selector": ".play-video",
                    "attributes": {
                        "embed_link": "data-player",
                        "name": "text_content",
                    }
                },
            },
        },
        "recommendations": {
            "parent_selector": ".recomendados.my-3",
            "children": {
                "slug": {
                    "selector": "a",
                    "attributes": {
                        "slug": "href",
                    }
                },
                "image": {
                    "selector": "img",
                    "attributes": {
                        "url": "src",
                    }
                },
                "date": {
                    "selector": "p",
                    "attributes": {
                        "text": "text_content",
                    }
                },
                "title": {
                    "selector": "h5",
                    "attributes": {
                        "text": "text_content",
                    }
                },
                "episode": {
                    "selector": "span",
                    "attributes": {
                        "text": "text_content",
                    }
                },
            },
        },
    }
    blueprints = {
    	"latanime_home": latanime_home_blueprint,
        "latanime_filter": latanime_filter_blueprint,
        "latanime_schedule": latanime_schedule_blueprint,
        "latanime_anime": latanime_anime_blueprint,
        "latanime_episode": Latanime_episode_blueprint,
    }
