# Generated by Django 3.1.2 on 2020-10-07 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='designation',
            name='short_description',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
    ]