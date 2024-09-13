from django.shortcuts import render

# Create your views here.
# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def homes(request):
    current_url = request.path
    template = loader.get_template('main/homes.html')
    return HttpResponse(template.render({'current_url': current_url}))

def abouts(request):
    current_url = request.path
    template = loader.get_template('main/about.html')
    return HttpResponse(template.render({'current_url': current_url}))