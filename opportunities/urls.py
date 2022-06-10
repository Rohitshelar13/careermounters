from django.contrib import admin
from django.urls import path,include
from opportunities import views
urlpatterns = [
    path('',views.opportunities,name='opportunities'),
]