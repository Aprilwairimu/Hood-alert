from django.shortcuts import render
from django.http  import HttpResponse,Http404
from .forms import RegisterForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def landing(request):

    return render(request, 'landing.html')
    
def home(request):

    return render(request, 'home.html')

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("login")
    else:
        form = RegisterForm()
    return render(request,'register/register.html', {"form":form})

def login_user(request):
    form=LoginForm()
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                return redirect('home')
            else:
                return HttpResponse('Such a user does not exist')
        else:
            return HttpResponse("Form is not Valid")
    return render(request,'register/login.html',{'form':form})

def logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    profile=Profile.objects.all()
    return render(request, 'profile.html',{'profile': profile})