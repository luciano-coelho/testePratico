import pytest
from tasks.models import Task
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_task_creation():
    user = User.objects.create_user(username='testuser', password='12345')
    task = Task.objects.create(
        title="Test Task",
        description="Test Description",
        completed=False,
        user=user
    )
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.completed is False
    assert task.user == user

@pytest.mark.django_db
def test_task_str():
    user = User.objects.create_user(username='testuser', password='12345')
    task = Task.objects.create(title="Test Task", user=user)
    assert str(task) == "Test Task"
