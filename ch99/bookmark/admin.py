from django.contrib import admin
from bookmark.models import Bookmark
# Register your models here.
#53p

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'url')

