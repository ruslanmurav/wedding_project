from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page

from project.settings import BASE_DIR
from wedding.views import MainView, pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
    path('portfolio/', include('wedding.urls', namespace='portfolio')),   # localhost/porfolio/wedding/<int:pk>
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns.append(path("__debug__/", include("debug_toolbar.urls")))


handler404 = pageNotFound



