from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('select', views.select, name='select'),
    path('view', views.view, name='view'),
    path('delete', views.delete, name='delete'),
]