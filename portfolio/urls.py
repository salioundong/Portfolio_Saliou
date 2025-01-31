from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("soccer_2023", views.soccer2023, name="soccer_2023"),
    path("roboGenius", views.roboGenius, name="roboGenius"),
    path("projectC", views.projectC, name="projectC")
]