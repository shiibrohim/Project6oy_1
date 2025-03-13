from itertools import product
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm
from .models import Product
from django.core.paginator import Paginator

from django.views.generic import ListView, DeleteView, UpdateView, DetailView, CreateView, CreateView
from django.urls import reverse_lazy
from django.views import View

# Create your views here.

def home(request):
    return render(request, 'home.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def contact_list(request):
    return render(request, 'contact_list.html')



class ProductListView(View):
    def get(self, request):
        t = request.GET.get('t', '')
        products = Product.objects.filter(name__icontains=t) if t else Product.objects.all()

        paginator = Paginator(products, 6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, 'list.html', {'page_obj': page_obj, 't': t})



class ProductDetailView(DetailView):
    model = Product
    template_name = 'details.html'


# class ProductUpdateView(View):
#     def get(self, request, pk):
#         products = Product.objects.get(pk=pk)
#         form = ProductForm(instance=products)
#         return render(request, 'update.html', {'form': form})
#     def post(self, request, pk):
#         products = Product.objects.get(pk=pk)
#         form = ProductForm(request.POST, request.FILES, instance=products)
#         if form.is_valid():
#             form.save()
#             return redirect('list')


class ProductUpdateView(View):
    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(instance=product)
        return render(request, 'update.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('list')  # Bu yerda to‘g‘ri URL name qo‘ying
        return render(request, 'update.html', {'form': form})



class ProductDeleteView(View):
    def get(self, request, pk):
        products = Product.objects.get(pk=pk)
        return render(request, 'delete.html', {'products': products})
    def post(self, request, pk):
        products = Product.objects.get(pk=pk)
        products.delete()
        return redirect('list')



class ProductCreateView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, 'create.html', {'form': form})
    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
        return render(request, 'create.html', {'form': form})


