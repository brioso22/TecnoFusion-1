# Generated by Django 5.0.7 on 2024-08-27 02:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelo',
            old_name='modelo',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='departamento',
            name='departamento',
        ),
        migrations.AddField(
            model_name='empleado',
            name='departamento',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='inicio.departamento'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='sucursal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='empleados', to='inicio.sucursal'),
        ),
        migrations.AddField(
            model_name='modelo',
            name='marca',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='modelos', to='inicio.marca'),
            preserve_default=False,
        ),
    ]
