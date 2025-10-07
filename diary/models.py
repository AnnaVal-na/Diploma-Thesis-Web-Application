from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class DiaryEntry(models.Model):
    """Модель для записей личного дневника"""

    # Связь с пользователем (один ко многим)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь'
    )

    # Заголовок записи
    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )

    # Содержание записи
    content = models.TextField(verbose_name='Содержание')

    # Дата создания (автоматически при создании)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    # Дата последнего обновления (автоматически при изменении)
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    # Метаданные модели
    class Meta:
        verbose_name = 'Запись дневника'
        verbose_name_plural = 'Записи дневника'
        ordering = ['-created_at']  # Сортировка по убыванию даты

    def __str__(self):
        """Строковое представление объекта"""
        return f"{self.title} - {self.user.username}"

    def get_absolute_url(self):
        """URL для просмотра деталей записи"""
        return reverse('diary:entry_detail', kwargs={'pk': self.pk})
