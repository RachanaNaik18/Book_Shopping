# Generated by Django 4.2.7 on 2023-12-22 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_order_quantity_delivered'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='order_id_no',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]
