from django.shortcuts import render
from django.views import View
from products_module.models import Products, Category


# Create your views here.
class ProductsListView(View):
    def get(self, request):
        context = {
            'products': Products.objects.all()
        }
        return render(request, 'products_module/products-list.html', context)


class CategoryListView(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'products_module/category-list.html', context)
