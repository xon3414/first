from django.contrib import admin
from .models import Article, Comment, Product

class CommentInLine(admin.TabularInline):
    model = Comment
    extra = 0

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInLine]

class ProductAdmin(admin.ModelAdmin):
    model = Product

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
admin.site.register(Product, ProductAdmin)

# Register your models here.
