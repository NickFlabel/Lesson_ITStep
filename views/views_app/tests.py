from django.test import TestCase
from .models import Author

from django.urls import reverse
from django.contrib.auth.models import User, Permission

# Create your tests here.

class AuthorViewTestCase(TestCase):

    def setUp(self) -> None:
        self.username = 'test_user'
        self.password = 'test_password'
        self.user = User.objects.create_user(username=self.username, password=self.password)
        self.superuser = User.objects.create_superuser(username='superuser',
                                                       password='superuser',
                                                       is_superuser=True)
        self.user_with_permissions = User.objects.create_user(username='user_with_permissions',
                                                              password='permissions')

        perm = Permission.objects.get(codename='delete_author')
        self.user_with_permissions.user_permissions.add(perm)

    def test_author_list_view_user_logged_in(self):
        self.client.force_login(self.user)

        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/author_list.html')

    def test_author_list_view_anonymous_user(self):
        response = self.client.get(reverse('author_list'))

        self.assertEqual(response.status_code, 302)

    def test_create_author(self):
        self.client.force_login(self.superuser)

        response = self.client.get(reverse('author_create'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'views_app/form.html')

    def test_create_author_anonymous_user(self):
        response = self.client.get(reverse('author_create'))

        self.assertEqual(response.status_code, 302)

    def test_create_author_post(self):
        self.client.force_login(self.superuser)
        author_name = 'test_author'
        author_email = 'test@test.com'

        response = self.client.post(reverse('author_create'),
                                    data={'name': author_name,
                                          'bio': 'author_email',
                                          'email': author_email})

        self.assertEqual(response.status_code, 302)
        Author.objects.get(email=author_email) # либо получает объект, либо, если такого нет он возбуждает ошибку <model_name>.DoesNotExist

    def test_delete_author_view(self):
        author_email = 'test2@test.com'
        new_author = Author.objects.create(name='test_author', bio='bio', email=author_email)
        self.client.force_login(self.user_with_permissions)

        response = self.client.post(reverse('author_delete', args=[new_author.pk]))

        self.assertEqual(response.status_code, 302)
        self.assertFalse(Author.objects.filter(pk=new_author.pk).exists()) # False == False -> True


# class TestAuthor(TestCase):
#
#     def setUp(self):
#         self.author = Author.objects.create(name='test_author',
#                                             email='test@test.com',
#                                             bio='test')
#
#     def test_get_authors(self):
#         url = reverse('author_list')
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200) # ==
#         self.assertIn(self.author, response.context['authors']) # in 3 in [1, 2, 3]
#
#     def test_get_author(self):
#         url = reverse('author_detail', kwargs={'pk': self.author.pk})
#
#         response = self.client.get(url)
#
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(self.author, response.context['author'])
#
#     def test_create_author(self):
#         url = reverse('author_create')
#         data = {'name': 'test_name', 'bio': 'test_bio', 'email': 'test2@test.com'}
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(len(Author.objects.all()), 2) # len(authors) == 2
#
#     def test_update(self):
#         url = reverse('author_update', kwargs={'pk': self.author.pk})
#         data = {'name': 'test_name2', 'bio': 'test_bio', 'email': 'test2@test.com'}
#
#         response = self.client.post(url, data)
#
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(Author.objects.get(pk=self.author.pk).name, 'test_name2') # len(authors) == 2
