# from django.http import HttpResponse, HttpResponseRedirect
# from django.views.generic import TemplateView
from django.shortcuts import render #, get_object_or_404
from django.conf import settings
from django.shortcuts import redirect

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def error_404_view(request, exception):
    
    # we add the path to the the 404.html file
    # here. The name of our HTML file is 404.html
    return render(request, '404.html')
