from django.contrib import admin
from .models import Servicio
# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

# De este modo podremos ver servicios en el panel de administrador
admin.site.register(Servicio, ServicioAdmin)

