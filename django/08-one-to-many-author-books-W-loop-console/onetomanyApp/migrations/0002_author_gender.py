# Generated by Django 3.0.7 on 2020-06-12 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onetomanyApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='gender',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
