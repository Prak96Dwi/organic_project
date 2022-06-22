""" apps/blog/admin.py """
from django_summernote.admin import SummernoteModelAdmin
from mptt.admin import MPTTModelAdmin

from django.contrib import admin

from .models import Blog, BlogCategory, Comment


class BlogCategoryAdmin(admin.ModelAdmin):
    """
    Blog Category Model Admin class

    """
    list_display = ('name', 'number_of_articles')

admin.site.register(BlogCategory, BlogCategoryAdmin)

admin.site.register(Comment, MPTTModelAdmin)


class BlogModelAdmin(SummernoteModelAdmin):
    """
    Blog model admin class in which we are inheriting SummernoteModelAdmin

    """
    summernote_fields = '__all__'

admin.site.register(Blog, BlogModelAdmin)
