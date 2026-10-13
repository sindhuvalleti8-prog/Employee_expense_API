from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from .views import (
    RegisterView,
    ExpenseListCreateView,
    ExpenseDetailView
)

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('expenses/', ExpenseListCreateView.as_view()),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view()),
]