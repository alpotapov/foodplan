from django.conf.urls import patterns, url
from menu_generator import views

urlpatterns = [
    url(r'^menu/generate/([0-9]+)$', views.generate),
    url(r'^menu/refresh/([0-9]+)/(mon|tue|wed|thu|fri|sat|sun)/(breakfast|lunch|dinner)$', views.refresh_meal),
]