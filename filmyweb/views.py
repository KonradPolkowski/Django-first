from django.shortcuts import render
from django.http import HttpResponse
from .models import Film


def wszystkie_filmy(request):
    # return HttpResponse("<h1>to jest nasz pierwszy test</h1>")
    test = "to jest cos we views"
    filmy = ["Avatar", "Titanic",  "godfaher"]
    wszystkie = Film.objects.all()
    return render(request, 'filmy.html', {'filmy': wszystkie, 'text': test})
