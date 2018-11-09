from django import template
from django.contrib.auth.models import Group

register = template.Library()

# @register.filter(name='has_group')
# def has_group(user, group_name):
#     group =  Group.objects.get(name=group_name)
#     return group in user.groups.all()

@register.filter('has_group')
def has_group(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False
