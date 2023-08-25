from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.views import View
from django.views.generic.base import ContextMixin, TemplateResponseMixin, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView


class PostsView(ListView):
    model = Post
    context_object_name = 'posts'

class PostById(DetailView):
    # model - модель, с которой мы хотим взаимодействоать
    model = Post
    pk_url_kwarg = 'post_id'
    # pk_url_kwarg = 'pk'
    # template_name - путь к желаемому шаблону
    # context_object_name - то: как в контексте будет называтся ваша переменная {'<context_object_name>'
    context_object_name = 'post' # {'post': obj}
    # '<Имя приложения>/<имя модели>_detail.html>'

    # 1) get_object() - собирает запись из базы данных и присваивает ее атрибуту self.object
    # 2) get_context_data() - формирует контекст - {'context_object_name': self.object}
    # 3) render_to_response(context) - self.template_name - '<Имя приложения>/<имя модели>_detail.html>'
    # 4) get()
