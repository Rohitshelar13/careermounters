from django.urls import path,include
from videos import views
urlpatterns = [
    path('',views.videos,name='videos'),
    path('AlumniTalk',views.AlumniTalk,name='AlumniTalk'),
    path('AlumniTalksearch',views.AlumniTalksearch,name='AlumniTalksearch'),
    path('InterviewCorner',views.InterviewCorner,name='InterviewCorner'),
    path('InterviewCornersearch',views.InterviewCornersearch,name='InterviewCornersearch'),
    path('Apptitude',views.Apptitude,name='Apptitude'),
    path('Apptitudesearch',views.Apptitudesearch,name='Apptitudesearch'),


]