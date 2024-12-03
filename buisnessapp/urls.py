from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('header/', views.header, name ='header'),

#--------- Register a user ---------#
    path('register/', views.register, name ="register"),

#--------- Log in a user ----------#
    path('my-login/', views.my_login, name ="my-login"),

#--------- Logout a user ----------#
    path('user-logout', views.user_logout, name ="user-logout"),

#---------- Dashboard ---------#
    path('dashboard/', views.dashboard, name ='dashboard'),


#---------- Events ----------#
    path('events/', views.events, name='events'),
    path ('view_events/', views.view_events, name ='view_event'),
    path ('update-event/<str:pk>', views.update_event, name='update_event'),
    path('delete-event/<str:pk>', views.delete_event, name = 'delete_event'),

#--------- Work_orders ---------#

    path ('work_orders/', views.work_orders, name = 'work_orders'),
]
