""" food/forms.py """
from .models import Food, FoodCategory
from django.utils.translation import gettext as _
from django.contrib.auth import authenticate
from django import forms


class FoodInsertForm(forms.ModelForm):
    categories = FoodCategory.objects.all()
    CATEGORY_CHOICES = [(category.name, category.name) for category in categories]

    name = forms.CharField(max_length=100, 
                            widget=forms.TextInput(
                            attrs={
                                'class': 'form-control'
                            }
                        )
                    )
    category = forms.CharField(widget=forms.Select(
                                choices=CATEGORY_CHOICES,
                                attrs={
                                    'class': 'form-control'
                                }
                            )
                        )
    price = forms.IntegerField(widget=forms.NumberInput(
                                attrs={
                                    'class': 'form-control'
                                }
                            )
                        )
    weight = forms.FloatField(widget=forms.NumberInput(
                            attrs={
                                'class': 'form-control'
                            }
                        )
                    )
    detail = forms.CharField(max_length=2000, 
                                widget=forms.Textarea(
                                                attrs={
                                                    'class': 'form-control'
                                                }
                                            )
                                )
    discount = forms.IntegerField(required=False,
                                widget=forms.NumberInput(
                                attrs={
                                    'class': 'form-control'
                                }
                            )
                        )
    image = forms.ImageField(required=False, 
                            widget=forms.FileInput(
                            attrs={
                                'class' : 'form-control'
                            }
                        )
                    )
    featured = forms.BooleanField(required=False, 
                                widget=forms.CheckboxInput(
                                attrs={
                                'class' : 'form-check-input'
                                }
                            )
                        )

    class Meta: # pylint: disable=too-few-public-methods
        """
        Food Insert meta class
        """
        model = Food
        fields = [
            'name', 'category', 'price', 'weight',
            'detail', 'discount', 'image', 'featured'
        ]


class FoodCategoryForm(forms.ModelForm):
    """
    Food category form class

    """
    name = forms.CharField(max_length=100, 
                            widget=forms.TextInput(
                                                attrs={
                                                    'class': 'form-control'
                                                }
                                            )
                            )

    image = forms.ImageField(widget = forms.FileInput(
                                                attrs = {
                                                'class' : 'form-control'
                                                }
                                            )
                            )

    class Meta: # pylint: disable=too-few-public-methods
        """
        Food Category Insert meta class
        """
        model = FoodCategory
        fields = '__all__'
