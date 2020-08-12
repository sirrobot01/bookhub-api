# Generated by Django 3.0.4 on 2020-07-24 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200718_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='shelvesmodel',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
