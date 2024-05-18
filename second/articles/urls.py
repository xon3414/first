from django.urls import path
from .views import (
    SaleView,
    PurchaseView,
    StockView,
    CashView,
    PriceView,
    ProductView,
    AddProductView,
    ProductListView,
    ModelListView,
    ArticleUpdateView,
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    ArticleCommentView,
)

urlpatterns = [
    path('sales/', SaleView.as_view(), name='sales'),
    path('purchases/', PurchaseView.as_view(), name='purchases'),
    path('stock/', StockView.as_view(), name='stock'),
    path('cash/', CashView.as_view(), name='cash_register'),
    path('price/', PriceView.as_view(), name='price_list'),
    path('catalog/', ProductView.as_view(), name='product_catalog'),
    path('catalog/add', AddProductView.as_view(), name='add_product'),
    path('', ProductListView.as_view(), name='product_list'),
    path('catalog/<str:pro>', ModelListView, name='category'),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('<int:pk>/comment/', ArticleCommentView.as_view(), name="article_comment"),
]