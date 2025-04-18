from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, TransactionSerializer
from .models import Category, Transaction
from django.contrib.auth.models import User
from django.db.models import Sum
from django.db.models.functions import TruncMonth
from django.db import models

class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error':'Все поля должны быть заполнены'},status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({'error':'Такой пользователь уже существует'},status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username,email=email,password=password)
        return Response({'message':'Пользователь успешно создан'},status=status.HTTP_201_CREATED)


class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionListCreateView(ListCreateAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)

class AnalyticsMonthlyView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        transactions = request.user.transaction_set.all()
        monthly_data = transactions.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            income = Sum('amount',filter=models.Q(category__type='IN')),
            expense = Sum('amount',filter=models.Q(category__type='EX')),
        ).order_by('month')
        return Response(monthly_data)
