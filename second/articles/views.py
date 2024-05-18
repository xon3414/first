#from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.template.defaultfilters import slugify

from .models import Article, Comment, Product
from .forms import ArticleForm, ArticleUpdateForm
from clients.models import Client

x = Client.objects.all()

class SaleView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'sales.html'

class PurchaseView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'purchases.html'

class StockView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'stock.html'

class CashView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'cash_register.html'

class PriceView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'price_list.html'

class ProductView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'catalog.html'

class AddProductView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ('name',)
    template_name = 'add_product.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser

    success_url = reverse_lazy('product_catalog')

class ProductListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'

def ModelListView(request, pro):
    category_posts = Article.objects.filter(product=pro)
    return render(request, 'model_list.html', {'pro':pro, 'category_posts':category_posts,})


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    form_class = ArticleUpdateForm
    template_name = 'article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('product_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    #user superuser ekanini tekshirish
    def test_func(self):
        return self.request.user.is_superuser


class ArticleCommentView(LoginRequiredMixin, CreateView):
    model = Comment
    fields = ('comment',)
    template_name = 'article_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.article_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('product_list')
