from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum
from .models import News
import itertools

# Create your views here.
def map_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    
    #return HttpResponse("<h1>Hello World</h1>") # string of html

    crime = []

    states = News.objects.values('statecode')
    statelist = set([state['statecode'] for state in states])

    print(statelist)
    for statecode in statelist:
        aggregate = {}
        aggregate['statecode'] = statecode
        total = News.objects.filter(statecode=statecode).aggregate(Sum('severity'))
        aggregate['severity'] = total['severity__sum']

        state = News.objects.filter(
            statecode=statecode).values('state')[0]['state']
        
        aggregate['state'] = state
        crime.append(aggregate)

    print(crime)
    crime_data = {
        "crimes": crime,
    }
    return render(request, "india.html", crime_data)
