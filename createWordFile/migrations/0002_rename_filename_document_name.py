# Generated by Django 3.2 on 2021-05-29 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('createWordFile', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='document',
            old_name='fileName',
            new_name='name',
        ),
    ]
