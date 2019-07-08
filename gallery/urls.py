from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',  views.home,name='gallery-home'),
    path('upload/', views.upload, name='gallery-upload'),
    path('success', views.success, name = 'success')

]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
