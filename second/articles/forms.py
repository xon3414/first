from django import forms
from .models import Article, Product
from django.template.defaultfilters import slugify

#choices = [('coding', 'coding'), ('sport', 'sport'), ('name', 'name'),]
choices = Product.objects.all().values_list('name', 'name')
choice_list = []
for item in choices:
    choice_list.append(item)

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'product', 'summary', 'body', 'photo',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})

        }
        template_name = 'article_new.html'

class ArticleUpdateForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'product', 'summary', 'body', 'photo',)
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'product': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            'summary': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'})

        }
        template_name = 'article_edit.html'