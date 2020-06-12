
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def first(request):
    return render(request, 'first_temp.html')
