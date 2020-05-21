from django import template
from video.models import User

register = template.Library()

@register.simple_tag
def get_custom_tag_fn():

    return User.objects.filter(pk__in=[1, 3])
