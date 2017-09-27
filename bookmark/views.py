from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Bookmark

class BookmarkListV(ListView):
    model = Bookmark

class BookmarkDetailV(DetailView):
    model  = Bookmark
