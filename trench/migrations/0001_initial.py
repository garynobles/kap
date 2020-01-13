# Generated by Django 2.1.3 on 2020-01-13 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trench',
            fields=[
                ('trench_id', models.AutoField(primary_key=True, serialize=False)),
                ('trench_name', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('area_easting', models.IntegerField()),
                ('area_northing', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'trenches',
                'db_table': 'kap"."trench',
                'ordering': ['area_easting', 'area_northing'],
                'managed': False,
            },
        ),
    ]