from django.urls import reverse
from rest_framework.test import APITestCase
from .models import Author, Publisher, Book, Location
from rest_framework import status

import json
# Create your tests here.


class AuthorListTests(APITestCase):
    def setUp(self) -> None:
        self.author_name = 'test_name'
        self.author_birthdate = '2023-10-02'
        self.author_data = {
            'name': self.author_name,
            'birthdate': self.author_birthdate
        }
        self.url = reverse('book_authors_list')

    def test_create_author(self):
        response = self.client.post(self.url, self.author_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Author.objects.count(), 1)
        self.assertEqual(Author.objects.first().name, self.author_name)

    def test_invalid_data(self):
        invalid_data = {'name': "John Doe"}

        response = self.client.post(self.url, invalid_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_author_list(self):
        Author.objects.create(name='author_1', birthdate='2000-02-15')
        Author.objects.create(**self.author_data)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


class AuthorDetailTests(APITestCase):

    def setUp(self) -> None:
        self.author_data = {
            'name': 'John Doe',
            'birthdate': '2000-01-01'
        }
        self.author = Author.objects.create(**self.author_data)
        self.url = reverse('book_author_detain', args=[self.author.pk])

    def test_get_author_detail(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.author_data['name'])

    def test_update_author(self):
        update_data = {'name': 'Update Name', 'birthdate': '1995-05-05'}

        response = self.client.put(self.url, update_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.author.refresh_from_db()
        self.assertEqual(self.author.name, update_data['name'])

    def test_delete_author(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class BookTests(APITestCase):
    def setUp(self) -> None:
        self.author_1 = Author.objects.create(name='author_1', birthdate='2000-01-01')
        self.author_2 = Author.objects.create(name='author_2', birthdate='2000-01-01')

        self.location = Location.objects.create(name="location")

        self.publisher = Publisher.objects.create(name="publisher", location=self.location)

        self.book_data = {
            "title": "test_book",
            "pub_date": "2020-01-01",
            "authors": [self.author_1.pk, self.author_2.pk],
            "publisher": self.publisher.pk
        }
        self.url = reverse("book_book_list")

    def test_create_book(self):
        response = self.client.post(self.url, self.book_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(Book.objects.first().authors.count(), 2)




