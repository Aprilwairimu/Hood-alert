from django.shortcuts import render, redirect
from django.http.response import Http404
from django.contrib.auth.decorators import login_required
from .models import News, Hood, Business, Profile
from django.contrib.auth.models import User
from .forms import EditProfileForm, HoodForm, BusinessForm, NewsForm
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='login')
def index(request):
    hoods = Hood.objects.all()
    ctx = {
        "hoods" : hoods
    }
    return render(request, 'index.html', ctx)


def profile(request , username):
    user = User.objects.get(username=username)
    try:
        profile = Profile.objects.get(user=user.id)
        
    except ObjectDoesNotExist:
        raise Http404()
    businesses = Business.objects.filter(owner = profile)
    posts = News.objects.filter(user = profile)
    ctx = {
        "user": user,
        "profile" : profile,
        "businesses": businesses,
        "posts":posts
    }
    return render(request, 'profile.html', ctx)

def edit_profile(request, username):
    user = User.objects.get(username = username)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance = request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile', user.username)

    else: 
        form = EditProfileForm(instance = request.user.profile)
    return render(request, 'edit_profile.html', {'form': form})

def new_hood(request):
    if request.method == 'POST':
        form = HoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('index')
    else:
        form = HoodForm()
    return render(request, 'create_hood.html', {'form': form})
def view_hood(request, hood_id):
    hood = Hood.objects.get(id =hood_id)
    business = Business.objects.filter(hood = hood)
    news = News.objects.filter(hood = hood)
    news = news[::-1]
    ctx = {
        'hood': hood,
        'business': business,
        'news': news
    }
    return render(request, 'view_hood.html', ctx)
def add_business(request, hood_id):
    if request.method == 'POST':
        hood = Hood.objects.get(id =hood_id)
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            bs_form = form.save(commit=False)
            bs_form.hood = hood
            bs_form.owner = request.user.profile
            bs_form.create_business()
            return redirect('view-hood', hood.id)
    else:
        form = BusinessForm()

    return render(request, 'new_business.html', {"form" : form})
def join_hood(request, id):
    try:
        hood = Hood.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.location = hood
    request.user.profile.save()
    return redirect('index')

def leave_hood(request, id):
    try:
        hood = Hood.objects.get(id =id)
    except ObjectDoesNotExist:
        return Http404
    request.user.profile.location = None
    request.user.profile.save()
    return redirect('index')

def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")

        results = Business.objects.filter(bs_name__icontains=name).all()
        print(results)
        message = f'name'
        ctx = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', ctx)
    else:
        message = "You haven't searched for any image category"
    return render(request, "results.html")

def hood_members(request, hood_id):
    hood = Hood.objects.get(id =hood_id)
    residents = Profile.objects.filter(location = hood)
    ctx ={
        'residents':residents
    }
    return render(request, 'hood_residents.html', ctx)

def new_post(request, hood_id):
    hood = Hood.objects.get(id =hood_id)
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            news = form.save(commit=False)
            news.hood = hood
            news.user = request.user.profile
            news.save()
            return redirect('view-hood', hood.id)
    else:
        form = NewsForm()
    return render(request, 'news.html', {'form': form})
