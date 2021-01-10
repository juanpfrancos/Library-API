from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_flex_fields import FlexFieldsModelViewSet
    
class BookViewSet(FlexFieldsModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
