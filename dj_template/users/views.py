from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import responses
from django.http import JsonResponse
from rest_framework.viewsets import ModelViewSet
from .serializers import *
from .models import *

# Create your views here.

class WriterViewSet(ModelViewSet):
    serializer_class    = WriterSerializer
    queryset            = Writer.objects.all()
    lookup_field        = 'id'

    @action(detail=True, methods=['GET'])
    def checkPalindrome(self, request, id=None):
        author = self.get_object()
        author_name = author.name
        print('hi')
        return JsonResponse({'isPalindrome':author_name[:len(author_name)//2] == author_name[len(author_name)//2:]})

class BooksViewSet(ModelViewSet):
    serializer_class    = BookSerializer
    queryset            = Book.objects.all()
    lookup_field        = 'id'


@action(detail=True, methods='GET')
def dummyRequest(request):
    return JsonResponse({'hello':'world'})