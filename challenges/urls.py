from django.urls import path
from . import views

urlpatterns =[
    path("january", views.index),
    path("example",views.example)
]