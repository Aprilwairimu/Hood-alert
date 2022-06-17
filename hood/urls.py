from django.urls import path
from . import views 
from django.conf.urls.static import static


urlpatterns =[
    path('',views.home, name='home'),
    path('register',views.register, name='register',),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout,name='logout'),
]