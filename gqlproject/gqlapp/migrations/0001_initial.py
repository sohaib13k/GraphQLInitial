# Generated by Django 3.0.5 on 2021-03-16 17:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('segment', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('product', models.CharField(max_length=255)),
                ('units', models.IntegerField()),
                ('sales', models.IntegerField()),
                ('date_sold', models.DateTimeField(default=django.utils.timezone.now, null=True)),
            ],
        ),
    ]