# Generated by Django 2.1.4 on 2020-01-22 03:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('age', models.BigIntegerField()),
                ('sex', models.CharField(max_length=254)),
                ('disability', models.CharField(max_length=254)),
                ('disab_stat', models.CharField(max_length=254)),
                ('learn_stat', models.CharField(max_length=254)),
                ('tribe', models.CharField(max_length=254)),
                ('religion', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Head',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('age', models.BigIntegerField()),
                ('sex', models.CharField(max_length=254)),
                ('disability', models.CharField(max_length=254)),
                ('disab_stat', models.CharField(max_length=254)),
                ('learn_stat', models.CharField(max_length=254)),
                ('tribe', models.CharField(max_length=254)),
                ('death_stat', models.BigIntegerField()),
                ('religion', models.CharField(max_length=254)),
                ('mar_stat', models.CharField(max_length=254)),
                ('employer', models.CharField(max_length=254)),
                ('ipm', models.BigIntegerField()),
                ('work_stat', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Population',
            fields=[
                ('join_count', models.BigIntegerField()),
                ('target_fid', models.BigIntegerField()),
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=80)),
                ('area_id', models.BigIntegerField()),
                ('area', models.FloatField()),
                ('name', models.CharField(max_length=254)),
                ('age', models.BigIntegerField()),
                ('sex', models.CharField(max_length=254)),
                ('disability', models.CharField(max_length=254)),
                ('disab_stat', models.CharField(max_length=254)),
                ('learn_stat', models.CharField(max_length=254)),
                ('tribe', models.CharField(max_length=254)),
                ('death_stat', models.CharField(max_length=254)),
                ('religion', models.CharField(max_length=254)),
                ('mar_stat', models.CharField(max_length=254)),
                ('employer', models.FloatField()),
                ('ipm', models.CharField(max_length=254)),
                ('work_stat', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Spouse',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=254)),
                ('age', models.BigIntegerField()),
                ('sex', models.CharField(max_length=254)),
                ('disability', models.CharField(max_length=254)),
                ('disab_stat', models.CharField(max_length=254)),
                ('learn_stat', models.CharField(max_length=254)),
                ('tribe', models.CharField(max_length=254)),
                ('death_stat', models.BigIntegerField()),
                ('religion', models.CharField(max_length=254)),
                ('mar_stat', models.CharField(max_length=254)),
                ('employer', models.CharField(max_length=254)),
                ('ipm', models.BigIntegerField()),
                ('work_stat', models.CharField(max_length=254)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPointField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Watuka',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=80)),
                ('area_id', models.BigIntegerField()),
                ('area', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
    ]