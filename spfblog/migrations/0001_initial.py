# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('headline', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'Publication date')),
            ],
            options={
                'ordering': ('-pub_date',),
                'db_table': 'blog_entries',
                'verbose_name_plural': 'entries',
                'get_latest_by': 'pub_date',
            },
        ),
    ]
