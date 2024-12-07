# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
# local imports
from wh.apps.fintrack.models.record import Record


class Transfer(Record):
    # relations
    transaction = models.ForeignKey(
        verbose_name=_('Transaction'),
        to='fintrack.Transaction',
        on_delete=models.CASCADE,
    )
    wallet_src = models.ForeignKey(
        verbose_name=_('Wallet source'),
        to='fintrack.Wallet',
        on_delete=models.CASCADE,
    )
    wallet_dst = models.ForeignKey(
        verbose_name=_('Wallet destination'),
        to='fintrack.Wallet',
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = _('Transfer')
        verbose_name_plural = _('Transfers')
        ordering = ('created_at',)

