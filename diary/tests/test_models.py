from django.test import TestCase
from django.contrib.auth.models import User
from diary.models import DiaryEntry


class DiaryEntryModelTest(TestCase):
    """Тесты для модели DiaryEntry"""

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.entry = DiaryEntry.objects.create(
            user=self.user,
            title='Тестовая запись',
            content='Это тестовое содержание записи'
        )

    def test_entry_creation(self):
        self.assertEqual(self.entry.title, 'Тестовая запись')
        self.assertEqual(self.entry.user.username, 'testuser')
        self.assertTrue(isinstance(self.entry, DiaryEntry))

    def test_entry_str_representation(self):
        expected_str = f"{self.entry.title} - {self.entry.user.username}"
        self.assertEqual(str(self.entry), expected_str)
