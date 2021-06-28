from django.urls import path ,include
from . import views


urlpatterns = [

    path('',views.blogHome,name='blogHome'),
    path('postComment',views.postComment,name="postComment"),
    path('<str:slug>/',views.blogPost, name='blogPost'),
    path('search',views.search,name='search'),
    path('signup',views.handlesignup,name='handlesignup'),
    path('login',views.handlelogin,name='login'),
    path('logout',views.handlelogout,name='logout'),

]