""" apps/blog/models.py

This module defines the four concrete, non-abstract models:
    * :class:`BlogCategory`
    * :class:`Blog`
    * :class:`Comment`

"""
from taggit.managers import TaggableManager
from mptt.models import MPTTModel, TreeForeignKey

from django.conf import settings
from django.shortcuts import redirect
from django.db.models import (
    CASCADE,
    Model,
    CharField,
    IntegerField,
    ImageField,
    DateField,
    ForeignKey,
    TextField,
    DateTimeField,
    ManyToManyField
)

from .managers import (
    BlogCategoryManager,
    BlogManager
)


class BlogCategory(Model):
    """
    Blog Category model data table

    """
    class Meta:
        verbose_name = 'BlogCategory'
        verbose_name_plural = 'BlogCategories'

    # Name of the blog Category
    name = CharField(max_length=100)

    # Number of articles of particular blog category
    number_of_articles = IntegerField(default=0, null=True)

    objects = BlogCategoryManager()


    def __str__(self):
        """ string representation of BlogCategory instance """
        return f'{self.name}'

    #==================================================================================
    def get_lowercase_category_name(self):
        """
        get lowercase category name
        """
        return self.name.lower()


class Blog(Model):
    """
    Blog model data table

    """
    class Meta:
        verbose_name = 'Blog'
        verbose_name_plural = 'Blogs'

    # Title of a blog post article
    title = CharField(max_length=200, null=False)
    
    # Category of a blog post article
    category = CharField(max_length=100, null=False)
    
    # Image of a blog post article
    image = ImageField(upload_to='blog-post/', null=True)
    
    # Content of a blog post article.
    body = TextField(null=True)
    
    # Date when the blog has been posted
    date = DateField(auto_now_add=True)
    
    # Number of comments in a particular blog
    number_of_comments = IntegerField(default=0, null=False)

    # tags of particular blog
    tags = TaggableManager()

    objects = BlogManager()

    # =====================================================================================
    def get_absolute_url(self):
        """
        Return absolute url of a blog.
        """
        return redirect('blog_detail_page_view', blog_id=self.id)

    #========================================================================================
    def update_number_of_articles_of_blog_category(self):
        """
        This method  updates  number of articles of blog category
        """
        blog_category = BlogCategory.objects.filter(name=self.category).first()
        blog_category.number_of_articles += 1
        blog_category.save()

    #======================================================================================
    def get_number_of_comments_in_blog(self) -> int:
        """
        This  method returns number of comments in blog
        """
        return Comment.objects.filter(post_id=self.id).count()

    def __str__(self) -> str:
        """ string representation of Blog instance """
        return f'{self.title}'


class Comment(MPTTModel):
    """
    Blog comments model table
    """
    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    post = ForeignKey(
        Blog, 
        on_delete=CASCADE,
        related_name='comments'
    )

    parent = TreeForeignKey(
        'self', 
        on_delete=CASCADE,
        null=True, 
        blank=True,
        related_name='children'
    )

    # User who is commenting on the blog post article
    user = ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=CASCADE,
        related_name='user_comments'
    )
    
    # Content of a comment.
    content = TextField()

    # Date and Time in which Comment is written
    publish = DateTimeField(auto_now_add=True)
    
    # Users liked a particular comment
    users_liked = ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='users_liked'
    )

    # Number of likes to a particular comment
    likes = IntegerField(default=0, null=False)

    # Number of dislikes to a particular comment
    dislikes = IntegerField(default=0, null=False)

    class MPTTMeta:
        order_insertion_by = ['publish']

    def __str__(self) -> str:
        """ sting representation of Comment instance """
        return 'Comment By {self.name}'

    #===================================================================================
    def adding_users_who_liked_the_comment(self, request):
        """
        This method adds users who liked the comment in users liked field
        """
        self.users_liked.add(request.user)
        self.incrementing_number_of_likes_of_comment()

    #===================================================================================
    def incrementing_number_of_dislikes_of_comment(self):
        """
        This method increments number of dislikes of comment
        """
        self.dislikes += 1
        self.save()

    #===================================================================================
    def incrementing_number_of_likes_of_comment(self):
        """
        This method increments number of likes of comment
        """
        self.likes += 1
        self.save()

    #==================================================================================
    def get_number_of_dislikes_in_comment(self) -> int:
        """
        Returns number of dislikes in comment
        """
        return self.dislikes

    #==================================================================================
    def get_number_of_likes_in_comment(self) -> int:
        """
        Returns number of likes in comment
        """
        return self.likes

    #=================================================================================
    def update_number_of_comments_of_blog(self):
        """
        Updates number of comments of blog
        """
        self.post.number_of_comments += 1
        self.post.save()
