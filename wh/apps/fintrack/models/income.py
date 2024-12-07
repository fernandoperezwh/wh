# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
# local imports
from wh.apps.fintrack.models.record import Record


class Income(Record):
    # relations
    transaction = models.ForeignKey(
        verbose_name=_('Transaction'),
        to='fintrack.Transaction',
        on_delete=models.CASCADE,
    )
    class Meta:
        verbose_name = _('Income')
        verbose_name_plural = _('Incomes')
        ordering = ('created_at',)
