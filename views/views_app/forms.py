from django import forms
from .models import Author
from django.forms import modelform_factory


author_form = modelform_factory(Author, fields=['name', 'email', 'bio'])
