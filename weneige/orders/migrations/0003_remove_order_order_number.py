# Generated by Django 4.0.5 on 2022-06-23 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_orderstatus_order_address_order_mobile_number_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_number',
        ),
    ]
