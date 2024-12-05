from django.contrib import admin
from .models import *


@admin.register(Role)
class Role(admin.ModelAdmin):
    list_display = ('role',)


@admin.register(Status)
class Role(admin.ModelAdmin):
    list_display = ('status',)


@admin.register(Visiting)
class Visiting(admin.ModelAdmin):
    list_display = ('client', 'child', 'employee', 'visiting_date', 'visiting_time',
                    'missed_date', 'rescheduled_date', 'rescheduled_time', 'status', 'comment')


@admin.register(Position)
class Position(admin.ModelAdmin):
    list_display = ('position',)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'login', 'role')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'phone_number')


@admin.register(Child)
class ChildAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'client')


@admin.register(TypeReference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('type',)


@admin.register(Reference)
class ReferenceAdmin(admin.ModelAdmin):
    list_display = ('client', 'child', 'type_of_reference', 'analysis_date', 'expiration_date', 'status', 'comment')
