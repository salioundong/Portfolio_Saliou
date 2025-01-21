from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("projectA", views.projectA, name="projectA")
]