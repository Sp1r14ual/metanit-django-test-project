from django.urls import path, re_path, include
from hello import views

urlpatterns = [
    path("", views.index),
    path("about/", views.about),
    path("contact/", views.contact),
    path("details/", views.details)
]
