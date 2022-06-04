# Generated by Django 4.0.4 on 2022-05-12 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divice_name', models.CharField(max_length=250)),
                ('secret', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Machines',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('machine_name', models.CharField(max_length=250)),
                ('buy_date', models.DateField(auto_now_add=True, verbose_name='fecha de compra')),
                ('marca', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Dots',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('units', models.CharField(max_length=250)),
                ('devices', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_api.devices')),
            ],
        ),
        migrations.AddField(
            model_name='devices',
            name='machines',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='test_api.machines'),
        ),
    ]
