# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160518_1113'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='name_of_cat',
        ),
    ]
