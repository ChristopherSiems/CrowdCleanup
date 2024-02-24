# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # Define URLs for reporting litter and cleaning litter views
    path('report_litter/', views.report_litter, name='report_litter'),
    path('clean_litter/', views.clean_litter, name='clean_litter'),
    path('pin_view/', views.pin_view, name = 'pin_view')
]
