from django.urls import path

from api import views

urlpatterns = [
    path('', views.index, name='index'),
    path('authors/', views.authors, name='authors'),
    path('categories/', views.categories, name='categories'),
]
