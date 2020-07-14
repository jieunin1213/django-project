from django.shortcuts import render

# 60p

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
    model = Bookmark    # Bookmark 는 bookmark_list.html 참조

class BookmarkDV(DetailView):
    model = Bookmark   # Bookmark는 bookmark_detail.html 참조

# Create your views here.
