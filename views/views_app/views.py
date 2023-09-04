from django.http import HttpResponse, HttpResponseNotFound, HttpRequest, HttpResponseRedirect, HttpResponseBadRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from django.urls import reverse

from . import forms


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
    form_class = forms.PostFormAlt
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
    context_object_name = 'posts' # Post.objects.all()


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


class UserRegistrationView(FormView):
    template_name = 'views_app/form.html'
    form_class = forms.UserRegistrationForm

    def form_valid(self, form):
        return HttpResponse('form valid!')

    def form_invalid(self, form):
        return HttpResponse('form invalid')


def add_record(request: HttpRequest):
    if request.method == 'POST':
        form = forms.SimpleForm(request.POST) # {'name': ..., 'description': ,,,}
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category_list'))
    elif request.method == 'GET':
        form = forms.SimpleForm()
        context = {'form': form}
        return render(request, 'views_app/form.html', context)
    else:
        return HttpResponseBadRequest()


def update_category(request: HttpRequest, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = forms.SimpleForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('category_detail', kwargs={'pk': pk}))
        else:
            return HttpResponseBadRequest()
    elif request.method == 'GET':
        form = forms.SimpleForm(instance=category) # initial
        context = {'form': form}
        return render(request, 'views_app/form.html', context)
    else:
        return HttpResponseBadRequest()


def author_search(request: HttpRequest):
    if request.method == 'POST':
        form = forms.AuthorSearchForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['author_name']
            author = Author.objects.filter(name__icontains=name).first()
            if author:
                return redirect('author_detail', pk=author.pk)
            else:
                messages.warning(request, 'Автор с этим ключем не был найден')
                messages.warning(request, 'custom')
    else:
        form = forms.AuthorSearchForm()

    context = {'form': form}
    return render(request, 'views_app/form.html', context)