from django import template

register = template.Library()

@register.filter
def aaa(x,y):
    return int(x)*2+int(y)

