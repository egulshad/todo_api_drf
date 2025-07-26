from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Todos

User = get_user_model()

class TodoAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user and get JWT token
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_task(self):
        """Test creating a new task"""
        data = {
            "title": "Write unit tests",
            "status": "New"
        }
        response = self.client.post('/api/tasks/tasks/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Todos.objects.count(), 1)

    def test_task_list_pagination(self):
        """Test pagination of task list"""
        # Create 10 tasks
        for i in range(10):
            Todos.objects.create(title=f"Task {i}", status="New", user=self.user)

        response = self.client.get('/api/tasks/tasks/?page=1')
        self.assertEqual(response.status_code, 200)
        self.assertIn('results', response.data)
        self.assertIn('count', response.data)
        self.assertLessEqual(len(response.data['results']), 5)  # because PAGE_SIZE = 5

    def test_filter_by_status(self):
        """Test filtering tasks by status"""
        Todos.objects.create(title="Task 1", status="Completed", user=self.user)
        Todos.objects.create(title="Task 2", status="New", user=self.user)

        response = self.client.get('/api/tasks/tasks/?status=Completed')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['status'], "Completed")
