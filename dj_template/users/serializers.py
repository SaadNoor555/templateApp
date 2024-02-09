from rest_framework import serializers
from .models import  *

class WriterSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Writer
        fields      = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model       = Book
        fields      = '__all__'

