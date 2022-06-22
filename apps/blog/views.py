""" apps/blog/views.py """

from apps.blog.models import Blog, BlogCategory, Comment
from apps.blog.forms import BlogForm, BlogCategoryForm

from django.shortcuts import (
    render, redirect, get_object_or_404, get_list_or_404
)
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import FormView
from django.views.generic import ListView, View


def blog_page(request):
    """
    This function is used to display the blog page
    to the user
    """
    tag_id = request.GET.get('tag')
    tag_name = request.GET.get('name')
    tags = Blog.tags.all()
    blog_categories = BlogCategory.objects.all()

    if tag_id:
        blog_articles = Blog.objects.blogs_of_particular_tag(tag_id)
    else:
        blog_articles = Blog.objects.get_queryset()

    # Creates Paginator objects
    paginator = Paginator(blog_articles, 5)
    page_number = request.GET.get('page', 1)

    try:
        blog_articles = paginator.get_page(page_number)  
        # returns the desired page object
    except PageNotAnInteger:
        # if page_number is not an integer then assign the first page
        blog_articles = paginator.page(1)
    except EmptyPage:
        # if page is empty then return last page,
        blog_articles = paginator.page(paginator.num_pages)

    context = {
        'blog_categories' : blog_categories, 
        'blog_articles' : blog_articles, 
        'tags' : tags,
        'tag_name' : tag_name
    }
    return render(request, 'blog/blog.html', context)


@login_required(login_url='user_login_form')
def blog_detail(request, blog_id=id):
    """
    This function is used to display the 
    blog information page to the user.

    Users can also comment to a particular blog.
    In request.POST method.

    Arguments
    ----------
    id : int
        Blog object id.

    """

    blog = get_object_or_404(Blog, pk=blog_id)

    tags = Blog.tags.all()
    related_blogs = Blog.objects.blogs_of_particular_category(
        blog.category, 
        blog_id=blog_id
    )
    recent_blogs = Blog.objects.recent_blogs_of_particular_category(
        blog.category
    )
    blog_categories = BlogCategory.objects.all()
    comments = Comment.objects.filter(post=blog)

    if request.method == 'POST':
        comment = Comment.objects.create(
            post=blog,
            user=request.user,
            content=request.POST.get('content')
        )
        if request.POST.get('nodeid'): # If parent comment id exists
            parent_comment_id = request.POST.get('nodeid')
            comment.parent = get_object_or_404(Comment, pk=parent_comment_id)
            comment.save()

        comment.update_number_of_comments_of_blog()
        # return redirect('blog_detail_page_view', blog_id=blog.id)
        return blog.get_absolute_url()

    context = {
        'blog_categories': blog_categories,
        'blog_detail': blog,
        'blog_list':related_blogs,
        'tags': tags,
        'comments': comments,
        'recent_blog_list': recent_blogs
    }
    return render(request, 'blog/blog_detail.html', context)


# class BlogDetailView(LoginRequiredMixin, View):

#     def get(self, request, *args, **kwargs):
#         blog_id = kwargs.get('blog_id')
#         blog = get_object_or_404(Blog, pk=blog_id)

#         tags = Blog.tags.all()
#         related_blogs = Blog.objects.blogs_of_particular_category(
#             blog.category, 
#             blog_id=blog_id
#         )
#         recent_blogs = Blog.objects.recent_blogs_of_particular_category(
#             blog.category
#         )
#         blog_categories = BlogCategory.objects.all()
#         comments = Comment.objects.filter(post=blog)
#         context = {
#             'blog_categories': blog_categories,
#             'blog_detail': blog,
#             'blog_list':related_blogs,
#             'tags': tags,
#             'comments': comments,
#             'recent_blog_list': recent_blogs
#         }
#         return render(request, 'blog/blog_detail.html', context)

#     def post(self, request, *args, **kwargs):
#         blog_id = kwargs.get('blog_id')
#         blog = get_object_or_404(Blog, pk=blog_id)
#         comment = Comment.objects.create(
#             post=blog,
#             user=request.user,
#             content=request.POST.get('content')
#         )
#         if request.POST.get('nodeid'): # If parent comment id exists
#             parent_comment_id = request.POST.get('nodeid')
#             comment.parent = get_object_or_404(Comment, pk=parent_comment_id)
#             comment.save()

#         comment.update_number_of_comments_of_blog()
#         # return redirect('blog_detail_page_view', blog_id=blog.id)
#         return blog.get_absolute_url()


def blog_categories_article(request, id):
    """
    This function will display articles link beloging
    to a particular category.

    Arguments
    ----------
    id : int
        id of blog cateagory object.

    """

    blog_category = get_object_or_404(BlogCategory, pk=id)
    blog_articles_of_particular_category = Blog.objects.blogs_of_particular_category(
        blog_category.name
    )
    tags = Blog.tags.all()
    blog_categories = BlogCategory.objects.all()

    context = {
        'blog_articles' : blog_articles_of_particular_category,
        'category' : blog_category,
        'tags' : tags,
        'blog_categories' : blog_categories
    }
    return render(request, 'blog/blog_category.html', context)


class BlogFormView(FormView):
    template_name = 'blog/blog_post_form.html'
    form_class = BlogForm
    success_url = '/admn/dashboard/'

    def form_valid(self, form):
        # This method is called when valid blog post form data has been POSTed.
        # It should return an HttpResponse.
        blog_post = form.save()
        blog_post.update_number_of_articles_of_blog_category()
        return super().form_valid(form)


class BlogCategoryFormView(FormView):
    template_name = 'blog/blog_category_form.html'
    form_class = BlogCategoryForm
    success_url = '/admn/dashboard/'

    def form_valid(self, form):
        # This method is called when valid blog post form data has been POSTed.
        # It should return an HttpResponse.
        form.save()
        return super().form_valid(form)


class BlogListView(ListView):
    """
    """
    template_name = 'blog/users_blog_list.html'
    model = Blog


def ajax_get_blog_post_title(request):
    """
    This ajax function is for getting blog post title when user
    type blog title in search bar in blog page.
    """
    return JsonResponse(tuple(Blog.objects.blogs_title_list()), safe=False)


def ajax_blog_comment_as_liked(request):
    """
    This ajax function likes the particular blog comment
    when user click on like button of blog post. 
    """
    node_id = request.GET.get('node_id')
    comment = get_object_or_404(Comment, pk=node_id)
    comment.adding_users_who_liked_the_comment(request)
    return JsonResponse(
        (comment.get_number_of_likes_in_comment(), ),
        safe=False
    )


def ajax_blog_comment_as_disliked(request):
    """
    This ajax function dislikes the particular blog comment
    when user clicks on dislikes button of blog post.
    """
    node_id = request.GET.get('node_id')
    comment = get_object_or_404(Comment, pk=node_id)
    comment.incrementing_number_of_dislikes_of_comment()
    return JsonResponse(
        (comment.get_number_of_dislikes_in_comment(), ),
        safe=False
    )
