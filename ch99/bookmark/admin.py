from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
#53p
#BookmarkAdmin 클래스 : Bookmark 클래스가 Admin사이트에서 어떤 모습으로 보여줄지 정의하는 클래스
#Bookmark 내용을 보여줄 때, id와 title, url을 화면에 출력하라고 지정했다.
# 그리고 @admin.register() 데코레이터를 사용하여 어드민 사이트에 등록한다.
@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')


# 데이터베이스 변경사항 반영
# 테이블의 신규 생성, 테이블의 정의  변경 등 데이터베이스에 변경이 필요한 사항이 있으면,# 이를 데이터베이스에 실제로 반영해주는 작업해야함
# python manage.py makemigrations bookmark
# python manage.py manage.py migrate
