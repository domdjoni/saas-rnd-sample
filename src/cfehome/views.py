import pathlib
from django.shortcuts import render
from django.http import HttpResponse
from visits.models import Visits

this_dir = pathlib.Path(__file__).resolve().parent


def home_page_view(request, *args, **kwargs):
    queryset = Visits.objects.all()
    my_title= "Ovo je moj naslov"

    my_context = {
        'page_title' : my_title,
        'queryset' : queryset.count()
    }

    home_html = "home.html"
    Visits.objects.create()
    return render(request, home_html, my_context)
