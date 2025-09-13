from django.urls import path

from izo.views import *

urlpatterns = [
    path('', index, name='home'),
    # path('services/', services, name='services'),
    # path('souvenirs/', souvenirs, name='souvenirs'),
    # path('contacts/', contacts, name='contacts'),
    # path('show_service/<slug:service_slug>', show_service, name='show_service'),

 ]