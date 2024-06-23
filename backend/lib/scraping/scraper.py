from ..handlers import ( ApiHandler )
from ..database import ( Cache )
from bs4 import BeautifulSoup

cache = Cache()

class Scraper(ApiHandler):
    def get(self, base, blueprint, endpoint="", params={}, https_safe=True, cache_id=""):
        if cache_id:
            data = cache.get(name=cache_id)
            if data: return data

        html = self.request(base=base, endpoint=endpoint, https_safe=https_safe, params=params, html=True)

        if not html: return None

        data = {}
        soup = BeautifulSoup(html, 'html.parser')
        for key, value in blueprint.items():
            data[key] = self.process(soup=soup, blueprint=value)

        if cache_id: cache.set(name=cache_id, data=data)

        return data

    def extract(self, element, config):
        data = {}
        for key, value in config.items():
            data[key] = {}
            selector = value.get("selector")
            return_type = value.get("return_type")
            selected_elements = element.select(selector)

            if return_type == "list": data = []

            for select_element in selected_elements:
                for attr_key, attr_value in value.get("attributes").items():
                    if return_type != "list": 
                        if attr_value == "text_content": 
                            data[key][attr_key] = select_element.text.strip()
                            continue

                        if attr_value == "html": 
                            data[key][attr_key] = str(select_element)
                            continue

                        data[key][attr_key] = select_element.get(attr_value) 
                        continue

                    if attr_value == "text_content": 
                        data.append(select_element.text)
                        continue

                    if attr_value == "html": 
                        data.append(str(select_element))
                        continue

                    data.append(select_element.get(attr_value)) 

        return data

    # processes each parent select, and passes to the children to the extract function
    def process(self, soup, blueprint):
        parent_selector = blueprint.get("parent_selector")
        single_select = blueprint.get("single_select")

        data = {}
        if single_select:
            elements = soup.select(parent_selector)
            attribute = blueprint.get("attribute")
            key = blueprint.get("key")

            for element in elements:
                if attribute == "html": data[key] = str(element); continue
                
                value = element.get(attribute).strip() if attribute != "text_content" else element.text.replace("\n", " ").strip()
                data[key] = value
            
            return data

        elements = soup.select(parent_selector)

        data = [self.extract(element, blueprint["children"]) for element in elements]

        return data
