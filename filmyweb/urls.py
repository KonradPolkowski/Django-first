from filmyweb.views import all_movies
from django.urls import path


urlpatterns = [
    path("all/", all_movies)
]
