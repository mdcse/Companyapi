from django.contrib import admin

from .models import Company, Employee

# Register your models here.

class Companyadmin(admin.ModelAdmin):
    list_display = ("name", "location", "type")
    search_fields = ["name",]
    list_filter = ['type']


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "possition","company")
    search_fields = ["possition"]

admin.site.register(Company, Companyadmin)
admin.site.register(Employee, EmployeeAdmin)
