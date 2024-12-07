from django.contrib.admin import register, ModelAdmin
from wh.apps.fintrack.models import Transaction


@register(Transaction)
class WalletAdmin(ModelAdmin):
    list_display = (
        'id',
        'wallet',
        'created_at',
    )
    ordering = ('created_at',)
