from ..routers import Admin
from django.urls import path, include
from ..handlers import produce_urlpatterns, route_producer

admin = Admin()

routes = [
    route_producer(route="", view=admin.base),
    route_producer(route="dashboard/", view=admin.dashboard),
    route_producer(route="login/", view=admin.admin_login, name="admin_login"),
    route_producer(route="scripts/", view=admin.scripts),
    route_producer(route="general/", view=admin.general),
    route_producer(route="advance/", view=admin.advance),
    route_producer(route="admins/", view=admin.admins),
]

urlpatterns = produce_urlpatterns(routes)
urlpatterns.append(path('ajax/', include('backend.lib.urls.adminAjaxUrls')))
