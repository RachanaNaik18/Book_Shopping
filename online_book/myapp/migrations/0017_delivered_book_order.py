# Generated by Django 4.2.7 on 2023-12-22 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0016_remove_delivered_book_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='delivered',
            name='book_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.order'),
        ),
    ]