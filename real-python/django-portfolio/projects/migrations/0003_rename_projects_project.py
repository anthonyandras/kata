# Generated by Django 4.2.7 on 2023-11-08 14:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projects_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Projects',
            new_name='Project',
        ),
    ]