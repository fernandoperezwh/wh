# python imports
import uuid
# django imports
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    # NOTE: Donde tomo esta dependencia?
    # avatar = StdImageField(
    #     _('Avatar'),
    #     upload_to='usuarios/%Y/%m/',
    #     default='usuarios/avatar.png',
    #    variations={
    #        'perfil': {'width': 240, 'height': 240, 'crop': True},
    #        'thumbnail': {'width': 45, 'height': 45, 'crop': True},
    #    },
    # )
    address = models.TextField(
        verbose_name=_("Dirección"),
        blank=True,
    )
    phone_number = models.CharField(
        verbose_name=_("Teléfono Celular"),
        max_length=250,
        blank=True,
        validators=[
            RegexValidator(regex=r'^\d+$', message=_('Ingrese solo números.')),
        ],
    )
    rfc = models.CharField(
        verbose_name='RFC/RUC/NIT',
        max_length=30,
        blank=True,
    )
    legal_name = models.CharField(
        verbose_name=_('Nombre facturación'),
        max_length=255,
        blank=True,
    )
    tax_id = models.CharField(
        verbose_name='RFC/RUC',
        max_length=30,
        blank=True,
    )
    tax_system = models.CharField(
        verbose_name=_('Regimen fiscal'),
        max_length=10,
        blank=True,
        null=True,
    )
    postal_code = models.CharField(
        verbose_name=_('Código postal'),
        max_length=50,
        blank=True,
    )
    billing_address = models.TextField(
        verbose_name=_('Dirección de facturación'),
        max_length=100,
        blank=True,
    )
    billing_email = models.EmailField(
        verbose_name=_('Email de facturación'),
        blank=True,
    )
    district = models.CharField(
        verbose_name=_('Localidad/Barrio/Departamento'),
        max_length=50,
        blank=True,
    )
    city = models.CharField(
        verbose_name=_('Ciudad/Municipio'),
        max_length=50,
        blank=True,
    )
    license = models.CharField(
        verbose_name=_('Licencia DNI/C.I./C.C.'),
        max_length=35,
        blank=True,
    )

    # relations
    user_type = models.ForeignKey(
        'users.TipoUsuario',
        verbose_name=_('Tipo de usuario'),
        related_name='user_type_user',
        on_delete=models.SET_NULL,
        null=True,
    )
    person_type = models.ForeignKey(
        'users.TipoPersona',
        verbose_name=_('Tipo de persona'),
        related_name='person_type_user',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    status = models.ForeignKey(
        "users.ClientStatus",
        verbose_name=_("Estatus"),
        related_name="client_status",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    company = models.ForeignKey(
        'system.Empresa',
        verbose_name=_('Empresa'),
        related_name='company_user',
        on_delete=models.CASCADE,
        null=True,
    )

    class Meta:
        ordering = ('-id',)

    def __str__(self):
        return self.username + '-' + self.get_full_name()

    # def avatar_path(self, filename):
    #     extension = os.path.splitext(filename)[1][1:]
    #     file_name = os.path.splitext(filename)[0]
    #     url = "usuarios/avatar/{}.{}".format(
    #         connection.tenant.domain_url, slugify(str(file_name)), extension
    #     )
    #     return url

