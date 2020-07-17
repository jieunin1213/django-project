from django.urls import path
# URLconf에서 뷰를 호출하므로, 뷰 모듈의 관련 클래스를 임포트한다.
#from bookmark.views import BookmarkLV, BookmarkDV
from bookmark import views

# 애플리케이션 이름공간(namespace)를 'bookmark'로 지정
app_name = 'bookmark'
urlpatterns = [
    path('', views.BookmarkLV.as_view(), name='index'),
    path('<int:pk>/', views.BookmarkDV.as_view(), name='detail'),
    # Example: /bookmark/add/
    path('add/',
         views.BookmarkCreateView.as_view(), name="add",
         ),

    # Example: /bookmark/change/
    path('change/',
         views.BookmarkChangeLV.as_view(), name="change",
         ),

    # Example: /bookmark/99/update/
    path('<int:pk>/update/',
         views.BookmarkUpdateView.as_view(), name="update",
         ),

    # Example: /bookmark/99/delete/
    path('<int:pk>/delete/',
         views.BookmarkDeleteView.as_view(), name="delete",
         ),
]