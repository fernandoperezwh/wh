# python imports
import uuid
# django imports
from django.db import models


class PlanEmpresa(models.Model):
    uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
    )
    nombre = models.CharField(
        max_length=100,
    )
    descripcion = models.TextField(
        blank=True,
    )
    precio = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    precio_sin_iva = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
    )
    mostrar = models.BooleanField(
        default=False,
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Fecha de Creación",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Última Actualización',
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = "Plan"
        verbose_name_plural = "Planes"

    def __str__(self):
        return '{}'.format(self.nombre)
