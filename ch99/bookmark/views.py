from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from mysite.views import OwnerOnlyMixin

class BookmarkLV(ListView): # ListView 제너릭 뷰를 상속받는다. ListView를 상속받는 경우는 객체가 들어 있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 된다.
    model = Bookmark

class BookmarkDV(DetailView): # BookmarkDV는 Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰로서, DetailView 제너릭 뷰를 상속받는다.
    model = Bookmark

class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class BookmarkChangeLV(LoginRequiredMixin, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)


class BookmarkUpdateView(OwnerOnlyMixin, UpdateView):
    model = Bookmark
    fields = ['title', 'url']
    success_url = reverse_lazy('bookmark:index')


class BookmarkDeleteView(OwnerOnlyMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('bookmark:index')