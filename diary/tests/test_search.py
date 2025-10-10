from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from diary.models import DiaryEntry

class SearchFunctionalityTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            password='testpass123'
        )
        self.entry1 = DiaryEntry.objects.create(
            user=self.user,
            title='Запись о программировании',
            content='Изучаю Python и Django'
        )

    def test_search_by_title(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('diary:entry_list'), {'search': 'программировании'})
        self.assertContains(response, 'Запись о программировании')
