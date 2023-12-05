from django.urls import path
from . import views

urlpatterns = [
   path("hello", views.index),
   path("liron",views.liron),
   path("dandon",views.daniela),
   path("matan",views.matan),
   path("daniel",views.daniel),
   path("oriya",views.oriya)
]