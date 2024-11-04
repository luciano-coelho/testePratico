import pytest
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tasks.models import Task

@pytest.mark.django_db(transaction=True)
def test_create_task():
    user = User.objects.create_user(username='testuser', password='12345')
    client = APIClient()
    client.force_authenticate(user=user)

    response = client.post('/api/tasks/', {
        'title': 'New Task',
        'description': 'Task description'
    })

    assert response.status_code == 201
    assert Task.objects.filter(title='New Task', user=user).exists()

@pytest.mark.django_db(transaction=True)
def test_get_task_list():
    Task.objects.all().delete()

    user = User.objects.create_user(username='testuser', password='12345')
    client = APIClient()
    client.force_authenticate(user=user)

    Task.objects.create(title="Task 1", user=user)
    Task.objects.create(title="Task 2", user=user)

    other_user = User.objects.create_user(username='otheruser', password='12345')
    Task.objects.create(title="Other User Task", user=other_user)

    response = client.get('/api/tasks/')
    assert response.status_code == 200
    assert response.data['count'] == 2 

@pytest.mark.django_db(transaction=True)
def test_update_task():
    Task.objects.all().delete()

    user = User.objects.create_user(username='testuser', password='12345')
    client = APIClient()
    client.force_authenticate(user=user)

    task = Task.objects.create(title="Task to Update", completed=False, user=user)
    response = client.put(f'/api/tasks/{task.id}/', {
        'title': 'Task to Update',
        'description': 'Updated description',
        'completed': True
    })

    assert response.status_code == 200
    task.refresh_from_db()
    assert task.completed is True
    assert task.description == 'Updated description'

@pytest.mark.django_db(transaction=True)
def test_delete_task():
    Task.objects.all().delete() 

    user = User.objects.create_user(username='testuser', password='12345')
    client = APIClient()
    client.force_authenticate(user=user)

    task = Task.objects.create(title="Task to Delete", user=user)
    response = client.delete(f'/api/tasks/{task.id}/')

    assert response.status_code == 204
    assert not Task.objects.filter(id=task.id).exists()
