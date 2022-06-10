from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def home(request):
    return render(request,'home/home.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        pass1 = request.POST['pass1']

        user = auth.authenticate(username=email, email=email,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect('courses')
        else:
            messages.info(request,' Credentials invalid')
            return redirect('signin')
    else:
        return render(request,'registration/signin.html')


def signup(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if len(fname)<2:
            messages.info(request,"Enter valid first name")
            return redirect('signup')
        elif len(lname)<3:
            messages.info(request,"Enter valid last name")
            return redirect('signup')
        elif len(email)<11:
            messages.info(request,"Enter valid email")
            return redirect('signup')
        if len(pass1)<8 or len(pass1)>=20:
            messages.info(request,"Password length should be 8 or maximum")
            return redirect('signup')
        if pass1 == pass2:
            if User.objects.filter(email=email).exists(): 
                messages.info(request, 'Email already exits')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=email, email=email, password=pass1, first_name=fname, last_name=lname)
                user.save();
                return redirect('signin')
        else:
            messages.info(request, 'Password not matches')
            return redirect('signup')
    return render(request,'registration/signup.html')