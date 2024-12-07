from django.contrib.admin import register, ModelAdmin
from wh.apps.fintrack.models import CtgTransaction


@register(CtgTransaction)
class CtgTransactionAdmin(ModelAdmin):
    list_display = (
        'name',
        'user',
        'created_at',
    )
    ordering = ('created_at',)
