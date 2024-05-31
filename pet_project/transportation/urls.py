from django.urls import path
from . import views
urlpatterns = [
#path("", views.transportation, name="transportation"),
path("about/", views.about, name="about"),
path("services/", views.services, name="services"),
path("pricing/", views.pricing, name="pricing"),
path("contact/", views.contact, name="contact"),
]
