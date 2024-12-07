# Generated by Django 4.2.16 on 2024-12-07 15:19

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEmpresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('precio_sin_iva', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('mostrar', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
            ],
            options={
                'verbose_name': 'Plan',
                'verbose_name_plural': 'Planes',
                'ordering': ('-created',),
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Identificador de empresa')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Última Actualización')),
                ('nombre', models.CharField(max_length=80, unique=True, verbose_name='Nombre')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Correo electronico')),
                ('direccion', models.TextField(blank=True, max_length=100, verbose_name='Direccion')),
                ('telefono', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Ingrese solo números.', regex='^\\d+$')], verbose_name='Teléfono')),
                ('detalles', models.TextField(blank=True, verbose_name='Detalles')),
                ('estado', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Activo'), (2, 'Suspendido'), (3, 'Cancelado')], default=1, verbose_name='Estado')),
                ('is_active', models.BooleanField(default=True, verbose_name='Estado activo?')),
                ('fecha_contratacion', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de contratación')),
                ('fecha_suspension', models.DateTimeField(blank=True, null=True, verbose_name='Fecha de suspension')),
                ('nombre_facturacion', models.CharField(blank=True, max_length=255, verbose_name='Nombre de facturación')),
                ('rfc', models.CharField(blank=True, max_length=30, verbose_name='RFC/RUC')),
                ('regimen_fiscal', models.CharField(blank=True, max_length=10, null=True, verbose_name='Regimen fiscal')),
                ('codigo_postal', models.CharField(blank=True, max_length=50, verbose_name='Codigo postal')),
                ('direccion_facturacion', models.TextField(blank=True, max_length=100, verbose_name='Dirección de facturación')),
                ('email_facturacion', models.EmailField(blank=True, max_length=254, verbose_name='Email de facturación')),
                ('timezone', models.CharField(default='Etc/UTC', max_length=190)),
                ('external_id', models.PositiveIntegerField(blank=True, db_index=True, null=True, verbose_name='Id externo del lote al que pertenece')),
                ('plan', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='empresa_plan_empresa', to='system.planempresa')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'permissions': {('crear_superusuarios', 'Crear super usuarios'), ('acciones_lista_empresas', 'Acciones lista de empresas'), ('eliminar_superusuarios', 'Eliminar super usuarios'), ('ver_perfil_financiero', 'Ver perfil financiero'), ('lista_empresas', 'Lista de empresas')},
            },
        ),
    ]