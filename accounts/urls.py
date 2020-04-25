
from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signup/', customer_signup, name='signup'),
    path('login/', customer_login, name='login'),
    path('logout/', customer_logout, name='logout'),
   ]