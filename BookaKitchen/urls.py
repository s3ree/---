"""
URL configuration for BookaKitchen project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from bookings import views

urlpatterns = [
    path('',views.home, name='home'),
    path('personal_info', views.personal_info, name='personal_info'),
    path('book_kitchen', views.book_kitchen, name='book_kitchen'),
    path('admin/', admin.site.urls),
    path('success', views.success_page, name='success'),
    path('my_bookings/', views.user_bookings, name='user_bookings')
]
