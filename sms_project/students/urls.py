from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_student, name='add'),
    path('delete/<str:roll>/', views.delete_student, name='delete'),
    path('update/<str:roll>/', views.update_student, name='update'),
]