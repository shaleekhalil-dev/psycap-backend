from django.contrib import admin
from .models import EmployeePsyCap

@admin.register(EmployeePsyCap)
class EmployeePsyCapAdmin(admin.ModelAdmin):
    # هذه السطور لتجعل اللوحة تظهر بشكل احترافي ومنظم
    list_display = ('name', 'hope', 'efficacy', 'resilience', 'optimism', 'created_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
