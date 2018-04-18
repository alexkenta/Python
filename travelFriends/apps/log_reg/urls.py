from django.conf.urls import url
from . import views


urlpatterns = [
    url('^$', views.index),
    url('^process_registration$', views.process_registration),
    url('^process_login$', views.process_login),
    url('^logout$', views.logout)
]