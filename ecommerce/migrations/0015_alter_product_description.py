# Generated by Django 5.1.1 on 2024-10-14 10:58

import django_summernote.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0014_alter_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=django_summernote.fields.SummernoteTextField(),
        ),
    ]