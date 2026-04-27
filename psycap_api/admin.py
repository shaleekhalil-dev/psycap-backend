from django.contrib import admin
from .models import EmployeePsyCap

@admin.register(EmployeePsyCap)
class EmployeePsyCapAdmin(admin.ModelAdmin):
    # عرض الأعمدة الأساسية مع المتوسط والحالة والتفاعلات
    list_display = ('name', 'average_score', 'status', 'likes', 'dislikes', 'created_at')
    
    # إضافة إمكانية البحث بالاسم والملاحظات
    search_fields = ('name', 'employee_notes')
    
    # إضافة فلاتر جانبية للتصفية حسب التاريخ أو الحالة
    list_filter = ('created_at',)
    
    # تنظيم واجهة الإضافة (داخل صفحة الموظف) إلى مجموعات (Fieldsets) لجمالية العرض
    fieldsets = (
        ("المعلومات الأساسية", {
            'fields': ('name',)
        }),
        ("أبعاد رأس المال النفسي (0-5)", {
            'fields': ('hope', 'efficacy', 'resilience', 'optimism')
        }),
        ("التفاعل والملاحظات", {
            'fields': ('likes', 'dislikes', 'employee_notes')
        }),
    )

    # جعل الحقول المحسوبة تظهر في صفحة العرض (اختياري)
    readonly_fields = ('average_score', 'status')