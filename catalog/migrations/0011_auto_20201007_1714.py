# Generated by Django 3.1.2 on 2020-10-07 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20201007_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
