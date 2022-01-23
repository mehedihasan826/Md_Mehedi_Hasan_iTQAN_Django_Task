from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Category, Product


class CategoryListView(ListView):
    model = Category
    template_name = 'home.html'
    context_object_name = 'category'


def CategoryDetailsView(request, pk):
    details = Product.objects.filter(group=pk)
    return render(request, 'product_list.html', {'pk': pk, 'details': details})


class ProductDetailsView(DetailView):
    model = Product
    template_name = 'details.html'
    context_object_name = 'products'


class SliderView(ListView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'slider'
