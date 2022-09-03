from django import views
from django.urls import path
from . import views
urlpatterns = [
    path('assets/',views.getasset,name="assets"),
    path('assetGL<str:assetid>/',views.showasset,name="assetshow"),
    path('asset/deleteasset<str:assetid>/',views.deleteasset,name="delete"),
    path('',views.dashboard,name="dashboard"),
    path('employee/',views.addemployee,name="employees"),
    path('delete/employee<str:pk>',views.deleteEmployee,name='employeedelete'),
    path('register/',views.register,name="register"),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutUser,name="logout"),
]  