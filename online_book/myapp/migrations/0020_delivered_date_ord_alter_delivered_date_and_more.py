# Generated by Django 4.2.7 on 2023-12-24 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_delivered_date_delivered_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='date_ord',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='delivered',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='delivered',
            name='quantity',
            field=models.PositiveIntegerField(null=True),
        ),
    ]