from operator import concat
from django.shortcuts import render, get_object_or_404
from izo.models import *


def index(request):
    
    context = {
        'title': 'izo studio',
        'services': Services.objects.filter(cat_id=1),
        'services_title': Category.objects.get(id=1),
        'souvenirs_title': Category.objects.get(id=2),
        'souvenirs': Services.objects.filter(cat_id=2),
        'posts': Post.objects.filter(is_published=True),
        'main_link': Nav.objects.get(id=1),
        'prices': Prices.objects.all(),
        'contacts': Contacts.objects.all(),
        'extra': Extra.objects.all(),
        'posts': Post.objects.all(),
        'logo':Nav.objects.get(title = 'логотип'),
        'anchor':Nav.objects.get(title = 'ссылка на контакты'),
    }
    return render(request, 'izo/index.html', context=context)
