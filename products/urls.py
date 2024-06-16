from django.urls import path

from products.views import ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail'),
]
