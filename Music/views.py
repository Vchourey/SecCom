from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
from .models import Album


def index(request):
    todays_dt = datetime.today()
    days_Week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    all_albums = Album.objects.all()
    for album in all_albums:
        url = 'music/' + str(album.id) + '/'

    return render(request, 'Music_html/First.html', {"today": todays_dt, "days_week": days_Week, "all_albums": all_albums})


def musicnum(request, musicid):

    try:
        album = Album.objects.get(pk=musicid)
    except:
        return redirect(index)

    return render(request, 'Music_html/Details_music.html', {"album": album})


def musiclist(request, year, month):
    text = "selected music list of month : %s/%s" % (year, month)
    return HttpResponse(text)
