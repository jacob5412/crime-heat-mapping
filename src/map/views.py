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

    # getting a set of unique statecodes
    statelist = set([state['statecode'] for state in states])

    print(statelist)

    # iterating through state codes
    for statecode in statelist:
        aggregate = {}
        aggregate['statecode'] = statecode

        # aggregating total severity for each statecode
        total = News.objects.filter(statecode=statecode).aggregate(Sum('severity'))
        aggregate['severity'] = total['severity__sum']

        # retreiving state name for statecode
        state = News.objects.filter(
            statecode=statecode).values('state')[0]['state']
        
        aggregate['state'] = state

        # appending result to crime list
        crime.append(aggregate)

    print(crime)
    crime_data = {
        "crimes": crime,
    }
    return render(request, "india.html", crime_data)
