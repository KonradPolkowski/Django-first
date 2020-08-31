from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def all_movies(request):
    # return HttpResponse("<h1>to jest nasz pierwszy test <h1>")
    #test = "to jest cos wewntątrz"
    return render(request, "filmy.html")
