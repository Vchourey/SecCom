from django.shortcuts import render,redirect
from django.http import Http404
from django.http import HttpResponse
from datetime import datetime
from .models import Books


def index(request):
    todays_dt = datetime.today()
    days_Week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    all_books = Books.objects.all()
    return render(request, 'book_html/First_book.html', {"today": todays_dt, "days_week": days_Week, "all_books": all_books})


def booknum(request, bookid):
    try:
        bookdetail = Books.objects.get(pk=bookid)
    except:
        return redirect(index)

    return render(request, 'book_html/Details_book.html', {"bookdetail": bookdetail})


def booklist(request, year, month):
    text = "selected book list of the month : %s/%s" % (year, month)
    return HttpResponse(text)
