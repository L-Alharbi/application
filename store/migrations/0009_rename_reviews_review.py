# Generated by Django 5.0.6 on 2024-07-22 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_reviews'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='reviews',
            new_name='Review',
        ),
    ]