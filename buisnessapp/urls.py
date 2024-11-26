from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('header/', views.header, name ='header'),
    path ('events/', views.events, name = 'events'),

    path ('work_orders/', views.work_orders, name = 'work_orders'),
]
