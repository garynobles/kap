# Generated by Django 2.1.3 on 2019-03-02 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Composition',
            fields=[
                ('composition_id', models.AutoField(primary_key=True, serialize=False)),
                ('material_type', models.CharField(default='', max_length=50)),
                ('type_count', models.DecimalField(decimal_places=4, max_digits=15)),
                ('whole_weight', models.DecimalField(decimal_places=4, max_digits=15)),
                ('fragment_weight', models.DecimalField(decimal_places=4, max_digits=15)),
            ],
            options={
                'verbose_name_plural': 'Composition',
                'db_table': 'kap"."composition',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flotation',
            fields=[
                ('flotation_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_easting', models.IntegerField(choices=[('', 'Area Easting'), (99, 99), (108, 108), (109, 109), (81, 81), (84, 84), (93, 93), (95, 95), (97, 97), (98, 98), (987, 987)])),
                ('area_northing', models.IntegerField(choices=[('', 'Area Northing'), (523, 523), (526, 526), (551, 551), (536, 536), (545, 545), (555, 555), (541, 541), (531, 531), (987, 987)])),
                ('context_number', models.IntegerField(blank=True, null=True)),
                ('sample_number', models.IntegerField(blank=True, null=True)),
                ('flotation_date', models.DateTimeField()),
                ('entry_date', models.DateTimeField()),
                ('notes', models.CharField(blank=True, default='', max_length=600, null=True)),
            ],
            options={
                'verbose_name_plural': 'Flotation',
                'db_table': 'kap"."flotation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Fraction',
            fields=[
                ('fraction_id', models.AutoField(primary_key=True, serialize=False)),
                ('fraction', models.CharField(max_length=20)),
                ('whole_count', models.DecimalField(decimal_places=3, max_digits=10)),
                ('weight_whole', models.DecimalField(decimal_places=3, max_digits=10)),
                ('weight_fragment', models.DecimalField(decimal_places=3, max_digits=10)),
                ('fragment_count', models.DecimalField(decimal_places=3, max_digits=10)),
                ('seed', models.BooleanField()),
                ('plant_part', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Fraction',
                'db_table': 'kap"."fraction',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LightResidue',
            fields=[
                ('lightresidue_id', models.AutoField(primary_key=True, serialize=False)),
                ('proportion_analysed', models.DecimalField(decimal_places=3, max_digits=5)),
                ('soil_volume', models.DecimalField(decimal_places=4, max_digits=15)),
                ('sample_volume', models.DecimalField(decimal_places=4, max_digits=15)),
                ('sample_weight', models.DecimalField(decimal_places=4, max_digits=15)),
                ('sediment', models.BooleanField()),
                ('stone', models.BooleanField()),
                ('roots', models.BooleanField()),
                ('leaves', models.BooleanField()),
                ('insect_parts', models.BooleanField()),
                ('charred_dung', models.BooleanField()),
                ('bone', models.BooleanField()),
                ('shell', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'LightResidue',
                'db_table': 'kap"."lightresidue',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PlantPart',
            fields=[
                ('plantpart_id', models.AutoField(primary_key=True, serialize=False)),
                ('plant_part', models.CharField(max_length=50)),
                ('part_count', models.DecimalField(decimal_places=3, max_digits=10)),
                ('part_weight', models.DecimalField(decimal_places=3, max_digits=10)),
            ],
            options={
                'verbose_name_plural': 'plant parts',
                'db_table': 'kap"."plantpart',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('sample_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_easting', models.IntegerField(choices=[('', 'Area Easting'), (99, 99), (108, 108), (109, 109), (81, 81), (84, 84), (93, 93), (95, 95), (97, 97), (98, 98), (987, 987)])),
                ('area_northing', models.IntegerField(choices=[('', 'Area Northing'), (523, 523), (526, 526), (551, 551), (536, 536), (545, 545), (555, 555), (541, 541), (531, 531), (987, 987)])),
                ('context_number', models.IntegerField()),
                ('sample_number', models.IntegerField()),
                ('sample_type', models.CharField(blank=True, choices=[('', 'Material'), ('Botanical', 'Botanical'), ('Ceramic', 'Ceramic'), ('Organic', 'Organic')], default='', max_length=200, null=True)),
                ('weight', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.CharField(blank=True, default='', max_length=500, null=True)),
                ('recovery_method', models.CharField(blank=True, choices=[('', 'Recovery Method'), ('Hand', 'Hand')], default='', max_length=200, null=True)),
                ('comments', models.CharField(blank=True, default='', max_length=1000, null=True)),
            ],
            options={
                'db_table': 'kap"."sample',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('author_name', models.CharField(max_length=100)),
            ],
        ),
    ]
