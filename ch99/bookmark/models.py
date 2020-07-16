from django.db import models

#52p
# 장고에서는 테이블을 하나의 클래스로 정의하고, 테이블의 컬럼은 클래스의 변수로 매핑
# 테이블 클래스는 django.db.models.Model 클래스를 상속받아 정의하고,
# 각 클래스 변수의 타입도 장고에서 미리 정의해 둔 필드 클래스를 사용 (CharField, URLField)
# __str()__ 함수 : 객체를 문자열로 표현할 때 사용하는 함수. 장고에서 모델 클래스의 객체는 테이블에 들어 있는 레코드 하나를 의미
# Admin사이트나 장고 셸 등에서 테이블의 레코드명을 보여줘야 하는데, __str()__안쓰면 레코드명이 제대로 표현되지 않음
class Bookmark(models.Model) :
    title = models.CharField('TITLE', max_length=100, blank=True)
    url = models.URLField('URL', unique=True)

    def __str__(self):
        return self.title