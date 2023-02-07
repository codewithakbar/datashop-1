from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('cart/', views.cartpage) ,
    path('detail/', views.productdtl)
]