from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projectA", views.projectA, name="projectA"),
    path("projectB", views.projectB, name="projectB"),
    path("projectC", views.projectC, name="projectC")
]