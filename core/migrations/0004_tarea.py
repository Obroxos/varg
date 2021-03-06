# Generated by Django 4.0.4 on 2022-05-27 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0003_alter_condominio_administrador'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tarea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nombre')),
                ('estado', models.CharField(choices=[('P', 'Pendiente'), ('C', 'Completado'), ('E', 'Eliminado'), ('A', 'Archivado')], max_length=1)),
                ('prioridad', models.CharField(choices=[('U', 'Urgente'), ('R', 'Regular')], max_length=1)),
                ('vencimiento', models.DateField()),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('asignado', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Administrador')),
                ('condominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.condominio', verbose_name='Condominio')),
            ],
            options={
                'verbose_name': 'tarea',
                'verbose_name_plural': 'tareas',
                'ordering': ['-created'],
            },
        ),
    ]
