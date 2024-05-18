from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

class Client(models.Model):
    name = models.CharField(max_length=155)
    category = models.CharField(max_length=155, default='premium')
    region = models.CharField(max_length=155, default='tashkent')
    city = models.CharField(max_length=155)
    phone = models.CharField(max_length=155)
    photo = models.ImageField(upload_to='images/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('client_detail', args=[str(self.id)])
