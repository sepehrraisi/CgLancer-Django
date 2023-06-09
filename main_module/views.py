from django.shortcuts import render
from django.views import View
from products_module.models import Category, Products

# Create your views here.
class HomeView(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all(),
            'products': Products.objects.all()
        }
        return render(request, "main_module/home.html", context)
