# Generated by Django 4.1.3 on 2022-12-11 00:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsstory_options_alter_newsstory_story_image'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsstory',
            options={'ordering': ['-pub_date']},
        ),
    ]
