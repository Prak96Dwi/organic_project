# apps/blog/managers.py
"""
	This modules contains some manager classes

	* class : BlogCategoryManager
	* class : BlogManager

"""
from django.db.models import Manager


class BlogCategoryManager(Manager):
    """
    food model manager class

    This class contains some methods which is used to retrieve
    objects.

    """

    def get_queryset(self):
        """
        Returns all the objects of the FoodManager class.

        """
        return super().get_queryset()

    def featured_foods(self):
        """
        Returns food products which are featured as True.

        """
        return self.get_queryset().filter(featured=True)


class BlogManager(Manager):
    """
    food model manager class

    This class contains some methods which is used to retrieve
    objects.

    """

    def get_queryset(self):
        """
        Returns all the objects of the FoodManager class.
        """
        return super().get_queryset()


    def latest_blogs(self):
        """
        Returns food products which are featured as True.
        """
        return self.get_queryset().order_by()[:3]


    def blogs_of_particular_tag(self, tags_id):
        """
        Returns blog articles which belongs to particular tag.
        """
        return self.get_queryset().filter(tags__in=list(tag_id))


    def blogs_of_particular_category(self, category, blog_id=None):
        """
        Returns blog articles which belongs to particular category.
        """
        if blog_id:
            # Returns blogs of particular category excluding one blog having
            # specific blog id
            return self.get_queryset().filter(category=category).exclude(
                id=blog_id
            )
        return self.get_queryset().filter(category=category)


    def recent_blogs_of_particular_category(self, category):
        """
        Returns recent blog articles of particular category.
        """
        return self.get_queryset().filter(category=category).order_by()[:3]


    def blogs_title_list(self):
        """
        Returns blog title list
        """
        return [blog.title for blog in self.get_queryset()]
