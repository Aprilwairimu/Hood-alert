from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('',views.home, name='home'),
    path('register',views.register, name='register',),
    path('login',views.login_user,name='login'),
    path('logout',views.logout,name='logout'),
    # path('create_profile/<user_id>', views.create_profile, name="create_profile"),
    # path('profile/<str:pk>', views.profile, name="profile"),
    # path('join_hood', views.join_hood, name='join-hood'),
    # path('leave_hood', views.leave_hood, name='leave-hood'),
    path('post', views.create_post, name='post'),
    path('single_hood', views.single_hood, name='single-hood'),
    path('search/', views.search_business, name='search'),


]