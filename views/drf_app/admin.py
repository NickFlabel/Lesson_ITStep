from django.contrib import admin
from .models import Author, Publisher, Book, Location

# Register your models here.

admin.site.register([Author, Publisher, Book, Location])
