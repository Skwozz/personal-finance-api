from rest_framework.serializers import ModelSerializer
from .models import Category, Transaction


class CategorySerializer(ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["user"]


class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = "__all__"
        read_only_fields = ["user"]
