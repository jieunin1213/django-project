# Generated by Django 3.0.8 on 2020-07-17 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200717_1009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='owners',
            new_name='owner',
        ),
    ]
