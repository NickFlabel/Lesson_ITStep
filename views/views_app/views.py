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


class CreatePostView(CreateView): # modelformmixin
    model = Post
    fields = ['title', 'author', 'content', 'categories', 'status']
    template_name = 'views_app/form.html'
    success_url = '/posts/{id}'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'views_app/form.html'
    success_url = '/posts/'


class UpdatePostView(UpdateView):
    model = Post
    fields = ['title', 'author', 'content', 'categories', 'status']
    success_url = '/posts/{id}'
    template_name = 'views_app/form.html'

class PostList(ListView):
    model = Post
    context_object_name = 'posts' # Author.objects.all()


class PostDetail(DetailView):
    model = Post
    context_object_name = 'post'



class CreateCategoryView(CreateView): 
    model = Category
    fields = '__all__'
    template_name = 'views_app/form.html'
    success_url = '/categories/{id}'


class DeleteCategoryView(DeleteView):
    model = Category
    template_name = 'views_app/form.html'
    success_url = '/categories/'


class UpdateCategoryView(UpdateView):
    model = Category
    fields = '__all__'
    success_url = '/categories/{id}'
    template_name = 'views_app/form.html'


class CategoryList(ListView):
    model = Category
    context_object_name = 'categories' 


class CategoryDetail(DetailView):
    model = Category
    context_object_name = 'category'
