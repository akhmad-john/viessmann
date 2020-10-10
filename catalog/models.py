from django.db import models

# Create your models here.

class Designation(models.Model):
    name = models.CharField(max_length=30)
    short_description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

class ProductGroup(models.Model):
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, verbose_name="Назначение")
    name = models.CharField(max_length=60)
    short_description = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.designation.name+" - "+self.name

class Product(models.Model):
    name = models.CharField(max_length=40)
    short_description = models.CharField(max_length=300, null=True, blank=True)
    full_description = models.TextField()
    productGroup = models.ForeignKey(ProductGroup, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class ProductParameter(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, verbose_name="Название свойства")
    measure_unit = models.CharField(max_length=15, null=True, verbose_name="Еденица измерения", blank=True)
    value = models.TextField(max_length=500, verbose_name="Значение")


    def __str__(self):
        return self.name+": "+self.value