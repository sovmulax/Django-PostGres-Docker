from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.views.static import serve
from django.conf import settings

admin.site.site_url = "/appname/"

urlpatterns = [
    path("appname/admin/", admin.site.urls),
    path("appname/session_security/", include("session_security.urls")),
    path("appname/", include("appname.urls")),
] + static(settings.MEDIA_URL, view=serve, document_root=settings.MEDIA_ROOT)
