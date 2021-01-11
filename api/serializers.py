from .models import Author, Book, Genre
from rest_framework import serializers
        
class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    genre = serializers.StringRelatedField(many=True)
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'summary', 'isbn', 'genre', 'image']
        
class AuthorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
        
class GenreSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Genre
        fields = ['name']
        