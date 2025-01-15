from django import template

register = template.Library()

# A custom filter to add a media path prefix to image paths in templates
@register.filter()
def media_filter(path):
    if path:
        return f'/media/{path}'
    else:
        return '#'