# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0014_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechTests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('marks', models.FloatField(null=True, verbose_name='marks', blank=True)),
                ('student', models.ForeignKey(to='registration.Student')),
            ],
        ),
        migrations.RemoveField(
            model_name='test',
            name='name',
        ),
        migrations.AddField(
            model_name='techtests',
            name='test',
            field=models.ForeignKey(to='registration.Test'),
        ),
    ]
