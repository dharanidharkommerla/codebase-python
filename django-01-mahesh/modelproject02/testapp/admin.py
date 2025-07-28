# from django.contrib import admin
# from testapp import models

# # Register your models here.
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['eid', 'ename', 'esal', 'eadd']

# admin.site.register(models.Employee, EmployeeAdmin)

# admin.py
from django.contrib import admin
from testapp.models import Employee  # ✅ Import the model class directly

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eid', 'ename', 'esal', 'eadd']

admin.site.register(Employee, EmployeeAdmin)  # ✅ Register the model class, not the module
