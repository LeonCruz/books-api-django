from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Books
from .serializer import BooksSerializer


# Create your views here.
@api_view(['GET'])
def index(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)

    return Response(serializer.data)
