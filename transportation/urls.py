from django.urls import path
from . import views 

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("services/", views.services, name="services"),
    path("pricing/", views.pricing, name="pricing"),
    path("contact/", views.contact, name="contact"),
    path("service-details/", views.service_details, name="service_details"),
    path("get-a-quote/", views.get_a_quote, name="get_a_quote"),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile_view, name='profile'),
    path('create-order/', views.create_order, name='create_order'),
    path('order_list/', views.order_list, name='order_list'),
    path('order_detail/<int:order_id>/', views.order_detail, name='order_detail'),
]
