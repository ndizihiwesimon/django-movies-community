from django.urls import path
from member import views

urlpatterns = [
    path('', views.login, name='login'),
    path('register', views.Register, name='register')
]