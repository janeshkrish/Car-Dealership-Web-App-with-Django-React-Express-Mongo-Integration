# Generated by Django 5.0.3 on 2025-06-11 09:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CarMake',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CarModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Sedan', 'Sedan'), ('SUV', 'SUV'), ('Wagon', 'Wagon'), ('Truck', 'Truck')], max_length=10)),
                ('year', models.IntegerField()),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.carmake')),
            ],
        ),
    ]
