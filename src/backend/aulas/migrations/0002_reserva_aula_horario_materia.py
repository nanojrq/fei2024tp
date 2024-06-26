# Generated by Django 5.0.6 on 2024-05-28 02:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aulas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserva_Aula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_desde', models.DateTimeField()),
                ('fh_hasta', models.DateTimeField()),
                ('observacion', models.TextField(max_length=256)),
                ('id_aula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.aula')),
            ],
        ),
        migrations.CreateModel(
            name='Horario_Materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fh_desde', models.DateTimeField()),
                ('fh_hasta', models.DateTimeField()),
                ('id_materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.materia')),
                ('id_reserva', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas.reserva_aula')),
            ],
        ),
    ]
