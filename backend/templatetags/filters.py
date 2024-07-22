from django import template
from decouple import config
import ast

register = template.Library()
SITE = config("SITE")


@register.filter(name='set_image')
def set_image(value):
    return f"{SITE}/{value}" if "http" not in value else value

@register.filter(name='replace')
def replace(value, arg):
    if not isinstance(value, str):
        return value

    old_value, new_value = arg.split(',')
    return value.replace(old_value, new_value)

@register.filter(name='times') 
def times(number):
    return range(1, number + 1)

@register.filter(name='pagi') 
def pagi(pages):
    end = 6 if pages > 6 else pages + 1
    return range(1, end)

@register.filter(name='safebool') 
def safebool(value):
    hashmap = {
        False: "false",
        True: "true"
    }
    
    return hashmap.get(value, value)

@register.filter(name='safe_list') 
def safe_list(value):
    return ast.literal_eval(value)

# @register.filter(name='build_url') 
# def build_url(value):
#     queries = value.split("||")
#     endpoint = queries[0]
#     print(queries[1])
#     params = {}
#     params = json.loads(queries[1])
#     url = f"{endpoint}"
#     count = 0
#     for key, value in params.items():
#         url += f"?{key}={value}" if not count else f"&{key}={value}"
#         count += 1
    
#     # return url
#     return