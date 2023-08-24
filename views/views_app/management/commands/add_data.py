from django.core.management.base import BaseCommand
from views_app.models import Author, Category, Post

class Command(BaseCommand):
    help = 'Наполняет базу данных новыми данными'

    def handle(self, *args, **kwargs):

        # authors
        author_1 = Author.objects.create(name='Джон', email='john@mail.com')
        author_2 = Author.objects.create(name='Джейн', email='jane@email.com')
        author_3 = Author.objects.create(name='Тим', email='tim@email.com')

        # categories
        category_1 = Category.objects.create(name='Путешествия')
        category_2 = Category.objects.create(name='Еда')
        category_3 = Category.objects.create(name='Технологии')
        category_4 = Category.objects.create(name='Искусство')

        # posts
        post_1 = Post.objects.create(title='Прогулки по Берлину', content='Прогулки по Берлину с Джоном', author=author_1, status='p')
        post_1.categories.add(category_1, category_4)
        post_2 = Post.objects.create(title='Парижские вечера', content='Еда и рестораны в Париже', author=author_2, status='d')
        post_2.categories.add(category_1, category_2)
        post_3 = Post.objects.create(title='Python: Введение в программирование', content='Содержание: Основы программирования на Python для начинающих', author=author_3, status='p')
        post_3.categories.add(category_3)
        post_4 = Post.objects.create(title='Введение в искусственный интеллект', content='Обзор технологий и применений искусственного интеллекта.', author=author_3, status='p')
        post_4.categories.add(category_3)
        post_5 = Post.objects.create(title='Путешествие в Тоскану', content='Прекрасная Флоренция', author=author_1, status='p', views=10)
        post_5.categories.add(category_1, category_4)