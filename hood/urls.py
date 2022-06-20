
from . import views
from django.urls import path


urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit-profile'),
    path('new-hood/', views.new_hood, name='new-hood'),
    path('view-hood/<hood_id>', views.view_hood, name='view-hood'),
    path('view-hood/<hood_id>/new-business', views.add_business, name='add-business'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('search/', views.search_business, name='search'),
    path('<hood_id>/members', views.hood_members, name= 'hood_members'),
    path('<hood_id>/add-post', views.new_post, name='post'),
]
