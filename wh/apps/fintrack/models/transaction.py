# python
import uuid
# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _


class Transaction(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
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
    wallet = models.ForeignKey(
        verbose_name=_('Wallet'),
        to='fintrack.Wallet',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
        ordering = ['created_at']

    def __str__(self):
        return F"${self.id}"
