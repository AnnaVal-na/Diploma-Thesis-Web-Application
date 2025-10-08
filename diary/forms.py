from django import forms
from .models import DiaryEntry


class DiaryEntryForm(forms.ModelForm):
    """Форма для создания и редактирования записей дневника"""

    class Meta:
        model = DiaryEntry
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок записи'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Напишите ваши мысли...',
                'rows': 10
            }),
        }
        labels = {
            'title': 'Заголовок',
            'content': 'Содержание'
        }
