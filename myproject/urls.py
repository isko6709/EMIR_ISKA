from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('en-us/', include('django.conf.urls.i18n')),
]
