from .models import Image, Book
from versatileimagefield.serializers import VersatileImageFieldSerializer
from rest_flex_fields import FlexFieldsModelSerializer

class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes=[
            ('full_size', 'url'),
            ('thumbnail', 'thumbnail__100x100'),
        ]
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']
        
class BookSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Book
        fields = ['pk', 'title', 'author', 'summary', 'isbn', 'genre', 'image']
        expandable_fields = {
            'image': ('ImageSerializer', {'many': True}),
        }