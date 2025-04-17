from core import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import CategoryListCreateView, TransactionListCreateView, RegisterView
urlpatterns = [
    path('categories/',CategoryListCreateView.as_view()),
    path('categories/',TransactionListCreateView.as_view()),
    path('register/',RegisterView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]