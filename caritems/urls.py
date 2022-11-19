from django.contrib import admin
from django.urls import path
from .views import Carlist_view,Detail_view

urlpatterns = [
    path('cart-items/', Carlist_view.as_view()),
    path('cart-items/<int:sino>/', Detail_view.as_view())

]
