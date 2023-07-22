from django.urls import path

from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('man/', ManClothing.as_view(), name='man_clothing'),
    path('shop/all/', ManClothingBase.as_view(), name='shop'),
    path('shop/<slug:post_slug>/', ManClothing.as_view(), name='shop_filter'),
    path('man/<slug:post_slug>/', ShowClothes.as_view(), name='show_clothes'),
    path('search/', search, name='search'),
    path('women/<slug:post_slug>/', ShowClothes.as_view(), name='show_clothes_women'),
    path('login/', LoginUser.as_view(), name='cart'),
    path('about/', about, name='about'),
    path('logout/', logout_user, name='logout'),
]