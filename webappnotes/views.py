from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Note
from .forms import NoteForm

class NoteListView(ListView):
    model = Note
    template_name = 'webappnotes/note_list.html'
    context_object_name = 'notes'
    ordering = ['-created_at']

class NoteDetailView(DetailView):
    model = Note
    template_name = 'webappnotes/note_detail.html'
    context_object_name = 'note'

def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'webappnotes/note_form.html', {'form': form})