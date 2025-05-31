from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NotesSummaryAPIView, NoteDetailAPIView

router = DefaultRouter()
router.register(r'notes', NoteViewSet)

urlpatterns = [
    path('notes/summary/', NotesSummaryAPIView.as_view(), name='notes-summary'),
    path('notes/<int:pk>/', NoteDetailAPIView.as_view(), name='note-detail'),
]
