"""fbvSerializers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from fbvApp import views as studentViews
from passApp import views as passViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', studentViews.student_list),
    path('students/<int:pk>', studentViews.student_detail),
    path('passengers/', passViews.passenger_list),
    path('passengers/<int:pk>', passViews.passenger_detail),
]
