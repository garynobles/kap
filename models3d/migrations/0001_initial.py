# Generated by Django 2.1.3 on 2019-02-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Models3d',
            fields=[
                ('model_id', models.AutoField(primary_key=True, serialize=False)),
                ('context_id', models.IntegerField(blank=True, null=True)),
                ('context_number_tmp', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '3D Models',
                'db_table': 'samples"."models3d',
                'managed': False,
            },
        ),
    ]
