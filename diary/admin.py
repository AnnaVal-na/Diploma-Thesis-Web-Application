from django.contrib import admin
from .models import DiaryEntry


@admin.register(DiaryEntry)
class DiaryEntryAdmin(admin.ModelAdmin):
    """Настройки отображения модели в админ-панели"""

    list_display = ('title', 'user', 'created_at', 'updated_at')
    list_filter = ('created_at', 'user')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_at'

    # Поля, которые отображаются при редактировании
    fields = ('user', 'title', 'content', 'created_at', 'updated_at')

    # Поля только для чтения
    readonly_fields = ('created_at', 'updated_at')
