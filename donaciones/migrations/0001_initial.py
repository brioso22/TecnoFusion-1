# Generated by Django 5.0.7 on 2024-08-24 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='donaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_aquipo', models.CharField(max_length=100)),
                ('donador', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
    ]
