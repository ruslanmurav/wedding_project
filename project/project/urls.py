from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from wedding.views import MainView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view(), name='main'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

