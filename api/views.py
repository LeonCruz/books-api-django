from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializer import BooksSerializer


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
            return Response(serializer.data)

        return Response(serializer.errors)
