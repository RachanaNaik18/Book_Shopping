# Generated by Django 4.2.7 on 2023-11-26 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_book_english_book_genra_book_hindi_book_marathi_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='English',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Hindi',
        ),
        migrations.RemoveField(
            model_name='book',
            name='Marathi',
        ),
        migrations.AddField(
            model_name='book',
            name='Language',
            field=models.CharField(default=False, max_length=100),
        ),
    ]