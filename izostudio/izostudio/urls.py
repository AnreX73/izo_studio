from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from izo.views import *
from izostudio import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('izo.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)