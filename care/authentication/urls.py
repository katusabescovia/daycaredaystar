from . import views
from django.urls import path

urlpatterns = [
    path('student_register/' , views.student_register, name='student_register'),
    path('student_login/' , views.student_login, name='student_login'),
    path('student_forgot/' , views.student_forgot, name='student_forgot'),
    
]
