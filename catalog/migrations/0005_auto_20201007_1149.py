# Generated by Django 3.1.2 on 2020-10-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='short_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
