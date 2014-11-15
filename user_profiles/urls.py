from django.conf.urls import patterns, url
from user_profiles import views

urlpatterns = [
    url(r'^users/([0-9]+)/$', views.user_detail),
]