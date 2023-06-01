from django import template

register = template.Library()

@register.filter(name='index')
def index(data,i):
    return data[i]