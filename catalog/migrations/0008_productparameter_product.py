# Generated by Django 3.1.2 on 2020-10-07 07:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20201007_1227'),
    ]

    operations = [
        migrations.AddField(
            model_name='productparameter',
            name='product',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='catalog.product'),
            preserve_default=False,
        ),
    ]