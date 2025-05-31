from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet, NotesSummaryAPIView

router = DefaultRouter()
router.register(r'notes', NoteViewSet, basename='notes')

urlpatterns = [
    path('notes/summary/', NotesSummaryAPIView.as_view(), name='notes-summary'),
    path('', include(router.urls)),
]
