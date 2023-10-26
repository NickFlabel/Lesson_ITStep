from .models import Author, Publisher, Book
from .serializers import AuthorSerializer, PublisherSerializer, AuthorUpdateSerializer, BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from drf_yasg.utils import swagger_auto_schema

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.decorators import action

# Create your views here.


class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    @swagger_auto_schema(operation_description='Отдает все книги данного автора',
                         responses={200: BookSerializer(many=True)})
    @action(detail=True, methods=['get'])
    def books(self, request, pk):
        author = self.get_object()
        books = author.book_set.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def authors_with_two(self, request):
        authors = Author.objects.filter(name__icontains='2')
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def get_authors(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         data = request.data
#         serializer = AuthorSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


@api_view(['GET', 'PUT', 'DELETE'])
def get_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'GET':
        serializer = AuthorUpdateSerializer(author)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = AuthorUpdateSerializer(author, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        author.delete()
        return Response(status=204)


@api_view(['GET', 'POST'])
def get_publishers(request):
    if request.method == 'GET':
        publishers = Publisher.objects.all()
        serializer = PublisherSerializer(publishers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        data = request.data
        serializer = PublisherSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

# Нужен view, реализующий GET, PUT, DELETE для конкретного издателя


@api_view(["GET", "PUT", "DELETE"])
def get_publisher(request, pk):
    publisher = get_object_or_404(Publisher, pk=pk)
    if request.method == 'GET':
        serializer = PublisherSerializer(publisher)
        return Response(serializer.data)

    elif request.method == 'PUT':
        data = request.data
        serializer = PublisherSerializer(publisher, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        publisher.delete()
        return Response(status=204)


class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()




