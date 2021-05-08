
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def first(request):
    books = Book.objects.all()
    return render(request, 'first_temp.html',{'books': books})
