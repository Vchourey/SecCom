from django.shortcuts import render, redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
from .models import Movies


def index(request):
    todays_dt = datetime.today()
    days_Week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    all_movie = Movies.objects.all()
    return render(request, 'Movies_html/First.html', {"today": todays_dt, "days_week": days_Week, "all_movie": all_movie})



def movienum(request, movieid):
    try:
        selectd_movi = Movies.objects.get(pk=movieid)
    except:
        return redirect(index)

    return render(request, 'Movies_html/Details_movie.html', {"selectd_movi": selectd_movi})


def movielist(request, year, month):
    text = "selected movies list if of month  : %s/%s" % (year, month)
    return HttpResponse(text)

def uploadmovie(request):

    movie = Movies(movie_title="", movie_category="", duration="", release_year="", actor="", director="")
    movie.save()
