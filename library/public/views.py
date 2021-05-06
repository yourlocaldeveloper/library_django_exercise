# libary views file
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Author, Book

def not_found_404(req, exception):
  return render(req, 'public/404.html')

def home(req):
  book_data = { 'book_data': Book.objects.all()}
  return render(req, 'public/home.html', book_data)

def show_book(req, id):
  print(Book.objects.get(pk=id))
  book_data = { 'book_data': Book.objects.get(pk=id) }
  return render(req, 'public/books.html', book_data)