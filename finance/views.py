from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CategorySerializer, TransactionSerializer
from .models import Category, Transaction
from django.contrib.auth.models import User


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

# @api_view(['GET'])
# def ping(request):
#     return Response({"ok": True})


class CategoryListCreateView(ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class TransactionListCreateView(ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        return Transaction.objects.filter(user=self.request.user)
