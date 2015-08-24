# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_blog_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='posts',
            new_name='Post',
        ),
    ]
