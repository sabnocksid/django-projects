# Generated by Django 5.1.1 on 2024-09-28 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0004_product_created_at_product_updated_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]