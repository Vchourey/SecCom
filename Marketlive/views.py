from django.shortcuts import render
from django.views.generic import ListView, TemplateView


def market(request):
    return render(request, 'Market_html/Liveupdate.html', {})


class static_temp(TemplateView):
    template_name = 'Market_html/Liveupdate.html'


class static_list(ListView):
    template_name = 'Market_html/Liveupdate.html'
