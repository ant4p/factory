from django.contrib import admin

from about.models import CommandUnit

# Register your models here.
class CommandUnitAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'fio', 'email', 'phone',)

admin.site.register(CommandUnit, CommandUnitAdmin)
