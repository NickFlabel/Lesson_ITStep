from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=20)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publication_year = models.IntegerField()

class Student(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'

class Course(models.Model):
    name = models.CharField(max_length=10)
    students = models.ManyToManyField(Student)
