from .models import Book
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer
        
class BookSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'summary', 'isbn', 'genre', 'image']
        