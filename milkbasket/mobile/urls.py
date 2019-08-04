from django.urls import path

from . import views

urlpatterns = [
    path('product/', views.ProductList.as_view()),
    path('product/<int:pk>/', views.ProductDetail.as_view()),
    path('product/create/', views.ProductCreate.as_view()),
    path('product/<int:pk>/update', views.ProductUpdate.as_view()),
    path('product/<int:pk>/delete', views.ProductDelete.as_view()),

    path('customer/', views.CustomerList.as_view()),
    path('customer/<int:pk>/', views.CustomerDetail.as_view()),
    path('customer/create/', views.CustomerCreate.as_view()),
    path('customer/<int:pk>/update', views.CustomerUpdate.as_view()),
    path('customer/<int:pk>/delete', views.CustomerDelete.as_view()),

    path('order/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),
    path('order/create/', views.OrderCreate.as_view()),
    path('order/<int:pk>/update', views.OrderUpdate.as_view()),
    path('order/<int:pk>/delete', views.OrderDelete.as_view()),

    path('bpm/<int:pk>/', views.BPMDetail.as_view()),
]