# Generated by Django 4.1.3 on 2022-12-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_story_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={},
        ),
        migrations.AlterField(
            model_name='newsstory',
            name='story_image',
            field=models.URLField(default='https://via.placeholder.com/150', max_length=500),
        ),
    ]
