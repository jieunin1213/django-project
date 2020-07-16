from django.db import models
from django.urls import reverse # reverse() 함수 : URL패턴을 만들어주는 장고의 내장함수.
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(verbose_name='TITLE', max_length= 50) # title컬럼 : CharField이므로 한 줄로 입력된다.
    slug = models.SlugField('SLUG', unique= True, allow_unicode= True, help_text='one word for title alias.') # slug : 제목의 별칭
    description = models.CharField('DESCRIPTION', max_length=100, blank=True, help_text='simple description text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)
    modify_dt = models.DateTimeField('MODIFY DATE', auto_now= True)
    tags = TaggableManager(blank=True)

    class Meta: #필드 속성 외에 필요한 파라미터가 있으면, Meta 내부 클래스로 정의
        verbose_name = 'post' # 테이블의 별칭은 단수와 복수를 가질 수 있는데, 단수별칭은 'post'
        verbose_name_plural = 'posts' # 복수별칭은 'posts'
        # 데이터베이스에 저장되는 테이블의 이름을 'blog_posts'로 지정한다.
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title


    # get_absolute_url : 이 메소드가 정의된 객체를 지칭하는 URL을 반환한다.
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=(self.slug,))
    # get_previous() : -modify_dt 컬럼을 기준으로 최신 포스트 반환
    def get_previous(self):
        return self.get_previous_by_modify_dt()

    # get_next() : -modifty_dt 컬럼을 기준으로 예전 포스트를 반환
    def get_next(self):
        return self.get_next_by_modify_dt()