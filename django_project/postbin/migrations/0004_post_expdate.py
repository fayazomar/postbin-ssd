# Generated by Django 2.1.7 on 2019-03-15 19:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postbin', '0003_post_invite'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='expdate',
            field=models.DateField(default=datetime.date.today, verbose_name='Date'),
        ),
    ]
