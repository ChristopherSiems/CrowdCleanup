# urls.py
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from CrowdCleanupApp import views


urlpatterns = [
    path('', views.home, name='home'),
    path('report_litter/', views.report_litter, name='report_litter'),
    path('clean_litter/', views.clean_litter, name='clean_litter'),
    path('pin_view/<int:pin_id>/', views.pin_view, name = 'pin_view'),
    path("admin/", admin.site.urls),
    path('after_submit/', views.after_submit, name='after_submit'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)