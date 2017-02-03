from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^$', views.MainView.as_view(), name="main"),
    url(r'^download/', views.download_data, name="download"),
]
