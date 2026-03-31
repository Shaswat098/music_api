from datetime import datetime

from django.contrib.auth.models import User
from rest_framework import serializers

from catalog.models import Album, Artist, Song

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ArtistSerializer(serializers.Serializer):
    class Meta:
        model = Artist
        fields = '__all__'

class AlbumSerializer(serializers.Serializer):
    class Meta:
        model = Album
        fields = '__all__'

class SongSerializer(serializers.Serializer):
    class Meta:
        model = Song
        fields = '__all__'





# class Comment:
#     def __init__(self, email, content, created = None):
#         self.email = email
#         self.content = content
#         self.created = created or datetime.now()

# class CommentSerializer(serializers.Serializer):
#     email = serializers.EmailField()
#     content = serializers.CharField(max_length = 200)
#     created = serializers.DateTimeField()

#     def create(self, validated_data):
#         return super().create(validated_data)
    
#     def update(self, instance, validated_data):
#         return super().update(instance, validated_data)

