from django.contrib.admin import register, ModelAdmin
# local packages
from wh.apps.system.models import PlanEmpresa


@register(PlanEmpresa)
class PlanEmpresaAdmin(ModelAdmin):
    list_display = (
        'uuid',
        'nombre',
        'precio',
        'mostrar',
        'created',
    )
    ordering = ('created',)
