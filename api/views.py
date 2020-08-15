from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Author, Books, Category
from .serializer import AuthorSerializer, BooksSerializer, CategorySerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def authors(request):
    authors_list = Author.objects.all()
    serializer = AuthorSerializer(authors_list, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def categories(request):
    categories_list = Category.objects.all()
    serializer = AuthorSerializer(categories_list, many=True)

    return Response(serializer.data)
