# Generated by Django 2.1.3 on 2019-04-16 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depot', '0004_friend_container_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='container_id',
        ),
    ]