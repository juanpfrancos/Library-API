from django.shortcuts import render
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_flex_fields import FlexFieldsModelViewSet
    
class BookViewSet(FlexFieldsModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
class AuthorViewSet(FlexFieldsModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
