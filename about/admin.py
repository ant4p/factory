from django.contrib import admin

from about.models import CommandUnit, JobUnit, ValueUnit

# Register your models here.
class CommandUnitAdmin(admin.ModelAdmin):
    list_display = ('job_title', 'fio', 'email', 'phone',)


class ValueUnitAdmin(admin.ModelAdmin):
    list_display = ('photo',)

class JobUnitAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]
    list_display = ('title',)


admin.site.register(CommandUnit, CommandUnitAdmin)
admin.site.register(ValueUnit, ValueUnitAdmin)
admin.site.register(JobUnit, JobUnitAdmin)
