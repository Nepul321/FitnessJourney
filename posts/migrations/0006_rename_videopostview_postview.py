# Generated by Django 4.1.6 on 2023-02-04 21:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0005_post_view_count_post_views'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='VideoPostView',
            new_name='PostView',
        ),
    ]
