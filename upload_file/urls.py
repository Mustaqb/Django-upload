from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core import views
from django.views.static import serve


urlpatterns = [
    path('', views.upload, name='home'),
    path('api/upload/', views.upload_api, name='upload_api'),
    path('api/', views.home, name='home_api'),

    path('admin/', admin.site.urls),

    # url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
