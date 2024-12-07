from django.contrib.admin import register, ModelAdmin
from wh.apps.users.models import TipoUsuario


@register(TipoUsuario)
class TipoUsuarioAdmin(ModelAdmin):
    list_display = (
        'name',
    )
