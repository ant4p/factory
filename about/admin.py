from django.contrib import admin
from django.utils.safestring import mark_safe

from about.models import CommandUnit, JobUnit, ValueUnit

# Register your models here.
class CommandUnitAdmin(admin.ModelAdmin):
    fields = [
        'job_title',
        'photo',
        'photo_image',
        'get_size',
        'fio',
        'email',
        'phone',
    ]
    readonly_fields = [
        'photo_image',
        'get_size',
    ]
    list_display = ('job_title', 'photo_image', 'fio', 'email', 'phone',)


    @admin.display(description="Фото")
    def photo_image(self, CommandUnit):
        if CommandUnit.photo:
            return mark_safe(f"<img src='{CommandUnit.photo.url}' width=75>")
        return 'Нет фото'
    
    @admin.display(description='Размер')
    def get_size(self, obj):
        return (f'{obj.photo.size / 1024:.2f} Кб')


class ValueUnitAdmin(admin.ModelAdmin):
    fields = [
        'photo',
        'photo_image',
        'get_size',
    ]
    readonly_fields = [
        'photo_image',
        'get_size',
    ]
    list_display = ('photo_image','get_size',)

    

    @admin.display(description="Фото")
    def photo_image(self, ValueUnit):
        if ValueUnit.photo:
            return mark_safe(f"<img src='{ValueUnit.photo.url}' width=75>")
        return 'Нет фото'


    @admin.display(description='Размер')
    def get_size(self, obj):
        return (f'{obj.photo.size / 1024:.2f} Кб')

class JobUnitAdmin(admin.ModelAdmin):
    readonly_fields = [
        'slug',
    ]
    list_display = ('title',)


admin.site.register(CommandUnit, CommandUnitAdmin)
admin.site.register(ValueUnit, ValueUnitAdmin)
admin.site.register(JobUnit, JobUnitAdmin)
