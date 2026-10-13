from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from .models import Expense
from .serializers import (
    RegisterSerializer,
    ExpenseSerializer,
)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


class ExpenseListCreateView(
    generics.ListCreateAPIView
):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Expense.objects.filter(
            user=self.request.user
        ).order_by('-created_at')

        category = self.request.query_params.get(
            'category'
        )

        if category:
            queryset = queryset.filter(
                category__iexact=category
            )

        return queryset

    def perform_create(self, serializer):
        serializer.save(
            user=self.request.user
        )


class ExpenseDetailView(
    generics.RetrieveUpdateDestroyAPIView
):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    http_method_names = [
        'get',
        'put',
        'delete',
        'head',
        'options',
    ]

    def get_queryset(self):
        return Expense.objects.filter(
            user=self.request.user
        )