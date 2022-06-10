from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from .models import userInfo
from django.contrib.auth.models import User
# Create your views here.
from django.contrib.auth.decorators import login_required
@login_required(login_url='signin')
def UserProfile(request):
    if request.user.is_authenticated:
        email1 = request.user.email
        print(email1)
    if userInfo.objects.filter(email=email1).exists():
        info = userInfo.objects.get(email=email1)
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            prnNo = request.POST['prnNo']
            departmentName = request.POST['departmentName']
            year = request.POST['year']
            cgpa = request.POST['cgpa']
            phno = request.POST['phno']
            bdate = request.POST['bdate']
            contact = userInfo.objects.update(first_name=first_name,last_name=last_name,email=email,prnNo = prnNo,departmentName=departmentName,year=year,cgpa=cgpa,phno=phno,bdate=bdate)
            messages.info(request, 'Contact request submittedddddd successfully.')
            info = userInfo.objects.get(email=email)
            return render(request,'UserProfile/profiles.html',{'info':info})
        return render(request,'UserProfile/profiles.html',{'info':info})
    else:
        if request.method == 'POST':
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            prnNo = request.POST['prnNo']
            departmentName = request.POST['departmentName']
            year = request.POST['year']
            cgpa = request.POST['cgpa']
            phno = request.POST['phno']
            bdate = request.POST['bdate']
            if userInfo.objects.filter(email=email).exists():
                contact = userInfo.objects.update(first_name=first_name,last_name=last_name,email=email,prnNo = prnNo,departmentName=departmentName,year=year,cgpa=cgpa,phno=phno,bdate=bdate)
                messages.info(request, 'Contact request submitted successfully.')
                info = userInfo.objects.get(email=email)
                return render(request,'UserProfile/profiles.html',{'info':info})
            else:
                contact = userInfo.objects.create(first_name=first_name,last_name=last_name,email=email,prnNo = prnNo,departmentName=departmentName,year=year,cgpa=cgpa,phno=phno,bdate=bdate)
                messages.info(request, 'Contact request submitted successfully.')
                info = userInfo.objects.get(email=email)
                return render(request,'UserProfile/profiles.html',{'info':info})
        return render(request,'UserProfile/profile.html')
        