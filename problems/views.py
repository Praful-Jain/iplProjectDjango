import json
from django.shortcuts import render
from django.db.models import *
from django.db.models.functions import Round
from django.http import JsonResponse

from .models import Matches, Deliveries

# Number of matches played per year for all the years in IPL.
def matches_played(request):
    # 'obj' is queryset
    result = Matches.objects.values('season').annotate(
        matches_count=Count('season')
    )
    return JsonResponse(list(result),safe=False)
    # return render(request,'matches-count.html',{'result':result})


# Number of matches won per team per year in IPL.
def matches_won(request):
    result = Matches.objects.values('season','winner').annotate(
        matches_won = Count('winner')
    )  
    return JsonResponse(list(result),safe=False)
    # return render(request,'matches-won.html',{'result':result})



# Extra runs conceded per team in the year 2016
def extra_runs(request, year):
    
    # filter rows from 'Matches' table having 'season' column equals 2016(ie..year) and take only 'id' of those rows in our queryset ids
    ids = Matches.objects.filter( season = year ).values('id')
    
    # filter rows from 'Deliveries' table whose 'match_id' column-value is present in 'id' of ids
    deliveries = Deliveries.objects.filter( match_id__in = ids ).values( 'bowling_team','extra_runs' )
    
    # extra-runs conceded each team
    result = deliveries.values('bowling_team').annotate( extra_run = Sum('extra_runs') )
    return JsonResponse(list(result),safe=False)
    # return render(request,'extra-runs.html',{'result':result})

    

# Top 10 economical bowlers in the year 2015
def economical_bowlers(request, year, count):
    # filter rows from 'Matches' table having 'season' column equals 2015(ie..year) and take only 'id' of those rows in our queryset ids
    ids = Matches.objects.filter( season = year ).values('id')
    
    # filter rows from 'Deliveries' table whose 'match_id' column-value is present in 'id' of obj1
    deliveries = Deliveries.objects.filter( match_id__in = ids ).values( 'bowler', 'wide_runs', 'bye_runs', 'legbye_runs', 'noball_runs', 'total_runs')
 
    temp = deliveries.values('bowler').annotate(
        # F is a class used to represent a database column in a query. 
        runs = Sum(F('total_runs') - F('bye_runs') - F('legbye_runs')),
        balls = Count('bowler', exclude=['noball_runs', 'wide_runs'])
    ).values('bowler','runs','balls')
    
    result = temp.annotate(
        economy = Round( F('runs')*6.0 / F('balls') , 2) 
    ).values('bowler', 'economy').order_by('economy')[:count]
   
    return JsonResponse(list(result),safe=False)
    # return render(request,'economical-bowlers.html',{'result':result})


def home(request):
    return render(request, 'base.html')
 
    
# CHARTS
def matches_played_chart(request):
    response = matches_played('matches-count/')
    chart_data = json.loads(response.content)
    return render(request, 'matches-count-chart.html', {'chart_data': json.dumps(chart_data)})

def matches_won_chart(request):
    response = matches_won('matches-won/')
    chart_data = json.loads(response.content)
    return render(request, 'matches-won-chart.html', {'chart_data': json.dumps(chart_data)})

def extra_runs_chart(request, year):
    response = extra_runs('extra-runs/2016/', year)
    chart_data = json.loads(response.content)
    return render(request, 'extra-runs-chart.html', {'chart_data': json.dumps(chart_data), 'year':year})

def economical_bowlers_chart(request, year, count):
    response = economical_bowlers('economical-bowlers/2015/10/', year, count)
    chart_data = json.loads(response.content)
    return render(request, 'economical-bowlers-chart.html', {'chart_data': json.dumps(chart_data), 'year':year, 'count':count})

