from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.admin_app.urls')),
    path('', include('apps.sales_app.urls')),
]
