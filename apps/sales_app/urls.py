from django.urls import path

from apps.sales_app import views


urlpatterns = [
    path('', views.post_list, name='post_list'),
]
