
# Employee Expense Management API

# Technologies
  Python
  Django
  Django REST Framework
  PostgreSQL
  JWT Authentication
  Postman

# Features
  User Registration
  JWT Login
  Create, View, Update and Delete Expenses
  Filter Expenses by Category
  Amount Validation
  User-Based Expense Access

# API Endpoints
POST /api/register/
POST /api/login/
GET /api/expenses/
POST /api/expenses/
GET /api/expenses/1/
PUT /api/expenses/1/
DELETE /api/expenses/1/
GET /api/expenses/?category=Food
# Installation
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver 8001
# Authentication
Use the JWT access token in Postman:
Authorization: Bearer Token
# Security
Each user can access only their own expenses.
Expense amount must be greater than zero.
