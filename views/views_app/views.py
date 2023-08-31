from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class CreateAutorView(CreateView): # modelformmixin
    model = Author
    fields = '__all__'
    template_name = 'views_app/form.html'
    success_url = '/authors/{id}'


class DeleteAuthorView(DeleteView):
    model = Author
    template_name = 'views_app/form.html'
    success_url = '/authors/'


class UpdateAuthorView(UpdateView):
    model = Author
    fields = '__all__' # ['name', 'bio']
    success_url = '/authors/{id}'
    template_name = 'views_app/form.html'
    context_object_name = 'form' # default
    pk_url_kwarg = 'pk' # default


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors' # Author.objects.all()


class AuthorDetail(DetailView):
    model = Author
    context_object_name = 'author'
    pk_url_kwarg = 'pk' # default
    template_name = 'views_app/author_detail.html' # default
