# Generated by Django 5.1.1 on 2024-09-11 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WiSSA_App', '0002_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='header_image',
            new_name='image',
        ),
    ]