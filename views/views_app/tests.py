from django.test import TestCase
from .models import Author

from django.urls import reverse

# Create your tests here.


class TestAuthor(TestCase):

    def setUp(self):
        self.author = Author.objects.create(name='test_author',
                                            email='test@test.com',
                                            bio='test')

    def test_get_authors(self):
        url = reverse('author_list')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200) # ==
        self.assertIn(self.author, response.context['authors']) # in 3 in [1, 2, 3]

    def test_get_author(self):
        url = reverse('author_detail', kwargs={'pk': self.author.pk})

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.author, response.context['author'])

    def test_create_author(self):
        url = reverse('author_create')
        data = {'name': 'test_name', 'bio': 'test_bio', 'email': 'test2@test.com'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(Author.objects.all()), 2) # len(authors) == 2

    def test_update(self):
        url = reverse('author_update', kwargs={'pk': self.author.pk})
        data = {'name': 'test_name2', 'bio': 'test_bio', 'email': 'test2@test.com'}

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Author.objects.get(pk=self.author.pk).name, 'test_name2') # len(authors) == 2
