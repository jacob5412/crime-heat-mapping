from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def map_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request)
    return HttpResponse("<h1>Hello World</h1>")