from django.contrib import admin
from django.conf.urls import url, include
from . import views
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'book', views.BookViewSet, basename='Book')
router.register(r'author', views.AuthorViewSet, basename='Author')

urlpatterns = [
    url('', include(router.urls)),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)