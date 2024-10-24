# Generated by Django 5.1.1 on 2024-10-20 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_alter_order_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='shipment_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Shipped', 'Shipped'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Pending', max_length=20),
        ),
    ]
