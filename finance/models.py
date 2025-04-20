from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    TYPE_CHOICES = [
        ("IN", "Income"),
        ("EX", "Expense"),
    ]
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Transaction(models.Model):
    amount = models.IntegerField()
    date = models.DateTimeField()
    description = models.TextField(max_length=264)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
