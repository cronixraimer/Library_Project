# Generated by Django 4.2.6 on 2023-11-23 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_delete_customuser'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='ISBN',
            new_name='isbn',
        ),
    ]
