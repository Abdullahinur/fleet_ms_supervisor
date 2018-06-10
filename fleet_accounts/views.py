import datetime as dt

from django.shortcuts import render

from .models import Sacco

# Create your views here.


def home(request):
    sacco_list = Sacco.objects.all()
    date = dt.date.today()
    return render(request, 'home.html', {"saccos": sacco_list, "date": date})
