from django.test import TestCase
from diary.forms import DiaryEntryForm


class DiaryEntryFormTest(TestCase):
    """Тесты для форм дневника"""

    def test_valid_form(self):
        form_data = {
            'title': 'Тестовая запись',
            'content': 'Тестовое содержание записи'
        }
        form = DiaryEntryForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form_empty_title(self):
        form_data = {
            'title': '',
            'content': 'Тестовое содержание'
        }
        form = DiaryEntryForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
