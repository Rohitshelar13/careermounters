from django.contrib import admin
from django.urls import path, include
from courses import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('logout',views.logout,name='logout'),
    path('CS_IT',views.CS_IT,name='CS_IT'),
    path('ENTC',views.ENTC,name='ENTC'),
    path('Electrical',views.Electrical,name='Electrical'),
    path('Mechanical',views.Mechanical,name='Mechanical'),
    path('Civil',views.Civil,name='Civil'),
    path('Trending',views.Trending,name='Trending'),
    path('CSsearch',views.CSsearch,name='CSsearch'),
    path('Mechsearch',views.Mechsearch,name='Mechsearch'),
    path('ENTCsearch',views.ENTCsearch,name='ENTCsearch'),
    path('Electricalsearch',views.Electricalsearch,name='Electricalsearch'),
    path('Civilsearch',views.Civilsearch,name='Civilsearch'),
    path('Trendingsearch',views.Trendingsearch,name='Trendingsearch'),
]