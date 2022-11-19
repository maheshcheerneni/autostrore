from django.contrib import admin
from django.urls import path
from BikeStore import views

urlpatterns = [
    path('bike/<int:pk>', views.bike_detailed.as_view()),
    path('bike/', views.bike_list.as_view()),

]
