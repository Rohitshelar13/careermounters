from django.urls import path,include
from UserProfile import views
urlpatterns = [
    path('',views.UserProfile,name='UserProfile'),
]