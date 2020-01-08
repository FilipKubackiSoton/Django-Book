from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Book

class BookListView(ListView):
    model = Book
    contex_object_name = 'book_list'#new
    template_name = 'books/book_list.html'

class BookDetailView(DetailView):
    model = Book
    contex_object_name = 'book'
    template_name = 'books/book_detail.html'
