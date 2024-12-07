from django.contrib.admin import register, ModelAdmin
from wh.apps.users.models import ClientStatus


@register(ClientStatus)
class ClientStatusAdmin(ModelAdmin):
    list_display = (
        'name',
        'created',
    )
    ordering = ('created',)
