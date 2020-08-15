from rest_framework import serializers

from .models import Author, Books, Category


class BooksSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Books
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
