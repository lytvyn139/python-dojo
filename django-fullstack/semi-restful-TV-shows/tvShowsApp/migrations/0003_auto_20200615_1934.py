# Generated by Django 3.0.7 on 2020-06-15 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvShowsApp', '0002_auto_20200615_1853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='description',
            new_name='desc',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='release',
            new_name='release_date',
        ),
        migrations.AlterField(
            model_name='show',
            name='network',
            field=models.CharField(max_length=150),
        ),
    ]
