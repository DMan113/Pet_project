"""
URL configuration for project_name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from transportation import views


urlpatterns = [
    path("", views.home, name="home"),
    path("transportation/", include("transportation.urls")),
    path("admin/", admin.site.urls),
    path("test/", views.test, name="test"),
    path("test2/", views.test2, name="test2"),
    path("test3/", views.test3, name="test3"),
]

