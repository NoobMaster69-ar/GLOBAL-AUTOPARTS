from django.contrib import admin
from .models import Supplier, Parameters

class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone')

admin.site.register(Supplier, SupplierAdmin)

class ParametersAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'description')

admin.site.register(Parameters, ParametersAdmin)