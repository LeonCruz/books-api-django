from django.test import TestCase
from rest_framework.test import APIClient

from api.models import Books


# Create your tests here.
class TestApi(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.book = {
            'title': 'A pedra filosofal',
            'author': 'J.K Rowlin',
            'category': 'infanto juvenil'
        }

    def test_register_book(self):
        book = self.book
        response = self.client.post('/', data=book, format='json')

        self.assertTrue(response.status_code, 201)
        self.assertTrue(Books.objects.count(), 1)

    def test_show_all_books(self):
        books = Books.objects.count()
        response = self.client.get('/')
        self.assertEqual(len(response.data), books)

        self.client.post('/', data=self.book, format='json')
        books = Books.objects.count()
        response = self.client.get('/')
        self.assertEqual(len(response.data), books)

    def test_show_all_authors(self):
        self.client.post('/', data=self.book, format='json')

        response = self.client.get('/authors/')
        author = Books.objects.values_list('author')

        self.assertEqual(len(response.data), len(author))

        self.client.post('/',
                         data={
                             'title': 'Universo numa casca de noz',
                             'author': 'Stephen Hawking',
                             'category': 'não ficção'
                         })

        response = self.client.get('/authors/')
        author = Books.objects.values_list('author')

        self.assertEqual(len(response.data), len(author))
