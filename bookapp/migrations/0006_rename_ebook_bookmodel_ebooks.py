# Generated by Django 3.2.25 on 2024-05-03 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_rename_ebooks_bookmodel_ebook'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookmodel',
            old_name='ebook',
            new_name='ebooks',
        ),
    ]
