from django.contrib import admin
from .models import MovieList, Movie

# Register your models here.

admin.site.register(Movie)
admin.site.register(MovieList)

