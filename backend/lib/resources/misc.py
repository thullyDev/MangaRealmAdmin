import re
import random
# import uuid
import json
import datetime
import string
import threading

def valid_email(email):
    email_regex = r"^[^\s@]+@[^\s@]+\.[^\s@]+$"
    return re.match(email_regex, email) is not None

def hide_text(text, limit=3): return text[:limit] + "..."

def get_data_from_string(rawdata):
    return json.loads(rawdata)

def generate_random_code(length=6): return ''.join(random.choices('0123456789', k=length))

def generate_unique_id(length=100):
    characters = string.ascii_letters + string.digits  
    return ''.join(random.choice(characters) for _ in range(length))

def get_email(data):
    return data.get("email")

def get_time_difference(TIME_A, TIME_B):
    time_a = datetime.datetime.strptime(TIME_A.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")
    time_b = datetime.datetime.strptime(TIME_B.strftime("%Y-%m-%d %H:%M:%S"), "%Y-%m-%d %H:%M:%S")

    return time_a - time_b

def set_interval(_time, func):
    _ttimer = threading.Timer(_time, func) 
    _ttimer.start()

    return _ttimer
