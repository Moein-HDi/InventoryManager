from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from .models import *

class HomePageView(LoginRequiredMixin ,TemplateView):
    template_name = 'home.html'


#-------------------ADMIN VIEWS-------------------


#Categories

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    template_name = 'category.html'


class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    template_name = 'category_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('category')


class CategoryDeleteView(LoginRequiredMixin, DeleteView): 
    model = Category 
    template_name = 'category_delete.html' 
    success_url = reverse_lazy('category')


#Product

class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'Product.html'


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    template_name = 'product_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('product')


class ProductDeleteView(LoginRequiredMixin, DeleteView): 
    model = Product 
    template_name = 'product_delete.html' 
    success_url = reverse_lazy('product')


#City

class CityListView(LoginRequiredMixin, ListView):
    model = City
    template_name = 'city.html'


class CityCreateView(LoginRequiredMixin, CreateView):
    model = City
    template_name = 'city_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('city')


class CityDeleteView(LoginRequiredMixin, DeleteView): 
    model = City 
    template_name = 'city_delete.html' 
    success_url = reverse_lazy('city')

#Inventory

class InventoryListView(LoginRequiredMixin, ListView):
    model = Inventory
    template_name = 'inventory.html'


class InventoryCreateView(LoginRequiredMixin, CreateView):
    model = Inventory
    template_name = 'inventory_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('inventory')


class InventoryDeleteView(LoginRequiredMixin, DeleteView): 
    model = Inventory 
    template_name = 'inventory_delete.html' 
    success_url = reverse_lazy('inventory')

#InventoryProduct

class InventoryProductListView(LoginRequiredMixin, ListView):
    model = InventoryProduct
    template_name = 'inventoryProduct.html'


class InventoryProductCreateView(LoginRequiredMixin, CreateView):
    model = InventoryProduct
    template_name = 'inventoryProduct_new.html' 
    fields = "__all__"
    success_url = reverse_lazy('inventoryProduct')


class InventoryProductDeleteView(LoginRequiredMixin, DeleteView): 
    model = InventoryProduct 
    template_name = 'inventoryProduct_delete.html' 
    success_url = reverse_lazy('inventoryProduct')

#Order

class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    template_name = 'order.html'


class OrderUpdateView(LoginRequiredMixin, UpdateView):
    model = Order
    template_name = 'order_update.html' 
    fields = "__all__"
    success_url = reverse_lazy('order')


class OrderDeleteView(LoginRequiredMixin, DeleteView): 
    model = Order 
    template_name = 'order_delete.html' 
    success_url = reverse_lazy('order')


#---------------------------------------------------------


class UserProductListView(LoginRequiredMixin, ListView):
    model = InventoryProduct
    template_name= 'home.html'
    
    def get_queryset(self):
        return InventoryProduct.objects.filter(inventory__city=self.request.user.city)
    

