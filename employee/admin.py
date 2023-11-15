from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['id','eid','eemail','econtact']