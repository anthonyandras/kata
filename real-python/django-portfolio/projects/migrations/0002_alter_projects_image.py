# Generated by Django 4.2.7 on 2023-11-08 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.FilePathField(path='/projects/img'),
        ),
    ]
