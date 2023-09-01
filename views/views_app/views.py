from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render


class CreateAutorView(CreateView): # modelformmixin
    model = Author
    fields = '__all__'
    template_name = 'views_app/form.html'
    success_url = '/authors/{id}'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Создание автора'
        return context


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = 'Обновить автора'
        context['update_text'] = True
        context['action'] = 'обновить'
        context['model'] = str(self.model)
        return context


class AuthorList(ListView):
    model = Author
    context_object_name = 'authors' # Author.objects.all()
    paginate_by = 2

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


class MainPage(TemplateView):
    template_name = 'views_app/main_page.html'

    def get_context_data(self, **kwargs):
        context = {}
        context['range'] = [i for i in range(10, 20)]
        context['first_condition'] = True
        context['second_condition'] = False
        return context


def paginator_view(request: HttpRequest):
    authors = Author.objects.all()
    paginator = Paginator(authors, 2) # authors/?page=1
    if 'page' in request.GET: # request.GET = {'page': 1}
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'authors': page.object_list, 'page': page}
    return render(request, 'views_app/authors_paginator.html', context)



