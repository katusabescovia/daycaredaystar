from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def student_login(request):
    template = loader.get_template('student_login.html')
    return HttpResponse(template.render())

def student_register(request):
    template = loader.get_template('student_register.html')
    return HttpResponse(template.render())
def student_forgot(request):
    template = loader.get_template('student_forgot.html')
    return HttpResponse(template.render())
