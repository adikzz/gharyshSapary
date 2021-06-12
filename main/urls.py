from django.urls import path
from . import views

app_name = "main"
urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.userCreate.as_view(), name='create'),
    path('update/<int:pk>/', views.userUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', views.userDelete, name='delete'),
]
