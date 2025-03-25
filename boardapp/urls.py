
from django.contrib import admin
from django.urls import path
from .views import signupfunc
from .views import Loginfunc
from .views import Listfunc 



urlpatterns = [
    path('signup/', signupfunc,name = 'signup'),
    path('login/',Loginfunc, name = 'login'),
    path('list/',Listfunc, name = 'list')

    
]