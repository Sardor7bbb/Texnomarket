from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from pages.form import ContactModelForm
from pages.models import AboutModel, TeamModel
from products.models import ProductModel, ProductCategoriesModel


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['teams'] = TeamModel.objects.all()
        context['products'] = ProductModel.objects.all()
        context['categories'] = ProductCategoriesModel.objects.all()
        context['abouts'] = AboutModel.objects.all()
        return context


class ContactTemplateView(CreateView):
    template_name = 'contact.html'
    form_class = ContactModelForm
    success_url = '/'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ShopTemplateView(TemplateView):
    template_name = 'shop-list.html'

