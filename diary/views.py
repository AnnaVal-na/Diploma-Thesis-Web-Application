from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from .models import DiaryEntry
from .forms import DiaryEntryForm


@login_required
def entry_list(request):
    """Список всех записей текущего пользователя с поиском"""
    entries = DiaryEntry.objects.filter(user=request.user)

    # Обработка поискового запроса
    search_query = request.GET.get('search', '')
    if search_query:
        entries = entries.filter(
            models.Q(title__icontains=search_query) |
            models.Q(content__icontains=search_query)
        )

    return render(request, 'diary/entry_list.html', {
        'entries': entries,
        'search_query': search_query
    })


@login_required
def entry_detail(request, pk):
    """Детальный просмотр одной записи"""
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})


@login_required
def entry_create(request):
    """Создание новой записи"""
    if request.method == 'POST':
        form = DiaryEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit=False)
            entry.user = request.user
            entry.save()
            messages.success(request, 'Запись успешно создана!')
            return redirect('diary:entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm()

    return render(request, 'diary/entry_form.html', {
        'form': form,
        'title': 'Новая запись'
    })


@login_required
def entry_update(request, pk):
    """Редактирование существующей записи"""
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        form = DiaryEntryForm(request.POST, instance=entry)
        if form.is_valid():
            entry = form.save()
            messages.success(request, 'Запись успешно обновлена!')
            return redirect('diary:entry_detail', pk=entry.pk)
    else:
        form = DiaryEntryForm(instance=entry)

    return render(request, 'diary/entry_form.html', {
        'form': form,
        'title': 'Редактирование записи',
        'entry': entry
    })


@login_required
def entry_delete(request, pk):
    """Удаление записи"""
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)

    if request.method == 'POST':
        entry.delete()
        messages.success(request, 'Запись успешно удалена!')
        return redirect('diary:entry_list')

    return render(request, 'diary/entry_confirm_delete.html', {'entry': entry})
