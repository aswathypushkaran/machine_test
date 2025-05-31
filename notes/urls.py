from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NotesSummaryAPIView, TagListAPIView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('notes/summary/', NotesSummaryAPIView.as_view(), name='notes-summary'),
    path('tags/', TagListAPIView.as_view(), name='tag-list'),
    path('', include(router.urls)),
    
]
