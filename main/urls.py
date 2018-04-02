
from django.urls import include,path
from . import views

urlpatterns = [
    path('', views.index),
    path(r'calendar/', views.calendar),
    path(r'assistants/', views.assistants),
    path(r'reports/', views.reports),
]