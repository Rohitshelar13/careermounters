from urllib import request
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from courses.models import CS_IT_Course,Entc_Course,Electrical_Course,Civil_Course,Mechanical_Course,Trending_Course
from django.core.paginator import Paginator
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='signin')
def courses(request):
    return render(request,'courses/courses.html')

@login_required(login_url='signin')
def CS_IT(request):
    allcourses = CS_IT_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def ENTC(request):
    allcourses = Entc_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def Electrical(request):
    allcourses = Electrical_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def Mechanical(request):
    allcourses = Mechanical_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def Civil(request):
    allcourses = Civil_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def Trending(request):
    allcourses = Trending_Course.objects.all().order_by('-timeStamp')
    paginator = Paginator(allcourses,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    # myFilter = CS_IT_Filter(request.GET, queryset=allcourses)
    # page_obj = myFilter.qs
    context = {'page_obj':page_obj}
    return render(request,'courses/courseList.html',context)

@login_required(login_url='signin')
def CSsearch(request):
    query = request.GET['query']
    allcourses = CS_IT_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

@login_required(login_url='signin')
def Mechsearch(request):
    query = request.GET['query']
    allcourses = Mechanical_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

@login_required(login_url='signin')
def ENTCsearch(request):
    query = request.GET['query']
    allcourses = Entc_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

@login_required(login_url='signin')
def Electricalsearch(request):
    query = request.GET['query']
    allcourses = Electrical_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

@login_required(login_url='signin')
def Civilsearch(request):
    query = request.GET['query']
    allcourses = Civil_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

@login_required(login_url='signin')
def Trendingsearch(request):
    query = request.GET['query']
    allcourses = Trending_Course.objects.all().filter(courseName__icontains=query).order_by('-timeStamp')
    paginator = Paginator(allcourses,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj':page_obj,'query':query}
    return render(request,'courses/search.html',context)

def logout(request):
    auth.logout(request)
    return redirect('/')

