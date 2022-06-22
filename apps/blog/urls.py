""" apps/blog/urls.py """
# Importing Core Django modules
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path(
        'blog/page/', views.blog_page, name='blog_view_page'),

    path(
        'blog/post/form/',
        views.BlogFormView.as_view(),
        name='blog_post_form_view'
    ),

    path(
        'blog/category/form/',
        views.BlogCategoryFormView.as_view(),
        name='blog_cat_form_view'
    ),

    path(
        'blog/details/<int:blog_id>/',
        views.blog_detail,
        name='blog_detail_page_view'
    ),

    path(
        'blog/category/article/<int:id>/',
        views.blog_categories_article,
        name='blog_categories_article'
    ),

    path(
        'user/blog/',
        views.BlogListView.as_view(),
        name='users_blog_list_view'
    ),

    # AJAX function Blog comment URL Path
    path(
        'ajax/blog/',
        views.ajax_get_blog_post_title,
        name='get_blog_post_title'
    ),

    path(
        'ajax/comment/liked/',
        views.ajax_blog_comment_as_liked,
        name='add_blog_comment_as_liked'
    ),

    path('ajax/comment/disliked/',
        views.ajax_blog_comment_as_disliked,
        name='add_blog_comment_as_disliked'
    )
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
