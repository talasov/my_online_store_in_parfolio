from django.contrib import admin
from .models import *
from django import forms
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ProductAdminForm(forms.ModelForm):
    content = forms.CharField(label='Описание товара', widget=CKEditorUploadingWidget())
    structure = forms.CharField(label='Состав', widget=CKEditorUploadingWidget())
    value = forms.CharField(label='пищевая ценность', widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ('title',)}
    form = ProductAdminForm
    list_display = ('id', 'title', 'category', 'get_photo', 'price', 'availability')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'category')
    list_filter = ('category', 'availability')
    readonly_fields = ('get_photo',)
    fields = ('title', 'slug', 'price', 'content', 'structure', 'value', 'storage', 'photo', 'get_photo', 'category', 'availability')
    list_editable = ('availability',)

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src = "{obj.photo.url}" width ="50">')
        return 'фото не опубликовано'

    get_photo.short_description = 'Фото'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
