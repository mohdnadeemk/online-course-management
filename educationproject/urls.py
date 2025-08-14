from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

media_url = settings.MEDIA_URL

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('home/',views.home),
    path ('login/',views.login),
    path('register/',views.register),
    path('adminhome/',include('adminapp.urls')),
    path('studenthome/',include('studentapp.urls')),
    path('batchlist3/',views.batchlist3),
    path('courselist3/',views.courselist3),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
