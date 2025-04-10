from django.urls import path
from . import views

urlpatterns = [
    path('', views.emp_list, name='emp_list'),
    path('create/', views.emp_create, name='emp_create'),
    path('update/<int:pk>/', views.emp_update, name='emp_update'),
    path('delete/<int:pk>/', views.emp_delete, name='emp_delete'),
]
