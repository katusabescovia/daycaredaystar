from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def about(request):
    # return HttpResponse("hello world  this is my  login method")
     template = loader.get_template('about.html')
     return HttpResponse(template.render())
    