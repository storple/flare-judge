# Generated by Django 5.0.3 on 2024-04-21 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [('learn', '0002_remove_guide_safe_guide_name_and_more'), ('learn', '0003_guide_in_main_page_page_in_main_page'), ('learn', '0004_rename_page_url_name_guide_safe_url_name_and_more'), ('learn', '0005_rename_safe_url_name_guide_url_name_and_more')]

    dependencies = [
        ('learn', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='guide',
            name='safe_guide_name',
        ),
        migrations.RemoveField(
            model_name='page',
            name='safe_page_name',
        ),
        migrations.AddField(
            model_name='guide',
            name='short_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='guide',
            name='visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='html_template_name',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='page',
            name='visible',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='guide',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='guide',
            name='in_main_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='page',
            name='in_main_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='guide',
            name='url_name',
            field=models.SlugField(default=models.CharField(default='', max_length=200), max_length=200),
        ),
        migrations.AddField(
            model_name='page',
            name='url_name',
            field=models.SlugField(default=models.CharField(default='', max_length=200), max_length=200),
        ),
    ]
