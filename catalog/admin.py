from django.contrib import admin
from .models import *
from django import forms
# Register your models here.



class ProductGroupAdmin(admin.ModelAdmin):
    list_display = ('name', 'designation')


# class ProductParameterForm(forms.ModelForm):
#     measure_unit = forms.CharField()
#
#     def save(self, commit=True):
#         measure_unit = self.cleaned_data.get('measure_unit', None)
#
#         return super(ProductParameterForm, self).save(commit=commit)
#
#
#     class Meta:
#         model = ProductParameter
#         fields = "__all__"

class ProductParameterAdmin(admin.TabularInline):
    model = ProductParameter


class ProductAdmin(admin.ModelAdmin):
    fields = ('productGroup', 'name', 'short_description', 'full_description', )
    inlines = [ProductParameterAdmin]

    # fieldsets = (
    #     (None, {
    #        'fields': ('productGroup', 'name', 'short_description', 'full_description', 'measure_unit')
    #     }),
    # )


admin.site.register(Designation)
admin.site.register(ProductGroup, ProductGroupAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductParameter)