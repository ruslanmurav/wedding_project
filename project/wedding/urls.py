
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.decorators.cache import cache_page
from wedding.views import PortfolioView, WeddingView

app_name = 'wedding'

urlpatterns = [
    path('', PortfolioView.as_view(), name='portfolio'),
    path('page/<int:page>', PortfolioView.as_view(), name='paginator'),
    path('wedding/<int:pk>/', WeddingView.as_view(), name='wedding'),
]

#myanyo