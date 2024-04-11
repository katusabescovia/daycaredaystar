from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def blog(request):
    template = loader.get_template('blog.html')
    return HttpResponse(template.render())
    # return HttpResponse("hello world , this is the refactory class for 2024")
