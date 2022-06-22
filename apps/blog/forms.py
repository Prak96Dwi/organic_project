""" apps/blog/forms.py """
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from django.conf import settings

from .models import BlogCategory, Blog


class BlogForm(forms.ModelForm):
	"""
	Blog form class
	"""
	blog_categories = BlogCategory.objects.all()
	CATEGORY_CHOICES = [(blog_category.name, blog_category.name) \
							for blog_category in blog_categories]

	title = forms.CharField(
							max_length=100, 
							widget = forms.TextInput(
												attrs={
													'class': 'form-control'
												}
											)
							)

	category = forms.CharField(widget=forms.Select(
												choices=CATEGORY_CHOICES,
												attrs = {
													'class': 'form-control'
												}
											)
							)

	image = forms.ImageField(required=False,
							widget=forms.FileInput(
											attrs = {
											'class' : 'form-control'
											}
										)
							)

	body = forms.CharField(
				widget=SummernoteWidget(
				attrs={
					'summernote': {
						'width': settings.BLOG_INBOX_WIDTH,
						'height': settings.BLOG_INBOX_HEIGHT
					}
				}
			)
		)

	class Meta:
		"""
		Blog meta class
		"""
		model = Blog
		fields = ['title', 'category', 'image', 'body']


class BlogCategoryForm(forms.ModelForm):
	"""
	blog category form
	"""
	name = forms.CharField(max_length=100,
							widget=forms.TextInput(
												attrs = {
													'class': 'form-control'
												}
											)
							)

	class Meta:
		"""
		Blog category meta class
		"""
		model = BlogCategory
		fields = ['name']
