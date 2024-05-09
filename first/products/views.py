#from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Product

class ProductCatalogView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog.html'

class AddProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ('name', 'author',)
    template_name = 'add_product.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser
