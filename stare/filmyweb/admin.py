from django.contrib import admin
from .models import Film

# admin.site.register(Film)


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    #fields = ["title", "description", "year"]
    #exclude = ["description"]
    list_display = ["title", "imbd_rating", "year"]
    list_filter = ["year", "imbd_rating"]
    search_fields = ["title", "description"]
