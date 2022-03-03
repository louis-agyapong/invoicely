from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include("djoser.urls")),
    path("api/v1/", include("djoser.urls.authtoken")),
    path("api/v1/", include("client.urls")),
]


if settings.DEBUG:
    import debug_toolbar

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += (path("__debug__/", include(debug_toolbar.urls)),)
