from django.urls import path
from . import views

urlpatterns = [

    #general path
    path('', views.home, name="home"),
    path('viewhistory/',views.viewhistory, name='viewhistory'),
    path('login/',views.login, name='login'),
    path('changepassword/',views.changepassword, name='changepassword'),
    path('logout/',views.logout, name='logout'),

    #admin path
    path('manageaccess/',views.manageaccess, name='manageaccess'),   
    path('searchuser/',views.searchuser, name='searchuser'),
    path('manageuser/<str:searchid>/', views.manageuser, name='manageuser'),
    path('register/',views.register, name='register'),

    #user path
    path('userportal/', views.userportal, name='userportal'),


]
