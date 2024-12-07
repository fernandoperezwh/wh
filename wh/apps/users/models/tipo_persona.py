from django.db import models
from django.utils.translation import gettext_lazy as _


class TipoPersona(models.Model):
    name = models.CharField(
        verbose_name=_('Nombre'),
        max_length=20,
    )

    def __str__(self):
        return self.name
