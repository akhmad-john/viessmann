from django.contrib import admin
from .models import *
from django import forms
# Register your models here.



class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')


class ProductParameterInline(admin.TabularInline):
    model = ProductParameter


class ProductAdmin(admin.ModelAdmin):
    fields = ('productGroup', 'name', 'short_description', 'full_description', )
    inlines = [ProductParameterInline]



admin.site.register(Designation)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductParameter)