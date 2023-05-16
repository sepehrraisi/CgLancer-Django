from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from products_module.models import Products, Category
from account_module.mixins import JustSuperUser
from django.urls import reverse


# Create your views here.
class ProductsListView(View):
    def get(self, request):
        context = {
            'products': Products.objects.all()
        }
        return render(request, 'products_module/products-list.html', context)

class ProductManagerView(JustSuperUser, View):
    def get(self, request):
        context = {
            'products': Products.objects.all()
        }
        return render(request, 'products_module/products-manager.html', context)

class ProductEditView(JustSuperUser, View):
    def get(self, request, pk):
        user: User = get_object_or_404(User, pk=pk, is_superuser=False)
        # user_init = {
        #     "full_name": user.full_name,
        #     "email": user.email,
        #     "national_code": user.national_code,
        #     "avatar": user.avatar,
        #     "birthday_date": user.birthday_date,
        # }
        form = UserEditForm(instance=user)
        context = {
            "user": user,
            "form": form,
        }
        return render(request, "account_module/user-edit.html", context)

    def post(self, request, pk):
        user = get_object_or_404(User, pk=pk, is_superuser=False)
        form = UserEditForm(request.POST, request.FILES, instance=user)
        print("valid")
        if form.is_valid():
            form.save()
            return redirect(reverse("user_list_view"))
        context = {
            "user": user,
            "form": form,
        }
        return render(request, "account_module/user-edit.html", context)


class CategoryListView(View):
    def get(self, request):
        context = {
            'categories': Category.objects.all()
        }
        return render(request, 'products_module/category-list.html', context)
