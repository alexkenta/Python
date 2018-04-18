from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.travels_index),
    url('^add_travel_plan$', views.add_travel_plan),
    url('^process_trip', views.process_trip),
    url('^(?P<id>\d+)$', views.view_trip),
    url('^join/(?P<id>\d+)$', views.join_trip)
]