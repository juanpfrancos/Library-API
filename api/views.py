from django.shortcuts import render
from .models import Image, Book
from .serializers import ImageSerializer, BookSerializer
from rest_flex_fields import FlexFieldsModelViewSet

class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()
    
class BookViewSet(FlexFieldsModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
