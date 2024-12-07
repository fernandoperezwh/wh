from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _


class CtgTransaction(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        max_length=255,
    )
    created_at = models.DateTimeField(
        verbose_name=_('Created at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name=_('Updated at'),
        auto_now=True,
    )
    # relations
    user = models.ForeignKey(
        verbose_name=_('User'),
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Transaction category')
        verbose_name_plural = _('Transaction categories')
        ordering = ('created_at',)