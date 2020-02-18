from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import CalibrationServices


def cali_serv(request):

    try:
        selected_cali = CalibrationServices.objects.all()
        unique_cali_type = CalibrationServices.objects.filter().values("cali_type").distinct()

    except:
        return HttpResponse("error while reading database")

    return render(request, 'calibration_html/calipage1.html', {"selected_all_cali": selected_cali,
                                                               "unique_cali_type": unique_cali_type})


def instr_serv(request):

    return render(request, 'calibration_html/instrupage1.html', {})


def auto_serv(request):

    return render(request, 'calibration_html/automation1.html', {})


def pneum_serv(request):

    return render(request, 'calibration_html/pneumaticpage.html', {})


def ac_serv(request):

    return render(request, 'calibration_html/acpage.html', {})