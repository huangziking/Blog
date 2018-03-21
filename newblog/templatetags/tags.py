from ..models import Post,Category
from django import template
from collections import Counter

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-creat_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('creat_time','month',order='DESC')

@register.simple_tag
def get_categories():
    return Category.objects.all()

@register.simple_tag
def get_categories_list():
    return Category.object.annotate(num_posts=Counter('post')).filter(num_posts_gt=0)

