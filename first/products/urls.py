from django.urls import path
from .views import (
    ProductCatalogView,
    AddProductView
)

urlpatterns = [
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name="article_edit"),
    path('<int:pk>/', ArticleDetailView.as_view(), name="article_detail"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name="article_delete"),
    path('<int:pk>/comment/', ArticleCommentView.as_view(), name="article_comment"),
    path('new/', ArticleCreateView.as_view(), name="article_new"),
    path('', ArticleListView.as_view(), name='article_list'),
    path('catalog/', ProductCatalogView.as_view(), name='product_catalog'),
    path('catalog/add', AddProductView.as_view(), name='add_product')
]