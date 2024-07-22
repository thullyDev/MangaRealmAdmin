from django.urls import path, include

urlpatterns = [
    path('admin/', include('backend.lib.urls.adminUrls')),
]
