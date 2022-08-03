from django.urls import path
from movie import views

urlpatterns = [
    path('', views.movie_list, name='movie-list'),
    path('create/', views.movie_create, name='movie-create'),
    path('<int:pk>/', views.movie_detail, name='movie-detail'),
]