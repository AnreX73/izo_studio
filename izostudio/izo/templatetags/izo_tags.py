from django import template

from izo.models import *

register = template.Library()


@register.inclusion_tag('izo/nav.html')
def show_nav():
    nav = Nav.objects.all()
    return {"nav": nav}


@register.filter
def dark_icon(url):
    """Возвращает путь к версии иконки для тёмной темы (суффикс _d)."""
    if not url:
        return url
    name, dot, ext = url.rpartition('.')
    if not dot:
        return url + '_d'
    if name.endswith('_d'):
        return url
    return f'{name}_d.{ext}'


@register.inclusion_tag('izo/header.html')
def show_header():
    header = Nav.objects.all()
    header_contacts = Contacts.objects.filter(is_header_published=True)
    return {"header": header,
            "header_contacts": header_contacts
            }
