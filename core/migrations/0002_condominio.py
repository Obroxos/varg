# Generated by Django 4.0.4 on 2022-05-26 19:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condominio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('rut', models.CharField(blank=True, max_length=200, verbose_name='RUT')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Dirección')),
                ('comuna', models.CharField(blank=True, max_length=200, verbose_name='Comuna')),
                ('region', models.CharField(blank=True, max_length=200, verbose_name='Región')),
                ('fondo_reserva', models.CharField(blank=True, max_length=200, verbose_name='Porcentaje de Fondo de Reserva')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('administrador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Administrador')),
            ],
            options={
                'verbose_name': 'condominio',
                'verbose_name_plural': 'condominios',
                'ordering': ['-created'],
            },
        ),
    ]
