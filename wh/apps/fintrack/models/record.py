# python imports
import uuid
# django imports
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import (
    MinValueValidator,
)

from wh.apps import fintrack


class Record(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
    )
    amount = models.DecimalField(
        verbose_name=_('Amount'),
        decimal_places=2,
        max_digits=10,
        validators=[
            MinValueValidator(0),
        ],
    )
    description = models.TextField(
        verbose_name=_('Description'),
        null=True,
        blank=True,
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
    transaction = models.ForeignKey(
        verbose_name=_('Transaction'),
        to='fintrack.Transaction',
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
