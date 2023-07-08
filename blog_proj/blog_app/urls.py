from django.urls import path
from .import views
app_name='blog_app'
urlpatterns=[
    path('',views.index,name='index'),
    path('createaccount',views.createaccount,name='createaccount'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('createpost',views.createpost,name='createpost'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout'),
    path('profiles',views.profiles,name='profiles'),
    path('myprofile',views.myprofile,name='myprofile')
]