# Generated by Django 3.0 on 2019-12-12 03:51

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
