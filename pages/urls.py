
from django.urls import path

from pages.views import HomePageView, ContactTemplateView, AboutTemplateView, ShopTemplateView


app_name = 'pages'

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('contact/', ContactTemplateView.as_view(), name='contact'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('shop/', ShopTemplateView.as_view(), name='shop'),

]
