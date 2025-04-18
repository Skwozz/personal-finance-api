from core import urls
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import CategoryListCreateView, TransactionListCreateView, RegisterView, CategoryDetailView, TransactionDetailView, AnalyticsMonthlyView
urlpatterns = [
    path('categories/',CategoryListCreateView.as_view()),
    path('transactions/',TransactionListCreateView.as_view()),
    path('register/',RegisterView.as_view(),name= 'register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('categories/<int:pk>/', CategoryDetailView.as_view()),
    path('transactions/<int:pk>/', TransactionDetailView.as_view()),
    path('analytics/monthly/',AnalyticsMonthlyView.as_view())
]