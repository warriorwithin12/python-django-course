from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def help(request):
    template_data = {"some_help": "This is a helpfully text from views.py from appTwo!"}
    return render(request, 'appTwo/help.html', context=template_data)

def page1(request):
    return render(request, 'appTwo/page1.html')

def page2(request):
    return render(request, 'appTwo/page2.html')
