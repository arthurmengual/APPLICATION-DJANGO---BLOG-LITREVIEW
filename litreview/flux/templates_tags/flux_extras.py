from django.template import Library

register = Library()


@register.filter
def filter_posts(request):
    pass
