from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("service-details/", views.services_details, name="services_details"),
    path("get-a-quote/", views.get_a_quote, name="get_a_quote"),
    path('register/', views.register, name='register'),
]
