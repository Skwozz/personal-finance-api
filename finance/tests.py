from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category
from django.contrib.auth.models import User

class AuthTests(APITestCase):
    def test_user_can_register(self):
        url = reverse('register')
        data = {
            'username':'testuser',
            'email':'test@ya.ru',
            'password':'12345678'
        }
        response = self.client.post('/api/register/',data)
        self.assertEqual(response.status_code,status.HTTP_201_CREATED)

class TokenTests(APITestCase):
    def test_user_can_get_token(self):
        User.objects.create_user(username="testuser", password="12345678")
        url = reverse('token_obtain_pair')
        data = {
            'username':'testuser',
            'password':'12345678'
        }
        response = self.client.post('/api/token/',data)
        self.assertEqual(response.status_code,status.HTTP_200_OK)


class CategoryTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345678")
        response = self.client.post('/api/token/',{
            'username':'testuser',
            'password':'12345678'
        })
        self.token = response.data['access']

    def test_can_create_category_with_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')
        data = {
            'name':'Продукты',
            'type':'EX'
        }
        response = self.client.post('/api/categories/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(),1)
        self.assertEqual(Category.objects.first().name, 'Продукты')





