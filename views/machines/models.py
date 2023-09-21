from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.


class Spare(models.Model):
    name = models.CharField(max_length=40)


class Machine(models.Model):
    name = models.CharField(max_length=40)
    spares = models.ManyToManyField(Spare, through='Kit', through_fields=('machine', 'spare'))


class Kit(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    spare = models.ForeignKey(Spare, on_delete=models.CASCADE)
    count = models.IntegerField()


class Car(Machine):
    max_speed = models.IntegerField()
    # OneToOneField


class AssemblyLine(Machine):
    max_capacity = models.IntegerField()


class Content(models.Model):
    title = models.CharField(max_length=40)

    class Meta:
        abstract = True


class Article(Content):
    text = models.TextField(null=True, blank=True)


class Photo(Content):
    image = models.ImageField(upload_to='photos/', null=True, blank=True)


class Comment(models.Model):
    text = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.IntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

