from django import template

from izo.models import *

register = template.Library()


@register.inclusion_tag('izo/nav.html')
def show_nav():
    nav = Nav.objects.all()
    return {"nav": nav}


@register.inclusion_tag('izo/header.html')
def show_header():
    header = Nav.objects.all()
    header_contacts = Contacts.objects.filter(is_header_published=True)
    return {"header": header,
            "header_contacts": header_contacts
            }
