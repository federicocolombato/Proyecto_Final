from django.urls import include, path
from HospítalGeneral import views



urlpatterns = [
    path('index', views.index, name = 'Index'),
    path('paciente', views.paciente, name = 'Paciente'),
    path('doctor', views.doctor, name = 'Doctor')    
]
