from django.urls import path
from . import views

urlpatterns=[
    path('',views.home),
    path('home/',views.home),
    path('contactus/',views.contactus),
    path('myblogs/',views.myblogs),
    path('createblogs/',views.createblogs),
    path('latestblogs/',views.latestblogs),
    path('signup/',views.signup),
    path('signin/',views.signin),
    path('about/',views.about),
    path('logout/',views.logout),

]