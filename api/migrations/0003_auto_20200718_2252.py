# Generated by Django 3.0.4 on 2020-07-18 22:52

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0002_auto_20200718_2251'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='bookmodel',
            unique_together={('user', 'name')},
        ),
    ]
