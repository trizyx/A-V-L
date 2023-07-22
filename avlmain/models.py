from django.db import models

# Create your models here.
from django.urls import reverse


class Items(models.Model):
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name = models.TextField(blank=False, verbose_name='NAME')
    image = models.ImageField(upload_to="photos/%Y/%m/&d/")
    price = models.CharField(max_length=30)
    key = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='get_category')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'
        ordering = ['price', 'name']


class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Category')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'key_slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        ordering = ['id']

class User(models.Model):
    time = models.DateTimeField(auto_now_add=True, verbose_name='Creation time')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    name = models.TextField(blank=False, verbose_name='NAME')
    adress = models.CharField(max_length=255)
    orders = models.CharField(max_length=255)
    order_details = models.ImageField(upload_to="photos/%Y/%m/&d/")
    key = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, related_name='get_gender')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Clothes'
        verbose_name_plural = 'Clothes'
        ordering = ['time', 'name']

