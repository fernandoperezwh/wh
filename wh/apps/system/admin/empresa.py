from django.contrib.admin import register, ModelAdmin
# local packages
from wh.apps.system.models import Empresa


@register(Empresa)
class EmpresaAdmin(ModelAdmin):
    list_display = (
        'uuid',
        'nombre',
        'plan',
        'estado',
        'created_at',
    )
    ordering = ('created_at',)
