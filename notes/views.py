from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse

class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
    def get_queryset(self):
        # Only return notes created by the authenticated user
        return Note.objects.filter(created_by=self.request.user)
    


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
    
