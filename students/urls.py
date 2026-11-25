from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('register/', views.register_student, name='register_student'),
    path('student/<int:id>/', views.student_detail, name='student_detail'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
]

   