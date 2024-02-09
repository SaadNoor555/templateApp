from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('books', BooksViewSet) 
router.register('authors', WriterViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('dummo', dummyRequest)
]