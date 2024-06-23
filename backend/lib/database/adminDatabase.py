from .database import Database
from ..resources import get_email

class AdminDatabase(Database):
    _instance = None
    
    def __new__(cls):
        if not cls._instance:
            cls._instance = super(Database, cls).__new__(cls)
        return cls._instance

    def get_admin(self, email):
        if not email: return 
        return self.get(unit="admin", key="email", unique_id=email)
        
    def set_admin(self, email, data):
        return self.set(unit="admin", unique_id=email, data=data)

    def update_admin(self, data):
        email = get_email(data)
        if not email: return 
        return self.update(unit="admin", data=data, unique_id=email, key="email")

    def get_admins(self):
        return self.get_all(unit="admin")

    def get_users(self):
        return self.get_all(unit="user")

    def update_users(self, data):
        email = get_email(data)
        if not email: return 
        return self.update(unit="user", data=data, unique_id=email, key="email")

    def get_query_users(self, query):
        return self.get_query(unit="user", username=query, email=query)
