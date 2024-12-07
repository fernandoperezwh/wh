from django.contrib.admin import register, ModelAdmin
from wh.apps.fintrack.models import Wallet


@register(Wallet)
class WalletAdmin(ModelAdmin):
    list_display = (
        'id',
        'name',
        'user',
        'created_at',
    )
    ordering = ('created_at',)
