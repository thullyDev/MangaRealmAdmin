from rest_framework.views import APIView
from django.shortcuts import render, redirect
from ....resources import valid_email, hide_text, generate_unique_id
from ....database import AdminDatabase
from ....handlers import ResponseHandler
from ....decorators import timer
from ...base import Base

admin_database = AdminDatabase()

class AdminAuthAjax(Base):
    @timer
    def login(self, request, POST, **kwargs):
        if not POST: return redirect("/")

        data = self.process_request(POST.get("data", "{}"))
        email = data.get("email")
        password = data.get("password")

        if not valid_email(email): 
            return self.bad_request_response(data={
                    "message": "this email is not a valid email"
                })

        if not email and not username: return self.forbidden_response()

        data = admin_database.get_admin(email) 

        if not data:
            return self.forbidden_response(data={
                    "message": "this user does not exist"
                })

        if data["deleted"] == True:  
            return self.forbidden_response()

        if password != data["password"]:
            return self.forbidden_response(data={
                    "message": "not valid password"
                })

        del data["deleted"]
        del data["password"]

        
        data["temporary_id"] = generate_unique_id()

        admin_database.update_admin(data={ "email": email, "temporary_id": data["temporary_id"] }) 

        return self.successful_response(data={ "message": "successful login" }, cookies=True, cookies_data={
            "email": data["email"],
            "username": data["username"],
            "temporary_id": data["temporary_id"],
        })
    