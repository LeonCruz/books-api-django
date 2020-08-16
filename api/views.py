from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializer import AuthorSerializer, BooksSerializer, CategorySerializer


# Create your views here.
@api_view(['GET'])
def books(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def authors(request):
    authors = Books.objects.all()
    serializer = AuthorSerializer(authors, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def categories(request):
    categories = Books.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(serializer.data)
