# Generated by Django 4.2.4 on 2023-08-18 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_tag_alter_post_author_alter_post_slug_post_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='image_name',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]
