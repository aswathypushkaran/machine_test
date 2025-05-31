from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NotesSummaryAPIView, TagListAPIView, NotesByTagAPIView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('notes/summary/', NotesSummaryAPIView.as_view(), name='notes-summary'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('tags/<int:tag_id>/notes/', NotesByTagAPIView.as_view(), name='notes-by-tag'),
    path('', include(router.urls)),
    
]
