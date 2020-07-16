"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite.views import HomeView
from django.conf.urls.static import static   # static() 함수 : 정적파일을 처리하기 위해 그에 맞는 URL패턴을 반환하는 함수
from django.conf import settings # settings 변수 : settings변수는 settings.py 모듈에서 정의한 항목들을 담고 있는 객체를 가리키는 reference이다.
# from bookmark.views import BookmarkLV, BookmarkDV
from mysite.views import UserCreateView, UserCreateDoneTV

urlpatterns = [
    path('admin/', admin.site.urls), # 장고의 Admin 사이트에 대한 URLcof는 이미 정의되어 있는데, 이를 사용하고 있다. Admin사이트를 사용하기 위해서는 항상 이렇게 정의한다.
    path('', HomeView.as_view(), name = 'home'),
    path('bookmark/', include('bookmark.urls')),
    path('blog/', include('blog.urls')),
    path('photo/', include('photo.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/register/done/', UserCreateDoneTV.as_view(), name='register_done'),

    # path('bookmark/', BookmarkLV.as_view(), name='index'),
    # path('bookmark/<int:pk>/', BookmarkDV.as_view(), name='detail'),

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
