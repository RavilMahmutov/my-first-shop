# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_of_cat',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='good',
            name='category',
            field=models.ForeignKey(to='blog.Category', related_name='goods'),
        ),
    ]
