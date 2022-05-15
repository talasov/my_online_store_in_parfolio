from django import template
from django.db.models import Count

from baton.models import Category

register = template.Library()


# @register.simple_tag()
# def get_categories():
#     return Category.objects.annotate(one=Count('products')).filter(one__gt=0)


@register.inclusion_tag('baton/shop_tpl.html')
def show_menu(menu_class='menu'):
    categories = Category.objects.annotate(one=Count('products')).filter(one__gt=0)
    return {'categories': categories,
            'menu_class': menu_class}


