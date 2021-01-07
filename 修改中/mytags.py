from django import template

register = template.library()

@register.simple_tag  #装饰器，加到django中
def add(v1,v2):
    return v1+v2