from django.urls import path

from api import views

urlpatterns = [
    path('', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
]
