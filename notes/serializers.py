from rest_framework import serializers
from .models import Note, Tag

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'title']
 
class NoteSerializer(serializers.ModelSerializer):
    tag_detail = TagSerializer(source='tag', read_only=True)  # optional

    class Meta:
        model = Note
        fields = ['id', 'title', 'note', 'tag_detail', 'created_by', 'created_at', 'updated_at']
        read_only_fields = ['created_by', 'created_at', 'updated_at']

    def create(self, validated_data):
        title = validated_data.get('title').strip()

        # Check if a tag with the same title exists
        tag, created = Tag.objects.get_or_create(title=title)

        # Attach the tag to the note
        validated_data['tag'] = tag

        # Create the note
        return Note.objects.create(**validated_data)