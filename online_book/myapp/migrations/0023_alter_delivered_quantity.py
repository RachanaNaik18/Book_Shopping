# Generated by Django 4.2.7 on 2024-01-03 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_delivered_cur_add'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivered',
            name='quantity',
            field=models.PositiveIntegerField(default=1, null=True),
        ),
    ]
