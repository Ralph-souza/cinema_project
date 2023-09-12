from django.urls import path

from apps.admin_app import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
