from django.urls import path
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns =[
    path('',views.landing, name='landing'),
    path('',views.home, name='home'),
    path('register',views.register, name='register',),
    path('login',views.login_user,name='login'),
    path('logout',views.logout,name='logout'),
    # path('create_profile/<user_id>', views.create_profile, name="create_profile"),
    # path('profile/<str:pk>', views.profile, name="profile"),


]