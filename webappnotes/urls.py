from django.urls import path
from .views import NoteListView, NoteDetailView, note_create

urlpatterns = [
    path('', NoteListView.as_view(), name='note_list'),
    path('note/<int:pk>/', NoteDetailView.as_view(), name='note_detail'),
    path('note/new/', note_create, name='note_create'),
]