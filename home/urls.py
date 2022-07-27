import imp
from django.urls import path
from .views import *
urlpatterns = [
    path('', login_view,name="login"),
    path('home', home,name="home"),
    path('logout', logout_view,name="logout"),
    path('signup', signup_view,name="signup"),
]
