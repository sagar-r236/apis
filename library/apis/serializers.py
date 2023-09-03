from rest_framework import serializers

from books.models import Book

class BookSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'