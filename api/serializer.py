from rest_framework import serializers

from .models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['author']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ['category']
