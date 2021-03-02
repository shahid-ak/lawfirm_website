from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('home',views.home, name='home'),
    path('register',views.register, name='register'),
    path('addnew',views.addnew, name='addnew'),
    path('addfield',views.addfield, name='addfield'),
    path('viewLawyer/<int:id>',views.viewLawyer, name='viewLayer'),
    path('deleteLawyer/<int:id>',views.deleteLawyer, name='deleteLayer'),
    path('allusers',views.allusers, name='allusers'),
    path('profile',views.profile, name='profile'),
]