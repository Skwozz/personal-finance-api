from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Category, Transaction
from django.contrib.auth.models import User


class AuthenticatedAPITestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="12345678")
        response = self.client.post(
            "/api/token/", {"username": "testuser", "password": "12345678"}
        )
        self.token = response.data["access"]
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")


class AuthTests(APITestCase):
    def test_user_can_register(self):
        url = reverse("register")
        data = {"username": "testuser", "email": "test@ya.ru", "password": "12345678"}
        response = self.client.post("/api/register/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TokenTests(APITestCase):
    def test_user_can_get_token(self):
        User.objects.create_user(username="testuser", password="12345678")
        url = reverse("token_obtain_pair")
        data = {"username": "testuser", "password": "12345678"}
        response = self.client.post("/api/token/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CategoryTests(AuthenticatedAPITestCase):

    def test_can_create_category_with_auth(self):

        data = {"name": "Продукты", "type": "EX"}
        response = self.client.post("/api/categories/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.first().name, "Продукты")


class CategoryPermisionTests(APITestCase):
    def test_cannot_create_category_without_auth(self):
        data = {"name": "Продукты", "type": "EX"}
        response = self.client.post("/api/categories/", data)
        self.assertEqual(response.status_code, 401)


class TransactionTests(AuthenticatedAPITestCase):

    def test_can_create_category_with_auth(self):

        self.category = Category.objects.create(name="Еда", type="EX", user=self.user)
        data = {
            "amount": 1500,
            "date": "2025-04-20T10:00:00Z",
            "description": "Кофе и круассаны",
            "category": self.category.id,
        }
        response = self.client.post("/api/transactions/", data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Transaction.objects.count(), 1)
        self.assertEqual(Transaction.objects.first().description, "Кофе и круассаны")


class TransactionPermisionTests(AuthenticatedAPITestCase):

    def test_cannot_create_transaction_without_auth(self):

        self.category = Category.objects.create(name="Еда", type="EX", user=self.user)
        self.client.credentials()
        data = {
            "amount": 1500,
            "date": "2025-04-20T10:00:00Z",
            "description": "Кофе и круассаны",
            "category": self.category.id,
        }
        response = self.client.post("/api/transactions/", data)
        self.assertEqual(response.status_code, 401)


class AnalyticsTests(AuthenticatedAPITestCase):

    def test_category_analytics(self):
        self.category_food = Category.objects.create(
            name="Еда", type="EX", user=self.user
        )
        self.category_transport = Category.objects.create(
            name="Транспорт", type="EX", user=self.user
        )

        Transaction.objects.create(
            amount=1500,
            date="2025-04-20T10:00:00Z",
            description="Кофе",
            category=self.category_food,
            user=self.user,
        )
        Transaction.objects.create(
            amount=2000,
            date="2025-04-21T12:00:00Z",
            description="Обед",
            category=self.category_food,
            user=self.user,
        )
        Transaction.objects.create(
            amount=1200,
            date="2025-04-22T14:00:00Z",
            description="Метро",
            category=self.category_transport,
            user=self.user,
        )
        response = self.client.get("/api/analytics/category/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        categories = {item["category"]: item["total"] for item in response.data}
        self.assertEqual(categories["Еда"], 3500)
        self.assertEqual(categories["Транспорт"], 1200)
