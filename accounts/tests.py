from django.test import TestCase

from django.shortcuts import reverse

from django.apps import apps

# Create your tests here.


class TestUser(TestCase):

    def test_register_new_user(self):
        data = {
            'username': 'test_user',
            'password1': 'mod_123456',
            'password2': 'mod_123456',
            'email': 'email@mail.com',
            'first_name': 'test_first_name',
            'last_name': 'test_last_name'
        }

        response = self.client.post(reverse('user_register'), data=data)

        self.assertEqual(response.status_code, 302)
        author_model = apps.get_model('views_app', 'Author')
        author = author_model.objects.get(name=data['username'])
        self.assertEqual(author.email, data['email'])
