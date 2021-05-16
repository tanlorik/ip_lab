from django.contrib import admin
from ip_lab.ip_lab.models import *

# Register your models here.


class InstitutieAdmin(admin.ModelAdmin):
    pass


class AgentGuvernAdmin(admin.ModelAdmin):
    pass


class TipMaterialAdmin(admin.ModelAdmin):
    pass


class MaterialAdmin(admin.ModelAdmin):
    pass


class PromisiuneMaterialAdmin(admin.ModelAdmin):
    pass


class SoferAdmin(admin.ModelAdmin):
    pass


class AdministratorAdmin(admin.ModelAdmin):
    pass


class IstoricAdmin(admin.ModelAdmin):
    pass


class CerereAdmin(admin.ModelAdmin):
    pass


admin.site.register(Institutie, InstitutieAdmin)
admin.site.register(AgentGuvern, AgentGuvernAdmin)
admin.site.register(TipMaterial, TipMaterialAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(PromisiuneMaterial, PromisiuneMaterialAdmin)
admin.site.register(Sofer, SoferAdmin)
admin.site.register(Administrator, AdministratorAdmin)
admin.site.register(Istoric, IstoricAdmin)
admin.site.register(Cerere, CerereAdmin)
