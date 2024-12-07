from django.db import models
from django.utils.translation import gettext_lazy as _


class ClientStatus(models.Model):
    name = models.CharField(
        verbose_name=_('Nombre'),
        max_length=70,
    )
    class_css = models.CharField(
        verbose_name=_("Class ccs color"),
        max_length=40,
    )
    created = models.DateTimeField(
        verbose_name=_('Fecha de creación'),
        auto_now_add=True,
        editable=False,
    )

    class Meta:
        ordering = ('-created',)
        verbose_name = _("Estado Clientes")
        verbose_name_plural = _("Estado Clientes")

    def __str__(self):
        return self.name

