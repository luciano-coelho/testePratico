import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tasks.models import Category

@pytest.mark.django_db
class TestCategoryEndpoints:
    @pytest.fixture
    def api_client(self):
        return APIClient()

    @pytest.fixture
    def user(self, api_client):
        user = User.objects.create_user(username='testuser', password='12345')
        api_client.force_authenticate(user=user)
        return user

    @pytest.fixture
    def category(self, user):
        return Category.objects.create(name="Trabalho")

    def test_create_category(self, api_client, user):
        response = api_client.post('/api/categories/', {
            "name": "Pessoal"
        })
        assert response.status_code == 201
        assert response.data["name"] == "Pessoal"

    def test_update_category(self, api_client, category):
        url = f'/api/categories/{category.id}/'
        response = api_client.patch(url, {
            "name": "Atualizado"
        })
        assert response.status_code == 200
        assert response.data["name"] == "Atualizado"
    
    def test_delete_category(self, api_client, category):
        url = f'/api/categories/{category.id}/'
        response = api_client.delete(url)
        assert response.status_code == 204
        assert not Category.objects.filter(id=category.id).exists()
