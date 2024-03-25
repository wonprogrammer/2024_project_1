from django.urls import path
from articles import views

urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>/', views.dinner),
    path('dinner_price/<str:name>/', views.dinner_price),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
]