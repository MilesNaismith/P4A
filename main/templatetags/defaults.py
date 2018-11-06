from django import template

register = template.Library()

@register.simple_tag(takes_context=True)
def anchor(context, name):
    if context.request.get_full_path() != '/':
        name = '../{}'.format(name)
    return name    