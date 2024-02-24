# urls.py
from django.urls import path
from django.contrib import admin
from CrowdCleanupApp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('report_litter/', views.report_litter, name='report_litter'),
    path('clean_litter/', views.clean_litter, name='clean_litter'),
    path('pin_view/', views.pin_view, name = 'pin_view'),
    path("admin/", admin.site.urls),
]
