import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from tasks.models import Task

@pytest.mark.django_db
def test_task_shared_with_user_can_view():
    user1 = User.objects.create_user(username='user1', password='pass123')
    user2 = User.objects.create_user(username='user2', password='pass123')
    task = Task.objects.create(title="Tarefa Compartilhada", user=user1)
    task.shared_with.add(user2)

    client = APIClient()
    client.force_authenticate(user=user2)
    response = client.get(f'/api/tasks/{task.id}/')
    assert response.status_code == 200
    assert response.data['title'] == "Tarefa Compartilhada"

@pytest.mark.django_db
def test_task_not_shared_with_user_cannot_view():
    user1 = User.objects.create_user(username='user1', password='pass123')
    user2 = User.objects.create_user(username='user2', password='pass123')
    user3 = User.objects.create_user(username='user3', password='pass123')  
    task = Task.objects.create(title="Tarefa Privada", user=user1)
    task.shared_with.add(user2)

    client = APIClient()
    client.force_authenticate(user=user3)
    response = client.get(f'/api/tasks/{task.id}/')
    assert response.status_code == 404  
