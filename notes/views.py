from rest_framework import viewsets, permissions
from .models import Note, Tag
from .serializers import NoteSerializer, TagSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.exceptions import NotFound

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        # Only return notes created by the authenticated user
        return Note.objects.filter(created_by=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # After deleting, get remaining notes for this user
        remaining_notes = self.get_queryset()
        serializer = self.get_serializer(remaining_notes, many=True)

        return Response({
            'detail': 'Note deleted successfully.',
            'remaining_notes': serializer.data
        }, status=status.HTTP_200_OK)


class NotesSummaryAPIView(generics.GenericAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

    def get(self, request, *args, **kwargs):
        notes = self.get_queryset()
        total_notes = notes.count()

        notes_list = [
            {
                'id': note.id,
                'title': note.title,
                'url': reverse('notes-detail', args=[note.id], request=request)
            }
            for note in notes
        ]

        return Response({
            'total_notes': total_notes,
            'notes': notes_list
        })
    

class TagListAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]  # Optional, if you want auth


class NotesByTagAPIView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        tag_id = self.kwargs.get('tag_id')
        # Validate tag existence
        try:
            tag = Tag.objects.get(id=tag_id)
        except Tag.DoesNotExist:
            raise NotFound('Tag not found')

        # Return notes linked to this tag and created by current user
        return Note.objects.filter(tag=tag, created_by=self.request.user)