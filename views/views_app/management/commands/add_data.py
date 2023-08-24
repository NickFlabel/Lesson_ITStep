from django.core.management.base import BaseCommand
from views_app.models import Author, Category, Post

class Command(BaseCommand):
    help = 'Наполняет базу данных новыми данными'

    def handle(self, *args, **kwargs):
        pass