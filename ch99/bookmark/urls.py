from django.urls import path
# URLconf에서 뷰를 호출하므로, 뷰 모듈의 관련 클래스를 임포트한다.
from bookmark.views import BookmarkLV, BookmarkDV

# 애플리케이션 이름공간(namespace)를 'bookmark'로 지정
app_name = 'bookmark'
urlpatterns = [
    path('', BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', BookmarkDV.as_view(), name='detail'),
]