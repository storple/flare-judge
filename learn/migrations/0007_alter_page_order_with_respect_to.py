# Generated by Django 5.0.4 on 2024-07-03 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_page_toc'),
    ]

    operations = [
        migrations.AlterOrderWithRespectTo(
            name='page',
            order_with_respect_to='guide',
        ),
    ]