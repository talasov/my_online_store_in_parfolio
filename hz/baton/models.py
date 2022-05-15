from django.db import models
from django.urls import reverse


class Category(models.Model):
    """Модель категории товара"""
    title = models.CharField(max_length=100, verbose_name='Категория')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='url')

    def get_absolute_url(self):
        return reverse('category', kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Категория(ю)'
        verbose_name_plural = 'Категории'


class Product(models.Model):
    """Модель продукта"""
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='url')
    photo = models.ImageField(verbose_name='Добавить изобращение', blank=True, upload_to='photos/%Y/%m/%d/')
    content = models.TextField(verbose_name='Описание товара',)
    price = models.DecimalField(verbose_name='Стоимость товара', max_digits=10, decimal_places=2)
    structure = models.TextField(verbose_name='Состав')
    value = models.TextField(verbose_name='Пищевая ценность')
    storage = models.CharField(max_length=300, verbose_name='Условия хранения')
    availability = models.BooleanField(default=True, verbose_name='В наличии')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='products', verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('product', args=[self.pk, self.slug])
