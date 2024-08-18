from django.views import View
from django.shortcuts import render

from django.core.paginator import Paginator
from django.db.models import Q
from inventory.models import (
    Category,
    Product,
    ProductImage,
    ProductAttributeValue,
    ProductInventory,
    Stock,
)


class ProductsListView(View):
    """View for the home page."""
    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        p = Paginator(Product.objects.all(), 35)
        page = request.GET.get('page')
        products = p.get_page(page)
        categories = Category.objects.all()
        context = {
            'products': products,
            'categories': categories,
        }
        categories = Category.objects.all()
        query = request.POST.get('search_query')
        if 'search_query' in request.GET:
            query = request.GET.get('search_query')
            if query == '' or query == 'All Categories':
                p = Paginator(Product.objects.all(), 35)
                page = request.GET.get('page')
                products = p.get_page(page)
                context = {
                    'products': products,
                    'categories': categories,
                }
                return render(
                    request,
                    'inventory/products_list.html',
                    context
                )
            else:
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(category__name__icontains=query) |
                    Q(brand__name__icontains=query) |
                    Q(tags__name__icontains=query)
                ).distinct()
                p = Paginator(products, 35)
                page = request.GET.get('page')
                products = p.get_page(page)
                context = {
                    'products': products,
                    'categories': categories,
                }
                return render(request, 'inventory/products_list.html', context)
        return render(request, 'home/home.html', context)

class ProductDetailView(View):
    """View for the product detail page."""
    def get(self, request, *args, **kwargs):
        """Handle GET requests."""
        #product = Product.objects.get(id=kwargs['pk'])
        category = Category.objects.get(id=kwargs['pk'])
        products = Product.objects.filter(category=category)
        context = {
            'products': products,
            'category': category,
        }
        print('products Detail')
        print(products)
        print('category Detail')
        print(category)

        query = request.POST.get('search_query')
        if 'search_query' in request.GET:
            query = request.GET.get('search_query')
            if query == '' or query == 'All Categories':
                p = Paginator(Product.objects.all(), 35)
                page = request.GET.get('page')
                products = p.get_page(page)
                context = {
                    'products': products,
                    'categories': categories,
                }
                return render(
                    request,
                    'inventory/products_list.html',
                    context
                )
            else:
                products = Product.objects.filter(
                    Q(name__icontains=query) |
                    Q(description__icontains=query) |
                    Q(category__name__icontains=query) |
                    Q(brand__name__icontains=query) |
                    Q(tags__name__icontains=query)
                ).distinct()
                p = Paginator(products, 35)
                page = request.GET.get('page')
                products = p.get_page(page)
                context = {
                    'products': products,
                    'category': category,
                }
                return render(request, 'inventory/products_list.html', context)
        return render(request, 'home/category_list.html', context)

class HomeView(View):
    """View for the home page."""
    def get(self, request):
        """Return the home page."""
        return render(request, 'home/home.html')
