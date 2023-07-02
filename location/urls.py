from django.conf.urls import url
from django.urls import path, include
from location import views as location_view

urlpatterns = [
    path('', location_view.LocationView.as_view()),
]
