# Generated by Django 4.0.3 on 2022-04-16 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0005_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='snippet',
            field=models.CharField(default='click link to read.....', max_length=255),
        ),
    ]
