from django.shortcuts import render
from django.http import HttpResponse
from .models import Alumni_Video,Apptitude_Video,Interview_Corner
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='signin')
def videos(request):
    return render(request,'videos/videos.html')

@login_required(login_url='signin')
def AlumniTalk(request):
    allvideos = Alumni_Video.objects.all().order_by('-added')
    paginator = Paginator(allvideos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request,'videos/alumni.html',context)

@login_required(login_url='signin')
def Apptitude(request):
    apptitude = Apptitude_Video.objects.all().order_by('-added')
    paginator = Paginator(apptitude,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'videos/apptitude.html',context)

@login_required(login_url='signin')
def InterviewCorner(request):
    interview = Interview_Corner.objects.all().order_by('-added')
    paginator = Paginator(interview,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj}
    return render(request, 'videos/interview.html',context)

def AlumniTalksearch(request):
    query = request.GET['query']
    allvideos = Alumni_Video.objects.all().filter(title__icontains=query).order_by('-added')
    paginator = Paginator(allvideos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'videos/search.html',context)

def InterviewCornersearch(request):
    query = request.GET['query']
    allvideos = Interview_Corner.objects.all().filter(title__icontains=query).order_by('-added')
    paginator = Paginator(allvideos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'videos/search.html',context)

def Apptitudesearch(request):
    query = request.GET['query']
    allvideos = Apptitude_Video.objects.all().filter(title__icontains=query).order_by('-added')
    paginator = Paginator(allvideos,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'videos/search.html',context)

