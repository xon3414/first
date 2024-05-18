from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.defaultfilters import slugify

from .models import Client


class ClientView(LoginRequiredMixin, ListView):
    model = Client
    template_name = 'client_list.html'

class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'client/client_detail.html'

class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    fields = ('name', 'category', 'region', 'city', 'phone',)
    template_name = 'client/client_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    template_name = 'client/client_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ClientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Client
    fields = ('name', 'category', 'region', 'city', 'phone',)
    template_name = 'client/client_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

