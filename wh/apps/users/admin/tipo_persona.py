from django.contrib.admin import register, ModelAdmin
from wh.apps.users.models import TipoPersona


@register(TipoPersona)
class TipoPersonaAdmin(ModelAdmin):
    list_display = (
        'name',
    )
