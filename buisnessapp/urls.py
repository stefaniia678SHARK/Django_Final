from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('header/', views.header, name ='header'),
    path('events/', views.events, name='events'),
    path ('work_orders/', views.work_orders, name = 'work_orders'),
    path ('view_events/', views.view_events, name ='view_event'),
    path ('update-event/<str:pk>', views.update_event, name='update_event'),
    path('delete-event/<str:pk>', views.delete_event, name = 'delete_event'),
]
