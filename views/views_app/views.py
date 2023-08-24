from django.http import HttpResponse, HttpResponseNotFound, HttpRequest
from .models import Author, Category, Post
from django.shortcuts import get_object_or_404
from django.template.loader import get_template

'''
def get_posts(request):
    published_posts = Post.objects.filter(status='p')
    list_of_posts = []
    for post in published_posts:
        list_of_posts.append({
            'title': post.title,
            'author': post.author.name,
            'categories': [category.name for category in post.categories.all()],
            'views': post.views,
            'content': post.content
        })
    # За формирование ответа на самом низком уровне в Django отвечает класс HttpResponse
    # В его конструкторе можно определить такие значения как статус-код нашего ответа, тип данных или HTTP-заголовки
    return HttpResponse(list_of_posts) 
'''


def get_post(request, post_id):
    # функция get_object_or_404 принимает первым аргументом желаемую модель, а затем - значения, по которым нам
    # необходимо доставать наш объект
    post = get_object_or_404(Post, pk=post_id) # Post.objects.get(pk=post_id)
    return HttpResponse(post)


def get_posts(request: HttpRequest):
    # request.GET - словарь с парметрами: передаваемыми при помощи метода GET в запросе
    # request.POST - словарь параметров, но для POST-запроса
    # request.method - по нему можно понять с каким методом пришел запрос
    # request.headers - тут хранятся HTTP заголовки запроса
    # request.body - это "тело" запроса
    published_posts = Post.objects.filter(status='p')
    template = get_template('views_app/index.html')
    context = {'posts': published_posts}
    return HttpResponse(template.render(request=request, context=context))
