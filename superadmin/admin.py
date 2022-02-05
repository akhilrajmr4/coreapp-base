from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = 'Core Application'


class Branch__view(admin.ModelAdmin):
    model = Branch
    list_display = ['Name', 'Location', ]


class Branch_manager_view(admin.ModelAdmin):
    model = Branch_manager
    list_display = ['Name', 'Emp_id', 'Email', ]


class Department_view(admin.ModelAdmin):
    model = Branch_department
    list_display = ['Branch_id', 'Department_name', ]


admin.site.register(Branch, Branch__view)
admin.site.register(Branch_manager, Branch_manager_view)
admin.site.register(Branch_department, Department_view)
