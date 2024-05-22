from django.urls import path
from articles import views

app_name = 'articles'
urlpatterns = [
    path('index/', views.index),
    path('dinner/<str:name>/', views.dinner),
    path('dinner_price/', views.dinner_price, name='dinner_price'),
    path('review/', views.review, name='review'),
    path('create_review/', views.create_review, name='create_review'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]