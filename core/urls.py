from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tours/', include('apps.tours.urls')),
    path('articles/', include('apps.articles.urls')),
    path('users/',include('apps.users.urls')),
    path('', RedirectView.as_view(url='/articles/', permanent=False))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)