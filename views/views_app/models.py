from django.db import models
from django.contrib.auth.models import User


class AuthorManager(models.Manager):

    def get_authors_with_published_posts(self):
        return self.filter(posts__status='p').distinct()


class CategoryManager(models.Manager):

    def get_categories_with_published_posts(self):
        return self.filter(post_set__status='p').distinct()


class Author(models.Model):

    objects = models.Manager()
    new_manager = CategoryManager()

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):

    objects = CategoryManager()

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')
    categories = models.ManyToManyField(Category)
    views = models.IntegerField(default=0)
    status = models.CharField(
        max_length=10,
        choices=[('d', 'Draft'), ('p', 'Published')],
        default='d'
    )

    def __str__(self):
        return self.title

    class Meta:
        permissions = (('hide', 'Возможность прятать посты'), )
