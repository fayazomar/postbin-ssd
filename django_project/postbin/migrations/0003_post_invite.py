# Generated by Django 2.1.7 on 2019-03-14 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('postbin', '0002_post_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='invite',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
