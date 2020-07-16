from django.shortcuts import render
from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

class BookmarkLV(ListView): # ListView 제너릭 뷰를 상속받는다. ListView를 상속받는 경우는 객체가 들어 있는 리스트를 구성해서 이를 컨텍스트 변수로 템플릿 시스템에 넘겨주면 된다.
    model = Bookmark

class BookmarkDV(DetailView): # BookmarkDV는 Bookmark 테이블의 특정 레코드에 대한 상세 정보를 보여주기 위한 뷰로서, DetailView 제너릭 뷰를 상속받는다.
    model = Bookmark