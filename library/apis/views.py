from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from books.models import Book
from . import serializers

class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = serializers.BookSerailizer