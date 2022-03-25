from django.urls import include, path
from HospítalGeneral import views
from django.contrib import admin


urlpatterns = [
    path('index', views.index)
]
