
from django.urls import path
from .views import *

app_name = 'shop'

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('shop-details-1/', shop_details_1, name='shop-details-1'),
    path('shop-details-2/', shop_details_2, name='shop-details-2'),
    path('shop-details-3/', shop_details_3, name='shop-details-3'),
    path('shop-details-4/', shop_details_4, name='shop-details-4'),



]