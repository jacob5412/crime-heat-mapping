from django.shortcuts import render
from django.http import HttpResponse
from .models import News

# Create your views here.
def map_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    
    #return HttpResponse("<h1>Hello World</h1>") # string of html

    crime = News.objects.all()
    crime_data = {
        "crime_id": crime
    }
    return render(request, "india.html", crime_data)