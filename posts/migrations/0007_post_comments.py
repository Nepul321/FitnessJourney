# Generated by Django 4.1.6 on 2023-02-04 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
        ('posts', '0006_rename_videopostview_postview'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comments',
            field=models.ManyToManyField(blank=True, related_name='blog_post_comments', to='comments.comment'),
        ),
    ]
