# Generated by Django 4.1.3 on 2023-02-24 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('labs', '0013_lab_lab_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='associated_users',
        ),
    ]