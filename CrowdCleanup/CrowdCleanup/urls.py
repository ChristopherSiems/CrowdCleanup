# urls.py
from django.urls import path
from django.contrib import admin
<<<<<<< Updated upstream
from CrowdCleanupApp import views
=======
from django.conf import settings
from django.conf.urls.static import static
from CrowdCleanupApp import views

>>>>>>> Stashed changes

urlpatterns = [
    path('', views.home, name='home'),
    path('report_litter/', views.report_litter, name='report_litter'),
    path('clean_litter/', views.clean_litter, name='clean_litter'),
<<<<<<< Updated upstream
    path('pin_view/', views.pin_view, name = 'pin_view'),
    path("admin/", admin.site.urls),
]
=======
    path('pin_view/<int:pin_id>/', views.pin_view, name = 'pin_view'),
    path("admin/", admin.site.urls),
]
>>>>>>> Stashed changes
