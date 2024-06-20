from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView

from products.form import SearchForm
from products.models import ProductModel, ProductCategoriesModel, ProductManufactureModel, ProductTagModel, \
    ProductColorModel, ProductSizeModel, Article
from users.models import TeamModel


class ProductListView(ListView):
    template_name = 'products/shop-list.html'
    model = ProductModel
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoriesModel.objects.all()
        context['manufactures'] = ProductManufactureModel.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        context['sizes'] = ProductSizeModel.objects.all()
        context['products'] = ProductModel.objects.all()

        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel
    context_object_name = 'products'

    def get_object(self, *args, **kwargs):
        return ProductModel.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, *, object_list=None, **kwargs):
        products = ProductModel.objects.get(id=self.kwargs['pk'])
        content = super().get_context_data(**kwargs)
        content.update({
            'categories': ProductCategoriesModel.objects.all(),
            'brand': ProductManufactureModel.objects.all(),
            'color': ProductColorModel.objects.all(),
            'tags': ProductTagModel.objects.all(),
            'product': ProductModel.objects.all(),
            'author': TeamModel.objects.all(),
            'sizes': ProductSizeModel.objects.all()
        })

        return content


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)
    else:
        cart.append(pk)
    request.session['cart'] = cart
    return redirect(request.GET.get('next', 'products:list'))


def add_or_remov(request, pk):
    wish = request.session.get('wish', [])
    if pk in wish:
        wish.remove(pk)
    else:
        wish.append(pk)
    request.session['wish'] = wish
    return redirect(request.GET.get('next', 'products:list'))


def search(request):
    query = ''
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Article.objects.filter(title__icontains=query)
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form, 'query': query, 'results': results})


class ProductCommentView(LoginRequiredMixin, CreateView):
    template_name = 'products/product-detail'