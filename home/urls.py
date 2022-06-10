from django.contrib import admin
from django.urls import path, include
from home import views
from django.contrib.auth import views as auth_views
from videos import views as v
from courses import views as c
from opportunities import views as o
from UserProfile import views as p

urlpatterns = [
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_from.html'), name='password_reset'),
    path('password_reset_done', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('password_reset_confirm/<slug:uidb64>/<slug:token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='registration/password_reset_complete.html'
         ),
         name='password_reset_complete'),
    path('videos',v.videos,name='videos'),
    path('courses',c.courses,name='courses'),
    path('opportunities',o.opportunities,name='opportunities'),
    path('UserProfile',p.UserProfile,name='UserProfile'),
]
