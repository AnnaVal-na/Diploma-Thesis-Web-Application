from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from diary.models import DiaryEntry


class DiaryViewsTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.entry = DiaryEntry.objects.create(
            user=self.user,
            title='Тестовая запись',
            content='Тестовое содержание'
        )

    def test_entry_list_view_authenticated(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('diary:entry_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Тестовая запись')
