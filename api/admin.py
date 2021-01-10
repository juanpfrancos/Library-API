from django.contrib import admin

# Register your models here.
from .models import BookInstance, Book, Genre, Author, Image

admin.site.register(BookInstance)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Image)