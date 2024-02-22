from django.contrib import admin
from django.urls import path , include
from django.urls import path

from .views import CreateStripeCheckoutSessionView

from . import views
from django.urls import path
from .views import product_detail


urlpatterns = [
    
    path("",views.index,name="index"),
    path("login",views.login1,name="login"),
    path("register",views.register,name="register"),
    path("home2",views.home2,name="home-2"),
    path("home3",views.home3,name="home-3"),
    path("contact",views.contact,name="contact"),
    path("cart",views.cart,name='cart'),
    path("logout",views.logout1,name='logout'),


    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
        views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
        views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),


    path("checkout",views.checkout,name='checkout'),
    path("placeorder",views.placeorder,name='placeorder'),

    path("create-checkout-session",
        CreateStripeCheckoutSessionView.as_view(),
        name="create-checkout-session"),

    path('seccess',views.sccessfull,name='seccess'),


    path('products/<slug:slug>/', product_detail, name='product_detail'),
    path("wishlist",views.wishlist,name='wishlist')
]
