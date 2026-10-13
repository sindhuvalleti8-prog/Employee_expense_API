from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Expense


class RegisterSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        source='first_name'
    )
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']

    def validate_email(self, value):
        if User.objects.filter(
            email__iexact=value
        ).exists():
            raise serializers.ValidationError(
                'Email already registered'
            )
        return value

    def create(self, validated_data):
        email = validated_data['email']
        return User.objects.create_user(
            username=email,
            email=email,
            first_name=validated_data['first_name'],
            password=validated_data['password']
        )


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'id',
            'user',
            'title',
            'amount',
            'category',
            'expense_date',
            'created_at',
        ]
        read_only_fields = [
            'id',
            'user',
            'created_at',
        ]

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                'Amount must be greater than 0'
            )
        return value