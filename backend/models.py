# from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Admin(models.Model):
    username = models.CharField(max_length=80, unique=True)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=100, blank=True) 
    profile_image = models.CharField(max_length=100, null=True, blank=True) 
    role = models.CharField(max_length=200, null=True) 
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)

    class Meta:
        # ordering = ("+username",)
        app_label = 'backend'

    def _str_(self):
        return self.name


class User(models.Model):
    username = models.CharField(max_length=80)
    email = models.CharField(max_length=80, unique=True)
    password = models.CharField(max_length=20) 
    temporary_id = models.CharField(max_length=100, blank=True) 
    profile_image = models.CharField(max_length=100, null=True, blank=True) 
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False,unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)

    class Meta:
        # ordering = ("+username",)
        app_label = 'backend'

    def _str_(self):
        return self.name


class Watchlists(models.Model):
    slug = models.CharField(unique=True, primary_key=True)
    user = models.IntegerField() 
    email = models.CharField(max_length=80)
    anime_title = models.CharField(max_length=200)
    watch_type = models.CharField(max_length=10) 
    anime_image = models.CharField(max_length=200) 
    created_at = models.DateTimeField(auto_now_add=True, editable=False,unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)

    class Meta:
        app_label = 'backend'

    def _str_(self):
        return self.name

class Rooms(models.Model):
    room_id = models.CharField(unique=True, primary_key=True)
    room_name = models.CharField(max_length=100, default="") 
    creator_email = models.CharField(max_length=80)
    creator_id = models.CharField(max_length=80)
    creator_username = models.CharField(max_length=80)
    creator_profile = models.CharField(max_length=300, null=True, default=None)
    slug = models.CharField(default=None)
    anime_image = models.CharField(max_length=200, default="") 
    anime_title = models.CharField(max_length=200)
    watch_type = models.CharField(max_length=200, default="main")
    unlimited = models.BooleanField(default=False)
    private = models.BooleanField(default=True)
    limit = models.IntegerField() 
    created_at = models.DateTimeField(auto_now=True, editable=False,unique=True)
    updated_at = models.DateTimeField(auto_now=True, editable=False, unique=True)
    room_code = models.CharField(max_length=7, null=True, default=None)

    class Meta:
        app_label = 'backend'

    def _str_(self):
        return self.name

