# Generated by Django 3.1.2 on 2020-10-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_auto_20201007_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='designation',
            name='short_description',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='productgroup',
            name='short_description',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
