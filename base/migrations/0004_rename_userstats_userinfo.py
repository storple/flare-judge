# Generated by Django 5.0.3 on 2024-03-10 23:25

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_userstats_delete_programmer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserStats',
            new_name='UserInfo',
        ),
    ]