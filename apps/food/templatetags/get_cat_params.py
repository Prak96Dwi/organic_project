from django import template
register = template.Library()

@register.simple_tag
def get_category_parameter(request):
	return request.GET.getlist('cats')
