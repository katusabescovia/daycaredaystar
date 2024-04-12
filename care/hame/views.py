from django.shortcuts import render
from django.http import HttpResponse
from  django.template import loader
# Create your views here.
def index(request):
    x=5
    y=34
    xy=x+y

    template = loader.get_template('home.html')
    return HttpResponse(template.render({"name":'scovia',"total":xy ,"age":20}))
    # return HttpResponse("hello world , this is the refactory class for 2024")
 