import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_registration():
    client = APIClient()
    
    response = client.post('/api/register/', {
        "username": "newuser",
        "password": "newpassword123",
        "email": "newuser@example.com"
    })

    assert response.status_code == 201
    assert User.objects.filter(username="newuser").exists()

@pytest.mark.django_db
def test_user_registration_invalid_username():
    client = APIClient()
   
    response = client.post('/api/register/', {
        "username": "invalid user",
        "password": "password123",
        "email": "invalid@example.com"
    })

    assert response.status_code == 400
    assert "username" in response.data

@pytest.mark.django_db
def test_obtain_jwt_token():
    user = User.objects.create_user(username="testuser", password="password123")
    client = APIClient()
    
    response = client.post('/api/token/', {
        "username": "testuser",
        "password": "password123"
    })

    assert response.status_code == 200
    assert "access" in response.data
    assert "refresh" in response.data

@pytest.mark.django_db
def test_obtain_jwt_token_invalid_credentials():
    client = APIClient()
    
    response = client.post('/api/token/', {
        "username": "wronguser",
        "password": "wrongpassword"
    })

    assert response.status_code == 401
    assert "access" not in response.data
