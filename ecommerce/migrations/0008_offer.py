# Generated by Django 5.1.1 on 2024-09-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0007_cart_cartitem_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title or description of the offer', max_length=255)),
                ('banner', models.ImageField(help_text='Upload banner image (PNG recommended)', upload_to='offers/')),
                ('start_date', models.DateTimeField(blank=True, help_text='Offer start date', null=True)),
                ('end_date', models.DateTimeField(blank=True, help_text='Offer end date', null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Check if the offer is active')),
            ],
        ),
    ]
