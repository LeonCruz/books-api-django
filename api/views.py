from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializer import AuthorSerializer, BooksSerializer, CategorySerializer


# Create your views here.
@api_view(['GET', 'POST'])
def books(request):
    if request.method == 'GET':
        books = Books.objects.all()
        serializer = BooksSerializer(books, many=True)

        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BooksSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors)


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
