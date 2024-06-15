from django.shortcuts import render
from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ShopTemplateView(TemplateView):
    template_name = 'shop-list.html'

