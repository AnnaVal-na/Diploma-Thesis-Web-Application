from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import DiaryEntry


@login_required
def entry_list(request):
    """Список всех записей текущего пользователя"""
    entries = DiaryEntry.objects.filter(user=request.user)
    return render(request, 'diary/entry_list.html', {'entries': entries})


@login_required
def entry_detail(request, pk):
    """Детальный просмотр одной записи"""
    entry = get_object_or_404(DiaryEntry, pk=pk, user=request.user)
    return render(request, 'diary/entry_detail.html', {'entry': entry})
