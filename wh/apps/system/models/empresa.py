# python imports
import uuid
# django imports
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class Empresa(models.Model):

    class EstadoEmpresa(models.IntegerChoices):
        ACTIVO = 1, 'Activo'
        SUSPENDIDO = 2, 'Suspendido'
        CANCELADO = 3, 'Cancelado'

    uuid = models.UUIDField(
        verbose_name=_('Identificador de empresa'),
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Fecha de registro'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Última Actualización'),
        auto_now=True,
    )
    nombre = models.CharField(
        verbose_name=_('Nombre'),
        max_length=80,
        unique=True,
    )
    email = models.EmailField(
        verbose_name=_('Correo electronico'),
        blank=True,
    )
    direccion = models.TextField(
        verbose_name=_('Direccion'),
        max_length=100,
        blank=True,
    )
    telefono = models.CharField(
        verbose_name=_('Teléfono'),
        validators=[
            RegexValidator(regex=r'^\d+$', message=_('Ingrese solo números.')),
        ],
        max_length=15,
        blank=True,
    )
    # pais = CountryField()
    detalles = models.TextField(
        verbose_name=_("Detalles"),
        blank=True,
    )
    # logo = StdImageField(upload_to=logo_path, default="empresas/logo-blanco.png",
    #                      variations={'thumbnail': {"width": 180, "height": 50, "crop": False}})
    estado = models.PositiveSmallIntegerField(
        verbose_name=_('Estado'),
        choices=EstadoEmpresa.choices,
        default=EstadoEmpresa.ACTIVO,
        blank=True,
    )
    is_active = models.BooleanField(
        verbose_name=_('Estado activo?'),
        default=True,
    )
    fecha_contratacion = models.DateTimeField(
        verbose_name=_('Fecha de contratación'),
        blank=True,
        null=True,
    )
    fecha_suspension = models.DateTimeField(
        verbose_name=_('Fecha de suspension'),
        blank=True,
        null=True,
    )
    nombre_facturacion = models.CharField(
        verbose_name=_('Nombre de facturación'),
        max_length=255,
        blank=True,
    )
    rfc = models.CharField(
        verbose_name="RFC/RUC",
        max_length=30,
        blank=True,
    )
    regimen_fiscal = models.CharField(
        verbose_name=_('Regimen fiscal'),
        max_length=10,
        blank=True,
        null=True,
    )
    codigo_postal = models.CharField(
        verbose_name=_('Codigo postal'),
        max_length=50,
        blank=True,
    )
    direccion_facturacion = models.TextField(
        verbose_name=_('Dirección de facturación'),
        max_length=100,
        blank=True,
    )
    email_facturacion = models.EmailField(
        verbose_name=_('Email de facturación'),
        blank=True,
    )
    timezone = models.CharField(
        max_length=190,
        default="Etc/UTC",
        blank=False,
        null=False,
    )
    # Grupos de Servidores y Subdominios
    external_id = models.PositiveIntegerField(
        verbose_name=('Id externo del lote al que pertenece'),
        db_index=True,
        blank=True,
        null=True,
    )
    # lote = models.CharField(
    #     _('Lote al que pertenece'),
    #     max_length=50,
    #     default=settings.LOTE_PRINCIPAL,
    # )
    plan = models.ForeignKey(
        'system.PlanEmpresa',
        related_name="empresa_plan_empresa",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )

    class Meta:
        verbose_name = _("Empresa")
        verbose_name_plural = _("Empresas")
        permissions = {
            ('lista_empresas', _('Lista de empresas')),
            ('acciones_lista_empresas', _('Acciones lista de empresas')),
            ('crear_superusuarios', _('Crear super usuarios')),
            ('eliminar_superusuarios', _('Eliminar super usuarios')),
            ('ver_perfil_financiero', _('Ver perfil financiero')),
        }

    def __str__(self):
        return F"{self.nombre}"

    # def logo_path(self, filename):
    #     extension = os.path.splitext(filename)[1][1:]
    #     file_name = os.path.splitext(filename)[0]
    #     url = "empresas/{}/logo/{}.{}".format(
    #         self.schema_name, slugify(str(file_name)), extension
    #     )
    #     return url
