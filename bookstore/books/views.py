from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from django.shortcuts import render

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def index(request):
    return render(request, 'index.html')